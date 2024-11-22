from dorker.modules.utils.utils import random_color,bold,white, reset
import random
from art import *

def banner():
    tool_name = "dorker"
    fonts = ["big", "ogre", "shadow", "script",  "graffiti", "slant"]
    selected_font = random.choice(fonts)
    banner = text2art(f"{tool_name}", font=selected_font)
    banner = f"""{bold}{random_color}{banner}{reset}
                    {bold}{white}- RevoltSecurities{reset}\n"""
    return banner