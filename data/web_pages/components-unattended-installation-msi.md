# Components for unattended installation (MSI)

Installing and deploying Cyber Protection agents > Installing and uninstalling protection agents by using the command-line interface > Installing and uninstalling protection agents in Windows > Components for unattended installation (MSI)
Components for unattended installation (MSI)

The table below summarizes the components that you can use for unattended installation via an MSI file. Use the value names to specify values for the ADDLOCAL parameter.

For more information, see Parameters for unattended installation (MSI).

Value name	Component description	Must be installed together with	Bitness
AgentFeature	Core components for agents	 	32-bit/64-bit
MmsMspComponents	Core components for backup	AgentFeature	32-bit/64-bit
BackupAndRecoveryAgent	Agent for Windows	MmsMspComponents	32-bit/64-bit
AmpAgentFeature	Agent for Antimalware protection and URL filtering	BackupAndRecoveryAgent	32-bit/64-bit
DlpAgentFeature	Agent for Data Loss Prevention	BackupAndRecoveryAgent	32-bit/64-bit
SasAgentFeature	Agent for File Sync & Share	TrayMonitor	32-bit/64-bit
ArxAgentFeature	Agent for Exchange	MmsMspComponents	32-bit/64-bit
ArsAgentFeature	Agent for SQL	BackupAndRecoveryAgent	32-bit/64-bit
ARADAgentFeature	Agent for Active Directory	BackupAndRecoveryAgent	32-bit/64-bit
ArxOnlineAgentFeature	Agent for Microsoft 365	MmsMspComponents	32-bit/64-bit
OracleAgentFeature	Agent for Oracle	BackupAndRecoveryAgent	32-bit/64-bit
AcronisESXSupport	Agent for VMware ESX(i) (Windows)	BackupAndRecoveryAgent	64-bit
HyperVAgent	Agent for Hyper-V	BackupAndRecoveryAgent	32-bit/64-bit
CommandLineTool	Command-Line Tool	 	32-bit/64-bit
TrayMonitor	Cyber Protect Monitor	AgentFeature	32-bit/64-bit
BackupAndRecoveryBootableComponents	Bootable Media Builder	 	32-bit/64-bit
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.