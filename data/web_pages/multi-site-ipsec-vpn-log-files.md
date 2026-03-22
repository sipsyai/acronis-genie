# Multi-site IPSec VPN log files

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Connectivity and networks > Multi-site IPSec VPN log files
Multi-site IPSec VPN log files
The availability of this feature depends on the service quotas that are enabled for your account.

The following list describes the IPsec VPN log files that are part of the zip archive, and the information that they contain.

ip.txt - The file contains the logs from the configuration of the network interfaces. You must see two IP addresses - a public IP address, and a local IP address. If you do not see these IP addresses in the log, there is a problem. Contact the Support team.

The mask for the public IP address must be 32.

swanctl-list-loaded-config.txt - The file contains information about all IPsec sites.

If you do not see a site in the file, then the IPsec configuration was not applied. Try to update the configuration and save it, or contact the Support team.

swanctl-list-active-sas.txt - The file contains connections and policies that are in status active or a connecting.



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.