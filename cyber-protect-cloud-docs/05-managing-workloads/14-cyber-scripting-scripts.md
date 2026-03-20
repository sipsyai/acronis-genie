---
title: "Scripts and script repository"
section: "Managing workloads in the Cyber Protect console"
subsection: "Cyber Scripting"
page_range: "466-475"
tags: [scripts, script repository, creating scripts, AI scripts, cloning, editing, versioning, script status]
acronis_version: "26.02"
---

# Scripts

A script is a set of instructions that are interpreted at runtime and executed on a target machine. Scripts provide a convenient solution for automating repetitive or complex tasks.

With Cyber Scripting, you can run a predefined script or create a custom script. You can view all scripts that are available to you in **Management** > **Script repository**. The predefined scripts are located in the **Library** section. The scripts that you created or cloned to your tenant are located in the **My scripts** section.

You can use a script by including it in a scripting plan or by performing a **Script quick run** operation.

> **Note:** You can only use approved scripts that are created in your tenant or were cloned to it. If a script was removed from the script repository or is in a **Draft** status, it will not run. You can check the details of a scripting operation or cancel it in **Monitoring** > **Activities**.

## Script statuses

| Status | Possible actions |
|--------|-----------------|
| **Draft** | The new scripts that you create and the scripts that you clone to your repository are in Draft status. You are not allowed to run these scripts or include them in scripting plans. |
| **Testing** | Administrators with the **Cyber administrator** role can run these scripts and include them in scripting plans. |
| **Approved** | You can run these scripts and include them in scripting plans. |

Only administrators with the **Cyber administrator** role can change the status of a script or delete an approved script.

## Creating a script

You can create a script by manually writing the code.

1. In the Cyber Protect console, go to **Management** > **Script repository**.
2. In **My Scripts**, click **Create script by using AI**.
3. In the main pane, write the body of the script.

> **Important:** When you create a script, include exit code checks for each operation. Otherwise, a failed operation might be ignored and the scripting activity status in **Monitoring** > **Activities** might be incorrectly shown as **Succeeded**.

4. Specify the script settings:

| Setting | Description |
|---------|-------------|
| **Script name** | Script name. The field is populated automatically, but you can change the value. |
| **Description** | Script description. This setting is optional. [For AI-generated scripts] The field will be populated automatically upon script generation. |
| **Language** | Script language: **PowerShell** (default) or **Bash**. [For AI-generated scripts] This setting is configured before the script generation. |
| **Operating system** | Target OS: **Windows** (default) or **macOS**. [For AI-generated scripts] This setting is configured before the script generation. |
| **Status** | Script status: **Draft** (default), **Testing** (Cyber administrator only), or **Approved** (Cyber administrator only). |
| **Tags** | Tags are not case-sensitive and can be up to 32 characters long. You cannot use round and angle brackets, commas, or spaces. This setting is optional. [For AI-generated scripts] The **AI-generated** tag will be added automatically. |

5. [Only for scripts that require credentials] Specify the credentials. You can use a single credential (e.g., a token) or a pair (e.g., a user name and a password).
6. [Only for scripts that require arguments] Specify the arguments and their values:
   a. Click **Add**.
   b. In the **Add arguments** field, specify the argument.
   c. Click **Add**.
   d. In the second field that appears, specify the argument value.

   > **Note:** You can only specify arguments that you have already defined in the script body.

7. Click **Save**.

The script is saved to your repository in the **Draft** status. You cannot use the script until an administrator with the **Cyber administrator** role changes its status to **Approved**.

## Creating a script by using AI

> **Note:** The availability of this feature depends on the license that you have.

You can use AI to transform prompts into powerful scripts, saving you time and efforts. The functionality uses the GPT-4 model of OpenAI. You can use it to create up to 100 scripts for your organization per calendar month, free of charge.

1. In the Cyber Protect console, go to **Management** > **Script repository**.
2. In **My Scripts**, click **Create a script by using AI**.
3. In the prompt, enter a description of what the script should do. Ensure that the description is as clear and detailed as possible.
4. In the prompt, click the arrow button.
5. In the confirmation window, select Language and Operating system, and then click **Generate**. The script is generated and displayed in the main pane. The name and description are automatically generated. The **AI-generated** tag is automatically assigned.
6. Review the script and if necessary, edit it manually.
7. If necessary, edit the script settings (same settings table as manual creation).
8. [Optional] Specify credentials and arguments as needed.
9. Click **Save**.

