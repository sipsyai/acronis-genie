# Required permissions for unattended installation in macOS

Installing and deploying Cyber Protection agents > Installing and uninstalling protection agents by using the command-line interface > Installing and uninstalling protection agents in macOS > Required permissions for unattended installation in macOS
Required permissions for unattended installation in macOS

Before you initiate an unattended installation on a Mac workload, you must modify the Privacy Preferences Policy Control to allow App access and kernel and system extensions in the macOS of the workload to enable the installation of the Cyber Protection agent. You can do this by deploying a custom PPPC payload or by configuring the preferences in the graphical user interface of the workload. The following tables list the required permissions.

See also Troubleshooting permission issues on macOS.

Requirements for macOS 11 (Big Sur) or later

Tab	Section	Field	Value


Privacy Preferences Policy Control

App Access	Identifier

com.acronis.backup


Identifier Type	Bundle ID
Code Requirement	identifier "com.acronis.backup" and anchor apple generic and certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = ZU2TV78AA6
APP OR SERVICE

SystemPolicyAllFiles


ACCESS	Allow
App Access	Identifier

com.acronis.backup.aakore


Identifier Type	Bundle ID
Code Requirement

identifier "com.acronis.backup.aakore" and anchor apple generic and certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = ZU2TV78AA6


APP OR SERVICE

SystemPolicyAllFiles


ACCESS	Allow
App Access	Identified

com.acronis.backup.activeprotection


Identifier Type	Bundle ID
Code Requirement

identifier "com.acronis.backup.activeprotection" and anchor apple generic and certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = ZU2TV78AA6


APP OR SERVICE

SystemPolicyAllFiles


ACCESS	Allow
App Access	Identifier

cyber-protect-service


Identifier Type	Bundle ID
Code Requirement

identifier "cyber-protect-service" and anchor apple generic and certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = ZU2TV78AA6


APP OR SERVICE

SystemPolicyAllFiles


ACCESS	Allow
System Extensions



Allow users to approve system extensions	Enabled


Allowed Team IDs and System Extensions

Display Name	Acronis Cyber Protection Agent System Extensions
System Extension Types	Allowed Team Identifiers
Team Identifier

ZU2TV78AA6



Requirements for macOS versions prior to version 11

Tab	Section	Field	Value


Privacy Preferences Policy Control

App Access	Identifier

com.acronis.backup


Identifier Type	Bundle ID
Code Requirement

identifier "com.acronis.backup" and anchor apple generic and certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = ZU2TV78AA6


APP OR SERVICE

SystemPolicyAllFiles


ACCESS	Allow


App Access

Identifier

com.acronis.backup.aakore


Identifier Type	Bundle ID
Code Requirement

identifier "com.acronis.backup.aakore" and anchor apple generic and certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = ZU2TV78AA6


APP OR SERVICE

SystemPolicyAllFiles


ACCESS	Allow
App Access	Identified

com.acronis.backup.activeprotection


Identifier Type	Bundle ID
Code Requirement	identifier "com.acronis.backup.activeprotection" and anchor apple generic and certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = ZU2TV78AA6
APP OR SERVICE

SystemPolicyAllFiles


ACCESS	Allow
App Access	Identifier

cyber-protect-service


Identifier Type	Bundle ID
Code Requirement	identifier "cyber-protect-service" and anchor apple generic and certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = ZU2TV78AA6
APP OR SERVICE

SystemPolicyAllFiles


ACCESS	Allow


Approved Kernel Extensions



Allow users to approve kernel extensions

Enabled


Allow standard users to approve legacy kernel extensions (macOS 11 or later)

Enabled
Approved Team IDs and Kernel Extensions	Approved Team ID - Display Name	Acronis Cyber Protection Agent Kernel Extensions
Team ID

ZU2TV78AA6


Kernel Extension Bundle IDs

com.acronis.systeminterceptors

com.acronis.ngscan

com.acronis.notifyframework




System Extensions



Allow users to approve system extensions

Enabled


Allowed Team IDs and System Extensions

Display Name

Acronis Cyber Protection Agent System Extensions


System Extension Types	Allowed Team Identifiers
Team Identifier

ZU2TV78AA6

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.