---
title: "Installing protection agents by using the graphical user interface"
section: "Installing and deploying Cyber Protection agents"
subsection: null
page_range: "61-68"
tags: ["installation", "GUI", "Windows", "Linux", "macOS", "agent", "logon-account", "gMSA"]
acronis_version: "26.02"
---

# Installing protection agents by using the graphical user interface

## Installing protection agents in Windows

### Prerequisites

- An installation file of the protection agent is downloaded to the workload that you want to protect. See [Downloading protection agents](./05-downloading-agents.md).
- The workload that you want to protect is connected to the Internet.

### To install Agent for Windows

1. On the workload that you want to protect, log on as an administrator, and then open the installation file.
2. [Optional] Click **Customize installation settings**, and then configure the installation settings. The following options are available:
   - Changing the components to install (for example, disabling the installation of Cyber Protect Monitor or the Command-Line Tool, or installing the Agent for Antimalware protection and URL filtering).
   - Changing the components to install (for example, disabling the installation of Cyber Protect Monitor or the Command-Line Tool, or installing the Agent for Antimalware protection and URL filtering or the SIEM Log Forwarder feature).
   - Changing the method of registering the workload in the Cyber Protection service. You can switch from **Use service console** (default) to **Use credentials** or **Use registration token**.
   - Changing the installation path.
   - Changing the user account under which the agent service will run. See "Changing the logon account on Windows machines" below.
   - Verifying or changing the host name or IP address of a proxy server, the port, username, and password to access it.

   > **Note:** On Windows machines, the antimalware protection and URL filtering features require the installation of Agent for Antimalware protection and URL filtering. This agent is installed automatically for protected workloads if the **Antivirus & Antimalware protection** and/or the **URL filtering** options are enabled in their protection plans.
   >
   > **Note:** If a proxy server is enabled in Windows, it is automatically detected and used.

3. Click **Install**.
4. [Only when installing Agent for VMware] Specify the address and access credentials for the vCenter Server or the stand-alone ESXi host on which you want to back up and recover virtual machines, and then click **Done**. We recommend that you use a dedicated account for accessing vCenter Server or the ESXi host.
5. [Only when installing on a domain controller] Specify the user account under which the agent service will run, and then click **Done**. For security reasons, the setup program does not automatically create new accounts on a domain controller.
6. [If you selected the default registration method **Use service console**] Wait until the registration screen appears.
7. Register the agent under a user account in a customer tenant. See "Registering workloads by using the graphical user interface" (p. 106).
8. [If you registered the agent in a tenant that uses Compliance mode] Set the encryption password.

### Changing the logon account on Windows machines

On the **Select agent components** tab, define the account under which the services will run by specifying **Logon account for the agent service**. You can select one of the following:

- **Use Service User Accounts** (default for the agent service) — Service User Accounts are Windows system accounts that are used to run services. The advantage is that the domain security policies do not affect these accounts' user rights. By default, the agent runs under the **Local System** account.
- **Create a new account** — The account name will be Agent User for the agent.
- **Use the following account** — If you install the agent on a domain controller, the system prompts you to specify existing accounts (or the same account) for the agent. For security reasons, the system does not automatically create new accounts on a domain controller.

> **Important:** Note that we do not recommend changing the logon accounts manually after the installation is completed.

### Privileges required for the logon account

The Cyber Protection agent for Windows is run as a Managed Machine Service (MMS) on protected Windows machines. The account under which the agent will run must have specific rights for the agent to work correctly. The MMS user account should be configured as follows:

1. Included in the **Backup Operators** and **Administrators** groups. On a Domain Controller, the user must be included in the group **Domain Admins**.
2. Granted the **Full Control** permission on the folder `%PROGRAMDATA%\Acronis` and on its subfolders.
3. Granted the **Full Control** permission on certain registry keys in: `HKEY_LOCAL_MACHINE\SOFTWARE\Acronis`.
4. Assigned the following user rights:
   - Log on as a service
   - Adjust memory quotas for a process
   - Replace a process level token
   - Modify firmware environment values

### Using gMSA accounts with the Cyber Protection agent

Group Managed Service Accounts (gMSA) can be used to run services on multiple servers without having to manage the password.

