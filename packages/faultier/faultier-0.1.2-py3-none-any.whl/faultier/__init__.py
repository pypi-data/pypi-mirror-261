import serial
import plotly.graph_objs as go
from IPython.display import display
from .faultier_pb2 import *
import struct
import subprocess
import os

# Get the directory of the current module
MODULE_DIR = os.path.dirname(os.path.realpath(__file__))

def convert_uint8_samples(input: bytes):
    r = []
    for b in input:
        r.append(b/255)
    return r
"""
    This class is used to control the Faultier.

    All functionality that configures the ADC or the glitcher
    require opening the device first, the OpenOCD debug probe
    is always active and does not use the serial interface.
    Because of this the functions using OpenOCD (such as nrf_flash_and_lock)
    are marked as static and can be called without initializing
    the Faultier first.
"""
class Faultier:
    """
    :param path: The path to the serial device. Note that the Faultier exposes
                 two serial devices - the first one is the control channel.
                 
                 On mac this will be /dev/cu.usbmodemfaultier1.
    """
    def __init__(self, path):
        """
        test
        """
        self.device = serial.Serial(path)
        self.device.timeout = 5
    
    def _read_response(self):
        header = self.device.read(4)
        if(header != b"FLTR"):
            print(header)
            raise ValueError("Invalid header received.")
        length_data = self.device.read(4)
        length = struct.unpack("<I", length_data)[0]
        return self.device.read(length)

    def _check_response(self):
        response = self._read_response()
        resp = Response()
        resp.ParseFromString(response)
        if resp.WhichOneof('type') == 'error':
            raise ValueError("Error: " + resp.error.message)
        if resp.WhichOneof('type') == 'trigger_timeout':
            raise ValueError("Trigger timeout!")
        return resp

    def _check_ok(self):
        response = self._read_response()
        resp = Response()
        resp.ParseFromString(response)
        if resp.ok:
            return
        if resp.error:
            raise ValueError("Error: " + resp.error.message)
        else:
            raise ValueError("No OK or Error received.", resp)

    # def captureADC(self):
    #     # TODO will be replaced by command structure
    #     self.device.write(b"A")
    #     response = self._read_response()
    #     resp = ResponseADC()
    #     resp.ParseFromString(response)
    #     return convert_uint8_samples(resp.samples)
    
    def _send_protobuf(self, protobufobj):
        serialized = protobufobj.SerializeToString()
        length = len(serialized)
        # Header
        self.device.write(b"FLTR")
        self.device.write(struct.pack("<I", length))
        self.device.write(serialized)
        self.device.flush()

    def configure_adc(self, source, sample_count):
        configure_adc = CommandConfigureADC(
            source = source,
            sample_count = sample_count
        )
        cmd = Command()
        cmd.configure_adc.CopyFrom(configure_adc)
        self._send_protobuf(cmd)
        self._check_ok()

    def configure_glitcher(self, trigger_type, trigger_source, glitch_output, delay, pulse, power_cycle_length=1000000, power_cycle_output = GLITCH_OUT_NONE, ):
        """
        Configures the glitcher, i.e. glitch-output, delay, pulse, etc. It does not Arm
        or cause any other change to IOs until glitch() is called.

        :param delay: The delay between Trigger and Glitch.

        :param pulse: The glitch pulse length.

        :param trigger_type: The type of trigger that should be used

            - `TRIGGER_NONE`: No Trigger. The glitch will wait the delay and then glitch.
            - `TRIGGER_LOW`: Waits for the signal to be low. If the signal is low to begin with this will trigger immediately.
            - `TRIGGER_HIGH`: Waits for the signal to be high. If the signal is low to begin with this will trigger immediately.
            - `TRIGGER_RISING_EDGE`: Waits for a rising edge on the trigger input.
            - `TRIGGER_FALLING_EDGE`: Waits for a falling edge on the trigger input.
        
        :param trigger_source: The source - as in physical input - of the trigger.

            - `TRIGGER_IN_NONE`: Ignored, use TRIGGER_NONE to disable triggering.
            - `TRIGGER_IN_EXT0`: Configure EXT0 as digital input and use it for triggering.
            - `TRIGGER_IN_EXT1`: Configure EXT1 as digital input and use it for triggering.

        :param glitch_output: The glitch-output that will be used.

            - `GLITCH_OUT_CROWBAR`: Route the glitch to the gate of the Crowbar MOSFET.
            - `GLITCH_OUT_MUX0`: Route the glitch to control channel 0/X of the analogue switch (the one exposed on the SMA connector).
            - `GLITCH_OUT_MUX1`: Route the glitch to channel 1/Y of the analogue switch (exposed on 20-pin header).
            - `GLITCH_OUT_MUX2`: Route the glitch to channel 2/Z of the analogue switch (exposed on 20-pin header).
            - `GLITCH_OUT_EXT0`: Route the glitch signal to the EXT0 header. Useful to trigger external tools such as a ChipSHOUTER or laser.
            - `GLITCH_OUT_EXT1`: Route the glitch signal to the EXT1 header. Same as above.
            - `GLITCH_OUT_NONE`: Disable glitch generation. Power-cycle, trigger, ADC & co will still run as regular. Good for trigger testing.

        :param power_cycle: Whether a separate output should be toggled before activating the trigger-delay-glitch pipeline. Useful to restart a target.

            - `GLITCH_OUT_CROWBAR`: Route the power-cycle to the gate of the Crowbar MOSFET.
            - `GLITCH_OUT_MUX0`: Route the power-cycle to control channel 0/X of the analogue switch (the one exposed on the SMA connector).
            - `GLITCH_OUT_MUX1`: Route the power-cycle to channel 1/Y of the analogue switch (exposed on 20-pin header).
            - `GLITCH_OUT_MUX2`: Route the power-cycle to channel 2/Z of the analogue switch (exposed on 20-pin header).
            - `GLITCH_OUT_EXT0`: Route the power-cycle signal to the EXT0 header. Useful to trigger external tools such as a ChipSHOUTER or laser.
            - `GLITCH_OUT_EXT1`: Route the power-cycle signal to the EXT1 header. Same as above.
            - `GLITCH_OUT_NONE`: Disable power-cycle generation.

        :param power_cycle_length: The number of clock-cycles for the power cycle.
        """
        configure_glitcher = CommandConfigureGlitcher(
                trigger_type = trigger_type,
                trigger_source = trigger_source,
                glitch_output = glitch_output,
                delay = delay,
                pulse = pulse,
                power_cycle_output = power_cycle_output,
                power_cycle_length = power_cycle_length)
        cmd = Command()
        cmd.configure_glitcher.CopyFrom(configure_glitcher)
        self._send_protobuf(cmd)
        self._check_ok()

    def glitch(self):
        cmd = Command()
        cmd.glitch.CopyFrom(CommandGlitch())
        self._send_protobuf(cmd)
        self._check_response()

    def swd_check(self):
        cmd = Command()
        cmd.swd_check.CopyFrom(CommandSWDCheck(function = SWD_CHECK_ENABLED))
        self._send_protobuf(cmd)
        response = self._check_response()
        return response.swd_check.enabled

    def nrf52_check(self):
        cmd = Command()
        cmd.swd_check.CopyFrom(CommandSWDCheck(function = SWD_CHECK_NRF52))
        self._send_protobuf(cmd)
        try:
            response = self._check_response()
        except:
            # TODO check for debug errors only
            return False
            pass
        return response.swd_check.enabled

    def read_adc(self):
        cmd = Command()
        cmd.read_adc.CopyFrom(CommandReadADC())
        self._send_protobuf(cmd)
        response = self._check_response()
        return convert_uint8_samples(response.adc.samples)

    @staticmethod
    def nrf_flash_and_lock():
        env = {
            'PATH': "/usr/local/bin:/usr/bin:/opt/homebrew/bin"
        
        }
        print("Erasing...")
        subprocess.run(["openocd", "-s", "/usr/local/share/openocd", "-f", "interface/tamarin.cfg", "-f", "target/nrf52.cfg", "-c", "init; nrf52_recover; exit"], env=env)
        print("Programming softdevice...")
        
        subprocess.run(["openocd", "-s", "/usr/local/share/openocd", "-f", "interface/tamarin.cfg", "-f", "target/nrf52.cfg", "-c", "program examples/nrf52/s132_nrf52_7.2.0_softdevice.hex; exit"], env=env)
        print("Programming firmware...")
        subprocess.run(["openocd", "-f", "interface/tamarin.cfg", "-f", "target/nrf52.cfg", "-c", "program examples/nrf52/nrf52832_xxaa.hex; exit"], env=env)
        print("Locking chip...")
        subprocess.run(["openocd", "-f", "interface/tamarin.cfg", "-f", "target/nrf52.cfg", "-c", "init; reset; halt; flash fillw 0x10001208 0xFFFFFF00 0x01; reset;exit"], env=env)
    
    def stm32_lock(self):
        import time
        print("This action is not reversible. Locking in 10 seconds, press stop to interrupt.")
        time.sleep(10)
        
