# Recovering data from an application-aware backup

Managing the backup and recovery of workloads and files > Protecting MySQL and MariaDB data > Recovering data from an application-aware backup
Recovering data from an application-aware backup

From an application-aware backup, you can recover MySQL or MariaDB instances, databases, and tables. You can also recover the entire server on which the instances are running, or files and folders from this server.

The table below summarizes all recovery options.

What to recover	Recover as	Recover to


MySQL Server

MariaDB Server

Entire machine

Machine* on which Agent for Linux is installed




MySQL Server

MariaDB Server

Files or folders

Machine* on which Agent for Linux is installed


Instance	Files

Machine* on which Agent for MySQL/MariaDB is installed


Database

The same database

New database



Machine* on which Agent for MySQL/MariaDB is installed

Original instance
Another instance
Original database
New database

Table

The same table

New table



Machine* on which Agent for MySQL/MariaDB is installed

Original instance
Another instance
Original database
Original table
New table

* A virtual machine with an agent inside is treated as a physical machine from the backup standpoint.

Recovering the entire server

Recovering instances

Recovering databases

Recovering tables

Recovering stored routines

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.