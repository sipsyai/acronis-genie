---
title: "Installing and uninstalling protection agents in Windows via CLI"
section: "Installing and deploying Cyber Protection agents"
subsection: "Installing and uninstalling protection agents by using the command-line interface"
page_range: "71-75"
tags: ["installation", "CLI", "command-line", "Windows", "unattended", "EXE", "MSI", "parameters"]
acronis_version: "26.02"
---

# Installing and uninstalling protection agents in Windows via CLI

In Windows, you can perform unattended installation or uninstallation in the following ways:

- By using the EXE file of the setup program and specifying the installation parameters on the command line.
- By using an MSI file that you extract from the setup program, and specifying the installation parameters in one of the following ways:
  - In an MST file
  - Directly on the command line

## Unattended installation and uninstallation with an EXE file

For this type of unattended installation, download the setup program, and then start it from the command line with the required installation parameters.

You do not need to extract installation packages, MSI, and MST files in advance.

### To install agents and components

1. Start the command-line interface as administrator, and then navigate to the EXE file of the setup program.
2. To start the setup program and specify the installation parameters, run the following command:

   ```
   <file path>/<EXE file><PARAMETER 1>=<value 1> ... <PARAMETER N>=<value n>
   ```

   Use spaces to separate the parameters, and commas without spaces to separate the values for a parameter. For example:

   ```
   C:\Users\Administrator\Downloads\AgentForWindows_web.exe --add-components=agentForWindows,agentForSql,commandLine --install-dir="C:\Program Files\BackupClient" --reg-address=https://eu2.company.cloud --reg-token=34F6-8C39-4A5C --quiet
   ```

### Examples

- Installing Agent for Windows, Agent for Antimalware protection and URL filtering, Command-Line Tool, and Cyber Protect Monitor. Registering by user name and password:

  ```
  AgentForWindows_web.exe --add-components=agentForWindows,agentForAmp,commandLine,trayMonitor --install-dir="C:\Program Files\BackupClient" --agent-account=system --reg-address=https://company.cloud --reg-login=johndoe --reg-password=johnspassword
  ```

- Installing Agent for Windows, Command-Line Tool, and Cyber Protect Monitor. Creating a new logon account. Registering by using a token:

  ```
  AgentForWindows_web.exe --add-components=agentForWindows,commandLine,trayMonitor --install-dir="C:\Program Files\BackupClient" --agent-account=new --reg-address=https://eu2.company.cloud --reg-token=34F6-8C39-4A5C
  ```

- Installing Agent for Windows, Command-Line Tool, Agent for Oracle and Cyber Protect Monitor. Registering by user name and password:

  ```
  AgentForWindows_web.exe --add-components=agentForWindows,commandLine,agentForOracle,trayMonitor --install-dir="C:\Program Files\BackupClient" --language=en --agent-account=system --reg-address=https://company.cloud --reg-login=johndoe --reg-password=johnspassword
  ```

- Setting the user interface language to German. Registering by token with HTTP proxy:

  ```
  AgentForWindows_web.exe --add-components=agentForWindows,commandLine,agentForOracle,trayMonitor --install-dir="C:\Program Files\BackupClient" --language=de --agent-account=system --reg-address=https://eu2.company.cloud --reg-token=34F6-8C39-4A5C --http-proxy-address=https://my-proxy.company.com:80 --http-proxy-login=tomsmith --http-proxy-password=tomspassword
  ```

### To remove an installed component

1. Start the command-line interface as administrator, and then navigate to `%ProgramFiles%\BackupClient\RemoteInstall`.
2. Run the following command:

   ```
   web_installer.exe --remove-components=<value 1>,<value 2> --quiet
   ```

### To uninstall an agent

1. Start the command-line interface as administrator, and then navigate to `%Program Files%\Common Files\Acronis\BackupAndRecovery`.
2. Run the following command:

   ```
   Uninstaller.exe --quiet --delete-all-settings
   ```

### Uninstallation examples

- Uninstalling Agent for Windows and all its components. Deleting all logs, tasks, and configuration settings:

  ```
  "C:\Program Files\Common Files\Acronis\BackupAndRecovery\Uninstaller.exe" --quiet --delete-all-settings
  ```

- Uninstalling a password-protected Agent for Windows and all its components:

  ```
  "C:\Program Files\Common Files\Acronis\BackupAndRecovery\Uninstaller.exe" --anti-tamper-password=<password> --quiet --delete-all-settings
  ```

## Parameters for unattended installation (EXE)

### General parameters

| Parameter | Description |
|-----------|-------------|
| `--add-components=<component1,component2,...>` | The components to be installed. See the full list in "Components for unattended installation (EXE)" (p. 78). Separate with commas, no spaces. If not specified, a default set of components will be installed. |
| `--install-dir=<path>` | Installation folder. Default: `C:\Program Files\BackupClient`. |
| `--log-dir=<path>` | Folder for installation logs. Default: `%ProgramData%\Acronis\InstallationLogs`. |
| `--language=<code>` | Product language. Available: en, bn, bg, cs, da, de, es, fr, ko, id, it, hi, hu, ms, nl, ja, nb, pl, pt, pt_BR, ru, fi, sr, sv, th, tr, vi, zh, zh_TW. |
| `--quiet` | Run the setup program without showing the graphical user interface. Do not use with `--register-only`. |
| `--help` | See a list of all available parameters and their descriptions. |
| `--fss-onboarding-auto-start` | Use with `--quiet` to show the File Sync & Share on-boarding wizard after an unattended installation. |
| `--fips={enabled \| disabled}` | Install the agent in FIPS-compliant mode. |

### Registration parameters

| Parameter | Description |
|-----------|-------------|
| `--registration={skip \| by-credentials \| by-token \| device-flow}` | Choose how to register the agent. `skip` — register later with `--register-only`. `by-credentials` — use `--reg-login` and `--reg-password`. `by-token` — use `--reg-token`. `device-flow` — OAuth 2.0 (opens registration page; do not use with `--quiet`). |
| `--reg-address=<url>` | The URL of the Cyber Protection service. |
| `--reg-login=<username>` | User name for the Cyber Protection service. |
| `--reg-password=<password>` | Password for the Cyber Protection service. |
| `--reg-token=<token>` | Registration token. |
