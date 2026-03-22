# Uploading software packages

RMM > Managing software > Working with software repositories and software packages > Uploading software packages
Uploading software packages

The availability of this feature depends on the license that you have.

On the My packages page, you can upload software packages in the following formats: .msi or .exe.

If you plan to use the package for updating existing installations, ensure that the package that you will upload supports upgrades.

Prerequisites

2FA is enabled for your user account.
You have one of the following roles for Cyber Protection: Company administrator or Cyber administrator.

To upload a software package

In the Cyber Protect console, go to Software management > My packages.

Click Add package.

On the Upload package tab, do the following:

Click Upload, select the software package that you want to upload, and then click Open.

Depending on whether you want to use Copilot to automatically populate the package details and required information, such as install and uninstall command and arguments, enable or disable the Try Copilot switch.

Click Next.

On the Package details tab, do the following:

If you used Copilot to automatically populate the package details, review the details, ensure that they are correct, and then click Next.

You can manually correct package details that were populated by Copilot, or click Revert changes to remove all package details.

If you did not use Copilot to automatically populate the package details, enter the details, and then click Next.

Field	Description
Software name

Name of the software. This field is required.


Vendor/Publisher

Name of the software vendor. This field is required.


Software description

Additional description of the software. This field is optional.


License type

License type of the software.

Proprietary. Proprietary licenses are owned and controlled by the software vendors. This is the default value.
Open source. These are the licenses for open-source software that are free for public distribution.

Version

Version of the software. This field is required.


Architecture type

Architecture type of the operating system on which the software package will be deployed. This field is required.


Language

Language of the software. This field is optional.


Release date

Release date of the software. This field is required.

On the Install / Uninstall commands tab, do the following:

If you used Copilot to automatically populate the install and uninstall commands and arguments, review the details, ensure that they are correct, and then click Next.

If you did not use Copilot to automatically populate the package information, do the following:

In the Installation options section, in the Command arguments field, enter the install command arguments.

In the Reboot return codes and Success return codes fields, specify the return codes that indicate the result of the installation process.

In the Uninstallation options section, select the uninstallation method:

Uninstallation method	Description
Command line	If you select this method, you must provide the correct silent uninstall command and arguments. Otherwise, the uninstallation might stop responding.
Software or vendor name

If you select this method, the system will use the software name, vendor name, or RegEx pattern that you provide to automatically locate and run the uninstall command.

Use this method if you are uncertain about the uninstall command for the application.

[If you selected Software or vendor name] In the Software name field, enter the software name.
[If you selected Software or vendor name] In the Vendor name field, enter the name of the software vendor.

[If you selected Command line] In the Uninstall path field, enter the uninstall path and command.

The uninstall path is the path to the directory on a computer where the uninstallation executable for the software program is located. The uninstall path is essential for ensuring that the software can be removed cleanly and completely from the system.

In the Command arguments field, enter the uninstall command arguments.

In the Reboot return codes, enter the return codes.

In the Success return codes fields, enter the return codes.

Click Next.

For more information installation and uninstallation commands and arguments, see Installation and uninstallation commands and arguments.

On the Summary tab, review the details of the software package, select I reviewed the package details and confirm that I want to add it to My packages and I accept the Terms and Conditions of the EULA, and then click Next.

On the Digital signature check tab:

If you want to perform a digital signature check of the package, select Enable digital signature check.

We recommend that you always perform a digital signature check. This ensures that the custom package that will be uploaded is compliant and digitally signed, and minimizes the risk of deploying unverified or tampered software.

If you want to skip the check, clear Enable digital signature check.

Click Add package.

Installation and uninstallation commands and arguments

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.