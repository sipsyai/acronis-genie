---
title: "Deploying Agent for Virtuozzo Hybrid Infrastructure (Virtual Appliance)"
section: "Installing and deploying Cyber Protection agents"
subsection: "Deploying virtual appliances"
page_range: "140-150"
tags: ["Virtuozzo", "Hybrid Infrastructure", "virtual appliance", "QCOW2", "OpenStack", "deployment", "user accounts"]
acronis_version: "26.02"
---

# Deploying Agent for Virtuozzo Hybrid Infrastructure (Virtual Appliance)

## Before you start

This appliance is a pre-configured virtual machine that you deploy in Virtuozzo Hybrid Infrastructure. It contains a protection agent that enables you to administer cyber protection for all virtual machines in a Virtuozzo Hybrid Infrastructure cluster.

> **Note:** To ensure that backups with enabled **Volume Shadow Copy Service (VSS) for virtual machines** backup option run properly and capture data in application-consistent state, verify that Virtuozzo Guest Tools are installed and up-to-date on the protected virtual machines.

## System requirements for the agent

When deploying the virtual appliance, you can choose between different predefined combinations of vCPUs and RAM (flavors). You can also create your own flavors.

2 vCPUs and 4 GB of RAM (medium flavor) are optimal and sufficient for most operations. To improve backup performance and avoid failures related to insufficient RAM memory, we recommend increasing to 4 vCPUs and 8 GB of RAM in more demanding cases.

## How many agents do I need?

One agent can protect the entire cluster. You can deploy more than one agent in the cluster if you need to distribute the backup traffic bandwidth load.

Virtual machines are automatically evenly distributed between agents, and automatic redistribution occurs when the load imbalance reaches 20 percent. Redistribution will not happen if an agent gets corrupted or is deleted manually from the Virtuozzo Hybrid Infrastructure node. Redistribution will start only after you remove such an agent from the Cyber Protection web interface.

### Limitations

- Virtuozzo Hybrid Infrastructure appliance cannot be deployed remotely.
- Application-aware backup of virtual machines is not supported.

## Configuring networks in Virtuozzo Hybrid Infrastructure

Before deploying and configuring the virtual appliance, you need to have your networks in Virtuozzo Hybrid Infrastructure configured.

### Network requirements

- The virtual appliance requires 2 network adapters.
- The virtual appliance must be connected to Virtuozzo networks with the following network traffic types:
  - Compute API
  - VM Backup
  - ABGW Public
  - VM Public

## Configuring user accounts in Virtuozzo Hybrid Infrastructure

To configure the virtual appliance, you need a Virtuozzo Hybrid Infrastructure user account. You can use one of the following accounts:

- **System administrator** (in the **Default** domain or in another domain) -- Grants access to all projects in the selected domain. The virtual appliance will be able to back up and recover all virtual machines in all child projects of the selected domain.
- **Project administrator** -- The virtual appliance will be able to back up and recover only the virtual machines in the project in which the account is created. No information about other projects in the domain will be available. You can use the project administrator account only with Virtuozzo Hybrid Infrastructure 6.2 and later.

> **Note:** If you want to protect multiple projects, you must deploy a separate virtual appliance for each project. Each virtual appliance must use a separate project administrator account that is created in the corresponding project.

### Using a system administrator account

1. Connect to the Virtuozzo Hybrid Infrastructure cluster by using the OpenStack Command-Line Interface, and then run the following script to create an environment file:
   ```
   su - vstoradmin
   kolla-ansible post-deploy
   exit
   ```
2. Use the environment file to authorize further OpenStack commands:
   ```
   . /etc/kolla/admin-openrc.sh
   ```
3. Create an administrator account in the **Default** domain:
   ```
   openstack --insecure user set --project admin --project-domain Default --domain Default <user name>
   ```
4. Assign the `admin` role to the account:
   ```
   openstack --insecure role add --domain Default --user <user name> --user-domain Default admin --inherited
   ```
