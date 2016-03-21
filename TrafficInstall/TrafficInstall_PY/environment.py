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

def set_usr_variable(var_name, value, value_type=reg.REG_SZ):
    """
    Sets a user environment variable to a specified value. Creates a new variable if the
    specified variable does not currently exist. If this variable already exists, this
    replaces the value of this variable with the new, given value.

        Args:
            var_name (str): Name of targeted user environment variable.
            value (str): Value which will be associated with the targeted
                user environment variable.
            value_type [Optional (_winreg REG_* constant)]: Describes the 
                type of the value to the Windows registry. Defaults to _winreg.REG_SZ.

        Returns:
            tuple: Tuple of 2 strings. The first is the previous value of <var_name>.
                The second is the new, updated value of <var_name>. If <var_name> did not
                previously exist, the first element of the tuple will be None.
    """
    env_key = reg.OpenKey(reg.HKEY_CURRENT_USER, "Environment")
    try:
        prev_val, prev_val_type = reg.QueryValueEx(env_key, var_name)
    except WindowsError:
        # The specified key does not exist
        prev_val = None
    print("\tSetting user environment variable {} to {}...".format(var_name, value))
    reg.SetValueEx(env_key, var_name, 0, value_type, value)
    reg.CloseKey(env_key)
    # Send message to Windows notifying of environment change
    win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, 'Environment')
    return (prev_val, value)


def append_usr_variable(var_name, value, value_type=reg.REG_SZ):
    """
    Sets a user environment variable to a specified value. Creates a new variable if the
    specified variable does not currently exist. If this variable already exists, this
    appends the new, given value to the existing value of this variable (semicolon delimited).

        Args:
            var_name (str): Name of targeted user environment variable.
            value (str): Value which will be associated with\appended to the targeted
                user environment variable.
            value_type [Optional (_winreg REG_* constant)]: Describes the 
                type of the value to the Windows registry. Defaults to _winreg.REG_SZ.

        Returns:
            tuple: Tuple of 2 strings. The first is the previous value of <var_name>.
                The second is the new, updated value of <var_name>. If <var_name> did not
                previously exist, the first element of the tuple will be None.
    """
    env_key = reg.OpenKey(reg.HKEY_CURRENT_USER, "Environment")
    try:
        val_prev, val_type = reg.QueryValueEx(env_key, var_name)
    except WindowsError:
        # The PATH user environment variable was previously undefined
        val_prev = ''

    val = val_prev.split(';')  # Assumes PATH contains no folder names with semicolons.
    if len(val[-1]) == 0:
        # Check for trailing semicolon & remove it if it exists
        new_val = val[:-1]
    new_val.append(value)
    val_write = ";".join(new_val)

    reg.SetValueEx(env_key, var_name, 0, value_type, val_write)
    reg.CloseKey(env_key)
    # Send message to Windows notifying of environment change
    win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, 'Environment')
    return (val_prev if val_prev else None, val_write)

def check_usr_var_exists(var_name):
    """
    Checks to see whether a specified environment variable exists in the current user's space.
    This function uses the _winreg API to query the HKEY_CURRENT_USER\Environment key in the 
    Windows registry.

        Args:
            var_name (str): String of variable to check existence of.

        Returns:
            bool: False if the variable does not exist, else True
    """
    env_key = reg.OpenKey(reg.HKEY_CURRENT_USER, "Environment")
    try:
        value, val_type = reg.QueryValueEx(env_key, var_name)
    except WindowsError:
        # The specified key does not exist
        ret = False
    else:
        ret = True
    finally:
        reg.CloseKey(env_key)
    return ret

def check_var_exists(var_name):
    """
    Checks to see whether a specified variable exists in the system environment.
    This function uses Python's os.environ.

        Args:
            var_name (str): String of variable to check existence of.

        Returns:
            bool: False if the variable does not exist, else True
    """
    try:
        val = environ[var_name]
    except KeyError:
        ret = False
    else:
        ret = True
    return ret