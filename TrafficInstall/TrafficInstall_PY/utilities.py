"""
Miscellaneous utilities to aid in the installation process.
"""
from os import environ
import os
import sys
import win32api
import win32con


def ensure_dir_exists(dir):
    """
    Checks to make sure the given directory exists. If it doesn't,
    the necessary directories are created so that it exists.
    
        Args:
            dir (str): Filepath to a directory.

        Returns:
            str: the input filepath to a directory.
    """
    if not os.path.exists(dir):
        os.makedirs(dir)
    return dir


def user_home_directory():
    """
    Returns the home directory of the current Windows user. This is 
    usually "C:\\Users\\<USERNAME>\\". The trailing slash is added to
    the values read from the environment variables.
    
    Args:
        None
    
    Returns:
        str: Home directory of the current Windows user
    """
    return environ["HOMEDRIVE"] + environ["HOMEPATH"] + "\\"

def identify_platform():
    true_platform = os.environ['PROCESSOR_ARCHITECTURE']  # Exists
    try:
            true_platform = os.environ["PROCESSOR_ARCHITEW6432"]  # Only exists on WOW64
    except KeyError:
            pass
    return true_platform

def is_64bit():
    """
    Checks the bitness of the current interpreter.
    
        Args:
            None

        Returns
            bool: True if 64-bit, else False.
    """
    return sys.maxsize > 2**32

def make_temp_dir(install_dir):
    """
    Makes a temporary hidden directory in the installation directory.
    This can be used for temporarily storing downloaded content and 
    support material during installation.

    Args:
        path (str): Path to a file or folder
    
    Returns:
        None
    """
    temp_dir = install_dir + ".install\\"
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)
    make_hidden(temp_dir)
    return temp_dir

def make_hidden(path):
    """
    On Windows, makes the given file or directory hidden.

    Args:
        path (str): Path to a file or folder
    
    Returns:
        None
    """
    win32api.SetFileAttributes(path, win32con.FILE_ATTRIBUTE_HIDDEN)

def cleanup(temp_dir):
    """
    Cleans up after an installation.
    
        Args:
            temp_dir (str): Path to temporary directory used to store downloaded
                files during the installation process. This will be deleted.
        
        Returns:    
            None
    """
    print("## Clean Up ##")
    print("Removing temporary files...")
    os.rmdir(temp_dir)