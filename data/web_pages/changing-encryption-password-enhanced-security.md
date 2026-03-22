# Changing the encryption password

Additional Cyber Protection tools > Compliance mode > Changing the encryption password
Changing the encryption password

You can change the encryption password before a protection plan creates any backups.

We recommend that you do not change the encryption password after backups are created, because subsequent backups will fail. To continue protecting the same machine, you must create a new protection plan for it. Changing both the encryption password and the protection plan will result in creating new backups that are encrypted with the changed password. The backups that were created before these changes will not be affected.

Alternatively, you can keep the applied protection plan, and change only the backup file name in it. This will also result in creating new backups that are encrypted with the changed password. To learn more about the backup file name, refer to Backup file name.

You can change the encryption password in the following ways:

In the Cyber Protect Monitor (for Windows and macOS).

By using the command line (for Windows and Linux).

For more information on how to set an encryption password with the Acropsh tool, refer to Encryption.

See also
Setting the encryption password
Encryption
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.