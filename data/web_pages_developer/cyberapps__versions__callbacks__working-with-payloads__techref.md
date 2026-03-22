---
title: "Payload JSON schema technical reference"
source: "https://developer.acronis.com/doc/cyberapps/versions/callbacks/working-with-payloads/techref.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:00:54.009623"
---

# Payload JSON schema technical reference

Payload JSON schema technical reference

Due to technical limitations, CyberApps only support a subset of the JSON Schema Draft 4 and JSON Schema Reference.
Additionally, Vendor Portal imposes some constraints to ensure that callback payload schemas can be mapped by users in the UI builder.


Supported JSON schema features

Note
We do not use the exact same terminology that the JSON Schema standard uses.


Schema properties
The minimum JSON schema is a schema property. A schema property is defined within brackets:
{
"type": "..."
}


The type keyword specifies which is the type of the property.
Not every property must have a type, but they usually do.


Data types
Every property contained in CyberApp schemas must have a type.
There are seven different data types that you can use:


Primitives


Number
Integer
String
Boolean
Null



Composed


Object
Array





A property with Integer type would then be defined as:
{
"type": "integer"
}


Objects and Arrays are special types, but they can be used here as well:
{
"type": "object"
}



Objects
Properties with Object type represent a JSON object with properties.
They also support a set of additional attributes that can help defining these properties:


Properties: An Object whose entries define the properties of the object itself. Every entry represents one object property, where the key is the name of the property and the value must be a valid JSON Schema representing the type of the object property. Note that objects can be naturally nested if an object property is also an object.


Important
One of our custom rules is that an Object property cannot be named “[i]”, as we use this name internally.





{
"type": "object",
"properties": {
"key1": {
"type": "string"
},
"key2": {
"type": "object",
"properties": {
"innerKey1": {
"type": "boolean"
}
}
}
}
}




Required: By default, none of the properties defined before is mandatory, which means that an empty object would match against our schema. If we want to require them, then we can add the required keyword with a list of the required property names.

{
"type": "object",
"properties": {
"key1": {
"type": "string"
},
"key2": {
"type": "null"
}
},
"required": ["key1"]
}



Note
We can see that key1 is required in the object, but key2 is not.


Additional properties: Unless stated otherwise, our schema supports additional properties (properties whose names are not listed). If we do not want schemas with additional properties to match with ours, then we can set additional properties to false.

{
"type": "object",
"properties": {
"key1": {
"type": "string"
},
"key2": {
"type": "null"
}
},
"additionalProperties": false
}







If we want to accept additional properties - but only if they have a given type - we can define additional properties as a schema property. For example, we will allow additional properties, but only if they are of type number.

{
"type": "object",
"properties": {
"key1": {
"type": "string"
},
"key2": {
"type": "null"
}
},
"additionalProperties": {
"type": "number"
}
}






Arrays
Properties with array type represent a JSON array. As such, an array can define the type of the items it will contain.
{
"type": "array",
"items": "string"
}


JSON Schema allows the items to have any type. For example, we can have objects as the items of an array:
{
"type": "array",
"items": {
"type": "object",
"properties": {
"innerArray": {
"type": "array"
}
}
}
}


Or even another array nested inside our first array:
{
"type": "array",
"items": {
"type": "array"
}
}


While all these schemas are considered valid, you should take into account that, due to some technical limitations, you will only be able to map the array nearest to the root of the schema (so, nested arrays are not eligible for mapping).



Compatible types
To create a mapping between two properties, their types must be compatible.

Note
Compatibility is one-sided: if property A is compatible with property B, property B does not necessarily need to be compatible with property A (even though it could be).


Primitive types are only compatible with the same type.

Note

Integer is an exception.
Integer is compatible with Number. This means that Integer can be assigned to Number.
Number is not compatible with Integer.




Objects are compatible depending on their properties.
If all properties in the right object are compatible with their counterpart in the left object, then they are compatible, unless:



The left object is missing properties that are required in the right object.
The left object has additional properties and they are either not compatible with the right object additional properties or the right object does not accept any additional properties.




Arrays are compatible, depending on their items types.
If their items types are compatible, then the arrays are compatible.





Multi-type

Some properties might have more than one primitive type, which is represented with a multi-type condition.
There are three multi-type conditions:




Any of
If any of the multiple types is compatible with the type on the other side, then they are compatible.



All of
If all of the multiple types are compatible with the type on the other side, then they are compatible.



One of
If one (and exactly one) of the multiple types is compatible with the type on the other side, then they are compatible.




A property declaring a multi-type looks like this:

{
"anyOf": [
{
"type": "string"
},
{
"type": "number"
}
]
}



This means it is any of String or Number. The rest of the conditions are represented in the same way:

{
"oneOf": [
{
"type": "string"
},
{
"type": "number"
},
{
"type": "null"
}
]
}




Note
Only primitive types can be used for multi-types. This is a custom rule to ensure consistency in mappings.

A multi-type property with any of condition can be also represented in a more compact way:

{
"type": ["string", "number", "null"]
}





Metadata
All schema properties support the following metadata keyword:

Title: Allows changing the title displayed when mapping the property.

For instance, the following schema:





However, the title can be changed:


The property will be now represented like this:




Note

The internal representation will remain the same (as uglyKeyName).
This only changes how it is displayed to the user.