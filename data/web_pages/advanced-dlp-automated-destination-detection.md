# Automated detection of destination

Data Loss Prevention > Automated detection of destination
Automated detection of destination

In Mixed Observation mode, Data Loss Prevention applies different rules depending on the destination of the detected data transfer - internal or external. The logic for determining a destination as internal is described below. All other destinations are considered external.

For each intercepted data transfer, Data Loss Prevention detects automatically if the destination HTTP, FTP, or SMB server is internal by performing a DNS request and comparing the FQDN names of the machine where the Data Loss Prevention agent runs and the remote server. If the DNS request fails, it also checks if the protected workload and the remote server are in the same network. Servers that have the same domain name (or are in the same subnetwork) as the machine where the Data Loss Prevention agent runs are considered internal.

For email communication, Data Loss Prevention treats as internal transfers all emails sent from a corporate email address by using the corporate mail server if the recipient email is on the same domain as the sender email, and the recipient mail server name is the same.

Non-corporate emails are treated as external communication unless the recipient account is known. Known email addresses are updated as Data Loss Prevention monitors the user activity on the network and updates the database at the back end with data for email addresses associated with the user.

Communications via messengers are treated as external communications unless the recipient account is known. Known accounts are updated as Data Loss Prevention monitors the user activity on the network and updates the database at the back end with data for accounts associated with the user.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.