import plotly.graph_objs as go
def update_vline_position(fig, old_x, new_x):
    for shape in fig.layout.shapes:
        if shape.type == 'line' and shape.x0 == old_x and shape.x1 == old_x:
            shape.update(x0=new_x, x1=new_x)
            break

class LivePlot:
    def __init__(self):
        self.fig = go.FigureWidget(data=[go.Scatter(y=[])])
        self.fig.update_layout(yaxis=dict(range=[0, 1]))
        self.fig.update_layout(
            margin=dict(l=20, r=20, t=20, b=20),
        )
        vline = self.fig.add_vline(x=200, line_width=1, line_dash="dash", line_color="red")
        self.vline_x = 200
        display(self.fig)
    
    def update(self, data):
        self.fig.data[0].y = data

    def update_vline(self, x):
        update_vline_position(self.fig, old_x=self.vline_x, new_x=x)
        self.vline_x = x

class LiveMarkerPlot:
    def __init__(self):
        self.fig = go.FigureWidget(data=[
            go.Scatter(x=[0], y=[0], mode="markers"),
            go.Scatter(x=[0], y=[0], mode="markers")
        ])
        # self.fig.update_layout(yaxis=dict(range=[0, 1]))
        self.fig.update_layout(
            margin=dict(l=20, r=20, t=20, b=20),
            xaxis_title="Delay",
            yaxis_title="Pulse"
        )
        # vline = self.fig.add_vline(x=200, line_width=1, line_dash="dash", line_color="red")
        self.vline_x = 200
        display(self.fig)
    
    def update(self, data):
        """
        Updates the live figure.

        :param data: Takes the scatters in the format [[4000, 8], [3950, 4]]
        """
        
        x_values = [point[0] for point in data[0]]
        y_values = [point[1] for point in data[0]]

        self.fig.data[0].x = x_values
        self.fig.data[0].y = y_values

        x_values = [point[0] for point in data[1]]
        y_values = [point[1] for point in data[1]]

        self.fig.data[1].x = x_values
        self.fig.data[1].y = y_values

    def update_vline(self, x):
        pass
        # update_vline_position(self.fig, old_x=self.vline_x, new_x=x)
        # self.vline_x = x

