#!/usr/bin/python3
import httpx
from colorama import Fore,Back,Style
import argparse
import yaml
import time as t
import random 
from googleapiclient.discovery import build
import os



red =  Fore.RED

green = Fore.GREEN

magenta = Fore.MAGENTA

cyan = Fore.CYAN

mixed = Fore.RED + Fore.BLUE

blue = Fore.BLUE

yellow = Fore.YELLOW

white = Fore.WHITE

reset = Style.RESET_ALL

colors = [red, green, yellow, cyan, blue, magenta]

random_color = random.choice(colors)



parser = argparse.ArgumentParser(description=f"{cyan}A Powerfull Tool for google dorking{reset}")

parser.add_argument("-q", "--query", help=f"[{green}ALERT{reset}]:Google dorking query for your target", type=str)

parser.add_argument("-d", "--domain", help=f"[{green}ALERT{reset}]:Target name for Google dorking", type=str)

parser.add_argument("-o", "--output", help=f"[{green}ALERT{reset}]:File name to save the dorking results that are found",type=str)

args = parser.parse_args()

banner ="""

   ______                  __     ____             __            
  / ____/___  ____  ____ _/ /__  / __ \____  _____/ /_____  _____
 / / __/ __ \/ __ \/ __ `/ / _ \/ / / / __ \/ ___/ //_/ _ \/ ___/
/ /_/ / /_/ / /_/ / /_/ / /  __/ /_/ / /_/ / /  / ,< /  __/ /    
\____/\____/\____/\__, /_/\___/_____/\____/_/  /_/|_|\___/_/     
                 /____/                                          
                 
                 
                               Author: D.Sanjai Kumar


"""

#git version
def version_check():
    
    version = "v1.0.0"
    
    url = f"https://api.github.com/repos/sanjai-AK47/GoogleDorker/releases/latest"
    
    try:
        
        requests = httpx.Client()
        
        response = requests.get(url)
        
        if response.status_code == 200:
            
            data = response.json()
            
            latest = data.get('tag_name')
            
            if latest == version:
                
                
                print(f"[{blue}Version{reset}]: Google Dorker current version {version} ({green}latest{reset})")
                
                t.sleep(1)
                
            else:
                
                print(f"[{blue}Version{reset}]: Google Dorker current version {version} ({red}outdated{reset})")
                
                t.sleep(1)
                
                print(f"[{blue}INFO{reset}]: Please Install the new version throug pip command: pip install --upgrade dorker")
                
                t.sleep(1)
                
                print(f"[{blue}INFO{reset}]: After updating through pip visit here: https://github.com/sanjai-AK47/GoogleDorker  to know the information of latest update")
                
        else:
            
            pass
                
    except Exception as e:
        
        pass
    



#config file

def config_file():

    filename = "google_dorker.yaml"
    
    path = "/"
    
    for root,dirs,files in os.walk(path):
        
        if filename in files:
            
            file_path = os.path.join(root, filename)
            
            print(f"[{blue}INFO{reset}]: Loading the configuration file from {file_path}")
            
            return file_path
        
    print(f"[{red}ALERT{reset}]: Config File not found please kindly install the dorker! with its {filename} file ")
    
    exit()



def query(domain,filename):


    try:
        
        with open (filename, "r") as keys:
            
            data = yaml.safe_load(keys)
            
            
                
        google_api = random.choice(data.get("Google-API", []))

        google_csi = random.choice(data.get("Google-CSE-ID", []))
        
        
                
        if google_api is None or google_csi is None:
            
                print(f"[{red}ALERT{reset}]: There is no api keys found for Google-API or Google-CSI-ID. Without these keys and ID dorking cannot perform")
                        
                exit()
            
        else:
            
                pass 
            
        
        api_key = google_api
        
        cse_id = google_csi
        
        if args.query and args.domain:
            
            query = f"site:{domain} {args.query}"
            
        elif args.query:
            
            query = f"{args.query}"
            
        elif args.domain:
            
            query = f"site:{domain}"
        
        results_per_page = 10
        
        total_results = 100
        
        service = build('customsearch', 'v1', developerKey=api_key)
        
        result = [] 
        
        start_index = 1
        
        while start_index < total_results:
            
            
            results = service.cse().list(
            q=query,
            cx=cse_id,
            num=results_per_page,
            start=start_index
            ).execute()
            
            
            for i, item in enumerate(results.get('items', []), start=start_index):
                
              title = item['title']
              link = item['link']

              result.append(f"{i}. {title} - {link}")
              
            start_index += results_per_page
            
            if start_index > total_results:
                
                break
            
            check = len(result)
            
            
        if check > 0:

                for url in result:

                    print(f"[{green}FOUND{reset}]: {url}")
                    
                    writer(url)
                    
                    t.sleep(1)
                    
                    
                print(f"[{green}INFO{reset}]Total urls found: {check}")
                    
        elif check == 0:

                print(f"[{red}ALERT{reset}]No results found for this query {args.query}")

                
    except Exception as e:
        
        print(f"Error occured due to {e}")
        
        
def writer(url):
    
    if args.output:
        
        if os.path.isfile(args.output):
            
            filename = args.output
            
        elif os.path.isdir(args.output):
            
            if args.query and args.domain:
            
                filename = os.path.join(args.output, f"{args.domain}.{args.query}.txt")
                
            elif args.query :
                
                filename = os.path.join(args.output,f"{args.query}.txt")
                
            elif args.domain:
                
                filename = os.path.join(args.output,f"{args.domain}.txt")
            
        else:
            
            filename = args.output
            
    else:
        
        if args.query and args.domain:
            
                filename = f"{args.domain}.{args.query}.txt"
                
        elif args.query :
                
                filename = f"{args.query}.txt"
                
        elif args.domain:
                
                filename = f"{args.domain}.txt"
                
        else:
            
            filename = f"dorker.txt"
                

    with open(filename, "a") as w:
        
        w.write(f"{url}\n")
        
        
def main():
    
    
    print(f"{random_color}{banner}{reset}")
    
    t.sleep(1)
    
    version_check()
    
    t.sleep(1)
    
    print(f"[{green}INFO{reset}]: Searching for the api configuration file")
    
    filename = config_file()
    
    if args.domain:
        
        domain = args.domain
        
    elif args.query:
        
        domain = args.query
        
    elif args.domain and args.query:
        
        domain = args.domain and args.query
        
    elif not args.domain or args.query:
        
        print(f"[{blue}INFO{reset}]: Please provide your target or dorking for GoogleDorker")
        exit()
        
    
    
    query(domain,filename)
    
    
    
    
    
if __name__ == "__main__":
    
    main()