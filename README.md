# SantosInstallation
Installing traffic monitoring code on various platforms.

## Recommended Installation
SantosPlatform was developed and tested on Ubuntu 14.04 LTS.  The current list of supported operating systems include

* Ubuntu 14.04

1. Install [SantosGUI](https://github.com/santosfamilyfoundation/SantosGUIs) onto your local machine.  Instructions for installing the front end is located in the [SantosGUI repository](https://github.com/santosfamilyfoundation/SantosGUI).
2. Download Vagrant from its [downloads page](https://www.vagrantup.com/downloads.html).
3. Clone this repo, [SantosInstallation](https://github.com/santosfamilyfoundation/SantosInstallation), which contains configuration files for Vagrant (Vagrantfile and install.sh).
4. Decide if your SantosPlatform will operate on a local machine, or on remote servers.

### 4a: Local installation (for testing and development)
First, download the Santos Vagrant box from [this link](https://goo.gl/6hl76J). Add it to your vagrant boxes with the command `vagrant box add santosbox santos.box`.

In the directory where SantosInstallation was cloned, run `vagrant up` to begin the install process. Verify installation with `vagrant ssh` and opening a python shell. Here, try `import storage`.

```
$ python
$ > import storage
$ >
```
If no errors appear in the console, it is setup correctly.

### 4b: Cloud installation (for distribution or universal access)
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
In the directory where SantosInstallation was cloned, copy the keys to the Vagrant file in the respective named variables.

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
An automated installer has been developed for the Windows operating system. More details are available in the [`windows` branch of this repository](https://github.com/santosfamilyfoundation/SantosInstallation/tree/windows).

The executable Windows installer may be downloaded [here](https://github.com/santosfamilyfoundation/SantosInstallation/raw/windows/TrafficInstall/TrafficInstall_PY/dist/TrafficInstaller.exe).
