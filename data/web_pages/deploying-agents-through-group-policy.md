# Deploying protection agents through Group Policy

Installing and deploying Cyber Protection agents > Deploying protection agents through Group Policy
Deploying protection agents through Group Policy

You can centrally install (or deploy) Agent for Windows onto machines that are members of an Active Directory domain, by using Windows Group Policy.

In this section, you will find out how to set up a Group Policy object to deploy agents onto machines in an entire domain or in its organizational unit.

Every time a machine logs on to the domain, the resulting Group Policy object will ensure that the agent is installed and registered.

Prerequisites
Active Directory domain with a domain controller running Microsoft Windows Server 2003 or later.
You must be a member of the Domain Admins group in this domain.

You have downloaded the All agents for Windows setup program.

To download the setup program, in the Cyber Protect console, click the account icon in the top-right corner, and then click Downloads. The download link is also available in the Add devices pane.

To deploy agents through Group Policy

Generate a registration token as described in Generating a registration token.

Create the .mst file, the .msi file, and the .cab files, as described in Creating the transform file and extracting the installation packages.
Set up the Group Policy object as described in Setting up the Group Policy object.

Creating the transform file and extracting the installation packages

Setting up the Group Policy object

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.