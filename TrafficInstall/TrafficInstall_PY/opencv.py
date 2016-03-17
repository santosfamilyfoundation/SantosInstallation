"""
Functions for dealing with OpenCV's installation.
"""
import urllib2
from utilities import user_home_directory
from tqdm import tqdm
from subprocess import call
from distutils.spawn import find_executable
import os
from shutil import copytree, rmtree, copy2

from environment import append_to_PATH

def check():
    """
    Checks for existing OpenCV installation.
    
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

def download(version, destination):
    """
    Downloads a copy of the specified OpenCV installer for Windows.

        Args:
            version (str): String specifying the OpenCV version to download.
                (e.g., "2.4.12")
            destination (str): Path to store downloaded file. Will be saved to
                <destination> + "opencv.exe"

        Returns:
            str: String specifying the absolute path of the downloaded file.
    """
    print("## Download OpenCV ##")
    # Check for trailing slash on destination directory specifier
    if destination[-1] is not "\\":
        destination = destination + "\\"

    base_url = "http://iweb.dl.sourceforge.net/project/opencvlibrary/opencv-win/"
    # "http://iweb.dl.sourceforge.net/project/opencvlibrary/opencv-win/2.4.12/opencv-2.4.12.exe"
    # Assemble url
    filename = "opencv-{ver}.exe".format(ver=version)
    rel_path = "{ver}/{file}".format(ver=version, file=filename)
    url = base_url + rel_path
    print("Downloading {}...".format(filename))
    response = urllib2.urlopen(url)
    meta = response.info()
    download_size = int(meta.getheaders("Content-Length")[0])
    CHUNK = 16 * 1024
    download_location = destination + "opencv.exe"
    with open(download_location, 'wb') as f:
        with tqdm(total=download_size, leave=False, unit="bit", unit_scale=True) as pbar:
            while True:
                chunk = response.read(CHUNK)
                if not chunk:
                    print("Download Complete.")
                    break
                pbar.update(CHUNK)
                f.write(chunk)
    return download_location

def install(downloaded_file, install_dir=None):
    """
    Unpacks a downloaded OpenCV self-extracting zip archive. It copies the folder to an installation 
    location.
    
        Args:
            downloaded_file (str): Path to the downloaded OpenCV installer.
            install_dir [Optional (str)]: Path to where OpenCV will be installed.
                if not given or None, defaults to "C:\opencv". This folder should
                not presently exist. It will be created by shutil.copytree().

        Returns:
            None
    """
    print("## Install OpenCV ##")
    print("Extracting OpenCV...")
    if install_dir:
        installation_directory = install_dir
    else:
        installation_directory = DEFAULT_INSTALL_LOCATION
    # Silently extract to an "opencv" folder next to the downloaded file
    call([downloaded_file, "-y","-gm2"])
    print("Moving OpenCV...")
    temp_dir = os.path.dirname(downloaded_file)
    opencv_temp = os.path.join(temp_dir, "opencv\\")
    copytree(opencv_temp, installation_directory)  # Move extracted files
    rmtree(opencv_temp)  # Delete temporary directory of extracted files
    

def connect_3rdparty(opencv_dir, anaconda_dir, opencv_version):
    """
     Installs the OpenCV Python bindings to an Anaconda distribution. Additionally 
     connects FFmpeg by renaming some .dll's and modifying the current user's PATH
    environment variable.

        Args:
            opencv_dir (str): Location of the "opencv" folder (e.g., "C:\\opencv" or "C:\\opencv\\")
            anaconda_dir (str): Location of the Anaconda Python distribution 
                (e.g., "C:\\Users\\<USERNAME>\\AppData\\Local\\Continuum\\Anaconda")
            opencv_version (str): Version of OpenCV installed (e.g., "2.4.12")

        Returns:
            None
    """
    print("## Connect OpenCV 3rd Party Components ##")
    ## Connect Python Bindings
    print("Connecting OpenCV Python bindings...")
    cv2_loc = os.path.join(opencv_dir, "build", "python", "2.7", "x64", "cv2.pyd")
    site_packages_dest = os.path.join(anaconda_dir, "lib", "site-packages", "cv2.pyd")
    copy2(cv2_dir, site_packages_dest)  # Copy cv2.pyd to site-packages

    ## Rename FFmpeg
    print("Connecting FFmpeg...")
    ffmpeg_dir = os.path.join(opencv_dir, "sources\\3rdparty\\ffmpeg\\")
    ver_str = opencv_version.replace('.', '')
    os.rename(ffmpeg_dir + "opencv_ffmpeg.dll", ffmpeg_dir + "opencv_ffmpeg{}.dll".format(ver_str))
    os.rename(ffmpeg_dir + "opencv_ffmpeg_64.dll", ffmpeg_dir + "opencv_ffmpeg{}_64.dll".format(ver_str))
    print("Adding FFmpeg to PATH...")
    old_PATH, new_PATH = append_to_PATH([ffmpeg_dir])

DEFAULT_INSTALL_LOCATION = "C:\\opencv"

if __name__ == "__main__":
    download("2.4.12", "C:\\Traffic\\.install\\", False)
