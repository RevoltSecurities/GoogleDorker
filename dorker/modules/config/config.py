import appdirs
from dorker.modules.utils.utils import Logger
import os

yamls = """google: []
"""

def config(): 
    try:
        get_config = appdirs.user_config_dir()
        dorker_dir =  os.path.join(get_config, "dorker")
        filename = "provider-config.yaml"
        config_path = os.path.join(dorker_dir, filename)
        if os.path.exists(dorker_dir):
            if os.path.exists(config_path):
                return config_path
            else:
                with open(config_path, "w") as w:
                    w.write(yamls)
                return config_path
        else:
            os.makedirs(dorker_dir, exist_ok=True)
            with open(config_path, "w") as w:
                w.write(yamls)
            return config_path
    except PermissionError:
        Logger(f"Not enough permission please try to run as a admin or root user", "warn")
        exit()
    except Exception as e:
        Logger(f"Exception occured at config module due to: {e}", "error")
        
def cachedir():
    try:
        cachedir = appdirs.user_cache_dir()
        return cachedir
    except Exception as e:
        pass
    
def custompath(args):
    try:
        if os.path.exists(args.config_path) and os.path.isfile(args.config_path):
            return args.config_path
        else:
            Logger(f"Please check that the custom config file exists", "warn")
            exit()
    except KeyboardInterrupt as e:
        quit()