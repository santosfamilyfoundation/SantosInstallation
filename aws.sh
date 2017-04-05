#!/usr/bin/env bash

sudo add-apt-repository -y ppa:mc3man/trusty-media
sudo echo "deb http://us.archive.ubuntu.com/ubuntu trusty main universe" | sudo tee -a /etc/apt/sources.list
sudo apt-get update
sudo apt-get -y install git libopencv-dev ffmpeg ipython ipython-notebook python-pandas python-numpy python-opencv python-sympy python-nose python-shapely python-skimage python-pip python-scipy build-essential checkinstall cmake pkg-config yasm libtiff4-dev libjpeg-dev libjasper-dev libavcodec-dev libavformat-dev libswscale-dev libdc1394-22-dev libxine-dev libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev libv4l-dev python-dev libtbb-dev libeigen3-dev libqt4-dev libgtk2.0-dev libfaac-dev libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev libvorbis-dev libxvidcore-dev x264 v4l-utils libgtk2.0-dev libboost-all-dev doxygen unzip mercurial vim cmake-curses-gui sqlite3 sqlite3-doc libsqlite3-dev libcppunit-dev libcppunit-doc cmake-qt-gui python-sklearn libblas-dev liblapack-dev gfortran
sudo pip install --upgrade scipy
curl -O -J -L http://sourceforge.net/projects/opencvlibrary/files/opencv-unix/2.4.10/opencv-2.4.10.zip/download
unzip OpenCV-2.4.10.zip
rm OpenCV-2.4.10.zip
cd opencv-2.4.10
rm -rf build
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local ..
make
sudo make install
sudo sh -c 'echo "/usr/local/lib" > /etc/ld.so.conf.d/opencv.conf'
sudo ldconfig
mkdir ~/Traffic
cd ~/Traffic
hg clone https://Nicolas@bitbucket.org/trajectories/trajectorymanagementandanalysis
cd ~/Traffic/trajectorymanagementandanalysis
hg pull
hg update
cd trunk/src/TrajectoryManagementAndAnalysis/
cmake .
make TrajectoryManagementAndAnalysis
cd ~/Traffic/
hg clone https://bitbucket.org/santosfamilyfoundation/trafficintelligence
cd trafficintelligence
hg pull
hg update
cd c
sed -i "3s,.*,TRAJECTORYMANAGEMENT_DIR=${HOME}/Traffic/trajectorymanagementandanalysis/trunk/src/TrajectoryManagementAndAnalysis," Makefile
make feature-based-tracking
make tests
cd ~/Traffic/trafficintelligence
make doc
sudo make install
echo 'export PYTHONPATH="${PYTHONPATH}:/home/vagrant/Traffic/trafficintelligence/python"' | tee -a ~/.bashrc
echo 'export PYTHONPATH="${PYTHONPATH}:/home/vagrant/SantosCloud"' | tee -a ~/.bashrc
. ~/.bashrc
sudo ln /dev/null /dev/raw1394
cd
git clone https://github.com/santosfamilyfoundation/SantosCloud.git
sudo pip install cvutils enum
cd SantosCloud
sudo pip install -r requirements.txt
mkdir project_dir
cd
