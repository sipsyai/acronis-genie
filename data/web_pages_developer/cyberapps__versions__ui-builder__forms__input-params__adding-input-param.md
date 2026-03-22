---
title: "Adding input parameters"
source: "https://developer.acronis.com/doc/cyberapps/versions/ui-builder/forms/input-params/adding-input-param.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:07:40.991678"
---

# Adding input parameters

Adding input parameters

To add an input parameter

Open the form.
In the configuration pane, in the Input parameters section, click .
Enter the input parameter ID.

Enter the input parameter Default value.
You can use Acronis variables in the default value. For more information, see Using Acronis variables in default value strings.



[Optional] Click the  type icon and select the input parameter type from the dropdown.
Input parameters can be one of three types:



Primitive
Primitive type is not a traditional type. It is a union of String, Number, Integer, Boolean, and Null.
You can store any of these data types in this type of input parameter, and you can map from/to radio buttons, checkboxes, etc.



Array
Array type provides no information regarding the type of the items of the array.
You can store any kind of array inside the input parameter and use the input parameter to map from/to a table or any other array, regardless of its item types.



Object
Object type is similar to how the array type works.
It represents an object with no information about its properties, which means any object can be mapped to the input parameter, and the input parameter can be used to map to any other object.
You can map this type of input parameter from/to a table row and other objects.







Example

In this example, the developer creates two input parameters.



UserGroup is given a default value of ALL and a Primitive type ().
tenant is given the generic Acronis variable of ‘’{{ $.tenant_ID }}’’ and a Primitive type ().
originDC is given the generic Acronis variable of ‘’{{ $.origin }}’’ and a Primitive type ().
userdetails is given a type of Object ().