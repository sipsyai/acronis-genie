# One-click recovery

Managing the backup and recovery of workloads and files > Backup options > One-click recovery
One-click recovery

With One-click recovery, you can automatically recover a disk backup of your Windows or Linux machine. The backup can be of the entire machine, or of specific disks or volumes on the machine. Machines with Secure Boot and BitLocker encryption are supported.

One-click recovery supports the following operations:

Automatic recovery from the latest backup
Recovery from a specific backup (also known as a recovery point) within the backup archive

One-click recovery supports the following backup storages:

Secure Zone
Network folder
Cloud storage

Suspend the BitLocker encryption until the next restart of your machine when you perform any of the following operations:

Creating, modifying, or deleting Secure Zone.
Enabling or disabling Startup Recovery Manager.
[Only if Startup Recovery Manager was not already enabled] Running the first backup after enabling One-click recovery in the protection plan. This operation enables Startup Recovery Manager automatically.
Updating Startup Recovery Manager, for example by updating the protection.

If the BitLocker encryption was not suspended during these operations, you will need to specify your BitLocker PIN after restarting the machine.

Enabling One-click recovery

Disabling One-click recovery

Recovering a machine with One-click recovery

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.