# Pre/Post data capture commands

Managing the backup and recovery of workloads and files > Backup options > Pre/Post data capture commands
Pre/Post data capture commands

The option enables you to define the commands to be automatically run before and after data capture (that is, taking the data snapshot). Data capture is performed at the beginning of the backup procedure.

The following scheme illustrates when the pre/post data capture commands are run.

<----------------------------        Backup        ---------------------------->


Pre-backup command



Pre-data capture command



Data capture



Post-data capture command

Write data to the backup set

Post-backup command

Interaction with other backup options

Running of the pre/post data capture commands can be modified by other backup options.

If the Multi-volume snapshot option is enabled, the pre/post data capture commands will run only once, because the snapshots for all volumes are created simultaneously. If the Multi-volume snapshot option is disabled, the pre/post data capture commands will run for every volume that is being backed up because the snapshots are created sequentially, one volume after another.

If the Volume Shadow Copy Service (VSS) option is enabled, the pre/post data capture commands and the Microsoft VSS actions will run as follows:

Pre-data capture commands > VSS Suspend > Data capture > VSS Resume > Post-data capture commands

By using the pre/post data capture commands, you can suspend and resume a database or application that is not compatible with VSS. Because the data capture takes seconds, the database or application idle time will be minimal.

See also
Multi-volume snapshot
Volume Shadow Copy Service (VSS)

Pre-data capture command

Post-data capture command

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.