---
title: "Connecting to discovered devices remotely and troubleshooting"
section: "Installing and deploying Cyber Protection agents"
subsection: "Device discovery"
page_range: "197-199"
tags: ["remote desktop", "RDP", "Apple Screen Sharing", "VNC", "troubleshooting", "device discovery", "Connect Client"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#connecting-to-discovered-devices.html"
---

# Connecting to discovered devices remotely and troubleshooting

## Connecting to discovered devices remotely

You can connect remotely to discovered Windows or macOS devices and provide one-time assistance.

### Prerequisites

- (For RDP connections) RDP is enabled on the Windows device.
- (For Apple Screen Sharing connections) Apple Screen Sharing is enabled on the macOS device.

### To connect remotely to a discovered device

1. In the Cyber Protect console, go to **Devices** > **Discovered devices**.
2. Click the device to which you want to connect remotely.
3. Click **Remote desktop**, and then, depending on the operating system of the device, click the view mode.

| Operating system | Connection protocol | View mode |
|------------------|-------------------|-----------|
| Windows | RDP | **Control** -- Observe and perform operations on the remote device. |
| macOS | Apple Screen Sharing | **Control** -- Observe and perform operations. |
| | | **View-only** -- Only observe the remote device. |
| | | **Curtain** -- Available only for macOS devices. The display of the remote device will be dimmed, and the remote user will not be able to see your actions. |

4. (If Connect Client is not installed on your device) In the **Connect to workload** dialog, click **Download Connect Client**, download and install the client, and then click **Connect**.
5. (If a confirmation pop-up appears) Click **Open Connect Client**.
6. (For Windows devices) In the **RDP Authentication** pop-up window, enter the username, password, and domain, and then click **Connect**.
7. (For macOS devices) In the **Authentication** window, select an authentication option, provide the required credentials, and then click **Connect**.

| Authentication option | Description |
|----------------------|-------------|
| **With macOS credentials** | Provide username and password of an administrator user of the remote device. |
| **by asking to observe** | Establish the remote connection in observe mode after the user who is logged in on the remote device allows it. |
| **with VNC password** | Establish the remote connection after you provide the VNC password. |

> **Note:** The authentication options that you will see depend on the screen sharing options that are configured on the remote macOS device.

## Troubleshooting device discovery

If you have any issues with the device discovery functionality, try to check the following:

- Check if NetBIOS over TCP/IP is enabled or set to default.
- In the "Control Panel\Network and Sharing Center\Advanced sharing settings", turn on Network discovery.
- Check if the Function Discovery Provider Host service is running on the machine that performs discovery and on the machines to be discovered.
- Check if the Function Discovery Resource Publication service is running on the machines to be discovered.
