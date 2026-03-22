# Changing the graphics adapter of a virtual appliance

Installing and deploying Cyber Protection agents > Deploying virtual appliances > Deploying Agent for oVirt (Virtual Appliance) > Changing the graphics adapter of a virtual appliance
Changing the graphics adapter of a virtual appliance

If you use an oVirt virtual appliance with Oracle Linux Virtualization Manager, you might receive the following error: "VM <name of the virtual appliance> is down with error. Exit message: unsupported configuration: domain configuration does not support video model 'qxl'."

To resolve this error, change the graphics adapter of the virtual appliance to CIRRUS.

To change the graphics adapter of a virtual appliance

Log in to Oracle Linux Administration Portal as an administrator.
Go to Compute > Virtual machines.
[If the virtual appliance is powered on] Right-click the virtual appliance, and then select Shutdown.
Right-click the virtual appliance, and then select Edit.
[If you see only the General tab] Click Show Advanced Options.
Click Console.
In Graphical Console, for Video Type, select CIRRUS.
Click OK.
In Oracle Linux Administration Portal, power on the virtual appliance.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.