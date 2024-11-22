from dorker.modules.utils.utils import reset, bold, white, blue

def help(path):
    print(f"""
          
{bold}{white}[{reset}{bold}{blue}DESCRIPTION{reset}{bold}{white}]{reset}: {bold}{white}GoogleDorker - Unleash the power of Google dorking for ethical hackers with custom search precision.{reset}

{bold}{white}[{reset}{bold}{blue}USAGE{reset}{bold}{white}]{reset}: {bold}{white}

    dorker [flags]{reset}
    
{bold}{white}[{reset}{bold}{blue}FLAGS{reset}{bold}{white}]{reset}: {bold}{white}

    {bold}{white}[{reset}{bold}{blue}INPUT{reset}{bold}{white}]{reset}: {bold}{white}
    
        -q,  --query                    :  single dorking query for Dorker to search
        -l,  --list                     :  filename that contains list of dorks with target name
        stdin/stdout                    :  Dorker now supports stdin/stdout for reading dorks
        
    {bold}{white}[{reset}{bold}{blue}OUTPUT{reset}{bold}{white}]{reset}: {bold}{white}
    
        -o,   --output                  :  filename to save the outputs.
        
    {bold}[{bold}{blue}Rate-Limits{reset}{bold}{white}]{reset}:{reset}{bold}{white}

        -t,    --threads                : set the concurrency level for dorking (default 20)
        
    {bold}{white}[{reset}{bold}{blue}OPTIMIZATION{reset}{bold}{white}]{reset}: {bold}{white}
    
        -t,   --timeout                 :  timeout value for every sources requests (default: 15).
        -d,   --delay                   :  specify a delay value between each requests (default: 1)
    
    {bold}{white}[{reset}{bold}{blue}UPDATE{reset}{bold}{white}]{reset}: {bold}{white}
    
        -up,   --update                 :  updates Dorker tool to latest version (info: requires pip to be insalled).
        
    {bold}{white}[{reset}{bold}{blue}CONFIG{reset}{bold}{white}]{reset}: {bold}{white}
    
        -px,  --proxy                   :  http proxy to use with Dorker's each request
        -cp,  --config-path             :  custom path of config file for Dorker to read api keys (default path:{path}).
        
    {bold}{white}[{reset}{bold}{blue}DEBUG{reset}{bold}{white}]{reset}: {bold}{white}
    
        -h,   --help                    :  displays this help message and exits 
        -s,   --silent                  :  disables showing banner and version of Dorker
        -v,   --verbose                 :  enable to increase the verbosity of the Dorker{reset}""")
    
    exit()