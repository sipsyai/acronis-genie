---
title: "CyberFit Score and disk health monitoring"
section: "Understanding your current level of protection"
subsection: "CyberFit Score and disk health"
page_range: "330-334"
tags: [CyberFit Score, disk health, SMART, HDD, SSD, prediction, monitoring, widgets]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#disk-health-monitoring.html"
---

# CyberFit Score by machine

This widget shows for each machine the total #CyberFit Score, its compound scores, and findings for each of the assessed metrics:

- Antimalware
- Backup
- Firewall
- VPN
- Encryption
- NTLM traffic

To improve the score of each of the metrics, you can view the recommendations that are available in the report.

| Metric | #CyberFit Score | Findings |
|--------|----------------|----------|
| Anti-malware | 275 / 275 | You have anti-malware protection enabled |
| Backup | 175 / 175 | You have a backup solution protecting your data |
| Firewall | 175 / 175 | You have a firewall enabled for public and private networks |
| VPN | 0 / 75 | No VPN solution was found, your connection to public and shared networks is not protected |
| Encryption | 0 / 125 | No disk encryption was found, your device is at risk from physical tampering |
| NTLM traffic | 0 / 25 | Outgoing NTLM traffic to remote servers is not denied, your credentials may be exposed |

# Disk health monitoring

Disk health monitoring provides information about the current disk health status and a forecast about it, so that you can prevent data loss that might be related to a disk failure. Both HDD and SSD disks are supported.

## Limitations

- Disk health forecast is supported only for machines running Windows.
- Only disks of physical machines are monitored. Disks of virtual machines cannot be monitored and are not shown in the disk health widgets.
- RAID configurations are not supported. The disk health widgets do not include any information about machines with RAID implementation.
- NVMe SSDs are not supported.
- External storage devices are not supported.

## Disk health statuses

The disk health is represented by one of the following statuses:

- **OK** -- Disk health is between 70% and 100%.
- **Warning** -- Disk health is between 30% and 70%.
- **Critical** -- Disk health is between 0% and 30%.
- **Calculating disk data** -- The current disk status and forecast are being calculated.

## How it works

The Disk Health Prediction Service uses an AI-based prediction model.

1. The protection agent collects the SMART parameters of the disks and passes this data to the Disk Health Prediction Service:
   - SMART 5 -- Reallocated sectors count.
   - SMART 9 -- Power-on hours.
   - SMART 187 -- Reported uncorrectable errors.
   - SMART 188 -- Command timeout.
   - SMART 197 -- Current pending sector count.
   - SMART 198 -- Offline uncorrectable sector count.
   - SMART 200 -- Write error rate.

2. The Disk Health Prediction Service processes the received SMART parameters, makes forecasts, and then provides the following disk health characteristics:
   - Disk health current state: OK, warning, critical.
   - Disk health forecast: negative, stable, positive.
   - Disk health forecast probability in percentage.

   The prediction period is one month.

3. The Monitoring Service receives these characteristics, and then shows the relevant information in the disk health widgets in the Cyber Protect console.

## Disk health widgets

The results of the disk health monitoring are presented in the following widgets that are available in the Cyber Protect console.

### Disk health overview

A treemap widget with two levels of detail that can be switched by drilling down:

- **Machine level** -- Shows summarized information about the disk health status of the selected customer machines. Only the most critical disk status is shown. The other statuses are shown in a tooltip when you hover over a particular block. The machine block size depends on the total size of all disks of the machine. The machine block color depends on the most critical disk status found.

- **Disk level** -- Shows the current disk health status of all disks for the selected machine. Each disk block shows one of the following disk health forecasts and its probability in percentage:
  - Will be degraded
  - Will stay stable
  - Will be improved

### Disk health status

A pie chart widget that shows the number of disks for each status (Calculating disk data, Critical, Warning, OK).

## Disk health status alerts

The disk health check runs every 30 minutes, while the corresponding alert is generated once a day. When the disk health changes from **Warning** to **Critical**, an alert is always generated.

| Alert name | Severity | Disk health status | Description |
|---|---|---|---|
| Disk failure is possible | Warning | (30 -- 70) | The disk on this machine is likely to fail in the future. Run a full image backup of this disk as soon as possible, replace it, and then recover the image to the new disk. |
| Disk failure is imminent | Critical | (0 -- 30) | The disk on this machine is in a critical state, and will most likely fail very soon. We do not recommend an image backup of this disk at this point, as the added stress can cause the disk to fail. Back up the most important files on this disk immediately and replace it. |
