# The patch management workflow

RMM > Managing software > Assessing vulnerabilities and managing patches > The patch management workflow
The patch management workflow

The patch management workflow includes steps for configuring and applying a protection plan, running a vulnerability assessment scan, configuring patch settings, approving patches and finally, installing patches that are approved. The exact steps of the workflow are as follows.

Configure a protection plan that has the Vulnerability assessment and Patch management modules enabled.
Configure the vulnerability assessment settings. For more information about these settings, see Vulnerability assessment settings.
Configure the patch management settings. For more information about these settings, see Patch management settings in the protection plan
Apply the protection plan to one or several machines.
Wait for a vulnerability assessment scan to be completed. The scan will start automatically, according to the schedule that is configured in the protection plan. Alternatively, you can manually start the scan on demand by clicking the Run now icon in the Vulnerability assessment module in the protection plan.
Approve the patches. You can define settings for automatic patch approval, which include an automatic installation of the patches on test machines. For more information, see Automatic patch approval. Alternatively, you can manually approve patches by setting their approval status to Approved. For more information, see Approving patches manually.
Install the patches. The approved patches can be installed automatically, according to the schedule that is configured in the protection plan. Alternatively, you can manually install patches on demand. For more information, see Installing patches on demand.

You can monitor the results of the patch installation in Monitoring> Overview > Patch installation history widget.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.