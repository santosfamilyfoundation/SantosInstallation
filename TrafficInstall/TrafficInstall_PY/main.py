import anaconda
import utilities as ut

def main():
    ### Main Installer Script ###
    print("### Beginning Traffic Analysis Toolkit Installation ###")
    ## Create directories ##
    install_dir = ut.ensure_dir_exists(ut.user_home_directory() + "Traffic\\")
    temp_dir = ut.make_temp_dir(install_dir)
    
    ## Anaconda ##
    anaconda_installed = anaconda.check()
    if anaconda_installed:
        print("Existing Anaconda installation detected.")
    else:
        dfile = anaconda.download("2.5.0", temp_dir)
        anaconda.install(dfile, "C:\\Users\\reggert\\Documents\\AnacondaTest")


if __name__ == "__main__":
    main()