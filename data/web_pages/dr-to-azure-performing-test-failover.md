# Performing a test failover in Microsoft Azure

Implementing disaster recovery > Disaster Recovery to Microsoft Azure > Failover in Microsoft Azure > Performing a test failover in Microsoft Azure
Performing a test failover in Microsoft Azure

Though performing a test failover is optional, we recommend that you make it a regular process with a frequency that you find adequate in terms of cost and safety.

You can perform failover only from recovery points (backups) that were created after the recovery server of the device was created.

At least one recovery point must be created before failing over to a recovery server. The maximum number of recovery points that is supported is 100.

Prerequisites

The recovery server is configured in Azure location and has at least one recovery point created after the recovery server was created.

An isolated Azure VNet and subnet for the test failover to ensure no interference with production environments.

Network security group (NSG) rules are configured to meet your requirements.

To perform a test failover in Microsoft Azure

In the Cyber Protect console, go to Disaster Recovery > Recovery servers.

Click the server that you want to fail over, and then click Failover.

In the Server failover window, select Test failover, and then select the recovery point (backup) from which the cloud server will be started.

Click Start.

If the backup that you selected is encrypted by using encryption as a machine property:

Enter the encryption password for the backup set.

The password will only be saved temporarily and will be used only for the current test failover operation. The password is automatically deleted from the credentials store if the test failover is stopped, or after the test failover completes.

To save the password for the backup set and use it in subsequent failover operations, select the Store the password in a secure credentials store... check box and then, in the Credentials name field, enter a name for the credentials.

The password will be stored in a secured credentials store and will be applied automatically in subsequent failover operations. However, saving passwords might conflict with your compliance obligations.

Click Done.

When the recovery server starts, its state changes to Testing failover.

Test the recovery server by using any of the following methods:

In Disaster Recovery > Recovery servers, select the recovery server, and then click Connect.
Connect to the recovery server by using RDP or SSH and the test IP address that you specified when creating the recovery server. Try the connection from both inside and outside the production network.

Run a script within the recovery server.

The script may check the login screen, whether applications are started, the Internet connection, and the ability of other machines to connect to the recovery server.

When the test is complete, click Stop testing.

The recovery server is stopped. Changes that are made to the recovery server during the test failover are not saved.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.