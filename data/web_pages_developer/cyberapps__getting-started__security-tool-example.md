---
title: "Security Tool CyberApp Example"
source: "https://developer.acronis.com/doc/cyberapps/getting-started/security-tool-example.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:57:34.270244"
---

# Security Tool CyberApp Example

Security Tool CyberApp Example

Overview
This page describes how to set up and run an end-to-end example of an inbound integration based on CyberApp technology.
The provided Security Tool CyberApp example:

Implements “mapping” enablement scenarios for partners and customers.
Supports custom integration settings: allows configuring a default action.
Declares custom alert types.
Allows posting a new alert of a custom type.
Declares a custom workload type.
Allows posting a new workload of that custom workload type.
Adds a menu item under the PROTECTION menu of the Acronis Protection console.
Adds two custom widgets to the MONITORING menu of the Acronis Protection console.


Note
In production, a callback handler must be accessible by the Acronis platform via a public URL. For demonstration purposes,
this guide recommends using the ngrok service, which provides secure traffic tunneling.
With ngrok, it is possible to use the CyberApp example in virtually any Windows environment connected to the Internet.
For production operation, you must expose a publicly accessible callback handler URL in your corporate environment.
See Basic requirements for more details.



Prerequisites
To run this example, you will need:

Python 3.8+.
An Acronis account with access to the vendor portal. If you do not have one,
see Getting started to learn how to register as a vendor.
A test partner tenant and a test customer tenant under the test partner in the Acronis Management console.



Step 1. Install and configure ngrok

Note
Skip this step if you already have a public URL routed to your environment.


Log in or sign up to ngrok.
Follow installation and configuration instructions provided in your dashboard here.
Save the ngrok dev domain, which is automatically generated for your account here.
Start ngrok using the following command to expose your local server to the Internet:
ngrok http --url=<your ngrok dev domain> 8080





Note
Keep the ngrok process running while you work with the CyberApp example.



Step 2. Configure CyberApp in the Vendor Portal

Create a new CyberApp
See Creating a CyberApp to learn how to create a new CyberApp.
As a result, you obtain the CyberApp code, client ID, and client secret required in the next steps.


Import the CyberApp description and version

Download the Security Tool Description package here.
From the CYBERAPP DESCRIPTIONS tab, click Import and follow the instructions to import the package.
Download the Security Tool Version package here.
From the CYBERAPP VERSION tab, click Import and follow the instructions to import the package.



Configure the CyberApp
Security Tool comes pre-configured with all extension points. You only need to set the callback URL.
To do this:

Open the imported CyberApp version.
Select General settings from the menu.
In the Callback handler base URL field, enter the public URL you got from ngrok, appending /mapping/callback.
For example, if ngrok provided https://1234abcd.ngrok-free.app, enter https://1234abcd.ngrok-free.app/mapping/callback.
Click Save.



Deploy the CyberApp
See Deploying to test to learn how to deploy the CyberApp to test environment.
After deployment, you can see it in the integrations catalog as Security Tool.



Step 3. Configure callback handler and connector

Download the package

Download the Callback handler and Connector archive here and
extract it into any folder.
Open a command prompt in the extracted folder.
Install the requirements with the following command:
pip install -r requirements.txt






Configure the callback handler

In constants.py, change the APPCODE variable to the code of your CyberApp. You can find it in the Vendor
Portal on the SETTINGS tab when you open your CyberApp.
Run the following script to create a database containing sample organizations and users
required for enablement and customer mapping:
python ./create_db.py


You will be prompted to enter the username and password of a test partner in the vendor backend.
These credentials will be used to enable the CyberApp from the integrations catalog in the
next steps.




Configure the connector
In constants.py, set the following parameters:

CLIENT_ID: the client ID of your CyberApp.
CLIENT_SECRET: the client secret of your CyberApp.




Step 4. Start the callback handler
Open a command prompt in the folder with the extracted callback handler and run the following command:
python ./run_server.py


This starts an HTTP server on port 8080 and connects to the vendor.db database file by default.

Note
Keep the callback handler process running while you work with the CyberApp example.



Step 5. Enable and test the CyberApp

Enable CyberApp

Log in to Acronis as an administrator on the tenant through which you published the CyberApp.
Select INTEGRATIONS from the menu.
Find the Security tool CyberApp in the catalog.
Click Configure.
Enter the username and password you specified in “Step 3. Configure callback handler and connector”.
Map the customer tenant to the Acronis tenant.



Run the connector
Open a command prompt in the folder with the extracted callback handler and run the following command:
python ./run_connector.py


This command posts a new alert of a custom alert type and reports a new workload of a custom type to the
Acronis platform.


Test CyberApp
Now the integration is enabled for both a test partner and test tenant, and you can browse the
extensions of the Acronis Management and Protection console UIs introduced by the CyberApp.








Acronis Console
Menu
Item to check
Where it is defined in the CyberApp



Management Console
INTEGRATIONS / DEFAULT ACTION
Custom tab
Vendor Portal > Custom Integration Settings

Protection Console
DEVICES / All devices
Custom workload


Vendor Portal > Workloads and actions
connector/generator.py




Protection Console
MONITORING / Alerts
Custom alerts


Vendor Portal > Alerts
connector/generator.py




Protection Console
PROTECTION / Security Tool
Custom menu item
Vendor Portal > Main menu






More Scenarios to Check

Mirroring Enablement
The same end-to-end integration example can demonstrate the mirroring enablement scheme as well.
To check this scenario, you need to:

Disable the integration on your test partner.
Duplicate the CyberApp version by following Duplicating a Version.
Update the CyberApp version:

Change CyberApp enablement options to “Create a new Partner-level record” for MSP and “Mirror Acronis Customer tenants” for Customers.
In Callback handler base URL, replace /mapping/callback with /mirroring/callback.
In CyberApp enablement form, remove Username and Password inputs.


Deploy the updated version to the test environment.
Enable the integration.



Custom Alert and Workload Attributes
You can specify your own attributes for custom alerts and workloads.
To do this, edit the templates in connector/generator.py.
See the following pages in the integration guide:

Reporting workloads
Reporting alerts