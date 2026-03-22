# URL exclusions

Configuring your antivirus and antimalware protection > URL filtering > URL filtering settings > URL exclusions
URL exclusions

URLs that are known to be safe can be added to the list of the trusted domain. URLs that represent a threat can be added to the list of the blocked domain.

To specify the URLs that will always be trusted

In the URL filtering section of a protection plan, click Exclusions.

The URL exclusions window opens.

In the Trusted items section, click Add, and then select from the available options.

Domain — When you select this option, the Add domain window opens.

In the Domain field, enter each domain on a new line.

Process — When you select this option, the Add process window is displayed.

In the Process field, enter the path for each process on a new line.

In the Description field, enter a short description, so that you can recognize your change in the list of trusted items. For example, reasons and purposes for the exclusion, time stamps, and so on.

If there are multiple items added in a single entry, there can only be one comment captured for the multiple items.

Click Add, and then click Done.

To specify the URLs that will always be blocked

In the URL filtering section of a protection plan, click Exclusions.

The URL exclusions window opens.

In the Blocked items section, click Add and then click Domain.

In the Domain field, enter each domain on a new line.

Local network paths are supported. For example, \\localhost\folderpath\file.exe.

In the Description field, enter a short description, so that you can recognize your change in the list of blocked items. For example, reasons and purposes for the exclusion, time stamps, and other.

If there are multiple items added in a single entry, there can only be one comment captured for the multiple items.

Click Add, and then click Done.

Using wildcards to define exclusions

You can use asterisk (*) wildcard character to add trusted processes to the exclusion lists. Asterisks substitute for zero or more characters, and can be used in the middle or at the end of a description. They cannot be used at the beginning of a description. Environment variables, such as %AppData%, cannot be used.

Valid descriptions using wildcards:

C:\*.exe
D:\folders\file.*
C:\Users\*\AppData\Roaming\*.exe

Invalid descriptions:

*.exe
*:\folder\process.exe
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.