# What information is included in an attack stage?

Endpoint Detection and Response (EDR) > How to use Endpoint Detection and Response (EDR) > Investigating incidents > What information is included in an attack stage?
What information is included in an attack stage?

Each attack stage provides an easy to understand interpretation of the attack, in easily readable human language. This interpretation is composed of a number of elements, as shown below and described in the following table.

Attack stage element	Description
Header

Describes what the attacker tried to do, and their objective (in the example above, Credential Access), with a link to a known MITRE ATT&CK technique. Click the link to learn more on the MITRE ATT&CK website.

If an attack stage is not a known MITRE ATT&CK technique, the header text won't be linked. This is relevant for generic techniques such as files detected in a random folder.

Timestamp	The time the attack stage occurred.
Technique

How the attacker technically achieved their objective, and what objects (registry entries, files, or scheduled tasks) were affected.

Included in the text description of the attack technique are color-coded links to each affected node in the cyber kill chain, as shown in the example above. These color-coded links enable you to navigate quickly to the affected node and to investigate what exactly happened. The colors used in an attack stage indicate the following:

Looking at the above legend, we can see that the Credential Access example attack stage has a link to a malware node  and a suspicious file node (click on the links to jump to the corresponding node in the cyber kill chain). For more information about navigating these nodes and the actions available, see Investigate individual nodes in the cyber kill chain.

Note that attack stages also include links to file nodes that have information about compromised files which contain sensitive information, such as protected health information (PHI), credit card numbers and social security numbers.

Each attack stage is a single detection event. The content listed in each stage (header, timestamp, technique) is generated according to specific parameters in the detection event, and which are based on attack stage templates stored by Endpoint Detection and Response (EDR).
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.