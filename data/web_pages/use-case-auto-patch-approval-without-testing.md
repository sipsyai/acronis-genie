# Use case for automatic patch approval without testing

RMM > Managing software > Assessing vulnerabilities and managing patches > Use case for automatic patch approval without testing
Use case for automatic patch approval without testing

If you want to automatically install new patches on your production machines as soon as possible, without installing them on test machines first, you can configure only one protection plan.

The use case consists of the following stages:

Configure the settings for Automatic patch approval. Select the Automatic patch approval without testing option. For more information, see Configuring automatic patch approval.
Configure a protection plan for the production environment (for example, 'Production patching') with the enabled Patch management module and apply it to the machines in the production environment. Specify the following condition of patch installation: the patch status must be Approved. For more information, see Configuring the Production patching protection plan.
Run the Production patching plan.



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.