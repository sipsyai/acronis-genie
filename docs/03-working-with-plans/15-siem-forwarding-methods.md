---
title: "SIEM forwarding methods"
section: "Working with plans"
subsection: "SIEM forwarding plans"
page_range: "272"
tags: [SIEM, forwarding methods, files, syslog, Linux, Windows]
acronis_version: "26.02"
---

# SIEM forwarding methods

With Acronis SIEM forwarding, the Acronis agent writes SIEM data on an Acronis-managed writer device. It can work with one of two forwarding methods:

- **Files** -- Applicable with a Windows or a Linux writer device.
- **Syslog** -- Applicable only with a Linux writer device.

## Files forwarding method

This method can be implemented with either a Windows or a Linux writer device.

The SIEM data is written as files to a directory. You can specify a directory or accept the default.

### Default directories

- Windows writer device: `C:\`
- Linux writer device: `/var/log/siem`

> **Important:** Only administrators have access to these files.

## Syslog server forwarding method

A syslog server is a centralized system that receives and stores log messages using the Syslog protocol.

> **Important:** Only Linux devices can be used for this method.

### To review forwarded SIEM data

1. Execute: `cat /var/log/syslog`
2. Execute: `cat /var/log/messages`
