## Creating icons

To create an icon file to use with PyInstaller, one may use the following method.

1. Find/design a image file (e.g., `.png`, `.jpg`) to serve as an icon. The size of the image does not matter, per se, but remember that an icon may be as small as 32x32, so try to avoid fine details.
2. Navigate to (https://www.icoconverter.com) and upload this file.
3. Elect to create all available resolutions of .ico file. Choose 32-bit depth.
4. Press the "Convert" button. An `.ico` will download. 
5. Place the downloaded `.ico` into the `icon` directory of the `TrafficInstal_PY` project.
6. Check ../build_installer.py to ensure PyInstaller is directed to use the correct icon file.
