# Configuring custom web interface URLs

Configuring custom web interface URLs
Configuring custom web interface URLs

A customized URL will point to a different IP address compared to the default URL. Keep it in mind when configuring firewall policies.

To configure the web interface URL for Cyber Protect Cloud services

In Management Portal, click Settings > Branding.
In the URL for Cyber Protect Cloud services section:
Click Configure to set a custom URL for the first time.
Click Reconfigure to change the existing custom URL.

On the Domain Settings step, prepare your domain and CNAME record.

To use a custom URL, you must have an active domain name and a CNAME record that is configured to point to the data center where your account is. The configuration of the CNAME record is done by your DNS registrar and might take up to 48 hours to propagate.

To locate the domain name of your data center and request the configuration of your CNAME record, refer to article Acronis Cyber Protect Cloud: How to define a CNAME record.

On the Check Your URL step, verify that your custom URL is accessible, and that your CNAME record is configured correctly. To do that, enter the main URL name and click Check. If you use a wildcard SSL certificate, you can add up to ten alternative domain names. If you use a "Let's Encrypt" certificate, alternative domain names will be ignored.

On the SSL Certificate step, you can do one of the following:

Create a "Let's Encrypt" certificate. To do this, click Free SSL certificate with "Let's Encrypt". This option uses "Let's Encrypt" certificates issued by a third-party entity. The service provider is not liable for any issues resulting from the use of these free certificates.

When Let's Encrypt certificates expire, they are updated automatically and no further actions are needed. See Automatic updates of Let's encrypt certificates.

Upload your wildcard certificate. To do this, click Upload wildcard certificate, and then provide a wildcard certificate and a private key.

A certificate validation error might occur with the error message: "Failed to verify the certificate: x509: certificate signed by unknown authority". Usually it means that some intermediate certificates are missing. Use a certificate chain resolver to fix the structure of your certificate and upload the full certificate chain.
Click Submit to apply the changes.

Automatic updates of Let's encrypt certificates

The lifetime and update time of Let’s Encrypt certificates are managed by using the following logic.

By default, the certificate lifetime (duration) is 90 days, and the certificates are renewed at 2/3 of the duration. If the renewal interval (renewBefore) and certificate lifecycle (duration) have not been configured explicitly, the certificate will be renewed at 2/3 through the duration of 90 days, or approximately 30 days before its expiry.

To reset the custom URL to default

In Management Portal, click Settings > Branding.
In the URL for Acronis Cyber Protect Cloud services section, click Reset to default to use the default URL (https://acronis.cloud).
Back to Top



Last build date: Tuesday, March 10, 2026

Partner Administrator Help for Management Portal26.02.