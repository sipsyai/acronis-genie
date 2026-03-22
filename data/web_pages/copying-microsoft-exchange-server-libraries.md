# Copying Microsoft Exchange Server libraries

Managing the backup and recovery of workloads and files > Protecting Microsoft applications > Recovering Exchange mailboxes and mailbox items > Copying Microsoft Exchange Server libraries
Copying Microsoft Exchange Server libraries

When recovering Exchange mailboxes or mailbox items to Microsoft 365, you may need to copy the following libraries from the machine that was backed up (or from another machine with the same Microsoft Exchange Server version) to the machine with Agent for Microsoft 365.

Copy the following files, according to the Microsoft Exchange Server version that was backed up.

Microsoft Exchange Server version	Libraries	Default location
Microsoft Exchange Server 2010

ese.dll

esebcli2.dll

store.exe

%ProgramFiles%\Microsoft\Exchange Server\V14\bin
Microsoft Exchange Server 2013	ese.dll	%ProgramFiles%\Microsoft\Exchange Server\V15\bin
msvcr110.dll	%WINDIR%\system32
Microsoft Exchange Server 2016, 2019	ese.dll	%ProgramFiles%\Microsoft\Exchange Server\V15\bin


msvcr110.dll

msvcp110.dll

%WINDIR%\system32

The libraries should be placed in the folder %ProgramData%\Acronis\ese. If this folder does not exist, create it manually.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.