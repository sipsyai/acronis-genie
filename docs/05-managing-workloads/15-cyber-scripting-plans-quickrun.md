---
title: "Scripting plans and script quick run"
section: "Managing workloads in the Cyber Protect console"
subsection: "Cyber Scripting"
page_range: "475-483"
tags: [scripting plans, script quick run, scheduling, start conditions, target workloads, automation]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#cyber-scripting-script-quick-run.html"
---

# Scripting plans

A scripting plan allows you to run a script on multiple workloads, to schedule the running of a script, and to configure additional settings.

You can find the scripting plans that you created and the ones that are applied to your workloads in **Management** > **Scripting plans**. Here, you can check the plan execution location, owner, or status.

## Plan statuses

A clickable color-coded bar shows the following statuses for scripting plans:

- Running (Blue)
- Checking for compatibility (Dark gray)
- Disabled (Light gray)
- OK (Green)
- Critical alert (Red)
- Error (Orange)
- Warning (Yellow)

By clicking the bar, you can see which status a plan has and on how many workloads. Each status is also clickable.

## Managing scripting plans

On the **Scripting plans** tab, you can manage the plans by performing the following actions: Run, Stop, Edit, Rename, Disable, Enable, Clone, Export (to JSON format), Delete.

The visibility of a scripting plan and the available actions with it depend on the plan owner and your user role. For example, company administrators can only see the partner-owned scripting plans that are applied to their workloads, and cannot perform any actions with these plans.

### To manage a scripting plan

1. In the Cyber Protect console, go to **Management** > **Scripting plans**.
2. Find the plan that you want to manage, and then click the ellipsis (...) next to it.
3. Select the desired action, and then follow the instructions on the screen.

## Creating a scripting plan

You can create a scripting plan in the following ways:

- On the **Devices** tab: Select workloads, and then create a scripting plan for them.
- On the **Management** > **Scripting plans** tab: Create a scripting plan and then select the workloads to which to apply the plan.

### To create a scripting plan on the Devices tab

1. In the Cyber Protect console, go to **Devices** > **Machine with agents**.
2. Select the workloads or the device groups to which you want to apply a scripting plan, and then click **Protect** or **Protect group**, respectively.
3. [If there are already applied plans] Click **Add plan**.
4. Click **Create plan** > **Scripting plan**. A template for the scripting plan opens.
5. [Optional] To modify the scripting plan name, click the pencil icon.
6. Click **Choose script**, select the script that you want to use, and then click **Done**.

   > **Note:** You can only use your approved scripts from **Script repository** > **My scripts**. Only an administrator with the **Cyber administrator** role can use scripts in the **Testing** status.

7. Configure the schedule and the start conditions for the scripting plan.
8. Choose under which account the script will run on the target workload:
   - System account (in macOS, this is the root account)
   - Currently logged-in account
9. Specify how long the script can run on the target workload. If the script cannot finish running within the set time frame, the Cyber Scripting operation will fail. The minimum value is one minute and the maximum is 1440 minutes.
10. [Only for PowerShell scripts] Configure the PowerShell execution policy.
11. Click **Create**.

### To create a scripting plan on the Scripting plans tab

1. In the Cyber Protect console, go to **Management** > **Scripting plans**.
2. Click **Create plan**. A template for the scripting plan opens.
3. [Optional] To select workloads or device groups, click **Add workloads**.
   a. Click **Machines with agents** to expand the list, and then select the desired workloads or device groups.
   b. Click **Add**.

   > **Note:** You can also select workloads or device groups after you create the plan.

4. [Optional] To modify the scripting plan name, click the pencil icon.
5. Click **Choose script**, select the script that you want to use, and then click **Done**.

   > **Note:** You can only use your approved scripts from **Script repository** > **My scripts**. Only an administrator with the **Cyber administrator** role can use scripts in the **Testing** status.

6. Configure the schedule and the start conditions for the scripting plan.
7. Choose the account under which the script will run (System account or Currently logged-in account).
8. Specify the script execution time limit (1-1440 minutes).
9. [Only for PowerShell scripts] Configure the PowerShell execution policy.
10. Click **Create**.

## Schedule and start conditions

### Schedule

You can configure a scripting plan to run once or repeatedly, and to start on a schedule or to be triggered by a certain event. The following options are available:

- **Run once** -- Configure the date and time when the plan will run.
- **Schedule by time** -- Configure scripting plans that run hourly, daily, or monthly. To make the schedule effective only temporarily, select the **Run within a date range** check box, and then configure the period during which the scheduled plan will run.
- **When user logs in to the system** -- Choose whether a specific user or any user who logs in triggers the scripting plan.
- **When user logs off the system** -- Choose whether a specific user or any user who logs off triggers the scripting plan.
- **On the system startup**
- **When system is shut down** -- This scheduling option only works with scripts that run under the system account.
- **When system goes online**

