# Setting up the Group Policy object

Installing and deploying Cyber Protection agents > Deploying protection agents through Group Policy > Setting up the Group Policy object
Setting up the Group Policy object

In this procedure you use the installation packages that you created in Creating the transform file and extracting the installation packages to set up a Group Policy object (GPO). The GPO will deploy the agents onto the machines in your domain.

To set up the Group Policy object

Log in to the domain controller as a domain administrator.

If the domain has more than one domain controller, log in to any of them as a domain administrator.

[If you deploy agents in an organizational unit] Ensure that the organizational unit in which you want to deploy the agents exists in this domain.
In the Windows Start menu, point to Administrative Tools, and then click Group Policy Management (or Active Directory Users and Computers for Windows Server 2003).
[For Windows Server 2008 or later] Right-click the name of the domain or organizational unit, and then click Create a GPO in this domain, and Link it here.
[For Windows Server 2003] Right-click the name of the domain or organizational unit, and then click Properties. In the dialog box, click the Group Policy tab, and then click New.
Name the new Group Policy object Agent for Windows.

Open the Agent for Windows Group Policy object for editing:

[In Windows Server 2008 or later] Under Group Policy Objects, right-click the Group Policy object, and then click Edit.
[In Windows Server 2003] Click the Group Policy object, and then click Edit.
In the Group Policy object editor snap-in, expand Computer Configuration.
[For Windows Server 2012 or later] Expand Policies > Software Settings.

[For Windows Server 2003 and Windows Server 2008] Expand Software Settings.

Right-click Software installation, point to New, and then click Package.
Select the agent's .msi installation package in the shared folder that you created, and then click Open.
In the Deploy Software dialog box, click Advanced, and then click OK.
On the Modifications tab, click Add, and then select the .mst file in the shared folder that you created.
Click OK to close the Deploy Software dialog box.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.