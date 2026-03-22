# Ports used by Device Sense ™

Installing and deploying Cyber Protection agents > Device discovery > Device discovery by using Device Sense ™ > Ports used by Device Sense ™
Ports used by Device Sense ™

This topic lists the ports that Device Sense ™ uses.

Passive device discovery uses the following ports.

Name	Port	Comment
DHCP	udp/67	Listens for REQUEST messages
NBNS	udp/137	Listens for NAME REGISTRATION REQUEST and NAME REFRESH REQUEST packets


NBDS (Browser)

udp/138	Listens for announcement messages
SSDP	udp/1900	Listens for M-SEARCH and NOTIFY messages
WSD	udp/3702	Listens for wsd:Probe messages
MDNS	udp/5353	Listens for various service info announcements
LLMNR	udp/5355	Listens for queries
TUYA	udp/6668	Listens for discovery packets

When Enhanced identification of devices on a network is enabled, Device Sense ™ uses the following ports.

Name	Ports	Comment
SSDP	udp/1900	Sends M-SEARCH requests
WSD	udp/3702	Sends wsd:Probe requests

Active device discovery (on-demand scan flow) uses the following ports.

Name	Ports	Comment
FTP	tcp/21	Reads service banners
SSH	tcp/22	Reads service banners
TELNET	tcp/23	Reads banners
SMTP	tcp/25, tcp/587

Reads EHLO messages


RDNS	udp/53

Makes a reverse DNS request *.in-addr.arpa


HTTP	tcp/80, tcp/8080, and other common HTTP ports	Sends GET requests
NBNS	udp/135

Sends NBSTAT requests


SNMP	udp/161

Reads MIBs: Versions: v1, v2c; Communities: public


HTTPS	tcp/443, tcp/8443	Sends GET requests
SMB	tcp/445	Extracts data from NTLMv2 auth messages
RTSP	tcp/554	Sends OPTIONS requests
SSDP	udp/1900

Sends M-SEARCH


ARD	udp/3283	Sends Start packets
RDP	tcp/3389

Sends Connection Request and reads Connection Confirm


WSD	udp/3702	Sends wsd:Probe messages
AirPlay	tcp/5000, tcp/7000

Sends wsd:Probe messages


MDNS	udp/5353

Sends PTR messages


iRobot	udp/5678

Sends iRobot discover packets

irobotmsc


VNC	udp/5900

Sends RFB ProtocolVersion and Security messages


MIIO	udp/54321

Sends Hello packets

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.