---
title: "Localizing the menu items"
source: "https://developer.acronis.com/doc/cyberapps/versions/extensions/mainmenu/localization/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:02:47.615444"
---

# Localizing the menu items

Localizing the menu items

Note
To localize main menu items created prior to Acronis release C25.06, you must re-save the menu items in order to create the new localization string pairings.

CyberApp menu items can display according to the language preference of the Acronis user who accesses them.
When you localize menu item content, Vendor Portal builds a ZIP file containing language localization files. The localization files alphabetically list all unique strings from all menu item forms.
You must then translate the contents of each localization file, and import the translations.

Note

If you have not localized for the user’s selected language, the original, English strings display.
If some of the strings have not been translated, those strings display as the original, English strings.



To localize the menu items

Note

If the Version is in the Draft state, you can modify the localization files.
If the Description is any other state, you cannot.
For more information about Version states, see the Version approval section.



Open the CyberApp Version.
Click Localization.


Click .



Select the languages you want to localize and click Export.
A .zip file containing a .json file for each language you selected.


Pass these files to your translation agency, and have the second entry of the string pairs translated into the corresponding language.
Save the modified files in a .zip file.
Click  and select the ‘’.zip’’ file.
Click Open.

When complete, the Existing languages section shows which languages have been localized.




Note
If you localize for an existing language, the localized language string pairings are exported.
To localize for a new language, you don’t need to export and import the existing languages again: only export the new language, translate, and import, as detailed, above.
Existing languages are not removed if they are not included in the import file, they are ignored.
To remove an existing localization, see Removing a localization


In this section

Localization example
Removing a localization