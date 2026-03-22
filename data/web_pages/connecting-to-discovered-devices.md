# Connecting to discovered devices remotely

Installing and deploying Cyber Protection agents > Device discovery > Connecting to discovered devices remotely
Connecting to discovered devices remotely

You can connect remotely to discovered Windows or macOS devices and provide one-time assistance.

Prerequisites

[For RDP connections] RDP is enabled on the Windows device.
[For Apple Screen Sharing connections] Apple Screen Sharing is enabled on the macOS device.

To connect remotely to a discovered device

In the Cyber Protect console, go to Devices > Discovered devices.

Click the device to which you want to connect remotely.

Click Remote desktop, and then, depending on the operating system of the device, click the view mode.

Operating system	Connection protocol	View mode
Windows	RDP	Control - In this mode, you will be able to observe and perform operations on the remote device.
macOS	Apple Screen Sharing

Control - In this mode, you will be able to observe and perform operations on the remote device.

View-only - In this mode, you will only be able to observe the remote device.

Curtain - available only for macOS devices. If you connect to the remote device in curtain mode, the display of the remote device will be dimmed, and the remote user will not be able to see your actions on the device.

[If Connect Client is not installed on your device] In the Connect to workload dialog, click Download Connect Client, download and install the client on your device, and then click Connect.

[If a confirmation pop-up appears] Click Open Connect Client.

[For Windows devices] In the RDP Authentication pop-up window, enter the username, password, and domain, and then click Connect.

[For macOS devices]In the Authentication window, select an authentication option, provide the required credentials depending on the option that you selected, and then click Connect.

Authentication option	Description
With macOS credentials

You will be allowed to establish the remote connection after you provide username and password of an administrator user of the remote device.


by asking to observe

You will be allowed to establish the remote connection in observe mode after the user who is logged in on the remote device allows it.


with VNC password

You will be allowed to establish the remote connection after you provide the VNC password.

The authentication options that you will see depend on the screen sharing options that are configured on the remote macOS device.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.