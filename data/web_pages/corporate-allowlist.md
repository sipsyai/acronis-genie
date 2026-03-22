# Corporate whitelist

Configuring your antivirus and antimalware protection > Corporate whitelist
Corporate whitelist

An antivirus solution might identify legitimate corporate-specific applications as suspicious. To prevent these false-positive detections, the trusted applications must be manually added to a whitelist.

Corporate whitelist does not affect antimalware scans of backups.

Cyber Protection can automate this process: backups are scanned by the Antivirus and Antimalware protection module and the scanned data is analyzed, so that such applications are moved to the whitelist, and false-positive detections are prevented. Also, the company-wide whitelist improves the further antimalware scanning performance.

The whitelist is created for each customer, and is based only on this customer's data.

The whitelist can be enabled and disabled. When it is disabled, the files added to it are temporarily hidden.

Only accounts with the administrator role (for example, Cyber Protection administrator, company administrator, partner administrator who acts on behalf of a company administrator, unit administrator) can configure and manage the whitelist.

This functionality is not available for a read-only administrator account or a user account.

Automatic adding to the whitelist
Run a cloud scanning of backups on at least two machines. You can do this by using the backup scanning plans.
In the whitelist settings, enable the Automatic generation of whitelist switch.
Manual adding to the whitelist

Even when the Automatic generation of whitelist switch is disabled, you can add files to the whitelist manually.

In the Cyber Protect console, go to Protection > Whitelist.
Click Add file.
Specify the path to the file, and then click Add.
Adding quarantined files to the whitelist

You can add files that are quarantined to the whitelist.

In the Cyber Protect console, go to Protection > Quarantine.
Select a quarantined file, and then click Add to whitelist.
Whitelist settings

When you enable the Automatic generation of whitelist switch, you must specify one of the following levels of heuristic protection:

Low
Corporate applications will be added to the whitelist only after a significant amount of time and checks. Such applications are more trusted. However, this approach increases the possibility of false-positive detections. The criteria to consider a file as clean and trusted are high.

Default
Corporate applications will be added to the whitelist according to the recommended protection level, to reduce possible false-positive detections. The criteria to consider a file as clean and trusted are medium.

High
Corporate applications will be added to the whitelist faster, to reduce possible false-positive detections. However, this does not guarantee that the software is clean, and it might later be recognized as suspicious or malware. The criteria to consider a file as clean and trusted are low.

Viewing details about items in the whitelist

You can click an item in the whitelist to view more information about it and to analyze it online.

If you are unsure about an item that you added, you can check it in the VirtusTotal analyzer. When you click Check on VirusTotal, the site analyzes suspicious files and URLs to detect types of malware by using the file hash of the item that you added. You can view the hash in the File hash (MD5) string.

The Machines value represents the number of machines where such hash was found during backup scanning. This value is populated only if an item came from Backup scanning or Quarantine. This field remains empty if the file has been added manually to the whitelist.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.