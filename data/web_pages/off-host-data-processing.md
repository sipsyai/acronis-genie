# Off-host data protection plans

Working with plans > Off-host data protection plans
Off-host data protection plans

In service-based billing mode, this feature requires the Servers quota to be enabled under Standard Protection as a prerequisite, but using the feature does not affect the quota usage.

With solution-based billing mode, this functionality is available in customer tenants that use Ultimate protection.

Replication, validation, and cleanup are usually performed by the protection agent that performs the backup. This puts additional load on the machine on which the agent is running, even after the backup process is complete. To offload the machine, you can create off-host data protection plans – that is, separate plans for replication, validation, cleanup, and conversion to a virtual machine.

With the off-host data protection plans, you can do the following:

Choose different agents for the backup and off-host data protection operations
Schedule the off-host data processing operations during off-peak hours to minimize the network bandwidth consumption
Schedule the off-host data processing operations during non-business hours, if you do not want to install a dedicated agent for off-host data processing
The off-host data processing plans run according to the time settings (including the time zone) of the machine on which the protection agent is installed. For a virtual appliance (for example, Agent for VMware or Agent for Scale Computing HC3), you can configure the time zone in the graphical user interface of the agent.

Backup replication

Validation

Cleanup

Conversion to a virtual machine

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.