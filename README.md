# SantosInstallation

SantosPlatform consists of two components: a server install named [SantosCloud](https://github.com/santosfamilyfoundation/SantosCloud) which provides an HTTP API that analyzed videos of intersections to produce traffic safety metrics, and a desktop application named [SantosGUI](https://github.com/santosfamilyfoundation/SantosGUI) that allows users to manage their projects and interfaces with SantosCloud to analyze the videos.

This repository contains instructions for installing these components.

## Recommended Installation

### SantosGUI

Installation instructions for SantosGUI exist in the [README of the SantosGUI repository](https://github.com/santosfamilyfoundation/SantosGUI). Follow those instructions to install the user interface onto your computer.

### SantosCloud

The recommended installation for SantosCloud uses a Vagrant virtual machine. This has the advantage of dramatically reducing installation time, and provides a set environment for all developers that can be easily upgraded.

Vagrant is a tool for building and managing virtual machine environments in a single workflow. This allows users on any operating system to easily create a virtual machine that already contains the environment necessary for running SantosCloud.

To install the SantosCloud virtual machine, follow these instructions:

#### 1. Download Vagrant from its [downloads page](https://www.vagrantup.com/downloads.html).
#### 2. Clone this repo, [SantosInstallation](https://github.com/santosfamilyfoundation/SantosInstallation) onto your computer, which contains configuration files for Vagrant.
#### 3. Install SantosCloud will operate on a local machine, or on remote servers.

##### Local installation (for testing and development)

###### Install Virtualbox

To install Virtualbox on Ubuntu/Debian, run `sudo apt-get install virtualbox`. For all other OSes, download and install from [Virtualbox's website](https://www.virtualbox.org/wiki/Downloads).

###### Download Vagrant Box

First, download the Santos Vagrant box from [this link](https://goo.gl/6hl76J). Add it to your vagrant boxes with the command `vagrant box add santos santos.box`.

###### Create Virtual Machine

In the directory where SantosInstallation was cloned, run `vagrant up` to begin the install process. Verify installation with `vagrant ssh` and opening a python shell. Here, try `import storage`.

```
$ python
$ > import storage
$ >
```
If no errors appear in the console, it is setup correctly.

##### Cloud installation (for distribution or universal access)

Begin by creating security rules and gathering auth details from [AWS: Getting started guide](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)

You will need to open ssh port 22 to your IP address.

The auth details needed are:
```
access_key
secret_access_key
session_token
key pair name
ami
region
ssh private_key_path
```

In the directory where SantosInstallation was cloned, copy the keys to the Vagrant file in the respective named variables. To get a session_token, run `aws sts get-session-token --duration-seconds 129600` using the AWS CLI.

Next, install a blank box and the AWS plugin by typing:

```
vagrant plugin install vagrant-aws
vagrant box add aws-dummy https://github.com/mitchellh/vagrant-aws/raw/master/dummy.box
```

Finally, launch an instance with:

```
vagrant up --provider=aws
```

The Vagrant install will help you set up the processing backend of the traffic analysis platform.
Vagrant is supported for all major operating systems.

## Platforms

### SantosGUI

You can find the list of supported OSes for SantosGUI in the [SantosGUI README](https://github.com/santosfamilyfoundation/SantosGUI).

### SantosCloud

SantosCloud was developed and tested on Ubuntu 14.04 LTS.  The current list of supported operating systems include:

* Ubuntu 14.04

However, the installation instructions above will work on any operating system, as it creates an Ubuntu virtual machine that contains the SantosCloud environment.

#### Windows TrafficInstallation Install (Deprecated)

At one point, the team developed an automated installer for Windows. This installer installs dependencies of the system. You *might* be able to use this installer to be able to run SantosCloud on Windows, but it is deprecated and will not be supported.

The installer is available in the [`windows` branch of this repository](https://github.com/santosfamilyfoundation/SantosInstallation/tree/windows).
