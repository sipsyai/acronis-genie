# Deploying Qcow2 Template Nutanix

Installing and deploying Cyber Protection agents > Deploying virtual appliances > Deploying Agent for Nutanix AHV > Deploying the QCOW2 template
Deploying the QCOW2 template

You can deploy the Nutanix virtual appliance by creating a virtual machine in the Nutanix cluster and deploying the QCOW template that you download from the Cyber Protect console.

You must deploy at least one virtual appliance per cluster.

To deploy the QCOW2 template

Log in to the Cyber Protect console.

Click Devices > All devices > Add > Nutanix AHV.

A ZIP archive is downloaded to your machine.

Unpack the ZIP archive and extract the QCOW2 image file.

Log in to the Nutanix Prism Element console as an administrator.

Upload the QCOW2 image file to the Nutanix Prism Element console.

Go to Settings and then, under General, select Image configuration.
Click Upload image.
Specify a name for the image.
In Image Type, select Disk.
Click Upload a file, and then click Choose file.
Select the QCOW2 image that you downloaded from the Cyber Protect console.
Click Save.

In the Nutanix Prism Element console, create a new virtual machine by using the QCOW2 image.

Go to VM, and then click Create VM.
Specify a name for the virtual machine.
In Compute Details, specify 4 vCPUs (single core) or 2 vCPUs with 2 cores each, and 8 GiB of memory.
In Disks, click Add New Disk.
In Operation, select Clone from Image Service.
In Image, select the image that you uploaded to the Nutanix Prism Element console.
Click Add.
In Network adapters (NIC), click Add New NIC.
Configure the network settings, and then click Add.

To hide the virtual appliance in the Cyber Protect console, in Description, specify the following:

{AB53A0F1-AD54-480f-80BB-FC72DC41DF53}

This will prevent you from accidentally applying protection plans to the appliance itself and including it in dynamic groups.

Click Save.

On the VM > Table tab, right-click the virtual machine that you created, and then select Power on.

As a result, the virtual appliance is deployed and powered on.

Next, configure the virtual appliance. See Configuring the Nutanix virtual appliance.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.