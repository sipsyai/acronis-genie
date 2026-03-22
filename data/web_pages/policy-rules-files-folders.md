# Policy rules for files and folders

Managing the backup and recovery of workloads and files > Selecting data to back up > Selecting files or folders > Policy rules for files and folders
Policy rules for files and folders

When you select files or folders to back up, you can use the following policy rules, according to the operating system of the protected workload.

Windows
Linux
macOS
Full path to a file or folder. For example, D:\Work\Text.doc or C:\Windows.
Predefined rules:
[All Files] selects all files on all volumes of the machine.
[All Profiles Folder] selects the folder in which all user profiles are located. For example, C:\Users or C:\Documents and Settings.

Environment variables:

%ALLUSERSPROFILE% selects the folder in which the common data of all user profiles is located. For example, C:\ProgramData or C:\Documents and Settings\All Users.

%PROGRAMFILES% selects the Program Files folder. For example, C:\Program Files.

%WINDIR% selects the Windows folder. For example, C:\Windows.

You can use other environment variables or a combination of environment variables and text. For example, to select the Java folder in the Program Files folder, specify: %PROGRAMFILES%\Java.

See also
Selecting files or folders



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.