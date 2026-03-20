---
title: "Unattended installation with MSI files"
section: "Installing and deploying Cyber Protection agents"
subsection: "Installing and uninstalling agents via MSI and MST"
page_range: "76-82"
tags: ["installation", "MSI", "MST", "Windows", "CLI", "unattended", "msiexec", "parameters", "components"]
acronis_version: "26.02"
---

# Unattended installation with MSI files

This section covers additional Windows CLI parameters for registration, logon accounts, vCenter/ESXi, proxy settings, and uninstallation, as well as the MSI-based installation workflow.

## Additional CLI parameters (EXE)

### Registration parameters

| Parameter | Description |
|-----------|-------------|
| `--reg-login=<login>` / `--reg-password=<password>` | Credentials for the account under which the agent will be registered. Cannot be a partner administrator account. When using these parameters, `--registration` is optional. Do not use with `--reg-token`. |
| `--reg-token=<token>` | The registration token (12 characters, separated into three segments by hyphens). When using this parameter, `--registration` is optional. Do not use with `--reg-login` and `--reg-password`. |
| `--register-only` | Skip installation and register the agent using OAuth 2.0 protocol (device-flow). After installation completes, the registration page opens automatically. Do not use with `--quiet`. |

### Logon account for the agent service

| Parameter | Description |
|-----------|-------------|
| `--agent-account={system \| new \| custom}` | Specify the logon account under which agent service will run. Use `system` or omit for **Local System** account. Use `new` to create a new **Acronis Agent User** account automatically. Use `custom` with `--agent-account-login` and `--agent-account-password` to specify an existing account. |

### vCenter/ESXi parameters

| Parameter | Description |
|-----------|-------------|
| `--esxi-address=<host>` | Host name or IP address of vCenter Server or ESXi host. Use when installing Agent for VMware. |
| `--esxi-login=<login>` / `--esxi-password=<password>` | Access credentials to vCenter Server or ESXi host. |

### Proxy parameters

| Parameter | Description |
|-----------|-------------|
| `--http-proxy={none \| system \| custom}` | Specify the HTTP proxy server for backup and recovery from cloud storage. Use `none` to disable, `system` or omit to use system-wide proxy, `custom` with address/login/password parameters for a custom proxy. |
| `--http-proxy-address=<host>:<port>` | Hostname or IP address and port of the custom HTTP proxy server. |
| `--http-proxy-login=<login>` | Login for the custom HTTP proxy server. |
| `--http-proxy-password=<password>` | Password for the custom HTTP proxy server. |

### Uninstallation parameters

| Parameter | Description |
|-----------|-------------|
| `--remove-components=<component1,...>` | Components to uninstall. To uninstall the product completely, use Windows Control Panel. |
| `--delete-all-settings` | Optional parameter to delete all product logs, tasks, and configuration settings when using `--remove-components`. |
| `--anti-tamper-password=<password>` | Password required for uninstalling a password-protected Agent for Windows or modifying its components. |

## Components for unattended installation (EXE)

Use these value names with the `--add-components` parameter:

| Value name | Component |
|-----------|-----------|
| `agentForWindows` | Agent for Windows |
| `agentForSas` | Agent for Files Sync & Share |
| `agentForAd` | Agent for Active Directory |
| `agentForAmp` | Agent for Antimalware protection and URL filtering |
| `agentForDlp` | Agent for Data Loss Prevention |
| `agentForEsx` | Agent for VMware (Windows) |
| `agentForExchange` | Agent for Exchange |
| `agentForHyperV` | Agent for Hyper-V |
| `agentForOffice365` | Agent for Office 365 |
| `agentForOracle` | Agent for Oracle |
| `agentForSql` | Agent for SQL |
| `commandLine` | Command-Line Tool |
| `mediaBuilder` | Bootable Media Builder |
| `trayMonitor` | Cyber Protect Monitor |
| `all` | All components combined |
| `allAgents` | All agents combined |

## Unattended installation and uninstallation with an MSI file

For MSI-based unattended installation, use the Windows Installer (`msiexec` program). Extract the installation packages and the MSI file in advance using the graphical user interface of the setup program.

When you install components with an MSI file, you can use an MST transform file to customize the installation parameters, or specify parameters directly on the command line.

### Extracting the MSI, MST, and CAB files

