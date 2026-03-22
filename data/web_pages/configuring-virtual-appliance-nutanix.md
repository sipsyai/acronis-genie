# Configuring the Nutanix virtual appliance

Installing and deploying Cyber Protection agents > Deploying virtual appliances > Deploying Agent for Nutanix AHV > Configuring the Nutanix virtual appliance
Configuring the Nutanix virtual appliance

After deploying the virtual appliance, you must configure its access to the Nutanix cluster and the Cyber Protect console.

Prerequisites

You have deployed and powered on the Nutanix virtual appliance. See Deploying the QCOW2 template.

To configure the Nutanix virtual appliance

Log in to the Nutanix Prism Element console as an administrator.
Go to VM > Table.

Right-click the virtual machine that you deployed, and then select Launch Console.

In the eth0 field, configure the network interfaces of the appliance.

If there are automatically assigned DHCP addresses, ensure that they are either valid within the networks that your virtual machine uses or assign them manually. Depending on the number of networks that the appliance uses, there might be one or more interfaces to configure.

Specify the IP address of the Nutanix cluster (Nutanix Prism Element) and credentials for accessing it.

You cannot configure Agent for Nutanix AHV with the IP address of Nutanix Prism Central. Even if you manage the cluster through Nutanix Prism Central, Agent for Nutanix AHV can only access it through Nutanix Prism Element.
Under Agent options, in the Nutanix field, click Change.
In the Server name/IP field, enter the IP address of the cluster.

In the User name and Password fields, enter the credentials for a Nutanix administrator account.

This account must have the User Admin and Cluster Admin roles in the Nutanix cluster.

To verify that the settings are correct, click Check connection.

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

Edit the default name for the virtual appliance, which is localhost.

This name is shown in the Cyber Protect console.

Under Virtual machine, in the Name field, click Change.

Edit the name, and then click OK.

Configure the time zone of the virtual appliance.

Under Virtual machine, in the Time zone field, click Change.
To ensure that the scheduled operations run at the correct time, select the time zone of your location.

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