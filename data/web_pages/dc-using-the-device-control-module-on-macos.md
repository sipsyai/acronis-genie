# Enabling the use of the device control module on macOS

Managing workloads in the Cyber Protect console > Working with the Device control module > Using device control > Enabling the use of the device control module on macOS
Enabling the use of the device control module on macOS

The device control settings of a protection plan become effective only after loading the device control driver on the protected workload. This section describes how to load the device control driver to enable the use of the device control module on macOS. This is a one-time operation that requires administrator privileges on the endpoint machine.

Supported macOS versions:

macOS 10.15 (Catalina) and later

macOS 11.2.3 (Big Sur) and later

macOS 12.2 (Monterey) and later

macOS 13.2 (Ventura) and later

macOS 14 (Sonoma) and later

macOS 15 (Sequoia) and later

To enable the use of device control module on macOS

Install Agent for Mac on the machine that you want to protect.
Enable device control settings in the protection plan.
Apply the protection plan.
The "System Extension Blocked" warning will appear on the protected workload. Click Open Security Preferences.

In the Security & Privacy pane that appears, select App Store and identified developers and then click Allow.

In the dialog that appears, click Restart to restart the workload and activate the device control settings.
You do not have to repeat these steps if the device control setting are disabled and then enabled again.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.