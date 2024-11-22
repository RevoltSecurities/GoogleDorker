import asyncio
import httpx
from dorker.modules.utils.utils import stdout, Logger, KeyReader, Useragents
from alive_progress import alive_bar
from dorker.modules.save.save import save

async def requests(filepath: str, dork: str, client: httpx.AsyncClient,args) -> set:
    try:
        Dorks = set()
        page = 1
        while True:
            randomkey, randomcx = await KeyReader(filepath)
            headers = {
                "User-Agent": Useragents()
            }
            if randomkey == "" or randomcx == "":
                return Dorks
            await asyncio.sleep(args.delay)
            response = await client.request("GET", f"https://customsearch.googleapis.com/customsearch/v1?q={dork}&cx={randomcx}&num=10&start={page}&key={randomkey}&alt=json", timeout=httpx.Timeout(connect=args.timeout, read=120, write=None, pool=None), follow_redirects=True, headers=headers)
            if response.status_code == 400 or response.status_code != 200:
                return Dorks
            data = response.json()
            Items = data.get("items")
            if not Items:
                return Dorks
            for item in Items:
                url = item.get("link")
                if url and url not in Dorks:
                    Dorks.add(url)
            page+=1
    except (KeyboardInterrupt, asyncio.CancelledError):
        exit()
    except httpx.ReadTimeout:
        Logger(f"Connection timeout reached for reading data from the response.", "error")
    except TimeoutError:
        Logger(f"Connection timeout reached for the request connection, please try to increase the timeout value with --timeout", "error")
    except httpx.ConnectError:
        Logger(f"Unable to make connection with google search API due to poor connection error", "error")
    except Exception as e:
        Logger(f"Exception occured in the google search request module due to: {e}, {type(e)}", "error")
        

async def manager(filepath: str, Dork: str, client: httpx.AsyncClient, sem: asyncio.Semaphore, args,bar) -> None:
    try:
        Dorks = await requests(filepath, Dork, client, args)
        if Dorks and len(Dorks) != 0:
            Logger(f"Dorking Results found for: {Dork}")
            for dork in Dorks:
                stdout(dork)
                if args.output:
                    await save(dork, args)
        else:
            if args.verbose:
                Logger(f"There is No Dorking results found for: {dork}", "warn")
    except Exception as e:
        Logger(f"Exception occured in manager core module due to: {e}, {type(e)}", "error")
    finally:
        sem.release()
        bar()

async def Dork(dorks: list[str], args,sem: asyncio.Semaphore, configfile: str) -> None:
    try:
        tasks = []
        async with httpx.AsyncClient(proxy=args.proxy if args.proxy else None, verify=False, max_redirects=30) as client:
            with alive_bar(bar="blocks", title="Dorker", total=len(dorks), enrich_print=False) as bar:
                for dork in dorks:
                    await sem.acquire()
                    task = asyncio.ensure_future(manager(configfile, dork, client, sem, args, bar))
                    tasks.append(task)
                await asyncio.gather(*tasks)
    except Exception as e:
        Logger(f"Exception occured in core module due to: {e}, {type(e)}", "error")
        