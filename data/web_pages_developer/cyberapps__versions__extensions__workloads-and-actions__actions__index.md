---
title: "Actions"
source: "https://developer.acronis.com/doc/cyberapps/versions/extensions/workloads-and-actions/actions/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:03:39.313797"
---

# Actions

Actions

Actions appear as entries in the Integrated App actions list in the DEVICES section of the Acronis Cyber Protect Cloud console.
You specify the workload types on which the user can perform the action: either native Acronis workload types or workload types defined in the CyberApp or a combination of both.

There are two action types:



Open link

Can open:


Simple URLs

Parametrized URLs
Parametrized URLs include variables in the {{$.<attribute_name>}} format, where <attribute_name> is a path to the attribute field in the JSONPath format
For example, your website (www.demoisv.com) displays workload (device) details when you provide the workload’s MAC address as a parameter named workloadmac.
If you specify the URL as https://demoisv.com?workloadmac={{$.mac}}, the toolbar button in the Cyber Protect Cloud console Devices section will redirect the user to your website and open details.



Desktop applications
For example, a remote desktop application.



Web applications
For example, a VNC console.






Open popup


Opens a popup form which you must create using the UI builder, and specify a data initializer callback for the popup form.


Important

When the popup form opens, the data initializer callback is sent to your callback handler to retrieve data from your server to fill in the values. Therefore, you must pre-define the data initializer callback.
For more information, see Callbacks.







In this section

Opening the action list
Creating an action
Editing an action
Deleting an action