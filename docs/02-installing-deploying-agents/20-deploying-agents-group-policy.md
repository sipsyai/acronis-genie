---
title: "Deploying protection agents through Group Policy"
section: "Installing and deploying Cyber Protection agents"
subsection: "Deploying protection agents through Group Policy"
page_range: "129-131"
tags: ["Group Policy", "GPO", "Active Directory", "deployment", "MST", "MSI", "Windows", "domain"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#deploying-agents-through-group-policy.html"
---

# Deploying protection agents through Group Policy

You can centrally install (or deploy) Agent for Windows onto machines that are members of an Active Directory domain, by using Windows Group Policy.

In this section, you will find out how to set up a Group Policy object to deploy agents onto machines in an entire domain or in its organizational unit.

Every time a machine logs on to the domain, the resulting Group Policy object will ensure that the agent is installed and registered.

## Prerequisites

- Active Directory domain with a domain controller running Microsoft Windows Server 2003 or later.
- You must be a member of the **Domain Admins** group in this domain.
- You have downloaded the **All agents for Windows** setup program. To download the setup program, in the Cyber Protect console, click the account icon in the top-right corner, and then click **Downloads**. The download link is also available in the **Add devices** pane.

## To deploy agents through Group Policy

1. Generate a registration token as described in "Generating a registration token."
2. Create the .mst file, the .msi file, and the .cab files, as described in "Creating the transform file and extracting the installation packages" below.
3. Set up the Group Policy object as described in "Setting up the Group Policy object" below.

## Creating the transform file and extracting the installation packages

To deploy protection agents via Windows Group Policy, you need a transform file (.mst), and the installation packages (.msi and .cab files).

> **Note:** The procedure below uses the default registration option, which is registration by token.

### To create the .mst file and extract the installation packages (.msi and .cab files)

1. Log in as an administrator on any machine in the Active Directory domain.
2. Create a shared folder that will contain the installation packages. Ensure that domain users can access the shared folder -- for example, by leaving the default sharing settings for **Everyone**.
3. Run the agent setup program.
4. Click **Create .mst and .msi files for unattended installation**.
5. In **What to install**, select the components that you want to include in the installation, and then click **Done**.
6. In **Registration settings**, click **Specify**, enter a registration token, and then click **Done**. You can change the registration method from **Use registration token** (default) to **Use credentials** or **Skip registration**. The **Skip registration** option presumes that you will register the workloads manually later.
7. Review or modify the installation settings, which will be added to the .mst file, and then click **Proceed**.
8. In **Save the files to**, specify the path to the shared folder that you created.
9. Click **Generate**.

As a result, the .mst file, the .msi file, and the .cab files are created and copied to the shared folder that you specified.

## Setting up the Group Policy object

In this procedure you use the installation packages created above to set up a Group Policy object (GPO). The GPO will deploy the agents onto the machines in your domain.

### To set up the Group Policy object

1. Log in to the domain controller as a domain administrator. If the domain has more than one domain controller, log in to any of them as a domain administrator.
2. (If deploying to an organizational unit) Ensure that the organizational unit in which you want to deploy the agents exists in this domain.
3. In the Windows **Start** menu, point to **Administrative Tools**, and then click **Group Policy Management** (or **Active Directory Users and Computers** for Windows Server 2003).
4. (For Windows Server 2008 or later) Right-click the name of the domain or organizational unit, and then click **Create a GPO in this domain, and Link it here**.
5. (For Windows Server 2003) Right-click the domain or organizational unit, click **Properties**, click the **Group Policy** tab, and then click **New**.
6. Name the new Group Policy object **Agent for Windows.**
7. Open the **Agent for Windows** Group Policy object for editing:
   - (In Windows Server 2008 or later) Under **Group Policy Objects**, right-click the Group Policy object, and then click **Edit**.
   - (In Windows Server 2003) Click the Group Policy object, and then click **Edit**.
8. In the Group Policy object editor snap-in, expand **Computer Configuration**.
9. (For Windows Server 2012 or later) Expand **Policies** > **Software Settings**.
10. (For Windows Server 2003 and Windows Server 2008) Expand **Software Settings**.
11. Right-click **Software installation**, point to **New**, and then click **Package**.
12. Select the agent's .msi installation package in the shared folder that you created, and then click **Open**.
13. In the **Deploy Software** dialog box, click **Advanced**, and then click **OK**.
14. On the **Modifications** tab, click **Add**, and then select the .mst file in the shared folder that you created.
15. Click **OK** to close the **Deploy Software** dialog box.
