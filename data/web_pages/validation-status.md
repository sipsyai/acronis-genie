# Validation status

Working with plans > Off-host data protection plans > Validation > Validation status
Validation status

A validation status is assigned to the backups for which a validation was completed.

If the validation completes successfully, the backup is marked with a green dot and the label Validated.

If the validation fails, the backup is marked with a red dot.

Validation status is updated after every validation operation. The status for each validation method is updated separately. Validation fails if one of the configured validation methods fails. In some cases, a failing validation might be caused by a misconfiguration of the validation plan. For example, if you use the VM heartbeat method for virtual machines on a wrong host.

If one of multiple configured validation method fails, the validation status of the backup will be shown as failed. This status will persist even if you reconfigure the validation plan by disabling the failing method, and validation via other methods completes successfully. For a Validated status, the failed validation method must complete successfully for the same backup.

Checking the validation status




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.