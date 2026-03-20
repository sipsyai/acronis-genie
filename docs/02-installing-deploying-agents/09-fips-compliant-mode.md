---
title: "FIPS-compliant mode"
section: "Installing and deploying Cyber Protection agents"
subsection: null
page_range: "56-61"
tags: ["FIPS", "compliance", "security", "cryptography", "installation", "Windows", "Linux", "virtual-appliance"]
acronis_version: "26.02"
---

# FIPS-compliant mode

To meet compliance requirements, you can install and use protection agents in FIPS-compliant mode.

This mode uses only algorithms and cryptography libraries that are certified according to the Federal Information Processing Standards 140-2, as follows:

- [Windows] FIPS-certified Microsoft Cryptography API: Next Generation (CNG).
- [Linux] FIPS-certified BoringCrypto library.
- [Windows and Linux] FIPS-certified OpenSSL 3 module.

## Supported agents

The FIPS-compliant mode is supported by the following agents:

- **Agent for Windows** (on 64-bit operating systems). See the supported versions in "Agent for Windows" (p. 484).
  > **Note:** Agent for Windows (Legacy) does not support the FIPS-compliant mode.
- **Agent for Linux**. See the supported versions in "Agent for Linux" (p. 488).
- **Virtual appliances:**
  - Agent for VMware (Virtual Appliance)
  - Agent for Virtuozzo Hybrid Infrastructure
  - Agent for Scale Computing HC3
  - Agent for oVirt

## Limitations

- The following components or services are not FIPS-compliant:
  - File Sync & Share
  - Endpoint Detection and Response (EDR)
  - Disaster recovery
  - Data loss prevention (DLP)
  - Acronis Cyber Protect app (backup of mobile devices)
  - Physical data shipping
  - Web Restore console
- Virtual appliances in FIPS-compliant mode do not support SMB shares.
- Bootable media that is created by FIPS-compliant Agent for Windows or FIPS-compliant Agent for Linux does not support SMB shares.
- You can select the FIPS mode for Agent for Windows and Agent for Linux only during the installation. To change the FIPS mode later, run the installation file again and modify the installation.

## Installing Agent for Windows in FIPS-compliant mode

You can install Agent for Windows in FIPS-compliant mode by using the graphical user interface or command-line interface.

### Prerequisites

- Your workload has a 64-bit Windows operating system.
- The operating system of the workload is working in FIPS mode.
- You downloaded the installation file for Agent for Windows.

### Graphical user interface

1. On the machine on which you want to install the agent, run Command Prompt as an administrator.
2. In Command Prompt, navigate to the installation file.
3. To run the installation procedure in FIPS-compliant mode, run the following command:

   ```
   <file path>/<EXE file> --fips=enabled
   ```

   For example:

   ```
   C:\Users\Administrator\Downloads\AgentForWindows_web.exe --fips=enabled
   ```

4. [Optional] Click **Customize installation settings** to configure installation options.
5. Click **Install**.
6. [Only when installing Agent for VMware] Specify the address and access credentials for the vCenter Server or the stand-alone ESXi host.
7. [Only when installing on a domain controller] Specify the user account under which the agent service will run.
8. [If you selected the default registration method **Use service console**] Wait until the registration screen appears.
9. Register the agent under a user account in a customer tenant.
10. [If you registered the agent in a tenant that uses Compliance mode] Set the encryption password.

### Command-line interface

1. On the machine on which you want to install the agent, run Command Prompt as an administrator.
2. In Command Prompt, navigate to the installation file.
3. Run the following command:

   ```
   <file path>/<EXE file> --fips=enabled <PARAMETER 1>=<value 1>...<PARAMETER N>=<value n>
   ```

> **Note:** To install FIPS-compliant agents on multiple machines, you can use an MSI file that is created by a FIPS-compliant agent. See "Unattended installation and uninstallation with an MSI file" (p. 79).

## Installing Agent for Linux in FIPS-compliant mode

You can install Agent for Linux in FIPS-compliant mode by using the command-line interface.

### Prerequisites

- You have downloaded the installation package for Agent for Linux.

### To install Agent for Linux in FIPS-compliant mode

1. Open Terminal.
2. Do one of the following:
   - To install the agent by specifying parameters on the command line:

     ```
     <package name> -a --fips-mode=1 <parameter 1> ... <parameter N>
     ```

   - To install the agent with parameters specified in a separate text file:

     ```
     <package name> -a --fips-mode=1 --options-file=<path to the file>
     ```

3. If UEFI Secure Boot is enabled on the machine, you are prompted to restart the system after the installation. When prompted for a password, use the password for the root user. If this password is not accepted, use the word "acronis" as a password. During the system restart, opt for MOK (Machine Owner Key) management, select **Enroll MOK**, and then enroll the key.

## Enabling FIPS-compliant mode for a virtual appliance

You can enable the FIPS-compliant mode in the appliance console.

### Prerequisites

- A virtual appliance is deployed and configured.

### To enable FIPS mode on a virtual appliance

1. Log in to the hypervisor interface as an administrator.
2. Open the console of the virtual appliance.
3. In the command-line interface, run the following command:

   ```
   fips-mode-setup --enable
   ```

As a result, the virtual appliance restarts. After the restart, the virtual appliance operates in FIPS-compliant mode.
