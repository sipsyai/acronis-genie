# Creating bootable media to recover operating systems

Managing the backup and recovery of workloads and files > Creating bootable media to recover operating systems
Creating bootable media to recover operating systems

Bootable media is a CD, DVD, USB flash drive, or other removable media that allows you to run the protection agent either in a Linux-based environment or a Windows Preinstallation Environment/Windows Recovery Environment (WinPE/WinRE), without the help of an operating system. The main purpose of the bootable media is to recover an operating system that cannot start.

Bootable media does not support hybrid drives.

Running the bootable media requires 1.5 GB of RAM.

Custom or ready-made bootable media?

By using Bootable Media Builder, you can create custom bootable media (Linux-based or WinPE-based) for Windows, Linux, or macOS computers. In the both Linux-based and WinPE/WinRE-based custom bootable media, you can configure additional settings, such as automatic registration, network settings, or proxy server settings. In the WinPE/WinRE-based custom bootable media, you can also add additional drivers.

Alternatively, you can download a ready-made bootable media (Linux-based only). You can use the ready-made bootable media for recovery operations and access to the Universal Restore feature.

Linux-based or WinPE/WinRE-based bootable media?
Linux-based

Linux-based bootable media contains a protection agent based on a Linux kernel. The agent can boot and perform operations on any PC-compatible hardware, including bare metal, and machines with corrupted or non-supported file systems.

WinPE/WinRE-based

WinPE-based bootable media contains a minimal Windows system called Windows Preinstallation Environment (WinPE) and a Cyber Protection plugin for WinPE. This plugin is a modification of the protection agent, and can run in the preinstallation environment. WinRE-based bootable media uses Windows Recovery Environment, and does not require installation of additional Windows packages.

WinPE proved to be the most convenient bootable solution in large environments with heterogeneous hardware.

Advantages:

Using Cyber Protection in Windows Preinstallation Environment provides more functionality than using Linux-based bootable media. After booting PC-compatible hardware into WinPE, you can use the protection agent, WinPE commands and scripts, and any plugins that you have added to the PE.
PE-based bootable media helps overcome some Linux-related bootable media issues, such as support for certain RAID controllers or certain levels of RAID arrays only. Media based on WinPE 2.x and later allows dynamic loading of the necessary device drivers.

Limitations:

Bootable media based on WinPE versions earlier than 4.0 cannot boot on machines that use Unified Extensible Firmware Interface (UEFI).

Creating physical bootable media

Bootable Media Builder

Connecting to a machine booted from bootable media

Local operations with bootable media

Remote operations with bootable media

NIC teaming support

Startup Recovery Manager

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.