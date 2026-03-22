# File filter values

Managing the backup and recovery of workloads and files > Backup options > File filters (Inclusions/Exclusions) > File filter values
File filter values

In a file filter, you can use the following values:

File or folder name

Specify the name of the file or folder, for example Document.txt. All files and folders with that name will be selected.

Full path to a file or folder

Specify the full path to the file or folder, starting with the drive letter (when backing up Windows data) or the root directory (when backing up Linux or macOS data). In Windows, Linux, and macOS, you can use forward slashes (C:/Temp/File.tmp). In Windows, you can also use the traditional backslashes (C:\Temp\File.tmp).

If the operating system of the backed-up machine is not detected correctly during a disk-level backup, file filters with full paths will not work. For an exclusion filter, a warning will be shown. For an inclusion filter, the backup will fail.

For example, a full path to a file is C:\Temp\File.tmp. If the operating system is not detected correctly, a full path filter, which includes the drive letter or the root directory, such as C:\Temp\File.tmp or C:\Temp\*, will result in a warning or failure.

A filter that does not use the drive letter or the root directory (for example, Temp\* or Temp\File.tmp) or a filter that starts with an asterisk (for example, *C:\) will not result in warning or failure. However, if the operating system is not detected correctly, these filters will not work.

Wildcards

Both with file or folder names and file or folder paths, you can use following wildcard characters:

Asterisk (*)

The asterisk represents zero or more characters.

For example, Doc*.txt matches the files Doc.txt and Document.txt.

Double asterisk (**)

The double asterisk represents zero or more characters, including the slash character.

For example, **/Docs/**.txt matches all TXT files in all subfolders of all folders named Docs.

You can use the double asterisk wildcard only for backups in the Version 12 format.

Question mark (?)

The question mark represents only one character.

For example, Doc?.txt matches the files Doc1.txt and Docs.txt but does not match the files Doc.txt or Doc11.txt.

Use the question mark wildcard if the file or folder name includes a comma or a semicolon. The comma and the semicolon are interpreted as delimiters and will split the filter into two parts. For example, if you want to use the folder MyCompany,Inc in a filter, use MyCompany?Inc when you specify the filter value. Otherwise, you will create two separate filters, as follows:

MyCompany
Inc
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.