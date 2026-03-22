# CyberApp workloads

Managing workloads in the Cyber Protect console > CyberApp workloads
CyberApp workloads

CyberApp workloads are created by ISVs (Independent software vendors) and appear in the Cyber Protect console after you enable a CyberApp integration. The following conditions must be met:

The Workloads and actions extension point must be enabled in the CyberApp.
At least one Workload type must be defined in the CyberApp.

The connector service hosted by the ISV must ensure that the CyberApp workloads are added and updated to the Acronis platform.

For more information about Vendor Portal and creating CyberApps, see the Vendor Portal User Guide.

Aggregated workloads

A physical workload may have Cyber Protect agent and one or several CyberApp agents installed at the same time. In this case, the same workload will have more than one representation on the All Devices screen - a separate record will be shown for the Acronis workload, and for each CyberApp workload. If the automatic merging of workloads is enabled and configured from Vendor Portal or from the Cyber Protect console, the system will compare the host addresses and the MAC addresses of the Acronis workloads and the CyberApp workloads, and will merge all representations into a single aggregated workload. You can also manually merge and unmerge workloads in the Cyber Protect console.

Working with CyberApp workloads

Working with aggregated workloads




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.