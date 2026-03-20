---
title: "Response Actions for Files, Registry, and Blocklist/Allowlist"
section: "Endpoint Detection and Response (EDR)"
subsection: "Response Actions - Files and Prevention"
page_range: "1202-1205"
tags: [edr, response-actions, delete, quarantine, registry, blocklist, allowlist, prevention]
acronis_version: "26.02"
---

# Response Actions for Suspicious Files

As part of your remediation response to an attack, you can apply the following actions to suspicious files:

## Delete a Suspicious File

1. In the cyber kill chain, click the file node you want to remediate.
2. In the displayed sidebar, click the **Response Actions** tab.
3. In the **Remediate** section, click **Delete**.
4. (Optional) Add a comment.
5. Click **Delete**. The file is deleted.

## Quarantine a Suspicious File

1. In the cyber kill chain, click the file node you want to remediate.
2. In the displayed sidebar, go to **Response Actions**.
3. In the **Remediate** section, click **Quarantine**.
4. (Optional) Add a comment.
5. Click **Quarantine**. The file is quarantined.

# Response Actions for Suspicious Registry Entries

As part of your remediation response to an attack, you can delete suspicious registry entries. This option is available for registry cyber kill chain nodes.

## Delete a Suspicious Registry Entry

1. In the cyber kill chain, click the node you want to remediate.
2. In the displayed sidebar, click the **Response Actions** tab.
3. In the **Remediate** section, click **Delete**.
4. (Optional) Add a comment.
5. Click **Delete**. The registry entry is deleted.

# Add or Remove a Process, File or Network in the Protection Plan Blocklist or Allowlist

As part of your prevention response to an attack, you can add a node to your protection plan allowlist or blocklist.

- Add a node to an **allowlist** if you consider the node safe and want to prevent any future detections for it.
- Add a node to a **blocklist** to stop the node from running in the future.
- You can also **remove** a node from the allowlist or blocklist to allow or prevent any future access to the node.

This option is available for the following cyber kill chain nodes: Process, File, and Network.

## Add to Blocklist

1. In the cyber kill chain, click the process, file, or network node you want to remediate.
2. In the displayed sidebar, click the **Response Actions** tab.
3. In the **Prevent** section, click the arrow icon next to **Blocklist**.
4. Select the relevant protection plan(s) you want to apply this action to.
5. (Optional) Add a comment.
6. Click **Add**. The action is implemented, and the process, file, or network will be prevented from launching in the future.

To remove from the blocklist later, follow the same steps but click **Remove** instead of **Add**. This will allow future access to the node.

## Add to Allowlist

1. In the cyber kill chain, click the process, file, or network node you want to remediate.
2. In the displayed sidebar, click the **Response Actions** tab.
3. In the **Prevent** section, click the arrow icon next to **Allowlist**.
4. Select the relevant protection plan(s) you want to apply this action to.
5. (Optional) Add a comment.
6. Click **Add**. The action is implemented and the process, file, or network will be prevented from detection in the future.

To remove from the allowlist later, follow the same steps but click **Remove** instead of **Add**. This will prevent any future access to the node.
