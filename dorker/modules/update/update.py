from dorker.modules.utils.utils import Logger
import asyncio


async def update():
    try:
        process = await asyncio.subprocess.create_subprocess_shell(
            cmd=f"pip install -U git+https://github.com/RevoltSecurities/GoogleDorker --break-system-packages",
            stderr=asyncio.subprocess.PIPE,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE
        )
        stdin, stderr = await process.communicate()
        if process.returncode == 0:
            Logger(f"Successfully Update the Dorker to its latest version")
        else:
            Logger(f"Unable to Update Dorker to its latet version, please try to update manually.", "warn")
            await asyncio.sleep(1)
            Logger(f"Reason for Update Failure: \n{stderr.decode()}", "warn")
            
    except PermissionError:
        Logger(f"Unable to update due insufficient access, please try as admin or root user", "warn")
    except Exception as e:
        Logger(f"Exception occured in update module due to: {e}, {type(e)}", "warn")