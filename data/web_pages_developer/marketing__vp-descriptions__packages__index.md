---
title: "Exporting and importing Descriptions"
source: "https://developer.acronis.com/doc/marketing/vp-descriptions/packages/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:13:45.062986"
---

# Exporting and importing Descriptions

Exporting and importing Descriptions

A Description can be exported to a ZIP file, called a Description package.
You can import a Description package to create a new Description.
Description packages are generally used to create a CyberApp Description from a Description of a different CyberApp.


Note
To create a new Description based on an existing Description of the same CyberApp, you can simply duplicate the Description.


Description package contents

Packages have a standardized directory structure, containing files which provide declarative definitions of the Description.
They consist of:



Two Vendor Portal system directories which start with a .


Warning
Vendor Portal system directories should not be modified.



An assets directory.
This contains binary images, such as company logos, presentation slides, user interface icons, etc., that are used by the entities.


Note

During the CyberApp deployment, assets are pushed to Acronis S3 storage and their names will be changed to relevant S3 storage paths.
All assets are considered public, and no additional access checks are applied to these assets on S3 storage.




A dictionaries directory.
This contains files with localized Description content strings.
For example, a dictionary file might provide the CyberApp’s Catalog card description and Detail page description fields in another language.



An entities directory.
This contains declarative definitions of the Description’s entities.


An index.json file, which provides overall information about which entities, assets, and localization dictionaries are included.


Note

You can download an example package for DemoCyberApp here.
If you try to import it, it might fail, as the CyberApp category is defined as a specific category created for the demo CyberApp.
If you edit the ‘’categories’’ property in the ‘’index.json’’ file in the root directory of the package to a valid category, it will work.



In this section

Exporting a Description
Importing a Description package