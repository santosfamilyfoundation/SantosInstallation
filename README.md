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

    Next, we must set some environment variables. One of these involved connecting FFmpeg to the Python OpenCV bindings. Navigate to `C:\opencv\sources\3rdparty\ffmpeg`. Rename `opencv_ffmpeg.dll` to `opencv_ffmpeg2412.dll` and `open, cv_ffmpeg_64.dll` to `opencv_ffmpeg2412_64.dll`, where 2412 refers to the version of OpenCV in use (2.4.12). Append `C:\opencv\sources\3rdparty\ffmpeg` to the `PATH` environment variable. Additionally, create a new environment variable named `OPENCV_DIR` and set it to `C:\opencv\build\x64\vc12`. Next append the `bin` directory of the `OPENCV_DIR` to the `PATH` environment variable. Do this by appending `%OPENCV_DIR$\bin` to `PATH`.

    > When editing environment variables, be sure to edit your username's environment variables and not system environment variables. The system environment variable `Path` is *not* the same as the user environment variable `PATH`. 

    To verify that this has worked, open a new command prompt, navigate to a directory with a video file, start a Python interpreter, and run the following--

    ```
    >>> import cv2
    >>> cap = cv2.VideoCapture(<VIDEO_FILENAME>)
    >>> cap.grab()
    True
    ```
    If `cap.grab()` returns True, Python is able to read videos via OpenCV and FFmpeg. If it returns False, reread step four and verify that the files are renamed as specified and the environment variables are set appropriately.
