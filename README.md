# TrafficInstallation
Installing traffic monitoring code on various platforms.

## Windows
The following instructions outline a procedure for installing the traffic monitoring code on computers running Microsoft Windows. This has been tested on a computer running Microsoft Windows 7, 64-bit. 

1. **Install a scientific Python distribution**. Much of the Python code relies on parts of the standard Python scientific stack (e.g., numpy, scipy). The recommended way for acquiring and managing the requisite packages is to install a scientific Python distribution such as [Anaconda](https://www.continuum.io/downloads). From this link, select the appropriate (likely 64-bit) Python 2.7 Windows installer and download it. Run the downloaded installer. 
2. **Download OpenCV**. Much of the existing Python scripts--especially those dealing with the display of information--make use of the OpenCV library and it's Python bindings. [Download](https://sourceforge.net/projects/opencvlibrary/files/opencv-win/2.4.12/opencv-2.4.12.exe/download) a prebuilt copy of the OpenCV library for Windows. 
**NOTE:**The link above will download a copy of OpenCV 2.4.12, which is what this procedure used. To download other versions, visit [this page](http://opencv.org/downloads.html). *Note that TrafficIntelligence currently uses OpenCV 2.4.x*.
3. **Extract OpenCV**. Run the downloaded OpenCV executable. It will prompt for an extraction location. Select your `C:\` drive. This will create a directory at `C:\opencv` with prebuilt libraries.
4. **Link OpenCV**. To use the included Python bindings, copy `C:\opencv\build\python\2.7\x64\cv2.pyd` to your Python distribution's `site-packages` directory. If you are using the Anaconda distribution discussed above, this exists at `C:\Users\<USERNAME>\AppData\Local\Continuum\Anaconda\Lib\site-packages`. This location can be confirmed by opening a command prompt, starting a Python interpreter, and running the following--

    ```
    >>> import numpy
    >>> numpy.__file__
    'C:\\Users\\<USERNAME>\\AppData\\Local\\Continuum\\Anaconda\\lib\\site-packages\\numpy\\__init__.pyc'
    ```

Verify that this copying has worked by opening a command prompt, starting a Python interpreter, and verifying that `import cv2` does not throw an error.
