---
title: "MSI parameters and components for unattended installation"
section: "Installing and deploying Cyber Protection agents"
subsection: "Parameters and components for MSI unattended installation"
page_range: "83-87"
tags: ["MSI", "parameters", "components", "msiexec", "ADDLOCAL", "registration", "proxy", "uninstallation", "Windows"]
acronis_version: "26.02"
---

# MSI parameters and components for unattended installation

This section documents the full set of parameters available when using an MSI file for unattended installation, and the component value names for the `ADDLOCAL` parameter.

## Parameters for unattended installation (MSI)

You can also use additional `msiexec` parameters. For example, use `/qn` to prevent any GUI elements from showing.

### General parameters

| Parameter | Description |
|-----------|-------------|
| `ADDLOCAL=<component1,...,componentN>` | The components to be installed. Separate multiple components with commas (no spaces). You must extract the installation files for all components that you want to install. |
| `TARGETDIR=<path>` | The installation folder. Default: `C:\Program Files\BackupClient`. If the specified folder does not exist, it will be created. |
| `REBOOT=ReallySuppress` | Specify this parameter to install components without restarting the machine. |
| `/l*v <log file>` | Save a verbose log. Useful for investigating installation issues. |
| `CURRENT_LANGUAGE=<language ID>` | The product language. Available values: en, bn, bg, cs, da, de, es, fr, ko, id, it, hi, hu, ms, nl, ja, nb, pl, pt, pt_BR, ru, fi, sr, sv, th, tr, vi, zh, zh_TW. If not specified and the system language is in the list, the system language is used. Otherwise defaults to en. |
| `SKIP_SHA2_KB_CHECK={0,1}` | Set to 1 to skip the check for SHA2 code signing support update (KB4474419). If set to 0 or not specified, the installation fails if the update is not found on systems that require it. |
| `FSS_ONBOARDING_AUTO_START={0,1}` | Set to 1 to show the File Sync & Share on-boarding wizard after unattended installation. Default is 0 (wizard not shown). |
| `ENABLE_FIPS_COMPLIANCE_MODE={0,1}` | Set to 1 to install the agent in FIPS-compliant mode. |

### Registration parameters

| Parameter | Description |
|-----------|-------------|
| `REGISTRATION_ADDRESS` | The URL of the Cyber Protection service. When used with `REGISTRATION_LOGIN` and `REGISTRATION_PASSWORD`, specify the login address (e.g., `https://company.cloud`). When used with `REGISTRATION_TOKEN`, specify the exact datacenter address (e.g., `https://eu2.company.cloud`). Do not use `https://company.cloud` with the `REGISTRATION_TOKEN` parameter. |
| `REGISTRATION_LOGIN` / `REGISTRATION_PASSWORD` | Credentials for the account under which the agent will be registered. Cannot be a partner administrator account. Do not use with `REGISTRATION_TOKEN`. |
| `REGISTRATION_PASSWORD_ENCODED` | The password encoded in base64. Use this if the password contains special characters or blank spaces. |
| `REGISTRATION_TOKEN` | The registration token (12 characters, separated into three segments by hyphens). Do not use with `REGISTRATION_LOGIN` and `REGISTRATION_PASSWORD`. |
| `REGISTRATION_REQUIRED={0,1}` | If set to 1, the installation also fails if registration fails. If set to 0 or not specified, installation completes successfully even if registration fails. |

### Logon account for the agent service

| Parameter | Description |
|-----------|-------------|
| `MMS_USE_SYSTEM_ACCOUNT={0,1}` | Set to 1 to make the service run under the **Local System** logon account. |
| `MMS_CREATE_NEW_ACCOUNT={0,1}` | Set to 1 to create a new **Acronis Agent User** logon account automatically. |
| `MMS_SERVICE_USERNAME=<user name>` / `MMS_SERVICE_PASSWORD=<password>` | Specify an existing logon account under which the agent service will run. |

### vCenter/ESXi parameters

| Parameter | Description |
|-----------|-------------|
| `SET_ESX_SERVER={0,1}` | Use when installing Agent for VMware. If set to 0, Agent for VMware will not be connected to vCenter Server or an ESXi host. If set to 1, specify `ESX_HOST`, `EXT_USER`, `ESX_PASSWORD`. |
| `ESX_HOST=<host name>` | Host name or IP address of vCenter Server or ESXi host. |
| `ESX_USER=<user name>` / `ESX_PASSWORD=<password>` | Access credentials to vCenter Server or ESXi host. |

### Proxy parameters

| Parameter | Description |
|-----------|-------------|
| `HTTP_PROXY_ADDRESS=<IP address>` / `HTTP_PROXY_PORT=<port>` | Specify the HTTP proxy server address and port. If you do not use a proxy server, do not specify these parameters. |
| `HTTP_PROXY_LOGIN=<login>` / `HTTP_PROXY_PASSWORD=<password>` | Credentials for the HTTP proxy server. Use if the proxy requires authentication. |

### Uninstallation parameters

| Parameter | Description |
|-----------|-------------|
| `REMOVE={<component1,...> \| ALL}` | Components to uninstall. Separate multiple components with commas (no spaces). Set to `ALL` to remove all product components. |
| `DELETE_ALL_SETTINGS={0,1}` | Set to 1 to delete all product logs, tasks, and configuration settings. Optional, use with `REMOVE`. |
| `ANTI_TAMPER_PASSWORD=<password>` | Password required for uninstalling a password-protected Agent for Windows or modifying its components. |

## Components for unattended installation (MSI)

Use these value names with the `ADDLOCAL` parameter:

| Value name | Component description | Must be installed together with | Bitness |
|-----------|----------------------|-------------------------------|---------|
| `AgentFeature` | Core components for agents | -- | 32-bit/64-bit |
| `MmsMspComponents` | Core components for backup | `AgentFeature` | 32-bit/64-bit |
| `BackupAndRecoveryAgent` | Agent for Windows | `MmsMspComponents` | 32-bit/64-bit |
| `AmpAgentFeature` | Agent for Antimalware protection and URL filtering | `BackupAndRecoveryAgent` | 32-bit/64-bit |
| `DlpAgentFeature` | Agent for Data Loss Prevention | `BackupAndRecoveryAgent` | 32-bit/64-bit |
| `SasAgentFeature` | Agent for File Sync & Share | `TrayMonitor` | 32-bit/64-bit |
| `ArxAgentFeature` | Agent for Exchange | `MmsMspComponents` | 32-bit/64-bit |
| `ArsAgentFeature` | Agent for SQL | `BackupAndRecoveryAgent` | 32-bit/64-bit |
| `ARADAgentFeature` | Agent for Active Directory | `BackupAndRecoveryAgent` | 32-bit/64-bit |
| `ArxOnlineAgentFeature` | Agent for Microsoft 365 | `MmsMspComponents` | 32-bit/64-bit |
| `OracleAgentFeature` | Agent for Oracle | `BackupAndRecoveryAgent` | 32-bit/64-bit |
| `AcronisESXSupport` | Agent for VMware ESX(i) | `BackupAndRecoveryAgent` | 64-bit |
