# Accessing a virtual appliance via an SSH client

Installing and deploying Cyber Protection agents > Deploying virtual appliances > SSH connections to a virtual appliance > Accessing a virtual appliance via an SSH client
Accessing a virtual appliance via an SSH client
Prerequisites
An SSH client must be available on the remote machine. The procedure below uses the WinSCP client as an example. You can use any SSH client, by adapting the steps accordingly.
The Secure Shell daemon (sshd) must be started on the virtual appliance. For more information, see Starting the Secure Shell daemon.

To access a virtual appliance via WinSCP

On the remote machine, open WinSCP.
Click Session > New Session.
In File protocol, select SCP.
In Host name, specify the IP address of your virtual appliance.
In User name and Password, specify root and the password for the root user.
Click Login.

A list of all directories on the virtual appliance is shown.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.