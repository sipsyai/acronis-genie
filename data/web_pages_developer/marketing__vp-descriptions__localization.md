---
title: "Localizing a Description"
source: "https://developer.acronis.com/doc/marketing/vp-descriptions/localization.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:13:27.902400"
---

# Localizing a Description

Localizing a Description

The Acronis catalogs display the CyberApp Description localization contents according to the Acronis partner’s default language preference.
If the partner’s default language preference is not one of the localizations you specify for the Description, the English Description details are displayed.
If you specified the partner’s default language preference as one of the Description language localizations in the Description General settings, the localization file details are displayed.
If the translation of some content is not supplied in the localization file, the default English version of the missing content is displayed.


To localize a Description

Note

If the Description is in the Draft state, you can modify the localization files.
If the Description is any other state, you cannot.
For more information about Description states, see the Description approval section.



Open the CyberApp Description.



Click Export localization.
A file named cti.zip downloads. It contains a .json file for each of the language localization options selected in General settings.
Localization files are initially exported as empty files.


Copy the en.json file contents into the empty language localization files and replace the English details with the translated version using the text editor of your choice.
Save the modified files as a .zip file.
Click Import localization.
Select the .zip file from step 4.