# Mounting Exchange Server databases

Managing the backup and recovery of workloads and files > Protecting Microsoft applications > Recovering Exchange databases > Mounting Exchange Server databases
Mounting Exchange Server databases

After recovering the database files, you can bring the databases online by mounting them. Mounting is performed by using Exchange Management Console, Exchange System Manager, or Exchange Management Shell.

The recovered databases will be in a Dirty Shutdown state. A database that is in a Dirty Shutdown state can be mounted by the system if it is recovered to its original location (that is, information about the original database is present in Active Directory). When recovering a database to an alternate location (such as a new database or as the recovery database), the database cannot be mounted until you bring it to a Clean Shutdown state by using the Eseutil /r <Enn> command. <Enn> specifies the log file prefix for the database (or storage group that contains the database) into which you need to apply the transaction log files.

The account you use to attach a database must be delegated an Exchange Server Administrator role and a local Administrators group for the target server.

For details about how to mount databases, see the following articles:

Exchange 2010 or later: http://technet.microsoft.com/en-us/library/aa998871.aspx
Exchange 2007: http://technet.microsoft.com/en-us/library/aa998871(v=EXCHG.80).aspx



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.