1. Run the setup program GUI, then click **Create .mst and .msi files for unattended installation**.
2. In **What to install**, select the components to install, then click **Done**.
3. In **Registration settings**, select **Use credentials** or **Use registration token**, provide the details, then click **Done**.
4. (Only on a domain controller) In **Logon account for the agent service**, select **Use the following account** and specify the user account, then click **Done**.
5. Review or modify installation settings that will be added to the MST file, then click **Proceed**.
6. Select the output folder and click **Generate**.

### Installing agents and components (MSI and MST combination)

Use the MST file to customize the installation settings for the MSI file. Use this method when installing agents on multiple machines through Windows Group Policy.

```
msiexec /i <MSI file> TRANSFORMS=<MST file>
```

For example:

```
msiexec /i BackupClient64.msi TRANSFORMS=BackupClient64.msi.mst
```

### Installing and uninstalling agents and components (MSI and direct selection)

Run the MSI file directly, specifying installation parameters on the command line. In this case, you do not need the MST file.

```
msiexec /i <MSI file> <PARAMETER 1>=<value 1> ... <PARAMETER N>=<value n>
```

For example:

```
msiexec.exe /i BackupClient64.msi
ADDLOCAL=MmsMspComponents,BackupAndRecoveryAgent,CommandLineTool,TrayMonitor
TARGETDIR="C:\Program Files\BackupClient" REGISTRATION_
ADDRESS=https://eu2.company.cloud REGISTRATION_TOKEN=34F6-8C39-4A5C
```

### MSI installation examples

**Installing Agent for Windows, Antimalware, Command-Line Tool, and Cyber Protect Monitor with credentials:**

```
msiexec.exe /i BackupClient64.msi /l*v my_log.txt /qn
ADDLOCAL=MmsMspComponents,BackupAndRecoveryAgent,AmpAgentFeature,CommandLineTool,Tray
Monitor TARGETDIR="C:\Program Files\BackupClient" REBOOT=ReallySuppress MMS_USE_
SYSTEM_ACCOUNT=1 REGISTRATION_ADDRESS=https://company.cloud REGISTRATION_
LOGIN=johndoe REGISTRATION_PASSWORD=johnspassword
```

**Installing Agent for Windows, Command-Line Tool, and Cyber Protect Monitor with token and new logon account:**

```
msiexec.exe /i BackupClient64.msi /l*v my_log.txt /qn
ADDLOCAL=MmsMspComponents,BackupAndRecoveryAgent,CommandLineTool,TrayMonitor
TARGETDIR="C:\Program Files\BackupClient" REBOOT=ReallySuppress MMS_CREATE_NEW_
ACCOUNT=1 REGISTRATION_ADDRESS=https://eu2.company.cloud REGISTRATION_TOKEN=34F6-
8C39-4A5C
```

**Installing with token and HTTP proxy:**

```
msiexec.exe /i BackupClient64.msi /l*v my_log.txt /qn
ADDLOCAL=MmsMspComponents,BackupAndRecoveryAgent,CommandLineTool,TrayMonitor
TARGETDIR="C:\Program Files\BackupClient" REBOOT=ReallySuppress CURRENT_LANGUAGE=en
MMS_USE_SYSTEM_ACCOUNT=1 REGISTRATION_ADDRESS=https://eu2.company.cloud REGISTRATION_
TOKEN=34F6-8C39-4A5C HTTP_PROXY_ADDRESS=https://my-proxy.company.com HTTP_PROXY_
PORT=80 HTTP_PROXY_LOGIN=tomsmith HTTP_PROXY_PASSWORD=tomspassword
```

### Removing an installed component

```
msiexec /i <MSI file> REMOVE=<value 1>,<value 2> REBOOT=ReallySuppress /qn
```

Example -- removing Cyber Protect Monitor:

```
msiexec.exe /i BackupClient64.msi /l*v uninstall_log.txt REMOVE=TrayMonitor
REBOOT=ReallySuppress /qn
```

### Uninstalling an agent

```
msiexec /x <MSI file> /l*v uninstall_log.txt DELETE_ALL_SETTINGS=1
REBOOT=ReallySuppress /qn
```

To uninstall a password-protected agent:

```
msiexec.exe /x BackupClient64.msi /l*v uninstall_log.txt ANTI_TAMPER_
PASSWORD=<password> DELETE_ALL_SETTINGS=1 REBOOT=ReallySuppress /qn
```
