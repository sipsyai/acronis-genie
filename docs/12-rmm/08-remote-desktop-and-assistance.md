---
title: "Remote Desktop and Remote Assistance"
section: "RMM"
subsection: "Remote Desktop and Assistance"
page_range: "1340-1359"
tags: [rmm, remote-desktop, remote-assistance, near, rdp, apple-screen-sharing, connect-client, connect-agent, quick-assist, protocols, management-plans]
acronis_version: "26.02"
---

# Connecting to Workloads for Remote Desktop or Remote Assistance

The remote desktop and assistance functionality is a convenient way to connect to the workloads in your organization for remote control or remote assistance. The functionality supports the NEAR, RDP, and Apple Screen Sharing protocols.

To activate the complete remote desktop and assistance functionality for a managed workload, you must configure and apply a remote management plan to the workload. Only one remote management plan can be applied per workload.

## Prerequisites

- A one-time installation of **Connect Client** on the managing (host) workload
- Installation of **Connect Agent** on the managed workloads (part of the Protection agent from version 15.0.31266)
- For macOS: required system permissions must be granted to the Connect Agent
- For unmanaged workloads: the **Acronis Quick Assist** application must be running

## Remote Desktop Capabilities

- Connect to remote Windows, macOS, and Linux workloads using NEAR in view-only mode
- Connect to remote Windows workloads using RDP
- Connect to remote macOS workloads using Apple Screen Sharing in view-only or curtain mode
- Connect to managed workloads using cloud remote connections
- Connect to unmanaged workloads using direct remote connections or Acronis Quick Assist
- Observe multiple monitors at the same time in multi-view
- Record remote sessions (when connected via NEAR)
- View the session history report

## Remote Assistance Capabilities

- Connect to remote Windows, macOS, and Linux workloads using NEAR in control mode
- Connect to remote macOS workloads using Apple Screen Sharing in control mode
- Provide remote assistance to workloads using cloud remote connections
- Transfer files between the local and remote workloads
- Perform basic management actions on the remote workload: restart, shut down, sleep, empty recycle bin, and log out the remote user
- Monitor the remote workload by periodically taking screenshots of its desktop

## Supported Features by License

| Feature | Standard Protection | Security and RMM / RMM Service |
|---------|-------------------|-------------------------------|
| Remote actions | Yes | Yes |
| Selecting a session for Windows/macOS/Linux | No | Yes |
| Direct connect via RDP and Apple Screen Sharing | No | Yes |
| Multi-window control | No | Yes |
| Connection modes: Control/View-only/Curtain | No | Yes |
| Common credentials support | Yes | Yes |
| Concurrent connections via RDP | Yes | Yes |
| Concurrent connections via NEAR | No | Yes |
| File transfer (all platforms) | No | Yes |
| Quick Assist (all platforms) | No | Yes |
| Remote connection via NEAR (all platforms) | No | Yes |
| Remote connection via RDP (desktop/web client) | Yes | Yes |
| Remote connection via Apple Screen Sharing | No | Yes |
| Session recording | No | Yes |
| Session history and search | No | Yes |
| Screenshot transmission | No | Yes |
| File exchange via clipboard | No | Yes |

## Supported Operating Systems

| Component | Supported Platforms |
|-----------|-------------------|
| Connect Client | Windows 7+, macOS 10.13+, Linux (openSUSE 8, Debian 9/10, Ubuntu 18.0-20.10, RHEL 8, CentOS 8, Fedora 31-33, SUSE Linux Enterprise Server 15 SP2, Linux Mint 20, Manjaro 20) |
| Connect Agent | Windows 7+, Windows Server 2008 R2+, macOS 10.13+, Linux (RHEL 8/8.1, Fedora 30, Ubuntu 18.4/19.04, Debian 9/10, CentOS 8, openSUSE 15.1) |
| Acronis Quick Assist | Windows 7+, Windows Server 2008 R2+, macOS 10.13+, Linux (RHEL 8/8.1, Fedora 30, Ubuntu 18.4/19.04, Debian 9/10, CentOS 8, openSUSE 15.1) |

## Remote Connection Protocols

### NEAR
NEAR is a highly secure protocol developed by Acronis with the following characteristics:
- **H.264**: Three quality modes: Smooth, Balanced, and Sharp. Smooth mode uses hardware H.264 encoding, limited to Full HD (1920x1080)
- **Adaptive codec**: In Balanced and Sharp modes, provides full picture quality in 32 bit. Balanced mode auto-adjusts quality based on network conditions. Sharp mode provides full quality but may reduce framerate
- **Sound transfer**: Captures and transfers remote computer sound to host
- **Login options**: Access code, Workload credentials, or Ask for permission to observe or control
- **Security**: All data is always two-way encrypted with AES encryption

### RDP
Remote Desktop Protocol (RDP) is a proprietary protocol developed by Microsoft for connecting to remote Windows computers.

### Apple Screen Sharing
Apple Screen Sharing is a VNC client included as part of macOS version 10.5 and later.

## Connection Types

### Cloud Connections
Established between Connect Client and the agent or Quick Assist on the workload via Acronis Cloud.

| Protocol | View Mode | Supported Remote Action | Available For |
|----------|-----------|------------------------|---------------|
| via NEAR | Control, View-only | Remote desktop, Remote assistance | Managed workloads |
| via RDP | Control | Remote desktop | Managed workloads |
| via Apple Screen Sharing | Control, View-only, Curtain | Remote desktop, Remote assistance | Managed workloads |

### Direct Connections
Established via TCP/IP in the local area network (LAN) between Connect Client and the remote workload. They do not require Internet access.

| Protocol | Supported Remote Action | Available For |
|----------|------------------------|---------------|
| via RDP | Remote desktop | Unmanaged workloads |
| via Apple Screen Sharing | Remote desktop, Remote assistance | Unmanaged workloads |

## Remote Management Plans

Remote management plans are plans applied to the Protection agent to enable and configure the remote desktop and assistance functionality on managed workloads. If no plan is applied, functionality is limited to basic remote actions (restart, shut down, sleep, empty recycle bin, log out).

### Creating a Remote Management Plan

1. Go to **Management > Remote management plans**.
2. Click **Create** or **Create plan**.
3. (Optional) Change the plan name.
4. Click **Connection protocols** and enable NEAR, RDP, or Apple Screen Sharing.
5. (Optional) For NEAR, configure **Security settings**:
   - Lock workload when user disconnects from console session
   - Allow only one user at a time to connect using NEAR or transfer files
   - Allow workload administrator to connect to any non-admin user session
   - Allow system session creation (macOS)
   - Allow clipboard synchronization
6. Configure **Security settings** for notifications:
   - Show if the workload is controlled remotely
   - Ask for user's permission to take screenshots
7. Click **Workload management** to enable:
   - File transfer (Windows, macOS, Linux)
   - Screenshot transmission (Windows, macOS, Linux)
   - Geolocation tracking (Windows, macOS, Linux)
   - Chat (Windows, macOS)
8. Click **Display settings** (NEAR only):
   - Use Desktop Deduplication for desktop capturing (Windows)
   - Use OpenCL acceleration (Linux)
   - Use hardware H.264 encoding (Windows, macOS)
9. Click **Toolbox**:
   - Show last logged-in users (Windows, macOS, Linux)
   - Remote command-line interface (Windows, macOS)
10. (Optional) Add workloads to the plan.
11. Click **Create**.

### Managing Remote Management Plans

From the **Remote management plans** screen, you can perform additional actions: view details, edit, view activities, view alerts, rename, enable, disable, clone, export (JSON), import, set as favorite, set as default, and delete.
