# Linux packages required for installation of agents in Linux

Installing and deploying Cyber Protection agents > Before you start > Linux packages required for installation of agents in Linux
Linux packages required for installation of agents in Linux

To add the necessary modules to the Linux kernel, the agent installer needs the following Linux packages:

The package with kernel headers or sources. The package version must match the kernel version.
The GNU Compiler Collection (GCC) compiler system. The GCC version must be the one with which the kernel was compiled.
The Make tool.
The Perl interpreter.
The libelf-dev, libelf-devel, or elfutils-libelf-devel libraries for building kernels starting with 4.15 and configured with CONFIG_UNWINDER_ORC=y. For some distributions, such as Fedora 28, they need to be installed separately from kernel headers.

The names of these packages vary depending on your Linux distribution.

In Red Hat Enterprise Linux, CentOS, and Fedora, the packages normally will be installed by the setup program. In other distributions, you need to install the packages if they are not installed or do not have the required versions.

Are the required packages already installed?

To check whether the packages are already installed, perform these steps:

Run the following command to find out the kernel version and the required GCC version:

cat /proc/version

This command returns lines similar to the following: Linux version 2.6.35.6 and gcc version 4.5.1

Run the following command to check whether the Make tool and the GCC compiler are installed:

make -v
gcc -v

For gcc, ensure that the version returned by the command is the same as in the gcc version in step 1. For make, just ensure that the command runs.

Check whether the appropriate version of the packages for building kernel modules is installed:

In Red Hat Enterprise Linux, CentOS, and Fedora, run the following command:

yum list installed | grep kernel-devel

In Ubuntu, run the following commands:

dpkg --get-selections | grep linux-headers
dpkg --get-selections | grep linux-image

In either case, ensure that the package versions are the same as in Linux version in step 1.

Run the following command to check whether the Perl interpreter is installed:

perl --version

If you see the information about the Perl version, the interpreter is installed.

In Red Hat Enterprise Linux, CentOS, and Fedora, run the following command to check whether elfutils-libelf-devel is installed:

yum list installed | grep elfutils-libelf-devel

If you see the information about the library version, the library is installed.

Installing the packages from the repository

The following table lists how to install the required packages in various Linux distributions.

Linux distribution	Package names	How to install
Red Hat Enterprise Linux

kernel-devel
gcc
make
elfutils-libelf-devel

The setup program will download and install the packages automatically by using your Red Hat subscription.


perl



Run the following command:

yum install perl



CentOS

Fedora



kernel-devel
gcc
make
elfutils-libelf-devel

The setup program will download and install the packages automatically.


perl



Run the following command:

yum install perl



Ubuntu

Debian



linux-headers
linux-image
gcc
make
perl



Run the following commands:

sudo apt-get update
sudo apt-get install linux-headers-$(uname -r)
sudo apt-get install linux-image-$(uname -r)
sudo apt-get install gcc-<package version>
sudo apt-get install make
sudo apt-get install perl



SUSE Linux

OpenSUSE



kernel-source
gcc
make
perl


sudo zypper install kernel-source
sudo zypper install gcc
sudo zypper install make
sudo zypper install perl

The packages will be downloaded from the distribution's repository and installed.

For other Linux distributions, see the distribution's documentation regarding the exact names of the required packages and the ways to install them.

Installing the packages manually

You may need to install the packages manually if:

The machine does not have an active Red Hat subscription or Internet connection.
The setup program cannot find the kernel-devel or gcc version corresponding to the kernel version. If the available kernel-devel is more recent than your kernel, you need to either update the kernel or install the matching kernel-devel version manually.
You have the required packages on the local network and do not want to spend time for automatic search and downloading.

Obtain the packages from your local network or a trusted third-party website, and install them as follows:

In Red Hat Enterprise Linux, CentOS, or Fedora, run the following command as the root user:

rpm -ivh PACKAGE_FILE1 PACKAGE_FILE2 PACKAGE_FILE3

In Ubuntu, run the following command:

sudo dpkg -i PACKAGE_FILE1 PACKAGE_FILE2 PACKAGE_FILE3
Example: Installing the packages manually in Fedora 14

Follow these steps to install the required packages in Fedora 14 on a 32-bit machine:

Run the following command to determine the kernel version and the required GCC version:

cat /proc/version

The output of this command includes the following:

Linux version 2.6.35.6-45.fc14.i686
gcc version 4.5.1

Obtain the kernel-devel and gcc packages that correspond to this kernel version:

kernel-devel-2.6.35.6-45.fc14.i686.rpm
gcc-4.5.1-4.fc14.i686.rpm

Obtain the make package for Fedora 14:

make-3.82-3.fc14.i686

Install the packages by running the following commands as the root user:

rpm -ivh kernel-devel-2.6.35.6-45.fc14.i686.rpm
rpm -ivh gcc-4.5.1.fc14.i686.rpm
rpm -ivh make-3.82-3.fc14.i686

You can specify all these packages in a single rpm command. Installing any of these packages may require installing additional packages to resolve dependencies.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.