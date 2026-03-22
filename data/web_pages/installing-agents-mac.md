# Installing protection agents in macOS

Installing and deploying Cyber Protection agents > Installing protection agents by using the graphical user interface > Installing protection agents in macOS
Installing protection agents in macOS

Prerequisites

An installation file of the protection agent is downloaded to the workload that you want to protect. See Downloading protection agents.
The workload that you want to protect is connected to the Internet.

To install Agent for Mac (x64 or ARM64)

Ensure that the machine is connected to the Internet.
Double-click the installation file (.dmg).
Wait while the operating system mounts the installation disk image.
Double-click Install.
If a proxy server is enabled in your network, click Protection Agent in the menu bar, click Proxy server settings, and then specify the proxy server host name/IP address, port, and credentials.
If prompted, provide administrator credentials.
Click Continue.
Wait until the registration screen appears.

Register the agent under a user account in a customer tenant. For more information about registration, see Registering workloads by using the graphical user interface.

[If you registered the agent in a tenant that uses Compliance mode] Set the encryption password.

If your macOS version is Mojave 10.14.x or later, grant full disk access to the protection agent to enable backup operations.

For instructions, see Grant the 'Full Disk Access' permission to the Cyber Protection agent (64657).

To use the remote desktop functionality, grant the required system permissions to the Connect Agent. For more information, see Granting the required system permissions to the Connect Agent.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.