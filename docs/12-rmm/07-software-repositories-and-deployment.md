---
title: "Software Repositories, Packages, and Deployment (DeployPilot)"
section: "RMM"
subsection: "Software Deployment"
page_range: "1313-1339"
tags: [rmm, deploypilot, software-deployment, software-packages, library, repositories, install, uninstall, deployment-plans]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#software-repositories-packages.html"
---

# Working with Software Repositories and Software Packages

With software deployment by using DeployPilot, you can:
- Perform fresh software installations on remote devices
- Update custom applications that are not supported by the Vulnerability assessment and Patch management feature (the uploaded installer must be preconfigured to support upgrades)

## Software Packages

Software packages are installer files (.msi or .exe) that you can use to remotely deploy (install or uninstall) software to Windows workloads. A software package is defined by the software version and some custom settings, such as language and architecture type.

## Software Repositories

Software repositories are depots where software packages are stored. There are two repositories:

### Library

The **Library** repository contains 40 of the most frequently used software applications. The content is predefined and maintained by the system. You cannot edit or delete packages from this repository, and you cannot directly deploy from it. To deploy a package, you must first add it to the **My packages** repository.

Library fields: Name, Latest version, Vendor, License type. Filters: Vendor, License type, Latest release period.

### My Packages

The **My packages** repository contains all software packages that you can deploy and include in software deployment plans. Initially empty. Maximum storage: 5 GB for customer tenants, 20 GB for partner tenants.

Add packages to My packages by:
- Adding a package from the **Library** repository
- Manually uploading a software package

My packages fields: Name, Version, Vendor, Digital signature check, Operating system, Last edited by, System type, Package size. Filters: Vendor, Last edited by, System type, Language, Release period.

DeployPilot distinguishes between Library packages and manually uploaded packages. For Library packages, DeployPilot checks before deployment if the software is already installed and prevents unnecessary reinstallation.

### Supported Windows Versions for DeployPilot

Windows 11, 10, 8.1, 8, 7 (Enterprise/Professional/Ultimate), Windows Server 2022, 2019, 2016, 2012 R2, 2012, 2008 R2.

## Adding Software Packages from the Library

Prerequisites: 2FA enabled, Company administrator or Cyber administrator role.

1. Go to **Software management > Library**.
2. On the row of the software package, click **Add**.
3. In the **Add to my packages** wizard, select settings: Version, Language, Architecture type.
4. Select **I accept the Terms and Conditions of the EULA**, and click **Add**.

## Uploading Software Packages

You can upload software packages in .msi or .exe formats on the **My packages** page.

Prerequisites: 2FA enabled, Company administrator or Cyber administrator role.

1. Go to **Software management > My packages**.
2. Click **Add package**.
3. On the **Upload package** tab:
   a. Click **Upload**, select the package, click **Open**.
   b. Enable or disable the **Try Copilot** switch (Copilot can auto-populate package details including install/uninstall commands).
   c. Click **Next**.
4. On the **Package details** tab, provide: Software name (required), Vendor/Publisher (required), Software description (optional), License type, Version (required), Architecture type (required), Language (optional), Release date (required).
5. On the **Install / Uninstall commands** tab:
   - **Installation options**: Command arguments, Reboot return codes, Success return codes
   - **Uninstallation options**: Choose method (Command line or Software/vendor name), provide uninstall path and command arguments
6. On the **Summary** tab, review details and confirm.
7. On the **Digital signature check** tab, enable or skip the digital signature check.
8. Click **Add package**.

### Installation and Uninstallation Commands and Arguments

When uploading packages, provide installation and uninstallation arguments to ensure smooth deployment. Commonly used command arguments include:

**For MSI packages:**
- `/quiet` or `/qn` - Silent installation (no user interaction)
- `/norestart` - Prevent automatic restart
- `INSTALLDIR="C:\Program Files\App"` - Custom install directory
- `/log "C:\install.log"` - Enable logging

**For EXE packages:**
- `/S` or `/silent` - Silent installation
- `/VERYSILENT` - Very silent mode (no UI)
- `/NORESTART` - Prevent restart
- `/DIR="C:\Program Files\App"` - Custom directory

## Installing Software

You can install software on managed workloads via quick deploy or software deployment plans.

### Quick Deploy (from My Packages)

1. Go to **Software management > My packages**.
2. Click the software package, then click **Install**.
3. Select the workloads.
4. Select restart options (Restart if required, Always restart, Do not restart).
5. Click **Install**.

### Quick Deploy (from Devices)

1. Go to **Devices > All Devices**.
2. Select the machine(s), then click **Install software**.
3. Select the software packages to install, click **Next**.
4. Select restart options.
5. Click **Install**.

## Uninstalling Software

1. Go to **Software management > My packages**.
2. Click the software package, then click **Uninstall**.
3. Select the workloads.
4. Select restart options.
5. Click **Uninstall**.

## Creating a Software Deployment Plan

Software deployment plans automate the software deployment process.

1. Go to **Management > Software deployment plans**.
2. Click **Create plan**.
3. Enter a plan name.
4. In the **Software packages** section, click **Add**, select the packages.
5. Define the **Action** for each package: Install or Uninstall.
6. In the **Target workloads** section, select the workloads.
7. Define the **Schedule**: Once, Daily, Weekly, Monthly, or Manual.
8. Define **Restart options**.
9. Click **Create**.

Plans can also be run manually from the Software deployment plans page by clicking **Run now**.
