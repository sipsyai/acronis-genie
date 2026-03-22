# Deleting a public cloud connection

Managing the backup and recovery of workloads and files > Backing up workloads to public clouds > Managing public cloud account access > Deleting a public cloud connection
Deleting a public cloud connection

You should delete the connection to a public cloud if you are not backing up workloads to it. Deleting the connection is the only way to remove access to the public cloud.

You can delete only connections that you added. To delete another user's connection to public cloud, you need one of the following roles: Company administrator, Unit administrator, Cyber administrator, or Administrator in the Cyber Protection service.

To delete a connection that is used for backups to a public cloud, first you must remove all backup locations that use this connection.

To delete a connection to public cloud

In the Cyber Protect console, go to Backups > Backup storage.

Delete all backup locations on public clouds that use this connection.

The objects on the storage will not be removed. This operation only deletes the location from the list of backup locations in the Cyber Protect console, without impacting the data.
Go to Infrastructure > Public clouds.
Select the connection from the list.
In the rightmost panel, click Delete.
On the confirmation screen, click Delete.

As a result, access to the public cloud is removed.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.