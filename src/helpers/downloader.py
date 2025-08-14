import requests
from pathlib import Path

def download_to_local(url:str, outpath:Path, parent_mkdir:bool=True):
    if not isinstance(outpath, Path):
        raise   ValueError(f"{outpath} needs to be a valid pathlib , object path")
    if parent_mkdir:
        outpath.parent.mkdir(parents=True, exist_ok=True)
    try:
        response = requests.get(url)
        response.raise_for_status()
        #write the file out in binaary mode to prevent any inline conversions
        outpath.write_bytes(response.content)
        return True
    except requests.RequestException as e:
        print(f"failed to dowload {url} : {e}")
        return False