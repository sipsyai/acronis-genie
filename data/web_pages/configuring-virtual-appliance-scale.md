# Configuring Virtual Appliance Scale

Installing and deploying Cyber Protection agents > Deploying virtual appliances > Deploying Agent for Scale Computing HC3 (Virtual Appliance) > Configuring the virtual appliance
Configuring the virtual appliance

After deploying the virtual appliance, you need to configure it so that it can reach both the Scale Computing HC3 cluster that it will protect and the Cyber Protection service.

To configure the virtual appliance

Log in to your Scale Computing HC3 account.
Select the virtual appliance that you want to configure, and then click the Console icon.

In the eth0 field, configure the network interfaces of the appliance.

Ensure that automatically assigned DHCP addresses (if any) are valid within the networks that your virtual machine uses or assign them manually. Depending on the number of networks that the appliance uses, there may be one or more interfaces to configure.

In the Scale Computing field, click Change to specify the Scale Computing HC3 cluster address and credentials for accessing it.

In the Server name/IP field, enter the DNS name or IP address of the cluster.

In the User name and Password fields, enter the credentials for the Scale Computing HC3 administrator account.

Ensure that this account has the roles required for operations with Scale Computing HC3 virtual machines. For more information about these roles, refer to Agent for Scale Computing HC3 – required roles.

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

In the Name field, click Change to edit the default name for the virtual appliance, which is localhost. This name is shown in the Cyber Protect console.

[Optional] In the Time field, click Change, and then select the time zone of your location to ensure that the scheduled operations run at the appropriate time.

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

To protect virtual machines in the Scale Computing HC3 cluster

Log in to your Cyber Protection account.
Navigate to Devices > Scale Computing HyperCore> <your cluster> or find your machines in Devices > All devices.
Select machines and apply a protection plan to them.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.