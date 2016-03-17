import anaconda
import opencv
import utilities as ut

def main():
    ### Main Installer Script ###
    print("### Beginning Traffic Analysis Toolkit Installation ###")
    ## Create directories ##
    install_dir = ut.ensure_dir_exists(ut.user_home_directory() + "Traffic\\")
    temp_dir = ut.make_temp_dir(install_dir)
    
    ## Anaconda ##
    anaconda_version = "2.5.0"  # TODO: Connect to config or ini file.
    anaconda_installed = anaconda.check()
    if anaconda_installed:
        print("Existing Anaconda installation detected.")
    else:
        dfile_anaconda = anaconda.download(anaconda_version, temp_dir)
        anaconda_dir = anaconda.install(dfile_anaconda, "C:\\Users\\reggert\\Documents\\AnacondaTest")
    
    ## OpenCV ##
    opencv_version = "2.4.12"  # TODO: Connect to config or ini file.
    opencv_installed = opencv.check()  # TODO: Check installed OpenCV version number. 
    if opencv_installed:
        print("Existing OpenCV installation detected. Please remove this and rerun installation.")
        return
    else:
        dfile_opencv = opencv.download("2.4.12", temp_dir)
        opencv_dir = opencv.install(dfile_opencv)
        opencv.connect_3rdparty(opencv_dir, anaconda_dir, "2.4.12")

if __name__ == "__main__":
    main()