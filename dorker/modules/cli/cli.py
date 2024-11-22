from dorker.modules.utils.utils import Logger
import argparse

def cli():
    try:
        parser = argparse.ArgumentParser(add_help=False, usage=argparse.SUPPRESS,exit_on_error=False)
        parser.add_argument("-q", "--query", type=str)
        parser.add_argument("-l", "--list", type=str)
        parser.add_argument("-o", "--output", type=str)
        parser.add_argument("-t", "--threads", type=int, default=20)
        parser.add_argument("-delay", "--delay", type=int, default=1)
        parser.add_argument("-up", "--update", action="store_true")
        parser.add_argument("-v", "--verbose", action="store_true")
        parser.add_argument("-cp", "--config-path", type=str)
        parser.add_argument("-s", "--silent", action="store_true")
        parser.add_argument("-h", "--help", action="store_true")
        parser.add_argument("-px", "--proxy", type=str)
        parser.add_argument("-to", "--timeout", type=int, default=15)
        return parser.parse_args()
    except argparse.ArgumentError as e:
        Logger(f"Please use the command for more infromation: dorker -h", "warn")
        exit()
    except argparse.ArgumentTypeError as e:
        Logger(f"Please use the command for more infromation: dorker -h", "warn")
        exit()
    except Exception as e:
        Logger(f"Core Exception occured in cli module due to: {e} and its type: {type(e)}", "warn")
        exit()