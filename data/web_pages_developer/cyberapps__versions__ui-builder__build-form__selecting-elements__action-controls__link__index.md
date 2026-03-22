---
title: "link objects"
source: "https://developer.acronis.com/doc/cyberapps/versions/ui-builder/build-form/selecting-elements/action-controls/link/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:04:55.896620"
---

# link objects

Link

This element opens the specified URL on user click.
The link can present as a standard link or as a button.

See examples

Properties


ID
Element identifier.


Width


Default
This is for backward compatibility purposes only.



Fit
Adjusts the width according to the Text contents.



Fill (default)
Uses all of the available width.
A standard link is not fill-responsive.
A button-style link is fill-responsive. (see examples)
For more information, see Element distribution.





Text
The link display text or button label.
For more information, see the Style property, below.



Note
This property can be controlled dynamically, using a callback. For more information, see :doc:<dynamic-link>.




URL
The link URL. You can add variables to the URL property string.



Note
This property can be controlled dynamically, using a callback. For more information, see :doc:<dynamic-link>.




Style




Link (default)
The link is displayed as a standard link.



Button
The link is displayed as a button element. Additional settings are available if you chose this style:





Type (see examples)
The button type. Each type has a different style.



Primary
Secondary
Danger
Ghost
Promo
Translucent







Padding (see examples)
The internal padding of the button, which determines its overall size.



Small
Medium (default)
Large




[Optional] Icon name (see examples)
Inserts an icon to the left of the label.



Note
If you select a monochrome icon, it is displayed in white.












Examples

Button types





Button width examples





Button padding examples





Button icons examples




In this section

Adding a variable to a link URL
Defining a link dynamically