---
title: "Localization example"
source: "https://developer.acronis.com/doc/cyberapps/versions/extensions/mainmenu/localization/example.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:02:43.256125"
---

# Localization example

Localization example
We will demonstrate localization of the following form:



We select four localization languages:



The following .zip file is created:



As this is the first time localizing this CyberApp, all exported localization files are identical. They contain language pairings with both sides of the pair in English:


We translate the localization files, but only partially translate the es Spanish language file (omitting the placeholder strings which begin User’s):


Then, we create a .zip file with our four translated localization files and import the .zip file.
The translations are registered in the Existing languages section Vendor Portal:




Note
If we localize the same languages again, the imported language string pairings are exported.
The Spanish localization file will include the untranslated language pairs.
To localize for a different language, we don’t have to export and import the existing languages again: we can simply export the new language, translate, and import.
Existing languages are not removed if they are not included in the import file, they are ignored.