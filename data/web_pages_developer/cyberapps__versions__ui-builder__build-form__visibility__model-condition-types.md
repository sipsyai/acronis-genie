---
title: "Setting model condition types"
source: "https://developer.acronis.com/doc/cyberapps/versions/ui-builder/build-form/visibility/model-condition-types.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:06:44.618502"
---

# Setting model condition types

Setting model condition types

Model condition types are element-specific: they correspond to the model value of individual form elements.
For more information, see Model condition type examples.


To set model condition types

Enter the ID of the form element in the Property name field.
Select a Property type:


Number


Select an Operator value from the dropdown.


Equals
Not equals
Greater than
Greater than or equals
Less than
Less than or equals




Enter a Value.
This can be any decimal rational number.





String


Select an Operator value from the dropdown.


Equals
Not equals
Contains
Not contains
Starts with
Not starts with
Ends with
Not ends with



Enter a Value.
[Optional] Switch on the Ignore case option.



Boolean (default)


Select an Is value from the dropdown.


True
False


Note
For non-Boolean elements, Model is True if the element value is not null, and False if it is.