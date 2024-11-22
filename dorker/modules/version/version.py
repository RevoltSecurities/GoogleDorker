import requests

def version():
    url = f"https://api.github.com/repos/RevoltSecurities/GoogleDorker/releases/latest"
    try:
        response = requests.get(url, verify=True, timeout=10)
        if response.status_code == 200:
            data = response.json()
            latest = data.get('tag_name')
            return latest
    except KeyboardInterrupt as e:
        quit()
    except Exception as e:
        pass