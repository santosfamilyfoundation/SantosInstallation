#!/usr/bin/env bash

sudo apt-get install python-numpy python-opencv -y
cd ~/Traffic/trajectorymanagementandanalysis
hg pull
cd trunk/src/TrajectoryManagementAndAnalysis/
cmake .
make TrajectoryManagementAndAnalysis
cd ~/Traffic/trafficintelligence/c
sed -i "3s,.*,TRAJECTORYMANAGEMENT_DIR=${HOME}/Traffic/trajectorymanagementandanalysis/trunk/src/TrajectoryManagementAndAnalysis," Makefile
make feature-based-tracking
make tests
cd ~/Traffic/trafficintelligence
make doc
sudo make install
cd ~/SantosCloud
git pull
sudo pip install -r requirements.txt
cd
