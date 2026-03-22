# Recovering files by using bootable media

Managing the backup and recovery of workloads and files > Recovery > Recovering files > Recovering files by using bootable media
Recovering files by using bootable media

Running the bootable media requires 1.5 GB of RAM.

For more information about how to create bootable media, see Creating physical bootable media.

To recover files by using bootable media

Boot the target machine by using the bootable media.
Click Manage this machine locally or click Rescue Bootable Media twice, depending on the media type you are using.
If a proxy server is enabled in your network, click Tools > Proxy server, and then specify the proxy server host name/IP address, port, and credentials. Otherwise, skip this step.
[Optional] When recovering Windows or Linux, click Tools > Register media in the Cyber Protection service, and then specify the registration token that you obtained when downloading the media. If you do this, you will not need to enter credentials or a registration code to access the cloud storage, as described in step 7.
On the welcome screen, click Recover.
Click Select data, and then click Browse.

Specify the backup location:

To recover from cloud storage, select Cloud storage. Enter the credentials of the account to which the backed up machine is assigned.

When recovering Windows or Linux, you have the option to request a registration code and use it instead of the credentials. Click Use registration code > Request the code. The software shows the registration link and the registration code. You can copy them and perform the registration steps on a different machine. The registration code is valid for one hour.

To recover from a local or a network folder, browse to the folder under Local folders or Network folders.

To recover from backup locations on public cloud storage such as Microsoft Azure, Amazon S3, or S3-compatible, first click Register media in the Cyber Protection service, and then configure recovery using the web interface. For more information about managing media remotely via the web interface, see Remote operations with bootable media.

Click OK to confirm your selection.

Select the backup from which you want to recover the data. If prompted, type the password for the backup.
In Backup contents, select Folders/files.
Select the data that you want to recover. Click OK to confirm your selection.
Under Where to recover, specify a folder. Optionally, you can prohibit overwriting of newer versions of files or exclude some files from recovery.
[Optional] Click Recovery options to specify additional settings.
Click OK to start the recovery.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.