## Cloning a script

Cloning a script is necessary when:
- Before using a script from the **Library**, you must first clone it to the **My Scripts** section.
- When you want to clone scripts that you created in a parent tenant to its child tenants or units.

### To clone a script

1. In **Script repository**, find the script that you want to clone.
2. Do one of the following:
   - [From **My Scripts**] Click the ellipsis (...) next to the script name, and then click **Clone**.
   - [From **Library**] Click **Clone** next to the name of the script.
3. In the **Clone script** pop-up, select a status from the **Status** drop-down list: **Draft** (default), **Testing**, or **Approved**.
4. [If you manage more than one tenant or unit] Select where you want to clone the script. In the **Clone script** dialog box, you see only the tenants that you can manage and which have the RMM or Security and RMM license.

> **Important:** Credentials that a script uses are not copied when you clone a script to a non-original tenant.

## Editing or deleting a script

### To edit a script

1. In **Script repository**, go to **My Scripts**, and then find the script that you want to edit.
2. Click the ellipsis (...) next to the script name, and then click **Edit**.
3. Edit the script, and then click **Save**.
4. [If the script is used by a scripting plan] Confirm your choice by clicking **Save script**.

> **Note:** The latest version of the script will be used next time the scripting plan runs.

### Script versions

A new version of the script is created if you edit any of the following script attributes: script body, script name, description, script language, credentials, or arguments. If you change other attributes, your edits will be added to the current script version.

> **Note:** The script status is updated only when you modify the value in the **Status** field. Only administrators with the Cyber administrator role can change a script status.

### To delete a script

1. In **Script repository**, go to **My Scripts**, and then find the script that you want to delete.
2. Click the ellipsis (...) next to the script name, and then click **Delete**.
3. Click **Delete**.
4. [If the script is used by a scripting plan] Confirm your choice by clicking **Save script**.

> **Note:** Scripting plans that use the deleted script will fail to run.

## Changing the script status

A new script in **Draft** state cannot be used until its status is changed to **Approved**. Depending on the use case, a script might be in status **Testing** for some period before it is approved.

**Prerequisites:**
- Your user is an administrator with the **Cyber administrator** role.
- A script with the corresponding state is available.

1. In **Script repository**, go to **My Scripts**.
2. Click the ellipsis (...) next to the script name, and then click **Edit**.
3. In the **Status** drop-down list, select the status.
4. Click **Save**.
5. [If you change the status of an approved script] To confirm the change, click **Save script**.

> **Note:** If the script status was downgraded to **Draft**, the scripting plans that use it will fail to run. Only administrators with the **Cyber administrator** role can run scripts in the **Testing** status and scripting plans with such scripts.

## Comparing script versions

You can compare two versions of a script and revert to an earlier version.

1. In **Script repository**, go to **My Scripts**, and then find the script whose versions you want to compare.
2. Click the ellipsis (...) next to the script name, and then click **Version history**.
3. Select two versions that you want to compare, and then click **Compare versions**. Any changes in the body text, arguments, or credentials are highlighted.

### To revert to an earlier version

1. In the **Compare script versions** window, click **Revert to this version**.
2. In the **Revert to a previous version** pop-up, in the **Status** drop-down list, select the script status.

> **Important:** You can execute scripts only with the **Testing** or **Approved** statuses.

## Downloading the output of a scripting operation

You can download the output of a scripting operation as a .zip file. It contains two text files -- `stdout` and `stderr`. In `stdout`, you can see the results of a successfully completed scripting operation. The `stderr` file contains information about the errors that occurred during the scripting operation.

1. In the Cyber Protect console, go to **Monitoring** > **Activities**.
2. Click the Cyber Scripting activity whose output you want to download.
3. On the **Activity details** screen, click **Download output**.

# Script repository

You can locate the script repository under the **Management** tab. In the repository, you can search the scripts by their name and description. You can also use filters, or sort the scripts by their name or status.

The script repository contains the following sections:

- **My scripts** -- Scripts that you can directly use in your environment. These are the scripts that you created from scratch and the scripts that you cloned here. You can filter by: Tags, Status, Language, Operating system, Script owner.
- **Library** -- Predefined scripts that you can use in your environment after cloning them to the **My scripts** section. You can only inspect and clone these scripts. You can filter by: Tags, Language, Operating system.
