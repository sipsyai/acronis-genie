# Filter examples

Managing the backup and recovery of workloads and files > Backup options > File filters (Inclusions/Exclusions) > Filter examples
Filter examples

The tables below show examples of file filter configurations.

Inclusion filter
What to back up	Filter value	Backup archive contains	Description


C:\Folder1 (contains MyFile.txt and other files)

C:\Folder2 (contains MyDocument.txt and other files)



MyFile.txt

C:\Folder2\MyDocument.txt



C:\Folder1\MyFile.txt

C:\Folder2\MyDocument.txt



The inclusion filter matches the backup scope (What to back up).

Only the files that are specified in the inclusion filter are present in the backed-up folders.

You can configure a file filter by using file or folder names, or by using file or folder paths.




C:\Folder1 (contains multiple files)



C:\Folder2\MyDocument.txt



C:\Folder1 (as an empty folder)



The inclusion filter does not match the backup scope (What to back up).

Folder1 is backed up but it is empty because it does not contain the file in the inclusion filter.

The file in the inclusion filter is not backed up because it is not part of the backup scope.




C:\Folder1 (contains MyFile.txt and other files)

C:\Folder2 (contains MyDocument.txt and other files)

MyFile.txt

C:\Folder1\MyFile.txt

C:\Folder2 (as an empty folder)



The inclusion filter partially matches the backup scope (What to back up).

Folder1 is backed up but it contains only the file that is specified in the inclusion filter.

Folder2 is backed up but it is empty because it does not contain the file in the inclusion filter.




C:\Folder1 (contains MyFile.txt and other files)

C:\Folder2\MyDocument.txt

MyFile.txt

C:\Folder1\MyFile.txt

C:\Folder2\MyDocument.txt



Folder1 is backed up but it contains only the file that is specified in the inclusion filter.

The second selected file is also backed up. Using filters does not affect the selection of specific files in the backup scope (What to back up).



Exclusion filter
What to back up	Filter value	Backup archive contains	Description


C:\Folder1 (contains MyFile.txt and other files)

C:\Folder2 (contains MyDocument.txt and other files)



MyFile.txt

C:\Folder2\MyDocument.txt



C:\Folder1 – all files except MyFile.txt

C:\Folder2 – all files except MyDocument.txt



The exclusion filter matches the backup scope (What to back up).

The files that are specified in the exclusion filter are missing in the backed-up folders.

You can configure a file filter by using file or folder names, or by using file or folder paths.




C:\Folder1 (contains multiple files)



C:\Folder2\MyDocument.txt



C:\Folder1 – all files



The exclusion filter does not match the backup scope (What to back up).

The entire content of Folder1 is backed up.




C:\Folder1 (contains MyFile.txt and other files)

C:\Folder2 (contains MyDocument.txt and other files)

MyFile.txt

C:\Folder1 – all files except MyFile.txt

C:\Folder2 – all files



The inclusion filter partially matches the backup scope (What to back up).

Folder1 is backed up but the file that is specified in the exclusion filter is missing.

The entire content of Folder2 is backed up.




C:\Folder1 (contains MyFile.txt and other files)

C:\Folder2\MyDocument.txt

MyFile.txt

C:\Folder1 – all files except MyFile.txt

C:\Folder2\MyDocument.txt



Folder1 is backed up but the file that is specified in the exclusion filter is missing.

The second selected file is backed up because it does not match the exclusion filter.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.