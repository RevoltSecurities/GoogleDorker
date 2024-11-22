try:
    from dorker.modules.utils.utils import Logger,Return_reader, stderror, blue, bold, reset, white, sys, green, red
    import asyncio
    from dorker.modules.banner.banner import banner
    from dorker.modules.cli.cli import cli
    from dorker.modules.core.core import Dork
    from dorker.modules.config.config import config, custompath
    from dorker.modules.update.update import update
    from dorker.modules.help.help import help
    from dorker.modules.version.version import version
except ImportError as e:
    Logger(f"AHH!, Looks like some package is missing due to {e}, if this occurs more than a time please report this issue to Revoltsecurities.", "warn")
    exit()
    
git = "v1.0.1"
Banner = banner()
args = cli()
configfile = config() if not args.config_path else custompath(args)
if not configfile:
    Logger("Unable to get config file, please try with valid config file", "warn")

def showversion() -> None:
    latest = version()
    if latest and latest == git:
        print(f"[{blue}{bold}version{reset}]:{bold}{white} dorker current version {git} ({green}latest{reset}{bold}{white}){reset}", file=sys.stderr)
    elif latest and latest != git:
        print(f"[{blue}{bold}version{reset}]:{bold}{white} dorker current version {git} ({red}outdated{reset}{bold}{white}){reset}", file=sys.stderr)
    else:
        Logger(f"unable to get the latest version of dorker", "warn")
    
async def core():
    try:
        if args.help:
            stderror(Banner)
            help(config())

        if not args.silent:
            stderror(Banner)
            showversion()
            
        if args.query:
            await Dork([args.query], args, sem=asyncio.Semaphore(args.threads),configfile=configfile)
            exit()
            
        if args.list:
            dorks = await Return_reader(args.list)
            if dorks:
                await Dork(dorks, args, sem=asyncio.Semaphore(args.threads),configfile=configfile)
            exit()
                
        if args.update:
            latest = version()
            if latest and latest == git:
                Logger(f"Dorker already in latest version")
                exit()
            elif latest and latest != git:
                Logger(f"Updating latest version of Dorker", "Update")
                await update()
                exit()
            else:
                Logger(f"Unable to get the current version, please try again", "warn")
                
        if sys.stdin.isatty():
            Logger(f"no input provided for dorker", "warn")
            exit()
            
        else:
            
            data = []
            for dork in sys.stdin:
                if dork:
                    dork = dork.strip()
                    data.append(dork)
            await Dork(data, args, sem=asyncio.Semaphore(args.threads),configfile=configfile)
            exit()
            
    except Exception as e:
        Logger(f"Exception occured in the core handler module due to: {e}, {type(e)}", "error")
    
def handler():
    asyncio.run(core())
    