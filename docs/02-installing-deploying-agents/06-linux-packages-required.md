---
title: "Linux packages required for installation of agents in Linux"
section: "Installing and deploying Cyber Protection agents"
subsection: "Before you start"
page_range: "47-50"
tags: ["linux", "packages", "kernel", "gcc", "installation", "prerequisites", "RHEL", "CentOS", "Ubuntu", "Debian", "SUSE"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#linux-packages.html"
---

# Linux packages required for installation of agents in Linux

To add the necessary modules to the Linux kernel, the agent installer needs the following Linux packages:

- The package with kernel headers or sources. The package version must match the kernel version.
- The GNU Compiler Collection (GCC) compiler system. The GCC version must be the one with which the kernel was compiled.
- The Make tool.
- The Perl interpreter.
- The `libelf-dev`, `libelf-devel`, or `elfutils-libelf-devel` libraries for building kernels starting with 4.15 and configured with `CONFIG_UNWINDER_ORC=y`. For some distributions, such as Fedora 28, they need to be installed separately from kernel headers.

The names of these packages vary depending on your Linux distribution.

In Red Hat Enterprise Linux, CentOS, and Fedora, the packages normally will be installed by the setup program. In other distributions, you need to install the packages if they are not installed or do not have the required versions.

## Are the required packages already installed?

To check whether the packages are already installed, perform these steps:

1. Run the following command to find out the kernel version and the required GCC version:

   ```
   cat /proc/version
   ```

   This command returns lines similar to the following: `Linux version 2.6.35.6` and `gcc version 4.5.1`

2. Run the following command to check whether the Make tool and the GCC compiler are installed:

   ```
   make -v
   gcc -v
   ```

   For **gcc**, ensure that the version returned by the command is the same as in the `gcc version` in step 1. For **make**, just ensure that the command runs.

3. Check whether the appropriate version of the packages for building kernel modules is installed:
   - In Red Hat Enterprise Linux, CentOS, and Fedora, run the following command:

     ```
     yum list installed | grep kernel-devel
     ```

   - In Ubuntu, run the following commands:

     ```
     dpkg --get-selections | grep linux-headers
     dpkg --get-selections | grep linux-image
     ```

   In either case, ensure that the package versions are the same as in `Linux version` in step 1.

4. Run the following command to check whether the Perl interpreter is installed:

   ```
   perl --version
   ```

   If you see the information about the Perl version, the interpreter is installed.

5. In Red Hat Enterprise Linux, CentOS, and Fedora, run the following command to check whether `elfutils-libelf-devel` is installed:

   ```
   yum list installed | grep elfutils-libelf-devel
   ```

## Installing the packages from the repository

| Linux distribution | Package names | How to install |
|-------------------|---------------|----------------|
| Red Hat Enterprise Linux | kernel-devel, gcc, make, elfutils-libelf-devel | The setup program will download and install the packages automatically by using your Red Hat subscription. |
| | perl | `yum install perl` |
| CentOS, Fedora | kernel-devel, gcc, make, elfutils-libelf-devel | The setup program will download and install the packages automatically. |
| | perl | `yum install perl` |
| Ubuntu, Debian | linux-headers, linux-image, gcc, make | `sudo apt-get update` then `sudo apt-get install linux-headers-$(uname -r)` then `sudo apt-get install linux-image-$(uname -r)` then `sudo apt-get install gcc-<package version>` then `sudo apt-get install make` |
| | perl | `sudo apt-get install perl` |
| SUSE Linux, OpenSUSE | kernel-source, gcc, make, perl | `sudo zypper install kernel-source` then `sudo zypper install gcc` then `sudo zypper install make` then `sudo zypper install perl` |

The packages will be downloaded from the distribution's repository and installed.

## Installing the packages manually

You may need to install the packages **manually** if:

- The machine does not have an active Red Hat subscription or Internet connection.
- The setup program cannot find the **kernel-devel** or **gcc** version corresponding to the kernel version. If the available **kernel-devel** is more recent than your kernel, you need to either update the kernel or install the matching **kernel-devel** version manually.
- You have the required packages on the local network and do not want to spend time for automatic search and downloading.

Obtain the packages from your local network or a trusted third-party website, and install them as follows:

- In Red Hat Enterprise Linux, CentOS, or Fedora:

  ```
  rpm -ivh PACKAGE_FILE1 PACKAGE_FILE2 PACKAGE_FILE3
  ```

- In Ubuntu:

  ```
  sudo dpkg -i PACKAGE_FILE1 PACKAGE_FILE2 PACKAGE_FILE3
  ```
