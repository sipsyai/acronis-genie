# Encryption

Managing the backup and recovery of workloads and files > Encryption
Encryption

Cyber Protect uses two levels of security to protect backed-up data from unauthorized access.

Backed-up data is encrypted with a 256-bit key, which is in turn encrypted by using the SHA-2 (256-bit) hash of a user-provided encryption password as a key, as follows:

When creating a protection plan with encryption enabled, the user specifies an encryption password.

Cyber Protect does not store this password. Recovering a lost password is not possible.

Password-Based Key Derivation Function 2 (PBKDF2) is applied to the user-provided encryption password 1,048,576 times (2 to the power of 20). As a result, a SHA-2 (256-bit) hash is created. This is the first key, which is used to encrypt the second key.
A random 256-bit key is created by using OpenSSL. This is the second key, which is used to encrypt the backed-up data.
The second key is encrypted by using Advanced Encryption Standard (AES-256), and the hash that is derived from the user-provided encryption password.
The encrypted second key is added to the backup archive.
Backed-up data is encrypted by using Advanced Encryption Standard with the Galois/Counter Mode (AES-256 GCM) and the second key.
When recovering data, the user must provide the encryption password. The hash of that password is the first encryption key. This key is used to decrypt the second key. With the second key, the backup archive can be decrypted and recovered.

Using the AES-256 algorithm with a strong password provides quantum-resistant encryption. It is safe against cryptanalytic attacks that rely on quantum computing.

We recommend that you encrypt all backups that are stored in the cloud storage, especially if your company is subject to regulatory compliance.

You can configure encryption in the following ways:

In the protection plan
As a machine property, by using the Cyber Protect Monitor or the command-line interface

Configuring encryption in the protection plan

Configuring encryption as a machine property

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.