5. (Optional) Allow the account to access additional domains:
   ```
   openstack --insecure role add --domain <domain name> --inherited --user <user name> --user-domain Default admin
   ```
6. Check the roles assigned to the account:
   ```
   openstack --insecure role assignment list --user <user name> --names
   ```

### Using a project administrator account

1. In the admin panel of Virtuozzo Hybrid Infrastructure, go to **Settings** > **Projects and users**.
2. Choose a domain and create a project in it.
3. In the same domain, create a user account. Assign the **Project member** role, select the **Image uploading** check box, and assign the user to the project.
4. Connect to the Virtuozzo Hybrid Infrastructure cluster by using the OpenStack Command-Line Interface.
   a. Run the environment file script.
   b. Source the environment file: `. /etc/kolla/admin-openrc.sh`
   c. Assign the `compute` role:
      ```
      openstack --insecure role add --project <project name> --user <user name> --project-domain <project domain name> --user-domain <user domain name> compute
      ```
   d. Assign the `quota_manager` role:
      ```
      openstack --insecure role add --project <project name> --user <user name> --project-domain <project domain name> --user-domain <user domain name> quota_manager
      ```

## Deploying the QCOW2 template

1. Log in to your Cyber Protection account.
2. Click **Devices** > **Add** > **Virtuozzo Hybrid Infrastructure**. The .zip archive is downloaded.
3. Unpack the .zip archive. It contains a .qcow2 image file.
4. Log in to your Virtuozzo Hybrid Infrastructure account.
5. Add the .qcow2 image file to the compute cluster:
   - On the **Compute** > **Virtual machines** > **Images** tab, click **Add image**.
   - In the **Add image** window, click **Browse**, and select the .qcow2 file.
   - Specify the image name, select the **Generic Linux OS** type, and click **Add**.
6. In **Compute** > **Virtual machines** > **Virtual machines**, click **Create virtual machine**:
   - In **Deploy from**, choose **Image**.
   - In the **Images** window, select the .qcow2 image file and click **Done**.
   - In the **Volumes** window, no additional volumes are needed.
   - In the **Flavor** window, choose your desired combination of vCPUs and RAM (usually 2 vCPUs and 4 GiB of RAM) and click **Done**.
   - In the **Network interfaces** window, click **Add**, select the virtual network of type *public*, and then click **Add**. Repeat for additional networks if necessary.
7. Click **Done**.
8. Back in the **Create virtual machine** window, click **Deploy** to create and boot the virtual machine.

## Configuring the virtual appliance

1. Log in to the Virtuozzo Hybrid Infrastructure self-service panel.
2. Go to **Compute** > **Virtual machines**, select the **Virtual machines** tab.
3. Click the ellipsis icon next to the virtual machine you created, and then click **Console**.
4. Configure the network interfaces of the appliance. Ensure DHCP addresses are valid or assign them manually.
5. Specify the Virtuozzo cluster address and credentials:
   - DNS name or IP address of the Virtuozzo Hybrid Infrastructure cluster (the management node address, default port 5000 is set automatically).
   - In **User name** and **Password**, enter the credentials for the Virtuozzo Hybrid Infrastructure user account.
   - In the **User domain name** field, specify the parent domain of the user account (e.g., **Default**). The domain name is case-sensitive.
6. Register the appliance in the Cyber Protection service (via GUI or command-line interface).
7. (If a proxy server is enabled) Configure the proxy server via `/opt/acronis/etc/aakore.yaml`.

### To protect the virtual machines in the Virtuozzo Hybrid Infrastructure cluster

1. Log in to the Cyber Protection console.
2. Go to **Devices** > **Virtuozo Hybrid Infrastructure** > <your cluster> > **Default project** > **admin** or find your machines in **Devices** > **All devices**.
3. Select machines and apply a protection plan to them.
