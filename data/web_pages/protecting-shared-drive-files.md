# Protecting Shared drive files

Managing the backup and recovery of workloads and files > Protecting Google Workspace data > Protecting Shared drive files
Protecting Shared drive files
What items can be backed up?

You can back up an entire Shared drive, or individual files and folders. Files are backed up together with their sharing permissions.

The Shared with me folder is not backed up.

Limitations
A Shared drive without members cannot be backed up, due to Google Drive API limitations.

Out of the Google-specific file formats, Google Docs, Google Sheets, and Google Slides are fully supported for backup and recovery. Other Google-specific formats might not be fully supported or might not be supported at all – for example, Google Drawings files are recovered as .svg files, Google Sites files are recovered as .txt files, Google Jamboard files are recovered as .pdf files, and Google My Maps files are skipped during a backup.

File formats that are not Google-specific – for example, .txt, .docx, .pptx, .pdf, .jpg, .png, .zip, are fully supported for backup and recovery.
What items can be recovered?

You can recover an entire Shared drive, or any file or folder that was backed up.

You can choose whether to recover the sharing permissions or let the files inherit the permissions from the folder to which they are recovered.

The following items are not recovered:

Sharing permissions for a file that was shared with a user outside the organization are not recovered if sharing outside the organization is disabled in the target Shared drive.
Sharing permissions for a file that was shared with a user who is not a member of the target Shared drive are not recovered if Sharing with non-members is disabled in the target Shared drive.
Limitations
Comments in files are not recovered.
Sharing links for files and folders are not recovered.

Selecting Shared drive files

Recovering Shared drive and Shared drive files

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.