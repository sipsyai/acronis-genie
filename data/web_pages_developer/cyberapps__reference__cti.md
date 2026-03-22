---
title: "Cross-domain Type Identifier (CTI)"
source: "https://developer.acronis.com/doc/cyberapps/reference/cti.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:58:57.615825"
---

# Cross-domain Type Identifier (CTI)

Cross-domain Type Identifier (CTI)
Cross-domain Type Identifier (CTI) is an Acronis-specific notation providing a unified way to identify:

Domain object types (i.e. object schemas such as alerts, protection plans, etc.).
Specific object instances, such as namespaces, groups.

Similar to other notation systems (such as Apple UTI or Amazon ARN, CTI is represented by a string that uniquely identifies the
API object’s entity kind (type or instance), origin (i.e., object vendor and application), and its version.
For the full specification of CTI, see Cross-domain Typed Identifiers (CTI) cersion 1.0 Specification on the Acronis GitHub repository.

Cross-domain Type eXtension (CTX)
Cross-domain Type eXtension (CTX) is the object definition that is always introduced by a certain vendor and application, and is defined as follows: <vendor_name>.<application_name>.<entity_code>.v<major>.<minor>.
With CTX notations, a fully qualified CTI object name could be represented as follows: cti.<vendor_a>.<application_a>.<entity_code_a>.v<major_a>.<minor_a>~<vendor_b>.<application_b>.<entity_code_b>.v<major_b>.<minor_b>.
Object version is defined by its major and minor version in the form of v<major>.<minor>. For example, “v2.0”.

Note

Object with the same v<major> version must have a backward compatible format and validation schema.
The <entity_code> claim could be a single word or a dot-separated title if you want to have an advanced naming. For example, to incorporate a namespace into the type name. See the <entity_code> naming best practices.


When defining the object, we recommend to use the following <entity_code> naming best practices:

Use a dot-separated name in the <namespace>.<type> format where:


<namespace> - 2-4 character abbreviation defining the namespace or domain. For example, ‘am’ - alert manager.
<type> - 3-8 character name of a specific self-explanatory type within a given namespace/domain. For example, ‘alert’.



Use the single word only for standalone types with clear self-explanatory names. Examples:


cti.vendor.app.type.v1.0 - bad naming. It’s not clear what this ‘type’ type is about.
cti.vendor.app.am.type.v1.0 - good naming. It’s clear that given CTX defines alert types (am is a short name for the alert management domain).
cti.vendor.app.alert_type.v1.0 - not recommended to use if there are other CTXs with the alert_ prefix, but OK if alert_type is the only CTX in the alert domain.




All the base types of the Acronis Cyber Protect Cloud domain model (like alerts, protection plans, etc.) are introduced by the Acronis vendor called “a” with the Platform CyberApp called “p”, for example:

cti.a.p.am.alert.v1.0 (am.alert stands for “alert management . alert”)
cti.a.p.wm.workload.v1.0 (”workload management . workload”)
cti.a.p.pm.policy.v1.0 (”policy management . policy”)
Etc.

Third-party vendors may inherit types introduced by Acronis, for example:

cti.a.p.am.alert.v1.0~a_vendor.dlp.data_leak_detected.v2.2
cti.a.p.am.alert.v1.0~another_vendor.email_security.malware.v1.0



Types and type inheritance
Acronis Cyber Protect Cloud domain types inheritance is based on the principle that the base object type has specific ‘extension points’ which can be ‘specialized’ by a derived type.
Inheritable base types always have:

generic fields common for base and all inherited types (For example, generic workload type has name and tenant_id fields)
blob payload that is used to store some data specific for the inherited type only (For example, backup_failed alert may store failure reason and protection plan ID associated with the failure).

Inherited types can not declare any new object attributes and can only override base type fields marked as overridable.
CTI defines the inheritance between the objects using the ~ character.
Example of workload CTI type


Note
Types represented with CTI notation could be abstract or concrete:

abstract types (like Generic alert) could not be instantiated (most base types introduced by Acronis SDK CyberApp are abstract and support inheritance).
concrete types (like Backup Failed alert) allow the creation of instances of that type.



Important

Type inheritance means both interface inheritance (i.e. schema inheritance) and semantic inheritance (i.e. behavior inheritance).
Practically, derived types inherit base type semantics as is, but can introduce some specific semantics. For example, generic alerts would introduce standard alerts management semantics like dismissal flow, rendering flow, alert generation rules, etc. Inherited alert types (like Backup Failed alert) would have the same base semantics applicable as well, but could have some additional flow like specific alerts aggregation/processing rules implemented by the corresponding application.




Syntax


General

Must start with cti. prefix.
Must be defined in snake_case.
Must be represented in form of cti.<ctx>[~<ctx>].



<ctx>
Must be represented in <vendor_name>.<application_name>.<entity_code>.v<major>.<minor>.


<vendor_name>,
<application_name>



Must not be empty.The URL to your company’s website.
Must contain only Latin letters, digits or underscore _.
Must be started with a letter.



<entity name>

Must not be empty.
Must contain only Latin letters, digits, asterisk *, dot . or underscore _.
Must not contain doubled dot . or underscore _ separators.




<Minor version>,
<Major version>


Must be a positive number without leading zeroes.



CTI notation could represent a type “inheritance” relation similar to class inheritance in any object-oriented programming language which can be expressed as: cti.<ctx_a>[~<ctx_b>[~<ctx_c>[…]]]
Where:

“ctx_a” - defines the parent type (generic alert, generic event, generic protection policy, etc.).
“~” - means that entity, defined with <ctx_b>, derives from entity, defined by <ctx_a> (like backup_failed alert inherits generic alert, etc.).
“[…]” - type inheritance could be chained and inheritance depth is unlimited.