### Start conditions

Start conditions add more flexibility to your scheduled plans. If you configure multiple conditions, all of them must be met simultaneously in order for the plan to start. Start conditions are not effective if you run the plan manually, by using the **Run now** option.

| Condition | Description |
|-----------|-------------|
| **Run only if workload is online** | This condition is met when the target workload is connected to the Internet. |
| **User is idle** | This condition is met when a screen saver is running on the machine or the machine is locked. |
| **User logged off** | Postpone a scheduled plan until the user of the target workload logs off. |
| **Fits time interval** | Define the time interval in which the plan can run. |
| **Save battery power** | Ensure that the plan would not be interrupted because of a low battery. Options: **Do not start when on battery** (plan starts only if connected to a power source); **Start when on battery if the battery level is higher than** (a specified value). |
| **Do not start on metered connection** | The plan will not run if the target workload accesses the Internet via a metered connection. |
| **Do not start when connected to the following Wi-Fi networks** | Specify the SSID of the forbidden network. The restriction applies to all networks that contain the specified name as a substring in their name, case-insensitive. |
| **Check device IP address** | The plan will not run if any of the IP addresses of the target workload are within or outside of the specified IP address range. Options: **Start if outside IP range**; **Start if within IP range**. Only IPv4 addresses are supported. |
| **If start conditions are not met, run the task anyway** | Set the time interval after which the plan will run irrespective of any other conditions. Not available if you selected the **Run once** option for the schedule. |

## Managing the target workloads for a plan

You can select the workloads or the device groups to which to apply a scripting plan while you create the plan, or later. Partner administrators can apply the same plan to workloads from different customers, and can create device groups that contain workloads from different customers.

### To add initial workloads to a plan

1. In the Cyber Protect console, go to **Management** > **Scripting plans**.
2. Click the name of the plan for which you want to specify target workloads.
3. Click **Add workloads**.
4. Select the desired workloads or device groups, and then click **Add**.
5. To save the edited plan, click **Save**.

### To manage existing workloads for a plan

1. In the Cyber Protect console, go to **Management** > **Scripting plans**.
2. Click the name of the plan whose target workloads you want to change.
3. Click **Manage workloads**.
4. The **Devices** screen lists the workloads to which the scripting plan is currently applied. To add new workloads or device groups, click **Add**, select them, and click **Add**. To remove workloads or device groups, select them, and then click **Remove**.
5. Click **Done**.
6. To save the edited plan, click **Save**.

## Importing scripting plans

You can import scripting plans that were exported in a JSON file. This can save time and ensure consistency of the settings across tenants.

**Prerequisites:** A JSON file with the plan configuration is available on the machine from which you are logged in to the console.

1. In the Cyber Protect console, go to **Management** > **Scripting plans**.
2. Click **Import**.
3. In the window that opens, browse to the JSON file.
4. Click the file, and then click **Open**.

The scripting plan appears on the screen. You can now apply it to workloads.

# Script quick run

You can run a script immediately, without including it in a scripting plan. You cannot use this operation on more than 150 workloads, on offline workloads, or on device groups.

The target workload must be assigned a service quota that supports the Script quick run functionality, and the RMM license or Security and RMM license must be enabled for its tenant.

> **Note:** You can only use your approved scripts from **Script repository** > **My scripts**. Only an administrator with the **Cyber administrator** role can use scripts in the **Testing** status.

## To run a script from the Devices tab

1. In the Cyber Protect console, go to **Devices** > **All devices**.
2. Select the workload on which you want to run the script, and then click **Protect**.
3. Click **Script quick run**.
4. Click **Choose script**, select the script that you want to use, and then click **Done**.
5. Choose under which account the script will run on the target workload: System account (root on macOS) or Currently logged-in account.
6. Specify how long the script can run on the target workload (1-1440 minutes).
7. [Only for PowerShell scripts] Configure the PowerShell execution policy.
8. Click **Run now**.

## To run a script from the Scripting repository tab

1. In the Cyber Protect console, go to **Management** > **Scripting repository**.
2. Select the script that you want to run, and then click **Script quick run**.
3. Click **Add workloads** to select the target workloads, and then click **Add**.
4. Click **Choose script**, select the script that you want to use, and then click **Done**.
5. Choose under which account the script will run on the target workload: System account (root on macOS) or Currently logged-in account.
6. Specify how long the script can run on the target workload (1-1440 minutes).
7. [Only for PowerShell scripts] Configure the PowerShell execution policy.
8. Click **Run now**.
