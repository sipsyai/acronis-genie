# Recovering stored routines

Managing the backup and recovery of workloads and files > Protecting MySQL and MariaDB data > Recovering data from an application-aware backup > Recovering stored routines
Recovering stored routines

When you recover a whole MySQL instance, the stored routines are automatically recovered.

When you recover an individual database to a non-original instance or recover it as a new database, the stored routines are not automatically recovered. You can recover them manually, by exporting them in an SQL file, and then adding them to the recovered database.

To export the stored routines and add them to a recovered database

On the machine with the original MySQL instance, open Terminal.

Run the following command to export the stored routines.

mysqldump -p [source_database_name] --routines --no-create-info --no-data > [exported_db_routines.sql]

On the machine where the database is recovered, open the MySQL command line client.

Run the following commands to add the routines to the recovered database.

mysql>  use [recovered_database_name];
mysql>  source [path_to_exported_db_routines.sql];
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.