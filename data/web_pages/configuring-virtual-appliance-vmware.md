# Configuring the virtual appliance

Installing and deploying Cyber Protection agents > Deploying virtual appliances > Deploying Agent for VMware (Virtual Appliance) > Configuring the virtual appliance
Configuring the virtual appliance

After deploying the virtual appliance, you must configure it so that it can access vCenter Server or the ESXi host and the Cyber Protection service.

To configure the virtual appliance

In the vSphere Client, open the console of the virtual appliance.

Ensure that the network connection is configured.

The connection is configured automatically via Dynamic Host Configuration Protocol (DHCP).

To change the default configuration, under Agent options, in the eth0 field, click Change, and then specify the network settings.

Connect the virtual appliance to vCenter Server or the ESXi host.

Under Agent options, in the vCenter/ESX(i) field, click Change, and then specify the following.
[If you use vCenter Server] The vCenter Server name or IP address.

[If you do not use vCenter Server] The name or IP address of the ESXi host on which you want to back up and recover virtual machines. For faster backups, deploy the virtual appliance on the same host.

The credentials required for the appliance to connect to vCenter Server or the ESXi host.

We recommend that you use a dedicated account for accessing vCenter Server or the ESXi host, instead of using an existing account with the Administrator role. For more information, see Required privileges for Agent for VMware.

Click Check connection to verify that the settings are correct.

Click OK.

Register the appliance in the Cyber Protection service by using one of the following methods.

Register the appliance in its graphical interface.

Under Agent options, in the Management Server field, click Change.

In the Server name/IP field, select Cloud.

The Cyber Protect service address appears. Do not change this address unless instructed otherwise.

In the User name and Password fields, specify the credentials for your Cyber Protect account. The virtual appliance and the virtual machines that the appliance manages are registered under this account.
[Only if two-factor authentication is enabled] Enter the TOTP code from your authenticator app, and then click OK.

Click OK.

Register the appliance in the command-line interface.

With this method, you need a registration token. For more information about how to generate one, see Generating a registration token.

Press CTRL+SHIFT+F2 to open the command-line interface.

Run the following command:

register_agent -o register -t cloud -a <service address> --token <registration token>

When you use a registration token, you must specify the exact data center address. This is the URL that you see after you log in to the Cyber Protect console. For example, https://eu2.company.cloud.

Do not use https://company.cloud here.

To return to the graphical interface of the appliance, press ALT+F1.

Add local backup storage to the virtual appliance.

In your virtual machine environment, select the virtual appliance, and then open its settings for editing.

Add a new hard disk to the virtual appliance.

The disk size must be at least 10 GB.

If you use a disk that contains data, the data will be deleted.

In your virtual machine environment, open the console of the virtual appliance.

Under Local storages, click Refresh.

The Create storage button becomes active.

Click Create storage, and then select the disk that you added to the virtual appliance.

Select a drive letter.

Specify a disk label.

The label length is limited to 16 characters, due to file system restrictions.

Click OK.
Click Yes.

[If a proxy server is enabled in your network] Configure the proxy server.

Press CTRL+SHIFT+F2 to open the command-line interface.
Open the file /opt/acronis/etc/aakore.yaml in a text editor.

Locate the env section or create it and add the following lines:

env:

http-proxy: proxy_login:proxy_password@proxy_address:port

https-proxy: proxy_login:proxy_password@proxy_address:port

Replace proxy_login and proxy_password with the proxy server credentials, and proxy_address:port with the address and port number of the proxy server.
Run the reboot command.

To be able to update a virtual appliance deployed behind a proxy, edit the appliance config.yaml file ( /opt/acronis/etc/va-updater/config.yaml), by adding the following line to the bottom of that file, and then entering values specific to your environment:

httpProxy: http://<proxy_login>:<proxy_password>@<proxy_address>:<port>

For example:

httpProxy: http://mylogin:mypassword@192.168.2.300:8080
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.