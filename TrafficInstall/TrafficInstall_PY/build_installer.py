from subprocess import call
from ConfigParser import SafeConfigParser
import argparse
import os

def build(args):
    print("## Installer Build Script ##")
    cfg_path = args.config_file
    if not os.path.isfile(cfg_path):
        print("Specified configuration file \"{}\" does not exist. Exiting...".format(cfg_path))
        return
    print("Using configuration file \"{}\".".format(cfg_path))
    cfg = SafeConfigParser()
    sect = "Installer Build Options"
    cfg.read(cfg_path)
    icon_path = cfg.get(sect, "icon_path")
    version_path = cfg.get(sect, "version_file_path")
    installer_name = cfg.get(sect, "installer_name")
    print("Build executable installer.")
    call(
            ["pyinstaller", # Use PyInstaller
             "main.py",     # main.py is the installer's entry point
             "--clean",     # Clean PyInstaller cache and remove temporary files before building
             "-F",          # Create a one-file bundled executable.
             "-n={}".format(installer_name),    # Name the installer as specified in config file.
             "--version-file={}".format(version_path),  # Use the version file specified in the config file.
             "-i={}".format(icon_path),                # Use the icon file specified in the config file.
             "--uac-admin"]                            # Request admin privileges
    )
    print("Build finished.")  

# To see all PyInstaller options, visit http://pythonhosted.org/PyInstaller/#general-options

if __name__ == "__main__":
    cl_parse = argparse.ArgumentParser(description='Build an executable installer. Be sure to run in build environment.')
    cl_parse.add_argument("-c" ,"--config-file", default="install_default.cfg", metavar="<config_file>",
                       help="Filepath of an installer configuration file. If unspecified, defaults to \"install_default.cfg\".")
    args = cl_parse.parse_args()
    build(args)
