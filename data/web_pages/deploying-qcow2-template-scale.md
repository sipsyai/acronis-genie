# Deploying Qcow2 Template Scale

Installing and deploying Cyber Protection agents > Deploying virtual appliances > Deploying Agent for Scale Computing HC3 (Virtual Appliance) > Deploying the QCOW2 template
Deploying the QCOW2 template
Log in to your Cyber Protection account.

Click Devices > All devices > Add > Scale Computing HyperCore.

The .zip archive is downloaded to your machine.

Unpack the .zip archive, and then save the .qcow2 file and the .xml file to a folder named ScaleAppliance.

Upload the ScaleAppliance folder to a network share and ensure that the Scale Computing HC3 cluster can access it.
Log in to the Scale Computing HC3 cluster as an administrator who has the VM Create/Edit role assigned. For more information about the roles required for operations with Scale Computing HC3 virtual machines, refer to Agent for Scale Computing HC3 – required roles.
In the Scale Computing HC3 web interface, import the virtual machine template from the ScaleAppliance folder.

Click the Import HC3 VM icon.

In the Import HC3 VM window, specify the following:

A name for the new virtual machine.

The network share on which the ScaleAppliance folder is located.

The user name and password required for accessing this network share.

A domain tag for the new virtual machine.

The path to the ScaleAppliance folder on the network share.

Click Import.

After the deployment completes, you must configure the virtual appliance. For more information on how to configure it, refer to Configuring the virtual appliance.

If you need more than one virtual appliance in your cluster, repeat the steps above and deploy additional virtual appliances. Do not clone an existing virtual appliance by using the Clone VM option in the Scale Computing HC3 web interface.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.