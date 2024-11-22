from colorama import Fore, Style, init
import aiofiles
import sys
import random
from typing import Tuple
import yaml
from fake_useragent import UserAgent

bold =Style.BRIGHT
blue = Fore.BLUE
red  = Fore.RED
white = Fore.WHITE
yellow = Fore.YELLOW
green = Fore.GREEN
magenta = Fore.MAGENTA
cyan = Fore.CYAN
reset = Style.RESET_ALL
colors = [ green, cyan, blue, white, magenta]
random_color = random.choice(colors)

init()

def Useragents() -> str:
    return UserAgent().random

async def Return_reader(filepath: str) -> list[str]:
    try:
        content = []
        async with aiofiles.open(filepath, "r") as streamr:
            async for data in streamr:
                data = data.strip()
                if data:
                    content.append(data)
        return list(set(content))
    except PermissionError:
        Logger(f"Not enough permission in the file {filepath} to read or write , please try as admin or root", "warn")
        exit()
    except FileNotFoundError:
        Logger(f"There is no such file exists: {filepath}", "warn")
        exit()
    except Exception as e:
        Logger(f"Exception occured in return reader module in utils due to: {e}, {type(e)}", "warn")
    
def Logger(message: str, level="info") -> None:
    if level == "info":
        leveler = f"{bold}{blue}INFO{reset}"
    elif level == "warn":
        leveler = f"{bold}{red}WARN{reset}"
    elif level == "error":
        leveler = f"{bold}{yellow}ERR{reset}"
    elif level == "verbose" :
        leveler = f"{bold}{green}VRB{reset}"
    else :
        leveler = f"{bold}{magenta}{level}{reset}"
    
    print(f"{bold}{white}[{reset}{leveler}{bold}{white}]{reset}: {bold}{white}{message}{reset}", file=sys.stderr)
    
def stdout(message: str) -> None:
    print(message, file=sys.stdout)
    
def stderror(message: str) -> None:
    print(message, file=sys.stderr)
    
async def KeyReader(filepath: str, source="google") -> Tuple[str, str] :
    try: 
        async with aiofiles.open(filepath, "r") as streamr:
            data = yaml.safe_load(await streamr.read())
            if source not in data:
                return "", ""
            randomkeys = random.choice(data.get(source, []))
            if len(randomkeys) == 0:
                return "", ""
            key, cxid = randomkeys.split(":")
            if key is None or cxid is None:
                return "", ""
            return key, cxid
    except FileNotFoundError:
        Logger(f"There is no such file exists: {filepath}", "warn")
        exit()
    except PermissionError:
        Logger(f"Not enough permission in the file {filepath} to read or write , please try as admin or root", "warn")
        exit()
    except Exception as e:
        Logger(f"Exception occured in the Keyreader module due to: {e}, {type(e)}","error")

