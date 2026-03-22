# Deploying the QCOW2 template

Installing and deploying Cyber Protection agents > Deploying virtual appliances > Deploying Agent for Virtuozzo Hybrid Infrastructure (Virtual Appliance) > Deploying the QCOW2 template
Deploying the QCOW2 template
Log in to your Cyber Protection account.

Click Devices > All devices > Add > Virtuozzo Hybrid Infrastructure.

The .zip archive is downloaded to your machine.

Unpack the .zip archive. It contains a .qcow2 image file.
Log in to your Virtuozzo Hybrid Infrastructure account.

Add the .qcow2 image file to the Virtuozzo Hybrid Infrastructure compute cluster as follows:

On the Compute > Virtual machines > Images tab, click Add image.
In the Add image window, click Browse, and then select the .qcow2 file.
Specify the image name, select the Generic Linux OS type, and then click Add.

In the Compute > Virtual machines > Virtual machines tab, click Create virtual machine. A window will open where you need to specify the following parameters:

A name for the new virtual machine.
In Deploy from, choose Image.
In the Images window, select the .qcow2 image file of the appliance, and then click Done.
In the Volumes window, you don’t need to add any volumes. The volume that is added automatically for the system disk is sufficient.
In the Flavor window, choose your desired combination of vCPUs and RAM, and then click Done. Usually, 2 vCPUs and 4 GiB of RAM are enough.
In the Network interfaces window, click Add, select the virtual network of type public, and then click Add. It will appear in the Network interfaces list.
If you use a setup with more than one physical network (and thus, with more than one virtual network of type public), repeat this step and select the virtual networks that you need.
Click Done.
Back in the Create virtual machine window, click Deploy to create and boot the virtual machine.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.