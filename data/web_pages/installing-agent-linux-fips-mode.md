# Installing Agent for Linux in FIPS-compliant mode

Installing and deploying Cyber Protection agents > FIPS-compliant mode > Installing Agent for Linux in FIPS-compliant mode
Installing Agent for Linux in FIPS-compliant mode

You can install Agent for Linux in FIPS-compliant mode by using the command-line interface.

Prerequisites

You have downloaded the installation package for Agent for Linux.

To install Agent for Linux in FIPS-compliant mode

Open Terminal.

Do one of the following:

To install the agent by specifying the parameters on the command line, run the following command:

<package name> -a --fips-mode=1 <parameter 1> ... <parameter N>

Here, <package name> is the name of the installation package (an .i686 or an .x86_64 file). See the available parameters and their values in Unattended installation or uninstallation parameters.

To install the agent with parameters that are specified in a separate text file, run the following command:

<package name> -a --fips-mode=1 --options-file=<path to the file>

This approach might be useful if you do not want to enter sensitive information on the command line. In this case, you can specify the configuration settings in a separate text file and ensure that only you can access it. Put each parameter on a new line, followed by the value for that parameter. For example:

--rain=https://company.cloud
--login=johndoe
--password=johnspassword
--auto

or

-C
https://company.cloud
-g
johndoe
-w
johnspassword
-a
--language
en

If the same parameter is specified on the command line and in the text file, the command-line value precedes.

If UEFI Secure Boot is enabled on the machine, you are prompted to restart the system after the installation. When prompted for a password, use the password for the root user. If this password is not accepted, use the word "acronis" as a password. During the system restart, opt for MOK (Machine Owner Key) management, select Enroll MOK, and then enroll the key by using the recommended password.

If you enable UEFI Secure Boot after installing the agent, repeat the installation, including this step. Otherwise, backups will fail.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.