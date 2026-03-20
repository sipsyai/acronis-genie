---
title: "Actions with protection plans"
section: "Working with plans"
subsection: "Protection plans and modules"
page_range: "233-238"
tags: ["protection-plans", "apply", "edit", "export", "import", "revoke", "enable", "disable", "delete", "clone"]
acronis_version: "26.02"
---

# Actions with protection plans

After creating a protection plan, you can perform the following actions with it:

- **Apply** a plan to a workload or a device group.
- **Rename** a plan.
- **Edit** a plan — enable and disable the modules, and change their settings.
- **Enable or disable** a plan — A disabled plan will not run on the workloads to which it is applied. The plan is not revoked from the workload and you can quickly restore the protection by re-enabling the plan.
- **Revoke** a plan from a workload — A revoked plan is not applied to the workload anymore. To restore protection, you must know the plan's name to find it and re-apply it.
- **Stop** a plan — Stops all running backup operations on all workloads to which the plan is applied. Backups will start again according to the plan schedule. Antimalware scanning is not affected.
- **Clone** a plan — Create an exact copy of an existing plan. The new plan is not assigned to any workloads.
- **Export and import** a plan — Export a plan as a JSON file, which you can import back later.
  > **Note:** This feature is not available for plans at the partner level.
- **Check the details** of a plan.
- **Check the activities and alerts** related to a plan.
- **Delete** a plan.

## Applying a protection plan to a workload

### From the Devices tab

1. Select one or more workloads that you want to protect.
2. Click **Protect**.
3. [If another protection plan was already applied] Click **Add plan**. A list of available protection plans is shown.
4. Select the protection plan that you want to apply, and then click **Apply**.

### From Management > Protection plans

1. In the Cyber Protect console, go to **Management** > **Protection plans**.
2. Select the protection plan that you want to apply.
3. Click **Edit**.
4. Click **Manage devices**.
5. In the **Devices** window, click **Add**.
6. Select the workloads to which you want to apply the plan, and then click **Add**.
7. In the **Devices** window, click **Done**.
8. In the protection plan panel, click **Save**.

## Editing a protection plan

When you edit a plan, you can enable and disable the modules in it, and change their settings. You can edit a protection plan for all workloads to which it is applied or only for selected workloads.

### From the Devices tab

1. Select one or more workloads to which the plan is applied.
2. Click **Protect**.
3. Select the protection plan that you want to edit.
4. Click the ellipsis icon (...) next to the plan name, and then click **Edit**.
5. Click a module that you want to edit, and then configure its settings as needed.
6. Click **Save**.
7. [If you have not selected all workloads to which the plan is applied] Select the scope of the edit:
   - To edit the plan for all workloads, click **Apply the changes to this protection plan (this will affect other devices)**.
   - To change the plan only for selected workloads, click **Create a new protection plan only for the selected devices**. The existing plan will be revoked from the selected workloads and a new plan with the configured settings will be created.

### From Management > Protection plans

1. Go to **Management** > **Protection plans**.
2. Select the protection plan that you want to edit.
3. Click **Edit**.
4. Click the modules that you want to edit, and then configure their settings as needed.
5. Click **Save**.

> **Note:** Editing a plan from the **Management** > **Protection plans** tab affects all workloads to which that plan is applied.

## Exporting a protection plan

You can export a protection plan in a JSON file.

1. In the Cyber Protect console, go to **Management** > **Protection plans**.
2. Click the plan that you want to export, and in the **Actions** menu, click **Export**. A JSON file is created and saved to the default download folder.

## Importing a protection plan

You can import protection plans that were exported in a JSON file.

1. In the Cyber Protect console, go to **Management** > **Protection plans**.
2. In the **Actions** menu, click **Import**.
3. In the window that opens, browse to the JSON file.
4. Click the file, and then click **Open**. The protection plan appears on the screen.

## Revoking a protection plan

When you revoke a plan, you remove it from one or more workloads. The plan still protects the other workloads to which it is applied.

### From the Devices tab

1. Select the workloads from which you want to revoke the plan.
2. Click **Protect**.
3. Select the protection plan that you want to revoke.
4. Click the ellipsis icon (...) next to the plan name, and then click **Revoke**.

## Enabling or disabling a protection plan

An enabled plan is active and runs on the workloads to which it is applied. A disabled plan is inactive — it is still applied to workloads but it does not run on them.

### From the Devices tab

1. Select the workload whose plan you want to disable.
2. Click **Protect**.
3. Select the protection plan.
4. Click the ellipsis icon (...) and then click **Enable** or **Disable**, respectively.

## Deleting a protection plan

When you delete a plan, it is revoked from all workloads and removed from the Cyber Protect console.

### From the Devices tab

1. Select any workload to which the protection plan that you want to delete is applied.
2. Click **Protect**.
3. Select the protection plan that you want to delete.
4. Click the ellipsis icon (...) and then click **Delete**.

### From Management > Protection plans

1. Go to **Management** > **Protection plans**.
2. Select the protection plan that you want to delete.
3. Click **Delete**.
4. Confirm your choice by selecting the **I confirm the deletion of plan** check box, and then click **Delete**.
