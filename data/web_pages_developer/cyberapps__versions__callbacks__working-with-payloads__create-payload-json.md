---
title: "Composing JSON schema for a payload"
source: "https://developer.acronis.com/doc/cyberapps/versions/callbacks/working-with-payloads/create-payload-json.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:00:45.261510"
---

# Composing JSON schema for a payload

Composing JSON schema for a payload

Important
Ensure that the schema you compose complies with the rules outlined in Payload JSON schema technical reference in order to comply CyberApps mapping rules).


To compose JSON schema for a payload
Currently, the Vendor Portal callback payload editor is an enriched textarea which offers suggestions, linting and validation to assist you with defining your payloads.

To compose JSON schema for a callback payload, you must either


Write the JSON schema manually.

Use a tool, such as JSON Schema Builder.
This tool is partically recommended, as it is simple.


Important

Not every JSON Schema generated with this tool might be valid for CyberApp mapping.
For example, the tool allows multi-types with objects and array, which is forbidden with CyberApp mapping rules.