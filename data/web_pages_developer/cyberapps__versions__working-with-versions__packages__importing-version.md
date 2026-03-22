---
title: "Importing a Version package"
source: "https://developer.acronis.com/doc/cyberapps/versions/working-with-versions/packages/importing-version.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:10:24.086953"
---

# Importing a Version package

Importing a Version package

To import a Version package

Open the CyberApp.
Select the CYBERAPP VERSIONS tab.
Click .


Drop the Version package file onto the screen or click choose a file to select it from your local disk.
Click Import



Import conflicts
If the Version specified in the Version package has the same version number as a Version in your Version list, and/or if any of the Version package extension points have the same CTI object version number as an already existing one, the import conflict resolution screen will appear.

To resolve a conflict with the version number of the Version to be imported, the imported Version version number is automatically ‘bumped’ by incrementing the minor version number.
To resolve a conflict with extension point CTI object version numbers, you must choose to either:


‘Bump’ the imported extension point CTI object version number(s), by incrementing the minor version number(s).
This imports all extension points, as defined in the Version package, but with modified CTI object version number(s).



Link the imported Version to pre-existing extension point(s) with the conficted CTI object version number(s).



Important

This option means the conflicted extension points are not imported, and are effectively replaced by your pre-existing extension points.
Ensure that the functionality of the pre-existing extension points is desired before selecting this option.