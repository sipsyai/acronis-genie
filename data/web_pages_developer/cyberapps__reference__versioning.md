---
title: "Versioning"
source: "https://developer.acronis.com/doc/cyberapps/reference/versioning.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:59:06.197162"
---

# Versioning

Versioning

CyberApp versioning
Versions of CyberApps use sequence-based version identifiers assigned in increasing order in the following format: <X>.<Y>,
where <X> is the major version and <Y> is the minor version. Versioning allows the maintenance of
the CyberApp revision history and the latest version of the CyberApp identifies the CyberApp.

When a CyberApp goes through the review process, it becomes fixed and cannot be changed unless it was sent
back for rework.

Note
For more information on CyberApp review stages, see CyberApp lifecycle.

The CyberApp can be copied at any stage to continue the CyberApp development in a new version.


Extension point versioning
Extension point versions use sequence-based version identifiers assigned in increasing order in the following format: <X>.<Y>,
where <X> is major version and <Y> is minor version.
Extension points are grouped by CyberApp Version.


When the CyberApp Version is in review, approved or declined, the extension point versions also become fixed.
This ensures that the CyberApp Version is reviewed and published only with the provided set of extension points, and that the extension point versions are consistent when used in other CyberApp Versions.



CyberApp Versions may combine different extensions points and their versions, but different versions of the same extension point cannot be used within the same CyberApp Version.
For example, one CyberApp Version may include the updated and fixed extension point versions and the other CyberApp Version may additionally introduce a new alert extension point.



Note
If multiple draft CyberApp Versions are sharing the same extension point version that is not fixed, the extension point will be updated for all CyberApp Versions when edited.



CyberApp Description versioning
CyberApp Description versions use sequence-based version identifiers, assigned in increasing order in
the following format: <X>.<Y>, where <X> is major version and <Y> is minor version.