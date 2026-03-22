# Validation methods

Working with plans > Off-host data protection plans > Validation > Validation methods
Validation methods

You can select one or more validation methods. If multiple validation methods are selected, they are applied in the following order:

VM heartbeat (part of the Run as virtual machine validation option)
Screenshot validation (part of the Run as virtual machine validation option)
Checksum verification

The Run as virtual machine validation option is available only for disk-level backups that contain an operating system. You can use it on ESXi or Hyper-V hosts that are managed by a protection agent (Agent for VMware or Agent for Hyper-V).

VM heartbeat
Screenshot validation
Checksum verification

With this validation method, the agent runs a virtual machine from the backup, connects to VMware Tools or Hyper-V Integration Services, and then checks the heartbeat response to ensure that the operating system has started successfully. If the connection fails, the agent attempts to connect every two minutes, to a total of five times. If none of the attempts are successful, the validation fails.

Regardless of the number of validation plans and validated backups, the agent that performs the validation runs one virtual machine at a time. When the validation result is clear, the agent deletes the virtual machine, and then runs the next one.

Use this method only when you validate backups of VMware virtual machines by running these backups as virtual machines on an ESXi host, and backups of Hyper-V virtual machines by running them as virtual machines on a Hyper-V host.

Changing the timeout for VM heartbeat and screenshot validation

Configuring the number of retries in case of an error




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.