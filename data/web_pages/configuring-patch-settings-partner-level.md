# Configuring patch settings at partner level

RMM > Managing software > Assessing vulnerabilities and managing patches > Configuring patch settings at partner level
Configuring patch settings at partner level

At the partner level (All customers), you can configure settings for automatic acceptance of license agreements and automatic patch approval and, optionally, propagate them to all your customers. Thus, your customers will inherit the settings that you configure, and will not be able to change them.

If you decide not to propagate the settings that you configure, your customers will initially see the default settings, and will be allowed to change them.

To configure patch settings at partner level

In Cyber Protect console at the partner level (All customers), go to Software management > Patches.

Click Settings, and then do the following:

Click Lifetime in list.

The patch will be removed from the list after it is successfully installed on all the machines on which it was indicated as missing, or after the lifetime in the list passes.

This setting is not propagated to your customers.

Configure the automatic patch approval settings.

Setting	Description
Automatic patch approval

A switch that enables or disables automatic patch approval for your customers.


Apply automatic patch approval to all low-level tenants

Select this field if you want to propagate the automatic patch approval settings to your customers.

If you turn on Automatic patch approval, the field is automatically selected and disabled, to avoid potential conflicts with your customers' settings.

Your customers will still be allowed to change the value for each patch manually, if necessary.


Automatic patch approval and testing

The approval status of the patch will change to Approved when the selected number of days passes after a successful installation of the patch.


Automatic patch approval without testing	The approval status of the patch will change to Approved when the selected number of days passes after the patch is found.
Period selector

Select the number of days that must pass after the condition from the automatic patch approval option is met. After this period, the approval status of the patches will automatically change from Pending approval to Approved.

The maximum period that you can select is 30 days.

Configure automatic acceptance of license agreements.

Setting	Description
Automatically accept the license agreements	A switch that enables or disables the automatic acceptance of license agreements for your customers.
Apply automatic license agreement to all low-level tenants

Select this field if you want to propagate the settings for automatic acceptance of license agreement to your customers.

If you turn on Apply automatic license agreement to all low-level tenants, the field is automatically selected and disabled, to avoid potential conflicts with your customers' settings.

Your customers will still be allowed to change the value for each agreement manually, if necessary.

Click Apply, and then, in the confirmation window that opens, click Confirm.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.