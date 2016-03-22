## Create build environment 
To reduce the size of the installer, be sure to build and develop in a virtual environment which has **only the neccessary packages installed**.
When using the Anaconda Scientific Python Distribution, this environment may be created as follows--
```
conda create -n traffic_install --file requirements.txt
```

## Installer build instructions ##
To build the installer, run the `build_installer.py` script. Be sure to run this within your build environment.

```
activate traffic_install

python build_install.py
```

## Installer configuration.
You may use the build_configure.py script to create a config file to customize elements of the installer. Be sure to specify this new configuration file when running `build_install.py`.
