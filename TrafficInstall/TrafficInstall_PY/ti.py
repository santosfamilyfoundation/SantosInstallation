"""
Functions for dealing with TrafficIntelligence.
"""
import urllib2
from utilities import user_home_directory
from tqdm import tqdm
from subprocess import call
from distutils.spawn import find_executable


#def check():
#    """
#    Checks for existing TrafficIntelligence installation.
    
#        Args:
#            None

#        Returns:
#            bool: True if found to be installed, else False
#    """
    

def download(version, destination, bit64=True):
    """
    Downloads a vetted copy of the main branch of the TrafficIntelligence repository.
    Additionally downloads 

        Args:
            version (str): String specifying the Anaconda version to download.
                (e.g., "2.5.0")
            destination (str): Path to store downloaded file. Will be saved to
                <destination> + "anaconda.exe" 
            bit64 [Optional(bool)]: True if 64-bit installer should be downloaded. Else
                the 32-bit (x86) version will be downloaded. Defaults to True.

        Returns:
            str: String specifying the absolute path of the downloaded file.
    """
    print("## Download Anaconda Scientific Python Distribution ##")
    # Check for trailing slash on destination directory specifier
    if destination[-1] is not "\\":
        destination = destination + "\\"

    repo_url = "https://bitbucket.org/Nicolas/trafficintelligence/get/0a05883216cf.zip"
    win_bin_url = "https://bitbucket.org/Nicolas/trafficintelligence/downloads/traffic-intelligence-win32-15-07-25.zip"
    print(url)
    print("Downloading TrafficIntelligence Repository...".format(filename))
    response = urllib2.urlopen(repo_url)
    meta = response.info()
    download_size = int(meta.getheaders("Content-Length")[0])
    CHUNK = 16 * 1024
    download_location_repo = destination + "ti.zip"
    with open(download_location_repo, 'wb') as f:
        with tqdm(total=download_size, leave=False, unit="bit", unit_scale=True) as pbar:
            while True:
                chunk = response.read(CHUNK)
                if not chunk:
                    print("Download Complete.")
                    break
                pbar.update(CHUNK)
                f.write(chunk)

    print("Downloading TrafficIntelligence Windows Binaries...".format(filename))
    response = urllib2.urlopen(win_bin_url)
    meta = response.info()
    download_size = int(meta.getheaders("Content-Length")[0])
    CHUNK = 16 * 1024
    download_location_bins = destination + "ti_bins.zip"
    with open(download_location_bins, 'wb') as f:
        with tqdm(total=download_size, leave=False, unit="bit", unit_scale=True) as pbar:
            while True:
                chunk = response.read(CHUNK)
                if not chunk:
                    print("Download Complete.")
                    break
                pbar.update(CHUNK)
                f.write(chunk)
    return (download_location_repo, download_location_bins)

def install(downloaded_file, install_dir=None):
    """
    Unzips and places the TrafficIntelligence repository and the Windows binaries.
    
        Args:
            downloaded_file (tuple): Path to the downloaded repo zip file (tuple[0]) and the 
                downloaded windows binaries (tuple[1]). 
            install_dir [Optional (str)]: Path to where the repo (.../trafficintelligence)
                and the binaries will be installed. If not given or None, defaults to 
                "C:\\Users\\<USERNAME>\\Traffic\\". "C:\\Users\\<USERNAME>" is dynamically 
                read using utilities.user_home_directory()

        Returns:
            str: Path to where the binaries and the repo have been installed.
    """
    print("## Install TrafficIntelligence Repository ##")
    
    if install_dir:
        installation_directory = install_dir
    else:
        installation_directory = DEFAULT_INSTALL_LOCATION
    
    print("## Install TrafficIntelligence Repository ##")
    # TODO: Unzip file


    return installation_directory

DEFAULT_INSTALL_LOCATION = user_home_directory() + "AppData\\Local\\Continuum\\Anaconda"

if __name__ == "__main__":
    download("2.5.0", "C:\\Traffic\\.install\\", False)
