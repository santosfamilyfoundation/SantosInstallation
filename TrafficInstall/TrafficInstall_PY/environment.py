"""
Functions for reading and writing persistently to Windows user environment variables.
"""
import _winreg as reg
import win32gui
from os import environ
def append_to_PATH(dp_list):
    """
    Appends a list of paths to the current user's "PATH" environment.

        Args:
            dp_list (list): List of absolute paths to be appended to the current
                user's "PATH" environment variable.

        Returns:
            tuple: Tuple of 2 strings. The first is the previous value of PATH.
                The second is the new, updated value of PATH.
    """
    env_key = reg.OpenKey(reg.HKEY_CURRENT_USER, "Environment")
    try:
        PATH_prev, val_type = reg.QueryValueEx(env_key, "PATH")
    except WindowsError:
        # The PATH user environment variable was previously undefined
        PATH_prev = ''

    paths = PATH_prev.split(';')  # Assumes PATH contains no folder names with semicolons.
    if len(paths[-1]) == 0:
        # Check for trailing semicolon & remove it if it exists
        paths = paths[:-1]
    paths.extend(dp_list)
    PATH_new = ";".join(paths)
    reg.SetValueEx(env_key, "PATH", 0, reg.REG_EXPAND_SZ, PATH_new)
    reg.CloseKey(env_key)
    # Send message to Windows notifying of environment change
    win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, 'Environment')
    return (PATH_prev, PATH_new)

def check_usr_var_exists(varname):
    """
    Checks to see whether a specified environment variable exists in the current user's space.
    This function uses the _winreg API to query the HKEY_CURRENT_USER\Environment key in the 
    Windows registry.

        Args:
            varname (str): String of variable to check existence of.

        Returns:
            bool: False if the variable does not exist, else True
    """
    env_key = reg.OpenKey(reg.HKEY_CURRENT_USER, "Environment")
    try:
        value, val_type = reg.QueryValueEx(env_key, varname)
    except WindowsError:
        # The specified key does not exist
        ret = False
    else:
        ret = True
    finally:
        reg.CloseKey(env_key)
    return ret

def check_var_exists(varname):
    """
    Checks to see whether a specified variable exists in the system environment.
    This function uses Python's os.environ.

        Args:
            varname (str): String of variable to check existence of.

        Returns:
            bool: False if the variable does not exist, else True
    """
    try:
        val = environ[varname]
    except KeyError:
        ret = False
    else:
        ret = True
    return ret