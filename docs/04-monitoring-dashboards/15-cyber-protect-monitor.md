---
title: "Cyber Protect Monitor"
section: "Understanding your current level of protection"
subsection: "Cyber Protect Monitor"
page_range: "356-361"
tags: [Cyber Protect Monitor, agent, Windows, Mac, proxy, chat, encryption, File Sync and Share]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#monitor.html"
---

# Cyber Protect Monitor

You can install Cyber Protect Monitor as an additional component that you select during the installation of Agent for Windows or Agent for Mac. Cyber Protect Monitor shows information about the protection status of the machine on which Agent for Windows or Agent for Mac is installed.

You can use Cyber Protect Monitor to configure the backup encryption and proxy server settings, and to chat with technicians.

## Supported operating systems

- With Agent for Windows:
  - Windows 10 version 1809 and later
  - Windows Server 2019 and later
- With Agent for Windows (Legacy):
  - Windows 7 and later
  - Windows Server 2008 R2 and later
- With Agent for Mac:
  - All macOS versions that are supported by Agent for Mac, except macOS 10.x and macOS 11.x.

When Agent for File Sync & Share is installed on the machine, Cyber Protect Monitor provides access to the File Sync & Share service. The File Sync & Share functionality is accessible after a mandatory onboarding during which the users sign in to their own File Sync & Share account and select a personal sync folder.

> **Important:** Cyber Protect Monitor is accessible to users who might not have administrative rights for the Cyber Protection or the File Sync & Share service.

## User permissions by agent type

| Installed agents | Users can | Users cannot |
|---|---|---|
| Agent for Windows or Agent for Mac | Apply the default protection plan to their machines; Check the protection status of their machines; Receive Active Protection notifications; Temporarily pause the backups of their machines; Configure the proxy server settings; Change the backup encryption settings; Chat with a technician | Apply custom protection plans; Manage protection plans that are already applied |
| Agent for Windows (Legacy) | Apply the default protection plan to their machines; Check the protection status of their machines; Receive Active Protection notifications; Temporarily pause the backups of their machines; Configure the proxy server settings; Change the backup encryption settings; Chat with a technician | Apply custom protection plans; Manage protection plans that are already applied |
| Agent for Windows and Agent for Sync and Share / Agent for Mac and Agent for Sync and Share | Sync content between their local sync folder and their File Sync & Share account; Pause the sync operations; Change the sync folder; Check the file types that cannot be synced; Chat with a technician | Edit the file types that cannot be synced |

> **Warning!** Changing the encryption settings in Cyber Protect Monitor overwrites the settings in the protection plan and affects all backups of the machine. This operation can cause some protection plans to fail. There is no way to recover encrypted backups if you lose or forget the password.

## Configuring proxy server settings in Cyber Protect Monitor

You can configure the proxy server settings in Cyber Protect Monitor. The configuration will affect all agents that are installed on the machine.

1. Open Cyber Protect Monitor, and then click the gear icon in the top right corner.
2. Click **Settings**, and then click **Proxy**.
3. Enable the **Use a proxy server** switch, and then enter the proxy server address and port.
4. [If the proxy server access is password-protected] Enable the **Password required** switch, and then enter the user name and password to access the proxy server. The password can include lowercase and uppercase alphanumeric characters, and the following special characters: `! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` } | { ~`
5. Click **Save**.

The proxy server settings are saved in the `http-proxy.yaml` file.

## Chats in Monitor

From your device, you can chat with technicians or administrators in the Cyber Protect console. In this way, you can have real-time assistance with issues.

### Starting a chat in Cyber Protect Monitor

You can use Cyber Protect Monitor to chat with technicians from the tenant in which your workload is registered in the Cyber Protect console. You can start a new chat session, or you can reply in chat sessions that were started in the console. Monitor shows desktop notifications when you have new messages in the chat.

> **Note:** Chat sessions are automatically closed if a user is inactive for 15 minutes.

**To start a new chat session from Monitor:**

1. Open Cyber Protect Monitor.
2. Click the chat icon. A chat window opens.
3. In the text field, type your message.
4. To send the message, click the arrow icon or press Enter. Your message is sent to the Cyber Protect console. The chat session will be assigned to a technician or administrator who will assist you.

### Additional actions with chats

If you have an active chat session in Cyber Protect Monitor, you can perform the following actions: edit message, delete message, search for a keyword or message, or end the chat.

**Edit message:**
1. In Monitor, in the chat window, locate the message that you want to edit.
2. Hover over the message, and click the pencil icon that appears.
3. Edit the message, and then click **Save**. The message is tagged as **Edited**.

**Delete message:**
1. In Monitor, in the chat window, locate the message that you want to delete.
2. Hover over the message, and click the trash bin icon that appears.
3. In the confirmation window, click **Delete**.

**Search in chat:**
1. In Monitor, in the chat window, click the loop icon.
2. [Optional] To see the chat history for a specific date, click the calendar icon, and then select the date.
   > **Note:** Only dates for which chat history is available are enabled for selection.
3. [Optional] In the search field, type the keyword or message which you want to find. The system displays the number of results that match the search. You can use the arrows to go to the next or previous result.

**End chat:**
1. In Monitor, open the chat window.
2. Click **End chat**.
3. In the confirmation window, click **End**. The chat session is closed.

### Enabling or disabling chat notifications

You can enable chat notifications and see a desktop notification when you receive new chat messages. Clicking the notification will open the chat window directly.

**To enable chat notifications:**
1. Open Cyber Protect Monitor.
2. Click **Settings**.
3. Click **Chat notifications**.
4. Select **Desktop notifications**, and then click **Save**.

**To disable chat notifications:**
1. Open Cyber Protect Monitor.
2. Click **Settings**.
3. Click **Chat notifications**.
4. Clear **Desktop notifications**, and then click **Save**.
