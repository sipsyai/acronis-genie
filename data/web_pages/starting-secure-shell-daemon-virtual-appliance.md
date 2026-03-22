# Starting the Secure Shell daemon

Installing and deploying Cyber Protection agents > Deploying virtual appliances > SSH connections to a virtual appliance > Starting the Secure Shell daemon
Starting the Secure Shell daemon

To allow SSH connections to a virtual appliance, start the Secure Shall daemon (sshd) on the appliance.

To start the Secure Shall daemon

In the hypervisor software, open the console of the virtual appliance.

In the graphical user interface of the appliance, press CTRL+SHIFT+F2 to open the command-line interface.

Run the following command:

/bin/sshd

[Only during the first connection to the appliance] Set the password for the root user.

To learn how to set the password, see Setting the root password on a virtual appliance.

We recommend that you stop the Secure Shell daemon when you do not use the SSH connection.



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.