# Protecting Google Drive files

Managing the backup and recovery of workloads and files > Protecting Google Workspace data > Protecting Google Drive files
Protecting Google Drive files
What items can be backed up?

You can back up an entire Google Drive, or individual files and folders. Files are backed up together with their sharing permissions.

The following items are not backed up:

The Shared with me folder
The Computers folder (created by the Backup and Sync client)
Limitations

Out of the Google-specific file formats, Google Docs, Google Sheets, and Google Slides are fully supported for backup and recovery. Other Google-specific formats might not be fully supported or might not be supported at all – for example, Google Drawings files are recovered as .svg files, Google Sites files are recovered as .txt files, Google Jamboard files are recovered as .pdf files, and Google My Maps files are skipped during a backup.

File formats that are not Google-specific – for example, .txt, .docx, .pptx, .pdf, .jpg, .png, .zip, are fully supported for backup and recovery.
What items can be recovered?

You can recover an entire Google Drive, or any file or folder that was backed up.

You can choose whether to recover the sharing permissions or let the files inherit the permissions from the folder to which they are recovered.

Limitations
Comments in files are not recovered.
Sharing links for files and folders are not recovered.
The read-only Owner settings for shared files (Prevent editors from changing access and adding new people and Disable options to download, print and copy for commenters and viewers) cannot be changed during a recovery.
Ownership of a shared folder cannot be changed during a recovery if the Prevent editors from changing access and adding new people option is enabled for this folder. This setting prevents the Google Drive API from listing the folder permissions. Ownership of the files in the folder is recovered correctly.

Selecting Google Drive files

Recovering Google Drive and Google Drive files

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.