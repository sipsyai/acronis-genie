# Configuring Virtual Appliance Virtuozzo

Installing and deploying Cyber Protection agents > Deploying virtual appliances > Deploying Agent for Virtuozzo Hybrid Infrastructure (Virtual Appliance) > Configuring the virtual appliance
Configuring the virtual appliance

After deploying the Agent for Virtuozzo Hybrid Infrastructure (Virtual Appliance), you must configure the virtual appliance to reach both the Virtuozzo Hybrid Infrastructure cluster and the Cyber Protection cloud service.

To configure the virtual appliance

Log in to the Virtuozzo Hybrid Infrastructure self-service panel.
Go to Compute > Virtual machines, and then select the Virtual machines tab in the horizontal menu.
Click the ellipsis icon (...) next to the virtual machine that you created, and then click Console.

Configure the network interfaces of the appliance. You might have to configure one or more interfaces, depending on the number of virtual networks that the appliance uses. Ensure that automatically assigned DHCP addresses (if any) are valid within the networks that your virtual machine uses, or assign them manually.

Specify the Virtuozzo cluster address and credentials.

DNS name or IP address of the Virtuozzo Hybrid Infrastructure cluster – this is the address of the management node of the cluster. The default port 5000 will be automatically set. If you use a different port, you must specify it manually.
In the User name and Password fields, enter the credentials for the Virtuozzo Hybrid Infrastructure user account. This can be a System administrator account or a Project administrator account. For more information about users, roles, and domains, see Configuring user accounts in Virtuozzo Hybrid Infrastructure.
In the User domain name field, specify the parent domain of the user account. For example, Default. The domain name is case-sensitive.

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

To protect the virtual machines in the Virtuozzo Hybrid Infrastructure cluster

Log in to the Cyber Protection console.
Go to Devices > Virtuozo Hybrid Infrastructure> <your cluster> > Default project > admin or find your machines in Devices > All devices.

Select machines and apply a protection plan to them.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.