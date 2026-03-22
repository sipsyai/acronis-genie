# Two-factor authentication

Two-factor authentication
Two-factor authentication

Two-factor authentication (2FA) is a type of multi-factor authentication that checks the identity of a user by a combination of two of these factors:

Something that a user knows (PIN or password)
Something that a user has (token)
Something that a user is (biometrics)

Two-factor authentication provides extra protection from unauthorized access to your account.

The Cyber Protect Cloud platform supports Time-based One-Time Password (TOTP) authentication. If the TOTP authentication is enabled in the system, users must enter their traditional password and the one-time TOTP code to access the system. In other words, a user provides the password (the first factor) and the TOTP code (the second factor). The TOTP code is generated in the authentication application on a user second-factor device on the basis of the current time and the secret (QR-code or alphanumeric code) that is provided by the platform.

For partner tenants in production mode, two-factor authentication is enabled by default and cannot be disabled.

For customer tenants, two-factor authentication is optional and can be disabled.

Partner administrator accounts that are used by an integration must be converted to service accounts. Otherwise, the integrations will not be able to authenticate to Cyber Protect Cloud. For example, accounts used by an integration are the accounts for the management agent and the backup agent in the VMware Cloud Director integration.

2FA brute-force protection

2FA propagation across tenant levels

How 2FA enablement works

Enabling 2FA

Replacing your second-factor device

Managing 2FA for users

Disabling 2FA

Back to Top



Last build date: Tuesday, March 10, 2026

Partner Administrator Help for Management Portal26.02.