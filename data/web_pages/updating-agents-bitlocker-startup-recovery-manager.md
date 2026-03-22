# Updating protection agents on BitLocker-encrypted workloads

Installing and deploying Cyber Protection agents > Updating protection agents > Updating protection agents on BitLocker-encrypted workloads
Updating protection agents on BitLocker-encrypted workloads

Agent updates that introduce changes to Startup Recovery Manager interfere with BitLocker on workloads on which both BitLocker and Startup Recovery Manager are enabled. In this case, after a restart, the BitLocker recovery key is required. To mitigate this issue, suspend or disable BitLocker before you update the agent.

Affected agent versions:

23.12.36943, released in December 2023
25.01.XXXXX released in January 2025
25.03.XXXXX released in March 2025

You can also check whether an update introduces changes to Startup Recovery Manager in the release notes of the protection agent.

To update the agent on a workload with BitLocker and Startup Recovery Manager enabled

On the workload on which you want to update the agent, suspend or disable BitLocker.
Update the agent.
Restart the workload.
Enable BitLocker.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.