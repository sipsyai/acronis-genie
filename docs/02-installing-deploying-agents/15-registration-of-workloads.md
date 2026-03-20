---
title: "Registration of workloads"
section: "Installing and deploying Cyber Protection agents"
subsection: null
page_range: "105-107"
tags: ["registration", "workload", "tenant", "token", "credentials", "console"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#registration-workloads.html"
---

# Registration of workloads

A registration is connecting a workload on which a protection agent is installed to a user account in a customer tenant. After the registration completes, you can see the workload in the Cyber Protect console, under **Devices** > **Machines with agents**. You can manage registered workloads by applying plans to them.

When you install a protection agent by using the graphical user interface, the registration is part of the installation procedure. When you use the command-line interface, you can perform the registration as a stand-alone procedure.

## Registering workloads by using the graphical user interface

When you install a protection agent by using the graphical user interface, the registration is part of the installation procedure.

The following registration methods are available:

- Registration in the Cyber Protect console
- Registration with user account credentials
- Registration with a registration token

The agent is automatically unregistered when you uninstall it.

### Registering workloads by using the Cyber Protect console

#### Prerequisites

- You finished the installation of a protection agent with the default installation settings (**Registration settings** > **Use Cyber Protect console**), and the installation wizard is still open.

> **Note:** Do not close the installation wizard before completing the registration. Otherwise, you will have to repeat the installation and start the registration again.

- To be able to select a plan during the registration, two-factor authentication (2FA) must be enabled for the tenant to which your account belongs.

#### To register a workload from the Cyber Protect console

1. In the installation wizard, click **Register workload**. The Cyber Protect console opens.
2. Log in to the Cyber Protect console. The **Register workload** wizard opens.
3. [If you log in as an administrator] On the **Select account** tab, select the account under which you want to register the workload. This account must be in a customer tenant or a unit. Partner administrators can see the customer tenants that they manage, and can register workloads under accounts in these tenants.
4. Click **Validate code**.
5. Click **Next**.
6. [If 2FA is enabled for your account] On the **Select plans** tab, review the preselected plans that will be applied to the workload.
7. [Optional] [If 2FA is enabled for your account] To change a preselected plan, click **Change**. Select a plan. Click **Select**.
8. [Optional] If you do not want to apply a preselected plan, click **Change**, and then click **Do not apply**.
9. On the **Review and register** screen, check the required quotas, and then do one of the following:
   a. To register the workload, click **Register**. If you are logged in as a partner administrator, any required advanced packs will be automatically enabled for the tenant in which you register the workload.
   b. To select different plans, go to the **Select plans** tab, and then continue this procedure.

As a result, the workload is registered under the specified account and the selected plans are automatically applied.

### Registering workloads by using user credentials

You can modify the default installation procedure and select registration with a user name and password, instead of registration in the Cyber Protect console.

#### To register a workload by using a user name and password

1. In the installation wizard, click **Customize installation settings**.
2. In the **Registration settings** section, click **Change**.
3. Select **Use credentials**.
4. Specify the user name and password of the account under which you want to register the workload. This account must be an account in a customer tenant.

> **Note:** You can use only accounts for which two-factor authentication is not enabled.

5. Click **Done**, and then complete the installation.
