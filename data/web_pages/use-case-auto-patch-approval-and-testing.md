# Use case for automatic patch approval and testing

RMM > Managing software > Assessing vulnerabilities and managing patches > Use case for automatic patch approval and testing
Use case for automatic patch approval and testing

If you want to test the new patches on a test machine before installing them on your production machines, you can configure two protection plans - a plan for installation of patches for test purposes, and a plan for installation of tested patches on production machines. Thus, you will ensure that the patches that you install in your production environment are safe and your production machines work correctly after the patch installation.

The use case consists of the following stages:

Configure the settings for Automatic patch approval. Select the Automatic patch approval and testing option. For more information, see Configuring automatic patch approval.
Configure a protection plan for test purposes (for example, 'Test patching') with the enabled Patch management module and apply it to the machines in the test environment. Specify the following condition of patch installation: the patch approval status must be Pending approval. This step is needed to validate the patches and check if the machines work properly after patch installation. For more information, see Configuring the Test patching protection plan.
Configure a protection plan for the production environment (for example, 'Production patching') with the enabled Patch management module and apply it to the machines in the production environment. Specify the following condition of patch installation: the patch status must be Approved. For more information, see Configuring the Production patching protection plan.
Run the Test patching plan and check the results. Leave the approval status of the machines that have no issues as Pending approval, but change the approval status of the machines working incorrectly to Declined. According to the number of days set in the Automatic patch approval setting, the status of the patches will automatically change from Pending approval to Approved. When you run the Production patching plan, only the Approved patches will be installed on the production machines. For more information, see Running the Test patching protection plan and decline unsafe patches.

Run the Production patching plan.

Configuring the Test patching protection plan

Configuring the Production patching protection plan

Running the Test patching protection plan and decline unsafe patches

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.