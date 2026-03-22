---
title: "Defining validation logic"
source: "https://developer.acronis.com/doc/cyberapps/versions/ui-builder/build-form/validation.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:06:27.639156"
---

# Defining validation logic

Defining validation logic
You can define validation logic for the following input control elements:

Input
Password
Switch
Select
Checkbox


If validation logic has been defined for an element, it is triggered when the user moves focus from the form element.
If the element contents are invalid, the field is highlighted in red and a warning message is displayed below it.


To define validation logic

Click the element on the UI Builder canvas.
Click the VALIDATION tab in the configuration pane.

Select the Condition block modifier:



And
Or



Click New validation.

Select a validation criterion from the Name dropdown:




Not empty
The value must be different from null, undefined or an empty text.



Email
The text must follow the regex (([<>()[]\\.,;:\s@"](\.[^<>()[]\\.,;:\s@"])*)|("."))@(([[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]\.)+[a-zA-Z]{2,}))$



Password
The text must meet all the following conditions:
*  Length greater than or equal to 8.
*  Contain at least one lowercase letter.
*  Contain at least one uppercase letter.
*  Contain at least one number.



Number
The value must be a number.



Phone Number
The text must follow the regex ^[\+\#]?[(]?\d{0,4}[)]?[-\s\.]?[(]?\d{0,6}[)]?[-\s\.]?\d{0,11}?[-\s\.]?\d{0,5}?[-\s\.]?\d{0,5}$.



Positive Number
The number must be strictly positive. That is, a rational number, excluding zero.



Whole Number
The number must be strictly positive and whole. That is, a natural number, excluding zero (1, 2, 3…).



Url
The text must follow the regex ^(?:https?:\/\/)?[a-zA-Z0-9][a-zA-Z0-9.-](?:\.[a-zA-Z0-9.-])[\w-._~:/?#[\]@!$&'()*+,;=.]+$
or be one of https://localhost, http://localhost or localhost.





[Optional] Click New validation to add another validation criterion to the logic block, and repeat step 5.
[Optional] Click New block to add another logic block, and repeat from step 3.


Note

To delete a validation, click Delete validation.
To delete a block, click Delete block, at the bottom of the block field set.




Simple examples



Compound example

In this example, there are two validation blocks.
To be valid, the element must not be empty, and the contents must either be a valid email format or a valid telephone number format.