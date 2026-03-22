---
title: "Auto-mapping a callback payload"
source: "https://developer.acronis.com/doc/cyberapps/versions/ui-builder/mapping/auto-map.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:08:06.221214"
---

# Auto-mapping a callback payload

Auto-mapping a callback payload
If you name callback payload data item the same as model property IDs, Vendor Portal can automatically map these matched entities.

To auto-map a callback payload

Create your form.
Select the appropriate callback as the data initializer callback or action for a button, etc.
Click Auto-map in the appropriate mapping section - request or response.

All matching callback payload data item and model property ID pairs are mapped.

Note
If you have a root and leaf mapping situation, such as mapping an array and a table, you can:


Auto-map the leaves first (this is effectively what standard auto-map does).
Auto-map the root first.