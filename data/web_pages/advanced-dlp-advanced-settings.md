# Advanced settings

Data Loss Prevention > Enabling Data Loss Prevention in protection plans > Advanced settings
Advanced settings

You can use the advanced settings in protection plans with Data Loss Prevention to increase the quality of data content inspection in channels controlled by Data Loss Prevention (DLP), as well as exclude from any preventive controls data transfers to peripheral device types in the allowlist, categories of network communications, destination hosts, as well as data transfers initiated by applications in the allowlist. You can configure the following advanced settings:

Optical character recognition

This setting turns on or off optical character recognition (OCR) in order to extract pieces of text in 31 language for further content inspection from graphical files and images in documents, messages, scans, screenshots, and other objects.

Transfer of password-protected data

The content of password-protected archives and documents cannot be inspected. With this setting, DLP allows the administrator to select whether outgoing transfers of password-protected data are to be allowed or blocked.

Prevent data transfer on errors

Sometimes, the analysis of content that is being sent might fail or another control error might occur in DLP agent operations. If this option is enabled, the transfer will be blocked. If the option is disabled, the transfer will be allowed despite the error.

Allowlist for device types and network communications

Data transfers to the types of peripheral devices and in network communications checked in this list are allowed regardless of their data sensitivity and the enforced data flow policy.

This option is used if issues with a specific Device type or Protocol occur. Do not enable it unless advised by a Support representative.
Allowlist for remote hosts

Data transfers to destination hosts specified in this list are allowed regardless of their data sensitivity and the enforced data flow policy.

Allowlist for applications

Data transfers performed by applications specified in this list are allowed regardless of their data sensitivity and the enforced data flow policy.

The Security level indicator of Advanced settings displayed in the Create protection plan view and in the "Details" view of a protection plan has the following logic of level indication:

Basic indicates that none of the advanced settings is turned on.
Moderate indicates that one or more settings are turned on, but the combination of OCR, Transfer of password-protected data, and Prevent data transfer on errors is not activated.
Strict indicates that at least the combination of OCR, Transfer of password-protected data, and Prevent data transfer on errors settings is activated.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.