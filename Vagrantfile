# -*- mode: ruby -*-
# vi: set ft=ruby :
require 'getoptlong'

opts = GetoptLong.new(
  ['--provider', GetoptLong::OPTIONAL_ARGUMENT],
)

provider = 'virtualbox'
begin opts.each do |opt, arg|
    case opt
      when '--provider'
        provider=arg
    end # case
  end # each
  rescue
end

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  config.vm.hostname = "vagrant"
  config.vm.define "default-#{provider}"
  config.ssh.shell = "bash -c 'BASH_ENV=/etc/profile exec bash'"

  config.vm.provider "virtualbox" do |vbox, override|
    override.vm.box = "santos"
    override.vm.box_check_update = false
    override.vm.network "forwarded_port", guest: 8888, host: 8888
    vbox.memory = "4096"
    vbox.cpus = "2"

    # Custom shell script
    override.vm.provision :shell, path: "vbox.sh", privileged: false
    config.vm.provision :shell, path: "onrun.sh", run: 'always'
  end

  config.vm.provider :aws do |aws, override|
    override.vm.box = "aws-dummy"
    aws.block_device_mapping = [{ 'DeviceName' => '/dev/sda1', 'Ebs.VolumeSize' => 64 }]
    aws.access_key_id = ""
    aws.secret_access_key = ""
    aws.session_token = ""
    aws.keypair_name = ""

    aws.ami = ""
    aws.region = ""
    override.ssh.username = "ubuntu"
    override.ssh.private_key_path = ""

    # Custom shell script
    override.vm.provision :shell, path: "aws.sh", privileged: false
    
  end

end
