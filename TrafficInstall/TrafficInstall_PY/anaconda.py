"""
Functions for dealing with the Anaconda scientific Python distribution.
"""
import urllib2
from utilities import user_home_directory
from tqdm import tqdm
from subprocess import call
from distutils.spawn import find_executable

def check():
    """
    Checks for existing Anaconda installation.
    
        Args:
            None

        Returns:
            bool: True if found to be installed, else False
    """
    
    install_dir_exists = os.path.exists(DEFAULT_INSTALL_LOCATION)
    anaconda_exists = find_executable("anaconda")
    conda_exists = find_executable("conda")
    if anaconda_exists and conda_exists:
        return True
    else:
        return False

def download(version, destination, bit64=True):
    """
    Downloads a copy of the specified Anaconda installer

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
    extensionLUT = {
        "Windows": "exe",
        "Linux": "sh",
        "MacOSX": "pkg"
    }
    print("## Download Anaconda Scientific Python Distribution ##")
    # Check for trailing slash on destination directory specifier
    if destination[-1] is not "\\":
        destination = destination + "\\"

    base_url = "https://repo.continuum.io/archive/"
    python_version = 2  # Either 2 or 3
    os = "Windows"  # Either "Windows", "MacOSX", or "Linux"
    
    # If anaconda version is 2.4 or newer, specify Anaconda2 or Anaconda3
    # Else, specify Anaconda or Anaconda3
    anaconda_version_parse = version.split(".")
    assert(len(anaconda_version_parse) == 3)
    if anaconda_version_parse[0] > 1 and anaconda_version_parse[1] >=4:
        pyv = str(python_version)
    else:
        pyv = "3" if python_version is 3 else ""

    # Assemble filename
    filename = "Anaconda{pyv}-{av}-{os}-x86{bit}.{ext}".format(
                    pyv=pyv,
                    av = version,
                    os=os,
                    bit="_64" if bit64 else "",
                    ext=extensionLUT[os]
    )
    url = base_url + filename
    print(url)
    print("Downloading {}...".format(filename))
    response = urllib2.urlopen(url)
    meta = response.info()
    download_size = int(meta.getheaders("Content-Length")[0])
    CHUNK = 16 * 1024
    download_location = destination + "anaconda.exe"
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
    Installs a downloaded anaconda executable.
    
        Args:
            downloaded_file (str): Path to the downloaded Anaconda installer.
            install_dir [Optional (str)]: Path to where Anaconda will be installed.
                if not given or None, defaults to "C:\Users\<USERNAME>\AppData\Local\Continuum\Anaconda".
                "C:\Users\<USERNAME>" is dynamically read using utilities.user_home_directory()

        Returns:
            str: Path to where Anaconda has been installed.
    """
    print("## Install Anaconda Scientific Python Distribution ##")
    install_type = "JustMe"  # "JustMe" or "AllUsers"
    add_to_path = 1  # 1 (yes, add to path) or 0 (do not add to path)
    register_python = 1 # 1 (Set as systemwide default Python) or 0 (set only as user default Python).
    if install_dir:
        installation_directory = install_dir
    else:
        installation_directory = DEFAULT_INSTALL_LOCATION
    install_options = "/InstallationType={it} /AddToPath={atp} /RegisterPython={rp} /S /D={install_dir}".format(
                            it=install_type,
                            atp=add_to_path,
                            rp=register_python,
                            install_dir=installation_directory
    )
    call([downloaded_file])
    return installation_directory

DEFAULT_INSTALL_LOCATION = user_home_directory() + "AppData\\Local\\Continuum\\Anaconda"

if __name__ == "__main__":
    download("2.5.0", "C:\\Traffic\\.install\\", False)
