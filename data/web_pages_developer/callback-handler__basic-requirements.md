---
title: "Basic requirements"
source: "https://developer.acronis.com/doc/callback-handler/basic-requirements.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:50:57.978033"
---

# Basic requirements

Basic requirements

Your callback handler must be implemented in a web service that will accept HTTP requests from the Acronis API Callback Gateway.
The web service where the callback handler endpoint is implemented must support HTTPS protocol with TLS v1.3.
You callback handler must be publicly accessible.

You must configure your firewall to enable connections from the appropriate Acronis data center IP addresses.
Acronis data center IPs are listed on this Acronis Support Portal page.



Important
These IP addresses are subject to occasional change. Notification of any changes are sent by email to your vendor account.
It is your responsibility to update your firewall configuration if these changes affect your CyberApp deployments.



The domain name of your callback handler must have a valid SSL certificate, issued by a trusted authority (such as GoDaddy, Comodo, Let’s Encrypt, GlobalSign, etc.).
Your callback handler must accept incoming requests, and respond with JSON data formatted according to the callback response configuration defined in the CyberApp.