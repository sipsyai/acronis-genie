# IPsec/IKE security settings

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Connectivity and networks > IPsec/IKE security settings
IPsec/IKE security settings
The availability of this feature depends on the service quotas that are enabled for your account.

The following table provides more information about the Psec/IKE security parameters.

Parameter	Description
Encryption algorithm	The encryption algorithm that will be used to ensure that data is not viewable while in transit. By default, all algorithms are selected. You must configure at least one of the selected algorithms on your local gateway device for each IKE phase.
Hash algorithm	The hash algorithm that will be used to verify the data integrity and authenticity. By default, all algorithms are selected. You must configure at least one of the selected algorithms on your local gateway device for each IKE phase.
Diffie-Hellman group numbers

The Diffie-Hellman group numbers define the strength of the key that is used in the Internet Key Exchange (IKE) process.

Higher group numbers are more secure but require additional time for the key to compute.

By default, all groups are selected. You must configure at least one of the selected groups on your local gateway device for each IKE phase.


Lifetime (seconds)

The lifetime value determines the duration of a connection instance with a set of encryption/authentication keys for user packets, from successful negotiation to expiry.

Range for Phase 1: 900-28800 seconds with default 28800.

Range for Phase 2: 900-3600 seconds with default 3600.

The lifetime for Phase 2 must be less than the lifetime for Phase 1.

The connection is re-negotiated through the keying channel before it expires, see Rekey margin time. If the local and the remote side do not agree on the lifetime, a clutter of superseded connections will occur on the side with the longer lifetime. See also Rekey margin time and Rekey fuzz.


Rekey margin time (seconds)	The margin time before connection expiration or keying-channel expiration, during which the local side of the VPN connection attempts to negotiate a replacement. The exact time of the rekey is randomly selected based on the value of Rekey fuzz. Relevant only locally, the remote side does not need to agree on it. Range: 900-3600 seconds. The default value is 3600.
Replay window size (packet)

The IPsec replay window size for this connection.

The default -1 uses the value configured with charon.replay_window in the strongswan.conf file.

Values larger than 32 are supported only when using the Netlink backend.

A value of 0 disables the IPsec replay protection.


Rekey fuzz (%)

The maximum percentage by which marginbytes, marginpackets and margintime are randomly increased to randomize rekeying intervals (important for hosts with many connections).

The Rekey fuzz value can exceed 100%. The value of marginTYPE, after the random increase, must not exceed lifeTYPE, where TYPE is one of bytes, packets or time.

The value 0% disables randomization. Relevant only locally, the remote side does not need to agree on it.


DPD timeout (seconds)	Time after which a dead peer detection (DPD) timeout occurs. You can specify value 30 or higher. The default value is 30.
Dead peer detection (DPD) timeout action

The action to take after a dead peer detection (DPD) timeout occurs.

Restart - Restart the session when DPD timeout occurs.

Clear - End the session when DPD timeout occurs.

None - Take no action when DPD timeout occurs.


Startup action

Determines which side initiates the connection and establishes the tunnel for the VPN connection.

Add - your local VPN gateway initiates the connection.

Start - the cloud VPN gateway initiates the connection.

Route - suitable for VPN gateways that support the route option. The tunnel is up only when there is traffic initiated from either the local VPN gateway, or the cloud VPN gateway.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.