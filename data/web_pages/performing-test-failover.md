# Performing a test failover

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Failover > Performing a test failover
Performing a test failover

Though performing a test failover is optional, we recommend that you make it a regular process with a frequency that you find adequate in terms of cost and safety. A good practice is creating a runbook – a set of instructions describing how to spin up the production environment in the cloud.

You must create a recovery server in advance to protect your devices from a disaster.

You can perform failover only from recovery points (backups) that were created after the recovery server of the device was created.

At least one recovery point must be created before failing over to a recovery server. The maximum number of recovery points that is supported is 100.

To perform a test failover

Select the original machine or select the recovery server that you want to test.

Click Disaster Recovery.

The description of the recovery server opens.

Click Failover.
Select the failover type Test failover.
Select the recovery point (backup), and then click Start.

If the backup that you selected is encrypted by using encryption as a machine property:

Enter the encryption password for the backup set.

The password will only be saved temporarily and will be used only for the current test failover operation. The password is automatically deleted from the credentials store if the test failover is stopped, or after the test failover completes.

To save the password for the backup set and use it in subsequent failover operations, select the Store the password in a secure credentials store... check box and then, in the Credentials name field, enter a name for the credentials.

The password will be stored in a secured credentials store and will be applied automatically in subsequent failover operations. However, saving passwords might conflict with your compliance obligations.

Click Done.

When the recovery server starts, its state changes to Testing failover.

Test the recovery server by using any of the following methods:

In Disaster Recovery > Servers, select the recovery server, and then click Console.
Connect to the recovery server by using RDP or SSH, and the test IP address that you specified when creating the recovery server. Try the connection from both inside and outside the production network (as described in "Point-to-site connection").

Run a script within the recovery server.

The script may check the login screen, whether applications are started, the Internet connection, and the ability of other machines to connect to the recovery server.

If the recovery server has access to the Internet and a public IP address, you may want to use TeamViewer.

When the test is complete, click Stop testing.

The recovery server is stopped. All changes made to the recovery server during the test failover are not preserved.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.