1. Create a gMSA following the standard procedure documented in the Microsoft knowledge base.
2. Configure the gMSA as described in "Privileges required for the logon account" above.
3. Assign the logon account for the MMS service on the machine where the agent runs:
   a. Open the Windows Start menu, and enter `services.msc` to open the list of local services.
   b. Right-click the **Acronis Managed Machine Service** and click **Properties**.
   c. On the **Log On** tab, select **This account** and then click **Browse** to find the gMSA that you want to use.
   d. Click **OK**.
4. Apply protection plans as needed.

---

## Installing protection agents in Linux

You can install Agent for Linux by running its installation file on a local machine.

### Prerequisites

- You downloaded the installation file for Agent for Linux. The 64-bit installation package contains additional agents, such as Agent for Virtuozzo, Agent for Oracle, Agent for MySQL/MariaDB, and Agent for Proxmox. These agents depend on Agent for Linux and are installed with it.
- You installed the required Linux packages. See [Linux packages required](./06-linux-packages-required.md).
- At least 2 GB of free disk space is available on the machine.
- When installing the agent in SUSE Linux, ensure that you use `su -` instead of `sudo`.

### Limitations

- Some Linux distributions do not allow the installation of packages that are signed with SHA-1. In such cases, the installation fails with the following message: 'Cannot find package Backup and Recovery Agent.'

### To install Agent for Linux

1. Ensure that the machine is connected to the Internet.
2. As the root user, navigate to directory with the installation file, make the file executable, and then run it.

   ```
   chmod +x <installation file name>
   ./<installation file name>
   ```

   If a proxy server is enabled in your network, when running the installation file, specify the server host name/IP address and port in the following format: `--http-proxy-host=ADDRESS --http-proxy-port=PORT --http-proxy-login=LOGIN --http-proxy-password=PASSWORD`.

   If you want to change the default method of registering the machine in the Cyber Protection service, run the installation file with one of the following parameters:
   - `--register-with-credentials` — to ask for a user name and password during the installation
   - `--token=STRING` — to use a registration token
   - `--skip-registration` — to skip the registration

3. Select the check boxes for the agents that you want to install. The following agents are available in the 64-bit installation package:
   - Agent for Linux
   - Agent for Virtuozzo
   - Agent for Oracle
   - Agent for MySQL/MariaDB
   - Agent for Proxmox

4. If you kept the default registration method in step 2, proceed to the next step. Otherwise, enter the user name and password for the Cyber Protection service, or wait until the machine will be registered by using the token.
5. Register the agent under a user account in a customer tenant.
6. [If you registered the agent in a tenant that uses Compliance mode] Set the encryption password.
7. If the UEFI Secure Boot is enabled on the machine, you are informed that you need to restart the system after the installation. Use the password for the root user, or use the word "acronis" as a password. During the system restart, opt for MOK management, select **Enroll MOK**, and then enroll the key.
8. After the installation completes, click **Restart** (if prompted) or click **Exit**.

Troubleshooting information is provided in the file: `/usr/lib/Acronis/BackupAndRecovery/HOWTO.INSTALL`

---

## Installing protection agents in macOS

### Prerequisites

- An installation file of the protection agent is downloaded to the workload. See [Downloading protection agents](./05-downloading-agents.md).
- The workload that you want to protect is connected to the Internet.

### To install Agent for Mac (x64 or ARM64)

1. Ensure that the machine is connected to the Internet.
2. Double-click the installation file (.dmg).
3. Wait while the operating system mounts the installation disk image.
4. Double-click **Install**.
5. If a proxy server is enabled in your network, click **Protection Agent** in the menu bar, click **Proxy server settings**, and then specify the proxy server host name/IP address, port, and credentials.
6. If prompted, provide administrator credentials.
7. Click **Continue**.
8. Wait until the registration screen appears.
9. Register the agent under a user account in a customer tenant.
10. [If you registered the agent in a tenant that uses Compliance mode] Set the encryption password.
11. If your macOS version is Mojave 10.14.x or later, grant full disk access to the protection agent to enable backup operations.
12. To use the remote desktop functionality, grant the required system permissions to the Connect Agent. See [Granting the required system permissions to the Connect Agent](./08-dynamic-installation-and-permissions.md).