from IPython.display import HTML
import xml.etree.ElementTree as ET
import tempfile
import os
import urllib

def update_text_fill(text_element, new_fill_color):
    """
    Updates the "fill" property of an SVG text element's style attribute.

    Args:
    text_element (ET.Element): The SVG text element to modify.
    new_fill_color (str): The new color to set for the fill property.
    """
    # Check if the element has a 'style' attribute
    if 'style' in text_element.attrib:
        # Split the style attribute into individual properties
        styles = text_element.get('style').split(';')
        new_styles = []
        fill_updated = False
        for style in styles:
            if style.strip().startswith('fill:'):
                # Update the fill color
                new_styles.append(f'fill:{new_fill_color}')
                fill_updated = True
            else:
                new_styles.append(style)
        if not fill_updated:
            # If fill was not previously set, add it
            new_styles.append(f'fill:{new_fill_color}')
        # Update the style attribute
        text_element.set('style', ';'.join(new_styles))
    else:
        # If there's no style attribute, simply add one with the fill color
        text_element.set('style', f'fill:{new_fill_color}')

class FaultierVis:
    def __init__(self, svg_file_path):
        ET.register_namespace('', 'http://www.w3.org/2000/svg')
         # Parse the SVG file
        tree = ET.parse(svg_file_path)
        self.root = tree.getroot()

        # SVG files have namespaces, so we need to handle them.
        self.namespaces = {'svg': 'http://www.w3.org/2000/svg'}

    def change_fill(self, group_id, fill):
        g_element = self.root.find(f".//*[@id='{group_id}']", self.namespaces)

        if g_element is not None:
            # Find the 'text' element within the 'g' element. Assuming it's the first 'text' element for simplicity.
            text_element = g_element.find('.//svg:text', self.namespaces)
            
            if text_element is not None:
                update_text_fill(text_element, fill)
            else:
                print(f"No 'text' element found within the group '{group_id}'.")
                return None
        else:
            print(f"No element with ID '{group_id}' found in the SVG file.")
            return None

    def replace_text(self, group_id, text, fill=None):
        # Find the 'g' element by ID
        g_element = self.root.find(f".//*[@id='{group_id}']", self.namespaces)

        if g_element is not None:
            # Find the 'text' element within the 'g' element. Assuming it's the first 'text' element for simplicity.
            text_element = g_element.find('.//svg:text', self.namespaces)
            
            if text_element is not None:
                # Update the entire text content directly if you want to replace everything inside <text>
                text_element.text = text

                # Optionally, clear existing tspan elements (if you want to remove them)
                for tspan in text_element.findall('.//svg:tspan', self.namespaces):
                    text_element.remove(tspan)

                if fill:
                    update_text_fill(text_element, fill)

                # Convert the updated SVG tree back to a string
                svg_string = ET.tostring(self.root, encoding='unicode')

                # Optionally, strip out the xml declaration if present
                # svg_string = svg_string.replace('<?xml version=\'1.0\' encoding=\'unicode\'?>', '')

                return svg_string
            else:
                print(f"No 'text' element found within the group '{group_id}'.")
                return None
        else:
            print(f"No element with ID '{group_id}' found in the SVG file.")
            return None   


    def create_tag(self):
        # fd, path = tempfile.mkstemp(suffix=".svg", text=True)
        # f = os.fdopen(fd, 'w')
        # print(f)
        svg_string = ET.tostring(self.root, encoding='unicode')

        # URL-encode the SVG string
        encoded_svg = urllib.parse.quote(svg_string)

        # Create the <img> tag with the encoded SVG as the src
        img_tag = f'<img width=800 src="data:image/svg+xml,{encoded_svg}" alt="Inline SVG" />'

        return img_tag

    def show(self):
        display(HTML(self.create_tag()))

    @staticmethod
    def show_stm32_glitch_configuration():
        fv = FaultierVis(MODULE_DIR + "/docs/topview.svg")
        fv.replace_text("text_crowbar", "To STM32 VCore")
        fv.replace_text("text_mux0", "To STM32 VCC")
        fv.replace_text("text_ext0", "To STM32 RST")
        fv.replace_text("text_ext1", "Unused", fill="#999")
        fv.show()
        fv = FaultierVis(MODULE_DIR + "/docs/sideview.svg")
        fv.change_fill("text_swd_vcc", "#555")
        for i in range(0, 10):
            fv.change_fill(f"text_io{i}", "#555")
        for i in range(1, 3):
            fv.change_fill(f"text_m{i}_out", "#555")
            fv.change_fill(f"text_m{i}_in0", "#555")
            fv.change_fill(f"text_m{i}_in1", "#555")
        fv.change_fill(f"text_5v", "#555")
        # fv.replace_text(f"text_3.3v", "3.3V", "#555")
        fv.change_fill(f"text_gnd_top", "#555")
        fv.change_fill(f"text_gnd_bottom", "#555")
        # fv.replace_text("text_mux0", "To STM32 VCC")
        # fv.replace_text("text_ext0", "Unused", fill="#999")
        # fv.replace_text("text_ext1", "Unused", fill="#999")
        fv.show()
    
    @staticmethod
    def show_nrf52_glitch_configuration():
        fv = FaultierVis(MODULE_DIR + "/docs/topview.svg")
        fv.replace_text("text_crowbar", "To nRF52 VCore")
        fv.replace_text("text_mux0", "To nRF52 VCC")
        fv.replace_text("text_ext0", "Unused", fill="#999")
        fv.replace_text("text_ext1", "Unused", fill="#999")
        fv.show()
        fv = FaultierVis(MODULE_DIR + "/docs/sideview.svg")
        fv.change_fill("text_swd_vcc", "#555")
        for i in range(0, 10):
            fv.change_fill(f"text_io{i}", "#555")
        for i in range(1, 3):
            fv.change_fill(f"text_m{i}_out", "#555")
            fv.change_fill(f"text_m{i}_in0", "#555")
            fv.change_fill(f"text_m{i}_in1", "#555")
        fv.change_fill(f"text_5v", "#555")
        # fv.replace_text(f"text_3.3v", "3.3V", "#555")
        fv.change_fill(f"text_gnd_top", "#555")
        fv.change_fill(f"text_gnd_bottom", "#555")
        # fv.replace_text("text_mux0", "To STM32 VCC")
        # fv.replace_text("text_ext0", "Unused", fill="#999")
        # fv.replace_text("text_ext1", "Unused", fill="#999")
        fv.show()


# Update the position of the vertical line from x=200 to x=250


import random
from math import gcd

class RandomOrderGenerator:
    def __init__(self, start, end):
        self.n = end - start
        self.start = start
        self.a = self.find_coprime_a()
        self.b = random.randint(0, self.n-1)
        self.current_x = 0

    def find_coprime_a(self):
        # Try to find a coprime number in [n/2, n) and limit the search to 100,000 attempts to ensure fast execution
        attempts = 0
        while attempts < 1000000:
            candidate = random.randint(self.n // 2, self.n - 1)
            if gcd(candidate, self.n) == 1:
                return candidate
            attempts += 1
        raise ValueError("Failed to find a coprime number within 1,000,000 attempts")

    def next_value(self):
        if self.current_x >= self.n:
            raise StopIteration("All values have been visited")
        value = (self.a * self.current_x + self.b) % self.n
        self.current_x += 1
        return self.start + value

    def reset(self):
        self.current_x = 0
        self.b = random.randint(0, self.n-1)
