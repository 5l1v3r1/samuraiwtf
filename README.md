# samuraiwtf

**Want to Contribute? See section at the end of this readme**

The purpose behind this project is to migrate the SamuraiWTF (http://www.samurai-wtf.org), which until now has been maintained as a monolithic virtual machine, to a "packageable" distribution system. The current direction of choice is Vagrant with a VirtualBox provider, which is the effort in this master branch.  Alternative efforts can be found in other branches.

**To download an OVA to import a full virtual machine, visit https://tiny.si/samurai. 

A [video tutorial](https://www.youtube.com/watch?v=3a3qOFubfGg) is available showing how to install from OVA.

## Prerequisites
- Vagrant - https://www.vagrantup.com/
- Virtualization Software - The base vagrant box used supports virtualbox, vmware, and parallels, but testing at this time has been solely on virtualbox - https://www.virtualbox.org/
- vagrant-vbguest plugin for vagrant (virtualbox only) - this automatically installs guest extensions which provide support for higher display resolutions, as well as other conveniences like clipboard sharing - https://github.com/dotless-de/vagrant-vbguest

## Initial Install
1. Make sure you have the prereqs listed above. Webpwnized has made some helpful [YouTube video instructionals](https://www.youtube.com/watch?v=MCqpTpxNSlA&list=PLZOToVAK85Mru8ye3up3VR_jXms56OFE5) for getting Vagrant and VirtualBox  with vbguest plugin installed in case you have not done so before.
2. Clone this repository.
3. From a command-line terminal in the project directory, run the command `vagrant up`. Then sit back and wait for it to finish. Immediately after the first time start up it is recommend you do a restart using `vagrant reload`.  Just running the `vagrant up` will build the primary target, which is a single VM with both the user environment and the targets.  You can run `vagrant up userenv` and `vagrant up target` to build seperate virtual machines for those purposes.
**NOTE: The Guest VM's window will open with the CLI while provisioning is still ongoing. It's best to leave it alone until the `vagrant up` command fully completes.**

### Provisioning Scripts
The main Vagrant provisioning script for SamuraiWTF is *install/userenv_bootstrap.sh*.  A standalone targets provisioning script is in *install/target_bootstrap.sh*.  Changes for the system, targets, or tools installation or initialization for SamuraiWTF are all handled within these scripts.

## Production VM Notes:
Once you load the VM, the username and password are:

- Username: samurai
- Password: samurai

The menus are available via a right click on the desktop.

Once you log in the target systems need to be provisioned. (Working on doing this during the build!)

First, load the Chrome bookmarks by starting *Chrome*.  Then select the *three dots* menu and select *Bookmarks*.
From the sub menu, select *Import bookmarks and settings*.  In the window that opens, select *Bookmarks HTML File*.
A file selector window will open.  Select the *chrome_bookmarks.html* file in the samurai home directory.

Some of the target environments need to be initialized before use.  Use their setup or Reset DB links to do this.

# License
The scripts and resources belonging to this project itself are licensed under the GNU Public License version 3 (GPL3).
All software loaded into the VM, including the tools, targets, utilities, and operating system itself retain their original license agreements.


# Contributors
Contributors are very welcome and the contribution process is standard:

  * fork this project
  * make your contribution
  * submit a pull request
  
Substantial or *Regular* contributors may also be brought in as full team members. This includes those who have made substantial contributions to previous versions of SamuraiWTF with the assumption they will continue to do so.


# Amazon Linux Notes
There is a Ansible playbook available for Amazon Linux (i.e. to set up SamuraiWTF in a AWS Workspaces).
This is for online classrooms.  There are some caveats to this build:

  * You must start with a Amazon Linux workspace.  4GB Ram is sufficient.  Disk size can be 20GB or more.
  * The build sets up targets and tools but some customizations, such as desktop wallpaper, must be completed manually.
  * AWS terms of services does not allow any hacking / scanning from workspaces. Therefore it is recommended that you remove the default outbound rule for the workspaces Security Group, so that no traffic will be able to leave the workspace.  Strictly speaking, once SamuraiWTF is installed and configured, internet access outbound should no longer be needed.  All the target apps are contained within the environment as local destinations.

## Amazon Linux Installation
  * Create a Workspace (4+GB Ram, 20+ GB user disk space)
  * Log in, open a terminal, and run each of the the commands under [install/amazon-linux/aws_workspace_bootstrap.sh](https://raw.githubusercontent.com/SamuraiWTF/samuraiwtf/amazon-linux/install/amazon-linux/aws_workspace_bootstrap.sh) in this branch.
