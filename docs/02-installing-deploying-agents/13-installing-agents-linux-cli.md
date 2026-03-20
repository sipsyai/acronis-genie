---
title: "Installing and uninstalling protection agents in Linux via CLI"
section: "Installing and deploying Cyber Protection agents"
subsection: "Installing and uninstalling protection agents by using the command-line interface"
page_range: "88-94"
tags: ["installation", "CLI", "command-line", "Linux", "unattended", "parameters", "uninstall"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#unattended-installation-or-uninstallation-in-linux.html"
---

# Installing and uninstalling protection agents in Linux via CLI

This section describes how to install or uninstall protection agents in the unattended mode on a machine running Linux, by using the command line.

## Prerequisites

- You downloaded the installation file for Agent for Linux. The 64-bit installation package contains additional agents, such as Agent for Virtuozzo, Agent for Oracle, Agent for MySQL/MariaDB, and Agent for Proxmox. These agents depend on Agent for Linux and are installed with it.
- You installed the required Linux packages. See [Linux packages required](./06-linux-packages-required.md).
- At least 2 GB of free disk space is available on the machine.
- When installing the agent in SUSE Linux, ensure that you use `su -` instead of `sudo`.

## Limitations

- Some Linux distributions do not allow the installation of packages that are signed with SHA-1. In such cases, the installation fails with the message: 'Cannot find package Backup and Recovery Agent.'

## To install an agent

1. Open Terminal.
2. Do one of the following:
   - To start the installation by specifying parameters on the command line:

     ```
     <package name> -a <parameter 1> ... <parameter N>
     ```

   - To start the installation with parameters specified in a separate text file:

     ```
     <package name> -a --options-file=<path to the file>
     ```

     This approach might be useful if you do not want to enter sensitive information on the command line. Put each parameter on a new line, followed by the value for that parameter.

3. If UEFI Secure Boot is enabled on the machine, you are prompted to restart the system after the installation. Use the password for the root user. If this password is not accepted, use the word "acronis" as a password. During the system restart, opt for MOK management, select **Enroll MOK**, and then enroll the key.

## To uninstall an agent

1. Open Terminal.
2. Do one of the following:
   - To uninstall the agent and remove all logs, tasks, and configuration settings:

     ```
     /usr/lib/Acronis/BackupAndRecovery/uninstall/uninstall -a
     ```

   - To uninstall the agent but keep its ID (if you plan to install the agent later):

     ```
     /usr/lib/Acronis/BackupAndRecovery/uninstall/uninstall -a --no-purge
     ```

   - To uninstall the agent by using the installation file:

     ```
     <package name> -a -u
     ```

     > **Note:** Use this command only when the installation package is the same version as the installed agent and if `/usr/lib/Acronis/BackupAndRecovery/uninstall/uninstall` is corrupted or inaccessible.

## Unattended installation or uninstallation parameters

The minimal configuration for unattended installation includes `-a` and registration parameters (for example, `--login` and `--password` parameters; `--rain` and `--token` parameters).

### Installation parameters

#### Basic parameters

| Parameter | Description |
|-----------|-------------|
| `{-i \|--id=}<list of components>` | Components to install, separated by commas without spaces. Available in 64-bit (x86_64) package: `BackupAndRecoveryAgent` (Agent for Linux), `AgentForPCS` (Agent for Virtuozzo), `OracleAgentFeature` (Agent for Oracle), `MySQLAgentFeature` (Agent for MySQL/MariaDB), `AgentForProxmox` (Agent for Proxmox). Without this parameter, all components will be installed. |
| `{-a\|--auto}` | Installation and registration will complete without any further user interaction. You must specify the account under which the agent will be registered. |
| `{-t\|--strict}` | Any warning during the installation results in installation failure. |
| `{-n\|--nodeps}` | Absence of required Linux packages will be ignored during installation. |
| `{-d\|--debug}` | Writes the installation log in verbose mode. |
| `--options-file=<location>` | Installation parameters will be read from a text file instead of the command line. |
| `--language=<language ID>` | The product language. Available: en, bg, cs, da, de, es, fr, hu, id, it, ja, ko, ms, nb, nl, pl, pt, pt_BR, ru, fi, sr, sv, th, tr, vi, zh, zh_TW. |

### Registration parameters

| Parameter | Description |
|-----------|-------------|
| `{-g\|--login=}<user name>` and `{-w\|--password=}<password>` | Credentials for the account under which the agent will be registered in the Cyber Protection service. Cannot be a partner administrator account. |
| `--token=<token>` | Registration token (12 characters, separated by hyphens in three segments). When using `--token`, you must also include the `{-C\|--rain=}` parameter and specify the exact datacenter address. |
| `{-C\|--rain=}<service address>` | The URL of the Cyber Protection service. Must use the exact datacenter address when using `--token`. |
| `--register-with-credentials` | The installer's graphical interface will start. Enter user name and password for registration. |
| `--skip-registration` | Install the agent but register it in the Cyber Protection service later. |

### Additional parameters

| Parameter | Description |
|-----------|-------------|
| `--http-proxy-host=<IP address>` and `--http-proxy-port=<port>` | HTTP proxy server for backup and recovery from the cloud. |
| `--http-proxy-login=<login>` and `--http-proxy-password=<password>` | Credentials for the HTTP proxy server. |
| `--tmp-dir=<location>` | Folder for temporary files during installation. Default is `/var/tmp`. |
| `{-s\|--disable-native-shared}` | Redistributable libraries will be used during installation even if present on the system. |
| `--skip-prereq-check` | No check for required snapapi compilation packages. |
| `--force-weak-snapapi` | Use a ready-made snapapi module instead of compiling one (not recommended). |
| `--skip-svc-start` | Services will not start automatically after installation. |

### Information parameters

| Parameter | Description |
|-----------|-------------|
| `{-?\|--help}` | Shows the description of parameters. |
| `--usage` | Shows brief description of command usage. |
| `{-v\|--version}` | Shows the installation package version. |
| `--product-info` | Shows the product name and the installation package version. |
| `--snapapi-list` | Shows available ready-made snapapi modules. |
| `--components-list` | Shows the installer components. |

### Uninstallation parameters

| Parameter | Description |
|-----------|-------------|
| `{-u\|--uninstall}` | Uninstalls the product. |
| `--purge` | Uninstalls and removes all logs, tasks, and configuration settings. |

## Examples

- Installing Agent for Linux without registering it:

  ```
  ./Cyber_Protection_Agent_for_Linux_x86_64.bin -i BackupAndRecoveryAgent -a --skip-registration
  ```

- Installing Agent for Linux, Agent for Virtuozzo, and Agent for Oracle, registering by credentials:

  ```
  ./Cyber_Protection_Agent_for_Linux_x86_64.bin -a --login=johndoe --password=johnspassword
  ```

- Installing Agent for Oracle and Agent for Linux, registering by token:

  ```
  ./Cyber_Protection_Agent_for_Linux_x86_64.bin -i BackupAndRecoveryAgent,OracleAgentFeature -a --rain=https://eu2.company.cloud --token=34F6-8C39-4A5C
  ```

- Installing with configuration settings in a separate text file:

  ```
  ./Cyber_Protection_Agent_for_Linux_x86_64.bin -a --options-file=/home/mydirectory/configuration_file
  ```

- Uninstalling Agent for Linux and all agents, removing all their logs, tasks, and configuration settings:

  ```
  ./Cyber_Protection_Agent_for_Linux_x86_64.bin -a --purge
  ```
