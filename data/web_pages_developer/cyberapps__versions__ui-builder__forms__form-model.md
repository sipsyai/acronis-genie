---
title: "The form model"
source: "https://developer.acronis.com/doc/cyberapps/versions/ui-builder/forms/form-model.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:07:32.397762"
---

# The form model

The form model
Form data is stored in the form model. The form model stores information about UI elements with an ID assigned and input parameters.

Note
If a UI element and an input parameter have the same ID, they are treated as the same piece of data.

The form model is considered a JSON schema object. Every element in the form model is transformed to a JSON schema property inside the object. The property name is the UI element or input parameter ID, and the type is given by the lists, below. Input parameters are string type by default, but if you give an input parameter and a UI element the same ID, the input parameter takes the data type of the UI element.

Note
For more information about CyberApp JSON schemas, see Payload JSON schema technical reference.


UI element types

Active elements
Active elements are available for both request and response mapping.

Button Group (when type is checkbox): Array of <String>
Button Group (when type is radio): String
Checkbox: Boolean
Date Picker: String
Group (when mode is repeater): Array of <Object<{ [component’s model property]: component type following this list }>>
Group (other modes): Nothing


Note
If it contains any contained elements: contained elements are mappable as if they are at the root level.



Input (when element Type property is Text or Textarea): String
Input (when element Type property is Number): Number
Number Picker: Number
Password: String
Select (when multiple is false): Any of <String, Number>
Select (when multiple is true): Array of <Any of <String, Number>>
Switch: Boolean
Tab container: Object<[tab internal form name]: tab form schema>
Time Picker: String



Passive elements
Passive elements are only available for response mapping.

Alert: String
Button: String
Header: String
Icon: Object<{ name: string, size: string, color: string, text: string }>


Note
For more information, see Defining an icon dynamically.



Link: Object<{ text: string, href: string }>


Note
For more information, see Defining a link dynamically.



Table: Array<Object<{ [column’s model property]: AnyOf<String, Number> }>>
Tag: Object<{ content: string, type: string, inverse: boolean, small: boolean }>


Note
For more information, see Defining a tag dynamically.



Text: String
Tooltip: String




Example
Consider this UI builder form



When deployed, a user enters some data.



For this data, the form model can be represented as:
{
"username": "johnsmith"
"email": "john.smith@demoisv.com"
"isActive": true
}



Note
Button has no ID, so there’s no value stored for it in the model.
Only properties that are present in the model can be mapped.

The JSON schema that represents the form indicates that the form model is an object that contains three properties: username (which is a string), email (which is a string), and isActive (which is a boolean).
We can also specify that there cannot be any other properties in our form model that are not listed in properties.
{
"type": "object",
"properties": {
"username": {
"type": "string"
},
"email": {
"type": "string"
},
"isActive": {
"type": "boolean"
}
},
"additionalProperties": false
}