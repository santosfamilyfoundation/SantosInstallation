import anaconda
import opencv
import ti
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
        print("Existing Anaconda installation detected. Skipping Anaconda installation...")
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

    ## TrafficIntelligence ##
    ti_installed = ti.check()  # TODO: Implement function 
    if ti_installed:
        print("Existing TrafficIntelligence installation detected. Skipping TrafficIntelligence installation...")
        return
    else:
        dfile_ti = ti.download(temp_dir)
        ti_dir = ti.install(dfile_ti)
        ti.install_python_deps(temp_dir)
        executable_path = ti.copy_executable(ti_dir)

    ## Delete temporary files.  
    ut.cleanup(temp_dir)

    # TODO: Tests?


if __name__ == "__main__":
    main()
