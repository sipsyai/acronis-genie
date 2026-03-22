# Deploying the OVA template

Installing and deploying Cyber Protection agents > Deploying virtual appliances > Deploying Agent for oVirt (Virtual Appliance) > Deploying the OVA template
Deploying the OVA template

You can deploy the oVirt virtual appliance by creating a virtual machine in the Red Hat Virtualization/oVirt environment and deploying the QCOW template that you download from the Cyber Protect console.

If you need more than one virtual appliance in your environment, deploy additional virtual appliances. Do not clone an existing virtual appliance by using the Clone VM option in Red Hat Virtualization/oVirt Administration Portal.

To deploy the OVA template

Log in to the Cyber Protect console.

Click Devices > All devices > Add > Red Hat Virtualization (oVirt).

A ZIP archive is downloaded to your machine.

Unpack the ZIP archive and extract the OVA image file.
Upload the OVA file to a host in the Red Hat Virtualization/oVirt environment that you want to protect.
Log in to Red Hat Virtualization/oVirt Administration Portal as an administrator. For more information about the roles required for operations with virtual machines, see Agent for oVirt – required roles and ports.
From the navigation menu, select Compute > Virtual machines.
Click the vertical ellipsis icon  above the main table, and then click Import.

In the Import Virtual Machine(s) window, do the following:

In Data center, select the data center that you want to protect.

In Source, select Virtual Appliance (OVA).

In Host, select the host on which you uploaded the OVA file.

In File Path, specify the path to the directory that contains the OVA file.

Click Load.

The oVirt virtual appliance template from the OVA file appears in the Virtual Machines on Source panel.

If the template does not appear in this panel, ensure that you have specified the correct path to the file, the file is not damaged, and the host can be reached.

In Virtual Machines on Source, select the oVirt virtual appliance template, and then click the right arrow.

The template appears in the Virtual machines to import panel.

Click Next.

In the new window, click the appliance name, and then configure the following settings:

On the Network interfaces tab, configure the network interfaces.
On the General tab, change the default name of the virtual machine with the agent.

To hide the virtual appliance in the Cyber Protect console, assign the tag acronis_virtual_appliance to the virtual appliance.

This will prevent you from accidentally applying protection plans to the appliance itself and including it in dynamic groups.

The deployment is now complete. Next, you must configure the appliance. See Configuring the virtual appliance.

If you use an oVirt virtual appliance with Oracle Linux Virtualization Manager, you might receive the following error: "VM <name of the virtual appliance> is down with error. Exit message: unsupported configuration: domain configuration does not support video model 'qxl'." To resolve this error, change the graphics adapter of the virtual appliance to CIRRUS. See Changing the graphics adapter of a virtual appliance.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.