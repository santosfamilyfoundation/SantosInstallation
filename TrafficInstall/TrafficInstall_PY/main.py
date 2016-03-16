import _winreg as reg
import win32gui

def append_to_PATH(fp_list):
    env_key = reg.OpenKey(reg.HKEY_CURRENT_USER, "Environment")
    try:
        PATH_prev, val_type = reg.QueryValueEx(env_key, "PATH")
    except WindowsError:
        # The PATH user environment variable was previously undefined
        PATH_prev = ''
    
    print(PATH_prev)

    paths = PATH_prev.split(';')  # Assumes PATH contains no folder names with semicolons.
    if len(paths[-1]) == 0:
        # Check for trailing semicolon
        paths = paths[:-1]
    print(paths)
    paths.extend(fp_list)
    print(paths)
    PATH_new = ";".join(paths)
    print(PATH_new)

    # reg.SetValueEx(env_key, "PATH", 0, reg.REG_EXPAND_SZ, PATH_new)
    # notify the system about the changes
    # win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, 'Environment')

if __name__ == "__main__":
    append_to_PATH(["C:\\Users\\reggert\\dave\\wat", "C:\\Ludicrosity\\nonsense\\toff"])