# Enabling  Data Loss Prevention in protection plans

Data Loss Prevention > Enabling Data Loss Prevention in protection plans
Enabling Data Loss Prevention in protection plans

Data Loss Prevention features can be included in any protection plan for a customer tenant if the Protection service and the Data Loss Prevention pack are enabled for this customer.

DLP features and Device control can be used independently or together (in a single protection plan, or in two plans protecting the same workload). If used together, their functional capabilities are coordinated as follows.

Device control stops controlling user access to those local channels in which DLP inspects the content of transferred data. However, Device control retains the control over the following device types if they are configured to Read-only or Denied access:
Removable
Encrypted removable
Mapped drive

For example, if you have both Device control and DLP enabled in a single protection plan or in two plans protecting the same workload, and you have the Read-only access configured for USB devices in Device control, the Read-only access will be applied to all USB devices, except for the ones in the allowlist, regardless of the access settings in the DLP module. If the default, Enable access is configured in Device control, the access setting in DLP will be applied.

User access to the following local channels and peripherals in the allowlist is enforced by Device Control:
Optical drives
Floppy drives
MTP-connected mobile devices
Bluetooth adapters
Windows clipboard
Screenshot captures
USB devices and device types (except for Removable storage and Encrypted)

To create a protection plan with DLP

Navigate to Management > Protection plans.
Click Create plan.
Expand the Data Loss Prevention section and click the Mode row.

The Mode dialog opens.

To start the creation or renewal of the data flow policy, select Observation mode and then select how to process data transfers:
Option	Description
Allow all	All transfers of sensitive data from user workloads are treated as necessary for the business process and safe. A new rule is created for every detected data flow that does not match an already defined rule in the policy.
Justify all	All transfers of sensitive data from user workloads are treated as necessary for the business process, but risky. Therefore, for every intercepted transfer of sensitive data to any recipient or destination both inside and outside the organization that does not match a previously created data flow rule, the user must provide a one-time business justification. When the justification is submitted, a new data flow rule is created in the data flow policy.
Mixed

The Allow all logic is applied for all internal transfers of sensitive data, and the Justify all logic is applied for all external transfers of sensitive data.

For definition of internal destinations, see Automated detection of destination

Select Observation mode only if you do not have a data flow policy created before or if you are renewing the policy. Before you start the policy renewal, see Data flow policy renewal.
Data leakage is not prevented in the Observation mode. See Observation mode in the Fundamentals guide.
To enforce the existing data flow policy, select Enforcement mode, and then select how strictly to enforce the data flow policy rules:
Option	Description
Strict enforcement	The data flow policy is enforced as is and will not be extended with new permissive policy rules when previously unobserved sensitive data flows are detected. See Strict enforcement in the Fundamentals guide.
Adaptive enforcement (Enforcement with learning)	The enforced policy continues its automatic adaptation to those business operations that were not performed during the observation period or to changes in business processes. This mode allows the enforced data flow policy to expand based on newly learned data flows detected on the workloads. See Adaptive enforcement in the Fundamentals guide.
Before switching a company or unit policy from Observation to Enforcement mode, it is crucial to adjust the default rules for each sensitive data category from the permissive to a prohibitive state. Default rules are marked with an asterisk (*) in the Data flow policy view. Read more about the types of policy rules in the Fundamentals guide.
Click Done to close the Mode dialog.
(Optional) To configure optical character recognition, allowlists, and more protection options, click Advanced Settings.

For information on available options, see Advanced settings.

Save the protection plan and apply it to the workloads that you want to protect.

Advanced settings

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.