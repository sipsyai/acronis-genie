---
title: "Building the example"
source: "https://developer.acronis.com/doc/cyberapps/versions/enablement-form/create-example-connection-setup-form.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:01:37.571202"
---

# Building the example

Building the example
The example CyberApp enablement form looks like this:


To build the example CyberApp enablement form

Open the Version.
Select CyberApp enablement form from the menu.
Select Connection setup.
Click  to open the UI builder.
Drag and drop a Text element onto the UI builder canvas.
Configure the Text element properties.


In the Text field, enter text to briefly describe what is necessary to configure the CyberApp.
For the example, enter Please provide credentials to your service account..




Drag and drop an Input element onto the UI builder canvas.
Configure the Input element properties.


In the ID field, specify a unique alphanumeric name for the element.
For example, username.


Set the Field type property to Identity.
In the Label field, enter Username.


Drag and drop a Password element onto the UI builder canvas.
Configure the Password element properties.


In the ID field, specify a unique alphanumeric name for the element.
For example, password.


Set the Field type property to Secret.

Note
Password elements have the Field type property set to Secret by default.


In the Label field, enter Password.

You should have the following structure in your UI builder:


[Optional] Click Preview to preview the changes.

Note
At this point, you will not see the form title or the Cancel and Connect buttons. These are added automatically when deployed.


Click Done.
Click Save changes.


Note

When an MSP enables the CyberApp, the callback requests will include X-CyberApp-Auth header in the following format:

<username>:{"password": "<password>"}

Where:

<username> is the value of the Username field
<password> is the value of the Password field