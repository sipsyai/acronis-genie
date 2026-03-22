# Creating physical bootable media

Managing the backup and recovery of workloads and files > Creating bootable media to recover operating systems > Creating physical bootable media
Creating physical bootable media

We highly recommend that you create and test the bootable media as soon as you start using disk-level backup. Also, it is a good practice to re-create the media after each major update of the protection agent.

You can recover either Windows or Linux by using the same media. To recover macOS, create a separate media on a machine running macOS.

To create physical bootable media in Windows or Linux

Create a custom bootable media ISO file or download the ready-made ISO file.

To create a custom ISO file, use Bootable Media Builder.

To download the ready-made ISO file, in the Cyber Protect console, select a machine, and then click Recover > More ways to recover... > Download ISO image.


[Optional] In the Cyber Protect console, generate a registration token. The registration token is displayed automatically when you download a ready-made ISO file.

This token allows the bootable media to access the cloud storage, without prompting you to enter a login and password.

Create physical bootable media in one of the following ways:

Burn the ISO file to a CD/DVD.

Create a bootable USB flash drive by using the ISO file and one of the free tools available online.

Use ISO to USB or RUFUS if you need to boot an UEFI machine, and Win32DiskImager for a BIOS machine. In Linux, using the dd utility makes sense.

For virtual machines, you can connect the ISO file as a CD/DVD drive to the machine that you want to recover.

To create physical bootable media in macOS

On a machine where Agent for Mac is installed, click Applications > Rescue Media Builder.

The software displays the connected removable media. Select the one that you want to make bootable.

All data on the disk will be erased.

Click Create.
Wait while the software creates the bootable media.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.