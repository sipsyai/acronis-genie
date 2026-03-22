# Attaching SQL Server databases

Managing the backup and recovery of workloads and files > Protecting Microsoft applications > Recovering SQL databases > Attaching SQL Server databases
Attaching SQL Server databases

This section describes how to attach a database in SQL Server by using SQL Server Management Studio. Only one database can be attached at a time.

Attaching a database requires any of the following permissions: CREATE DATABASE, CREATE ANY DATABASE, or ALTER ANY DATABASE. Normally, these permissions are granted to the sysadmin role of the instance.

To attach a database

Run Microsoft SQL Server Management Studio.
Connect to the required SQL Server instance, and then expand the instance.
Right-click Databases and click Attach.
Click Add.
In the Locate Database Files dialog box, find and select the .mdf file of the database.

In the Database Details section, make sure that the rest of database files (.ndf and .ldf files) are found.

Details. SQL Server database files may not be found automatically, if:

They are not in the default location, or they are not in the same folder as the primary database file (.mdf). Solution: Specify the path to the required files manually in the Current File Path column.
You have recovered an incomplete set of files that make up the database. Solution: Recover the missing SQL Server database files from the backup.
When all of the files are found, click OK.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.