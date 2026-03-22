# Configuring proxy server settings

Installing and deploying Cyber Protection agents > Before you start > Configuring proxy server settings
Configuring proxy server settings

The protection agents can transfer data through an HTTP/HTTPS proxy server. The server must work through an HTTP tunnel without scanning or interfering with the HTTP traffic. Man-in-the-middle proxies are not supported.

Because the agent registers itself in the cloud during the installation, you must configure the proxy server settings during the installation of the agent or in advance.

For Windows
For macOS
For Linux
For bootable media

If a proxy server is configured in Control panel > Internet Options > Connections, the setup program reads the proxy server settings from the registry and uses them automatically.

Use this procedure if you want to perform the following tasks.

Configure the proxy settings before the installation of the agent.
Update the proxy settings after the installation of the agent.

To configure the proxy settings during the installation of the agent, see Installing protection agents in Windows.

This procedure is valid only when the http-proxy.yaml file does not exist on the machine. If the http-proxy.yaml file exists on the machine, you must update the proxy settings in the file, as it overrides the settings in the aakore.yaml file.

The %programdata%\Acronis\Agent\var\aakore\http-proxy.yaml file is created when you configure the proxy server settings by using Cyber Protection Monitor. For more information, see Configuring proxy server settings in Cyber Protect Monitor.

To open the http-proxy.yaml file, you must be member of the Administrators group in Windows.

To configure the proxy settings

Create a new text document and open it in a text editor, such as Notepad.

Copy and paste the following lines into the file.

Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Acronis\Global\HttpProxy]
"Enabled"=dword:00000001
"Host"="proxy.company.com"
"Port"=dword:000001bb
"Login"="proxy_login"
"Password"="proxy_password"
Replace proxy.company.com with your proxy server host name/IP address, and 000001bb with the hexadecimal value of the port number. For example, 000001bb is port 443.
If your proxy server requires authentication, replace proxy_login and proxy_password with the proxy server credentials. Otherwise, delete these lines from the file.
Save the document as proxy.reg.
Run the file as an administrator.
Confirm that you want to edit the Windows registry.
If the agent is not installed on this workload yet, install it now. If the agent is already installed on the workload, continue to the next step.

Open the %programdata%\Acronis\Agent\etc\aakore.yaml file in a text editor.

To open this file, you must be member of the Administrators group in Windows.

Locate the env section or create it, and then add the following lines.

env:
http-proxy: proxy_login:proxy_password@proxy_address:port
https-proxy: proxy_login:proxy_password@proxy_address:port
Replace proxy_login and proxy_password with the proxy server credentials, and proxy_address:port with the address and port number of the proxy server.
In the Start menu, click Run, type: cmd, and then click OK.

Restart the aakore service by running the following commands.

net stop aakore
net start aakore

Restart the agent by running the following commands.

net stop mms
net start mms



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.