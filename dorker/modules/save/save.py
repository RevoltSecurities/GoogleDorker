import os
import aiofiles
import asyncio
from dorker.modules.utils.utils import Logger

async def save(url, args):
    try:
        if os.path.isdir(args.output):
            filename = os.path.join(args.output, f"dorks.txt")
        else:
            filename = args.output
        async with aiofiles.open(filename, "a") as w:
            await w.write(url + '\n')
    except (KeyboardInterrupt, asyncio.CancelledError):        
        exit()
    except PermissionError:
        Logger(f"Permssion not enough for this file {args.output} to write, please try as admin or root user", "warn")
    except asyncio.CancelledError as e:
        SystemExit
    except Exception as e:
        Logger(f"Exception occured in the save module due to: {e}, {type(e)}", "error")