# Setting the root password on a virtual appliance

Installing and deploying Cyber Protection agents > Deploying virtual appliances > SSH connections to a virtual appliance > Setting the root password on a virtual appliance
Setting the root password on a virtual appliance

Before establishing an SSH connection to a virtual appliance for the first time, you must set the root password on the appliance.

To set the root password

In the hypervisor software, open the console of the virtual appliance.

In the graphical user interface of the appliance, press CTRL+SHIFT+F2 to open the command-line interface.

Run the following command:

passwd

Specify a password, and then press Enter.

The password must contain at least nine characters and must have complexity score of three or more. The complexity score is calculated automatically. To reach higher score, use a combination of special symbols, uppercase and lowercase symbols, and digits.

Confirm the password, and then press Enter.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.