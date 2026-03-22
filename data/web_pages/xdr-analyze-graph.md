# How to analyze the XDR graph

Extended Detection and Response (XDR) > Working with the XDR graph > How to analyze the XDR graph
How to analyze the XDR graph

XDR (Extended Detection and Response) adds additional details to an EDR (Endpoint Detection and Response) incident, such as verifying if the threat came from an email attachment, collaboration application, or a link in an email, and which user was logged in and responsible for opening the malicious attachment. By analyzing the XDR graph, you are provided with additional context of what happened in the incident and if action beyond the functionality of EDR is required, such as blocking the user account, and/or blocking the email sender.

Looking at the nodes displayed in the XDR graph shown below, you can see that a malicious threat was extracted from a zip file attached to an email downloaded to DESKTOP-DEABSS0. The sender's email address was finance.dept@proton.me, and the user that logged in and opened the zip file was bobby.smith@xys.com.

By clicking on the desktop icon, you can see in the Overview tab if the workload is the logged in user's usual workload. If the user logged in with an operating system or IP address they never used previously, the probability is that the incident is malicious. You can then apply the required response actions to users on compromised devices to ensure they have no access to sensitive data and IT resources.

There are additional XDR graph elements that help you understand exactly what happened.

For example, XDR integration with Microsoft 365 services includes the following:

When a malicious file is located in a Microsoft 365 application (OneDrive, SharePoint, Teams, or Outlook), a line is shown to connect the malicious file node to the relevant collaboration application node.

Similarly, XDR integration with FortiMail Workspace Security (formerly Perception Point) includes the following:

When a malicious file is a direct attachment of an email, a line is shown to connect the malicious file node to the email node.
When the malicious node is an URL node, a line is shown to connect the malicious URL node to the email node.
When a malicious file was extracted from a zip archive attachment (or other type of compressed archive), a file node is created for the zip archive, and a line is shown to connect the malicious file node to the attachment node.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.