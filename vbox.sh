#!/usr/bin/env bash

cd ~/Traffic/trajectorymanagementandanalysis
hg pull
hg update
cd trunk/src/TrajectoryManagementAndAnalysis/
cmake .
make TrajectoryManagementAndAnalysis
cd ~/Traffic/trafficintelligence
hg pull
hg update
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
