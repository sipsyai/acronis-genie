---
title: "Configuring proxy server settings"
section: "Installing and deploying Cyber Protection agents"
subsection: "Before you start"
page_range: "50-53"
tags: ["proxy", "network", "configuration", "Windows", "macOS", "Linux", "registry", "aakore"]
acronis_version: "26.02"
---

# Configuring proxy server settings

The protection agents can transfer data through an HTTP/HTTPS proxy server. The server must work through an HTTP tunnel without scanning or interfering with the HTTP traffic. Man-in-the-middle proxies are not supported.

Because the agent registers itself in the cloud during the installation, you must configure the proxy server settings during the installation of the agent or in advance.

## For Windows

If a proxy server is configured in **Control panel** > **Internet Options** > **Connections**, the setup program reads the proxy server settings from the registry and uses them automatically.

> **Note:** This procedure is valid only when the `http-proxy.yaml` file does not exist on the machine. If the `http-proxy.yaml` file exists on the machine, you must update the proxy settings in the file, as it overrides the settings in the `aakore.yaml` file.

### To configure the proxy settings

1. Create a new text document and open it in a text editor, such as Notepad.
2. Copy and paste the following lines into the file.

   ```
   Windows Registry Editor Version 5.00

   [HKEY_LOCAL_MACHINE\SOFTWARE\Acronis\Global\HttpProxy]
   "Enabled"=dword:00000001
   "Host"="proxy.company.com"
   "Port"=dword:000001bb
   "Login"="proxy_login"
   "Password"="proxy_password"
   ```

3. Replace `proxy.company.com` with your proxy server host name/IP address, and `000001bb` with the hexadecimal value of the port number. For example, `000001bb` is port 443.
4. If your proxy server requires authentication, replace `proxy_login` and `proxy_password` with the proxy server credentials. Otherwise, delete these lines from the file.
5. Save the document as `proxy.reg`.
6. Run the file as an administrator.
7. Confirm that you want to edit the Windows registry.
8. If the agent is not installed on this workload yet, install it now. If already installed, continue to the next step.
9. Open the `%programdata%\Acronis\Agent\etc\aakore.yaml` file in a text editor. You must be a member of the Administrators group in Windows.
10. Locate the **env** section or create it, and then add the following lines:

    ```yaml
    env:
        http-proxy: proxy_login:proxy_password@proxy_address:port
        https-proxy: proxy_login:proxy_password@proxy_address:port
    ```

11. Replace credentials and address/port with the actual proxy server values.
12. In the **Start** menu, click **Run**, type: **cmd**, and then click **OK**.
13. Restart the aakore service: `net stop aakore` then `net start aakore`
14. Restart the agent: `net stop mms` then `net start mms`

## For macOS

### To configure the proxy settings

1. Create the `/Library/Application Support/Acronis/Registry/Global.config` file and open it in a text editor.
2. Copy and paste the following lines into the file:

   ```xml
   <?xml version="1.0" ?>
   <registry name="Global">
       <key name="HttpProxy">
           <value name="Enabled" type="Tdword">"1"</value>
           <value name="Host" type="TString">"proxy.company.com"</value>
           <value name="Port" type="Tdword">"443"</value>
           <value name="Login" type="TString">"proxy_login"</value>
           <value name="Password" type="TString">"proxy_password"</value>
       </key>
   </registry>
   ```

3. Replace `proxy.company.com` with your proxy host name/IP address, and `443` with the decimal value of the port number.
4. If your proxy server requires authentication, replace `proxy_login` and `proxy_password` with the proxy server credentials. Otherwise, delete these lines from the file.
5. Save the file.
6. If the agent is not installed yet, install it now. If already installed, continue.
7. Open the `/Library/Application Support/Acronis/Agent/etc/aakore.yaml` file in a text editor.
8. Add the env section with proxy lines (same format as Windows above).
9. Replace credentials and address/port with actual values.
10. Go to **Applications** > **Utilities** > **Terminal**.
11. Restart the aakore service: `sudo launchctl stop aakore` then `sudo launchctl start aakore`
12. Restart the agent: `sudo launchctl stop acronis_mms` then `sudo launchctl start acronis_mms`

## For Linux

Run the installation file with the `--http-proxy-host=ADDRESS --http-proxy-port=PORT --http-proxy-login=LOGIN --http-proxy-password=PASSWORD` parameters. Use the following procedure to update the proxy settings after the installation of the protection agent.

### To configure the proxy settings

1. Open the `/etc/Acronis/Global.config` file in a text editor.
2. If proxy settings were specified during installation, locate and update the `HttpProxy` section. If not, add the `HttpProxy` key between the `<registry name="Global">...</registry>` tags.
3. Replace ADDRESS, PORT, LOGIN, and PASSWORD with the actual values.
4. If your proxy server requires authentication, replace LOGIN and PASSWORD. Otherwise, delete these lines.
5. Save the file.
6. Open file `/opt/acronis/etc/aakore.yaml` in a text editor.
7. Add the env section with proxy lines (same format as Windows above).
8. Replace credentials and address/port with actual values.
9. Restart the aakore service: `sudo service aakore restart`
10. Restart the agent: `sudo service acronis_mms restart`

## For bootable media

When working under bootable media, you might need to access the cloud storage via a proxy server. To configure the proxy server settings, click **Tools** > **Proxy server**, and then configure the proxy server host name/IP address, port, and credentials.
