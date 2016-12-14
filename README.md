# TrafficInstallation
Installing traffic monitoring code on various platforms.

## Recommended Installation
TrafficPlatform was developed and tested on Ubuntu 14.04 LTS.  The current list of supported operating systems include

* Ubuntu 14.04

1. Install [TrafficGUI](https://github.com/santosfamilyfoundation/TrafficGUIs) onto your local machine.  Instructions for installing the front end is located in the [TrafficGUI repository](https://github.com/santosfamilyfoundation/TrafficGUIs).
2. Download Vagrant from its [downloads page](https://www.vagrantup.com/downloads.html).
3. Clone this repo, TrafficInstallation, which contains configuration files for Vagrant (auth.py, install.sh, Vagrantfile).
4. Decide if your TrafficPlatform will operate on a local machine, or on remote servers

### 4a: Local installation (for testing and development)
In the directory where TrafficInstallation was cloned, run `vagrant up` to begin the install process. This step takes about 10 minutes to complete.
Verify installation with `vagrant ssh` and opening a python shell and try `import storage`.

```
$ python
$ > import storage
$ > 
```
If no errors appear in the console, it is setup correctly.

### 4b: Cloud installation (for distribution or universal access)
Begin by creating security rules and gathering auth details from [AWS: Getting started guide
](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)

You will need to open ssh port 22 to your IP.

The auth details needed are: 
```
access_key
secret_access_key
session_token
key pair name.
```
In the directory where TrafficInstallation was cloned, copy the keys to the Vagrant file in the respective named variables. 

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
Vagrant is supported for the Ubuntu operating system.

## Platforms
An automated installer has been developed for the Windows operating system. More details are available in the [`windows` branch of this repository](https://github.com/santosfamilyfoundation/TrafficInstallation/tree/windows). 

The executable Windows installer may be downloaded [here](https://github.com/santosfamilyfoundation/TrafficInstallation/raw/windows/TrafficInstall/TrafficInstall_PY/dist/TrafficInstaller.exe). 
