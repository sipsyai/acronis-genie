# Protecting Gmail data

Managing the backup and recovery of workloads and files > Protecting Google Workspace data > Protecting Gmail data
Protecting Gmail data
What items can be backed up?

You can back up Gmail users' mailboxes. A mailbox backup also includes the Calendar and Contacts data. Optionally, you can choose to back up the shared calendars.

The following items are skipped during a backup:

The Birthdays, Reminders, Tasks calendars
Folders attached to calendar events
The Directory folder in Contacts

The following Calendar items are skipped, due to Google Calendar API limitations:

Appointment slots
The conferencing field of an event
The calendar setting All-day event notifications
The calendar setting Auto-accept invitations (in calendars for rooms or shared spaces)

The following Contacts items are skipped, due to Google People API limitations:

The Other contacts folder
The external profiles of a contact (Directory profile, Google profile)
The contact field File as
What items can be recovered?

The following items can be recovered from a mailbox backup:

Mailboxes
Email folders (According to Google terminology, "labels". Labels are presented in the backup software as folders, for consistency with other data presentation.)
Email messages
Calendar events
Contacts

You can use search to locate items in a backup.

When recovering mailboxes and mailbox items, you can select whether to overwrite the items in the target location.

Limitations
Contact photos cannot be recovered
The Out of office calendar item is recovered as a regular calendar event, due to Google Calendar API limitations

Selecting Gmail mailboxes

Recovering mailboxes and mailbox items

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.