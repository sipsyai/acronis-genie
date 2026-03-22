# Device control alerts

Managing workloads in the Cyber Protect console > Working with the Device control module > Device control alerts
Device control alerts

The device control maintains an event log by tracking user attempts to access controlled device types, ports, or interfaces. Certain events can raise alerts that are logged in the Cyber Protect console. For example, the device control module can be configured to prevent the use of removable devices, with an alert logged whenever a user tries to copy data to or from such a device.

When configuring the device control module, you can enable alerts for most items listed under device Type (except screenshot capture) or Ports. If alerts are enabled, each attempt by a user to perform an operation that is not allowed generates an alert. For example, if access to removable devices is restricted to read-only, and the Show alert option is selected for that device type, an alert is generated every time a user on a protected computer attempts to copy data to a removable device.

To view alerts in the Cyber Protect console, go to Monitoring > Alerts. Within each device control alert, the console provides the following information about the respective event:

Type—Warning.
Status—Displays “Peripheral device access is blocked”.
Message—Displays “Access to '<device type or port>' on '<computer name>' is blocked”. For example, “Access to 'Removable' on 'accountant-pc' is blocked”.
Date and time—The date and time that the event occurred.
Device—The name of the computer on which the event occurred.
Plan name—The name of the protection plan that caused the event.
Source—The device type or port involved in the event. For example, in the event of a denied user attempt to access a removable device, this field reads Removable device.
Action—The operation that caused the event. For example, in the event of a denied user attempt to copy data to a device, this field reads Write. For more information, see Action field values.
Name—The name of the event target object, such as the file the user attempted to copy or the device the user attempted to use. Not displayed if the target object cannot be identified.
Information—Additional information about the event target device, such as the device ID for USB devices. Not displayed if no additional information about the target device is available.
User—The name of the user who caused the event.
Process—The fully qualified path to the executable file of the application that caused the event. In some cases, the process name might be displayed instead of the path. Not displayed if process information is not available.

If an alert applies to a USB device (including removable devices and encrypted removable devices), then, directly from the alert, the administrator can add the device to the allowlist, which prevents the device control module from restricting access to that particular device. Clicking Allow this USB device adds it to the USB devices allowlist in the device control module’s configuration, and also adds it to the USB devices database for further reference.

See also steps to view device control alerts.

Action field values

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.