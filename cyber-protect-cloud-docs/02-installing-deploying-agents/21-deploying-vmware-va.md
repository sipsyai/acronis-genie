---
title: "Deploying Agent for VMware (Virtual Appliance)"
section: "Installing and deploying Cyber Protection agents"
subsection: "Deploying virtual appliances"
page_range: "131-135"
tags: ["VMware", "virtual appliance", "OVF", "vSphere", "ESXi", "vCenter", "deployment", "DRS", "HotAdd"]
acronis_version: "26.02"
---

# Deploying Agent for VMware (Virtual Appliance)

## System requirements for the agent

By default, the virtual appliance is assigned 4 GB of RAM and 2 vCPUs, which is optimal and sufficient for most operations. To improve backup performance and avoid failures related to insufficient RAM memory, we recommend increasing these resources to 16 GB of RAM and 4 vCPUs in more demanding cases -- for example, when backup traffic exceeds 100 MB per second (in 10-Gigabit networks) or if you simultaneously back up multiple virtual machines with large hard drives (500 GB or more).

The appliance's own virtual disks occupy no more than 6 GB. Thick or thin disk format does not matter, as it does not affect the appliance performance.

## How many agents do I need?

Even though one virtual appliance is able to protect an entire vSphere environment, the best practice is deploying one virtual appliance per vSphere cluster (or per host, if there are no clusters). This makes for faster backups because the appliance can attach the backed-up disks by using the HotAdd transport, and therefore the backup traffic is directed from one local disk to another.

It is normal to use both the virtual appliance and Agent for VMware (Windows) at the same time, as long as they are connected to the same vCenter Server *or* they are connected to different ESXi hosts. Avoid cases when one agent is connected to an ESXi directly and another agent is connected to the vCenter Server which manages this ESXi.

We do not recommend using locally attached storage (i.e. storing backups on virtual disks added to the virtual appliance) if you have more than one agent.

## Disable automatic DRS for the agent

If the virtual appliance is deployed to a vSphere cluster, be sure to disable automatic vMotion for it. In the cluster DRS settings, enable individual virtual machine automation levels, and then set **Automation level** for the virtual appliance to **Disabled**.

## Deploying the OVF template

1. Click **All devices** > **Add** > **Broadcom (VMware) ESXi** > **Virtual Appliance (OVF)**. The .zip archive is downloaded to your machine.
2. Unpack the .zip archive. The folder contains one .ovf file and three .vmdk files.
3. Ensure that these files can be accessed from the machine running vSphere Client.
4. Start vSphere Client and log on to the vCenter Server.
5. Deploy the OVF template.
   - When configuring storage, select the shared datastore, if it exists. Thick or thin disk format does not matter, as it does not affect the appliance performance.
   - When configuring network connections, be sure to select a network that allows an Internet connection, so that the agent can properly register itself in the cloud.

## Configuring the virtual appliance

After deploying the virtual appliance, you must configure it so that it can access vCenter Server or the ESXi host and the Cyber Protection service.

1. In the vSphere Client, open the console of the virtual appliance.
2. Ensure that the network connection is configured. The connection is configured automatically via Dynamic Host Configuration Protocol (DHCP). To change the default configuration, under **Agent options**, in the **eth0** field, click **Change**, and then specify the network settings.
3. Connect the virtual appliance to vCenter Server or the ESXi host.
   a. Under **Agent options**, in the **vCenter/ESX(i)** field, click **Change**, and then specify the following:
      - (If using vCenter Server) The vCenter Server name or IP address.
      - (If not using vCenter Server) The name or IP address of the ESXi host on which you want to back up and recover virtual machines. For faster backups, deploy the virtual appliance on the same host.
      - The credentials required for the appliance to connect to vCenter Server or the ESXi host. We recommend using a dedicated account with the appropriate privileges.
   b. Click **Check connection** to verify that the settings are correct.
   c. Click **OK**.
4. Register the appliance in the Cyber Protection service by using one of the following methods:
   - **Register via the graphical interface:**
     a. Under **Agent options**, in the **Management Server** field, click **Change**.
     b. In the **Server name/IP** field, select **Cloud**.
     c. In the **User name** and **Password** fields, specify your Cyber Protect credentials.
     d. (Only if two-factor authentication is enabled) Enter the TOTP code from your authenticator app, and then click **OK**.
     e. Click **OK**.
   - **Register via the command-line interface:**
     a. Press CTRL+SHIFT+F2 to open the command-line interface.
     b. Run: `register_agent -o register -t cloud -a <service address> --token <registration token>`

     > **Note:** When you use a registration token, you must specify the exact data center address. This is the URL that you see after you log in to the Cyber Protect console. For example, `https://eu2.company.cloud`. Do not use `https://company.cloud` here.

     c. To return to the graphical interface, press ALT+F1.
5. (Optional) Add local backup storage to the virtual appliance.
   a. In your virtual machine environment, select the virtual appliance, and open its settings for editing.
   b. Add a new hard disk to the virtual appliance. The disk size must be at least 10 GB.

   > **Warning!** If you use a disk that contains data, the data will be deleted.

   c. In your virtual machine environment, open the console of the virtual appliance.
   d. Under **Local storages**, click **Refresh**. The **Create storage** button becomes active.
   e. Click **Create storage**, select the disk that you added, select a drive letter, and optionally specify a disk label (limited to 16 characters).
   f. Click **OK**, then click **Yes**.
6. (If a proxy server is enabled) Configure the proxy server.
   a. Press CTRL+SHIFT+F2 to open the command-line interface.
   b. Open the file `/opt/acronis/etc/aakore.yaml` in a text editor.
   c. Locate the **env** section or create it and add:
      ```
      env:
          http-proxy: proxy_login:proxy_password@proxy_address:port
          https-proxy: proxy_login:proxy_password@proxy_address:port
      ```
   d. Replace credentials and proxy address with your values.
   e. Run the `reboot` command.

> **Note:** To update a virtual appliance deployed behind a proxy, edit the appliance `config.yaml` file (`/opt/acronis/etc/va-updater/config.yaml`), by adding the following line to the bottom:
> ```
> httpProxy: http://<proxy_login>:<proxy_password>@<proxy_address>:<port>
> ```
> For example: `httpProxy: http://mylogin:mypassword@192.168.2.300:8080`
