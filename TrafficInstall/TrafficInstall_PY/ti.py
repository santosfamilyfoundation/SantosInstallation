"""
Functions for dealing with TrafficIntelligence.
"""
import urllib2
from utilities import user_home_directory
from tqdm import tqdm
from subprocess import call
from distutils.spawn import find_executable
import zipfile
import os
from environment import append_usr_variable, check_usr_var_exists
from shutil import copytree, copy2


def check():
    """
    Checks for existing TrafficIntelligence installation.
    
        Args:
            None

        Returns:
            bool: True if found to be installed, else False
    """
    return os.path.exists(os.path.join(DEFAULT_INSTALL_LOCATION, "trafficintelligence"))


def download(destination):
    """
    Downloads a vetted copy of the main branch of the TrafficIntelligence repository.
    Additionally downloads 

        Args:
            destination (str): Path to store downloaded file. Will be saved to
                <destination> + "ti.zip" 

        Returns:
            str: String specifying the absolute path of the downloaded file.
    """
    print("## Download TrafficIntelligence ##")
    # Check for trailing slash on destination directory specifier
    if destination[-1] is not "\\":
        destination = destination + "\\"

    url = "https://codeload.github.com/santosfamilyfoundation/Traffic/zip/windows"
    print("Downloading TrafficIntelligence...")
    response = urllib2.urlopen(url)
    meta = response.info()
    download_size = int(meta.getheaders("Content-Length")[0])
    CHUNK = 16 * 1024
    download_location = destination + "ti.zip"
    with open(download_location, 'wb') as f:
        with tqdm(total=download_size, leave=False, unit="bit", unit_scale=True) as pbar:
            while True:
                chunk = response.read(CHUNK)
                if not chunk:
                    print("\nDownload Complete.")
                    break
                pbar.update(CHUNK)
                f.write(chunk)
    return download_location


def install(downloaded_file, install_dir=None):
    """
    Unzips and places the TrafficIntelligence repository and the Windows binaries.
    
        Args:
            downloaded_file (str): Path to the downloaded trafficintelligence zip file.
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
    parent_dir = os.path.dirname(downloaded_file)
    extract_dir = os.path.join(parent_dir, "ti")
    print("Unzipping TrafficIntelligence...")
    with zipfile.ZipFile(downloaded_file, "r") as z:
        z.extractall(extract_dir)
    print("Copying TrafficIntelligence...")
    # Remove .gitignore and readme.md 
    os.remove(os.path.join(extract_dir, "Traffic-windows", ".gitignore"))
    os.remove(os.path.join(extract_dir, "Traffic-windows", "README.md"))
    copytree(os.path.join(extract_dir, "Traffic-windows"), installation_directory)
    ## Set environment variables. 
    python_dir = os.path.join(installation_directory, "trafficintelligence", "python")
    append_usr_variable("PYTHONPATH", python_dir)
    return installation_directory


def install_python_deps(temp_dir):
    """
    Installs Python packages pillow and shapely. Pillow installation uses Anaconda's
    `conda` installer. The shapely installation uses `pip` to install a downloaded wheel.

        Args:
            temp_dir (str): Path to the temporary directory for storing downloaded files. 
                This will store a precompiled wheel for the Shapely package in this directory;
                this will be named "shapely.whl".

        Returns:
            None
    """
    print("## Install TrafficIntelligence Python Dependencies ##")

    # Install Python Imaging Library [pillow]
    print("Acquiring PILLOW (imaging library)...")
    call(["conda", "install", "pillow", "-y"])

    # Download and install shapely.
    url = "http://www.lfd.uci.edu/~gohlke/pythonlibs/djcobkfp/Shapely-1.5.13-cp27-none-win_amd64.whl"
    print("Acquiring Shapely...")
    response = urllib2.urlopen(url)
    meta = response.info()
    download_size = int(meta.getheaders("Content-Length")[0])
    CHUNK = 16 * 1024
    download_location = os.path.join(destination, "shapely.whl")
    with open(download_location_repo, 'wb') as f:
        with tqdm(total=download_size, leave=False, unit="bit", unit_scale=True) as pbar:
            while True:
                chunk = response.read(CHUNK)
                if not chunk:
                    print("\nDownload Complete.")
                    break
                pbar.update(CHUNK)
                f.write(chunk)
    call(["pip", "install", download_location])


def copy_executable(ti_dir):
    """
    Makes a copy of downloaded "trafficintelligence.exe" and renames it to "feature-based-tracking.exe"
    to align with executable names used in Linux.

        Args:
            ti_dir (str): Path to installed TrafficIntelligence.

        Returns:
            str: Path to the new copy of the executable.
    """
    exe_dir = os.path.join(ti_dir, "windows_built")
    exe_path = os.path.join(exe_dir, "trafficintelligence.exe")
    exe_copy = os.path.join(exe_dir, "feature-based-tracking.exe")
    copy2(exe_path, exe_copy)
    return exe_copy


DEFAULT_INSTALL_LOCATION = os.path.join(user_home_directory(), "Traffic")

if __name__ == "__main__":
    dloc = download("C:\\Traffic\\.install\\")
    install(dloc, "C:\\TrafficTEST")
