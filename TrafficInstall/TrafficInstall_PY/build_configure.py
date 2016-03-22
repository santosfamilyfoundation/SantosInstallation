import ConfigParser

config = ConfigParser.SafeConfigParser()

# TODO: Implement version-specification in a new config file section. 

ibo = "Installer Build Options"
config.add_section(ibo)
config.set(ibo, "icon_path", "icon/belt.ico")
config.set(ibo, "version_file_path", "version.txt")
config.set(ibo, "installer_name", "TrafficInstaller")

with open('installer.cfg', 'wb') as configfile:
    config.write(configfile)
