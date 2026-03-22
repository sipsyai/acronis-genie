---
title: "JSON object structure"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/offering-items/obj-structures.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:16:21.293559"
---

# JSON object structure

JSON object structure
The API represents offering items and quotas as JSON objects.

Offering item object structure







Name
Value type
Description



application_id
UUID string
The universally unique identifier (UUID) of a service to which this offering item belongs.

edition
string
The edition. Set to null for all offering items except Cyber Protection service offering items.

infra_id
UUID string
The UUID of the storage related to this offering item. Present only if type is infra.

locked
boolean (default false)
Flag that specifies if the offering item is locked.

measurement_unit
string
The measurement unit. See the list of available measurement units.

name
string
Offering item name.

quota
quota object
An object that contains quota settings.

usage_name
string
The name of the usage related to this offering item.

status
number
The state of the offering item. 1 means enabled.

type
string
The type. See list of available offering item types.





Quota object structure







Name
Value type
Description



value
number
Soft quota setting.

overage
number
Hard quota setting.

version
number
Revision number of the quota object.





Sample JSON object of an offering item
{
"application_id": "6e6d758d-8e74-3ae3-ac84-50eb0dff12eb",
"edition": "standard",
"infra_id": "debe7865-fa8d-4c16-8e26-adcf8d7fd23d",
"locked": false,
"measurement_unit": "bytes",
"name": "dr_storage",
"quota": {
"overage": null,
"value": null,
"version": 0
},
"status": 1,
"type": "infra",
"usage_name": "dr_storage"
}




Available offering item types






Value
Description



count
Countable items like number of protected devices, size of used cloud storage or number of sync & share users.

feature
Non-countable features like availability of local backup storage.

infra
Infrastructure components like Acronis-hosted cloud storage or partner-hosted storage can be registered on the platform and offered in the form of an offering item.





Available measurement units






Value
Description



bytes
This measurement unit is used to count storage space. The platform uses binary (base 2) bytes. This means that 1073741824 bytes will be shown as 1 GB in the management portal.

quantity
This measurement unit is used to count virtual machines, mobile devices, workstations and etc.

n/a
This measurement unit is only used for the feature type, since the offering items of this type do not have countable items.





Available editions

Cyber Protection service


Name
Value
Offering item prefix
Example



Per gigabyte
pck_per_gigabyte
pg_base_
pg_base_workstations

Per workload
pck_per_workload
pw_base_
pw_base_workstations





Sync & Share service


Name
Value
Offering item prefix
Example



Legacy
fss_legacy
No prefix
fc_seats

Per gigabyte
fss_per_gigabyte
pg_base_
pg_base_fc_seats

Per user
fss_per_user
pu_base_
pu_base_fc_seats





Legacy editions


Name
Value
Offering item prefix
Example



(Legacy) Cyber Backup - Standard
standard
N/A
workstations

(Legacy) Cyber Backup - Advanced
advanced
adv
adv_workstations

(Legacy) Cyber Backup - Disaster Recovery
disaster_recovery
dre
dre_workstations

(Legacy) Cyber Protect - Standard
cyber_protect_std
p
p_workstations

(Legacy) Cyber Protect - Advanced
cyber_protect_adv
p_adv
p_adv_workstations

(Legacy) Cyber Protect - Disaster Recovery
cyber_protect_dre
p_dre
p_dre_workstations

Cyber Protect (per workload)
per_workload

pw_p_ess_ (Cyber Protect Essentials functionality)
pw_p_ (Cyber Protect Standard functionality)
pw_p_adv_ (Cyber Protect Advanced functionality)
pw_ (Cyber Backup functionality)



pw_p_ess_workstations
pw_p_workstations
pw_p_adv_workstations
pw_workstations



Cyber Backup (per gigabyte)
per_gigabyte
pg_
pg_workstations