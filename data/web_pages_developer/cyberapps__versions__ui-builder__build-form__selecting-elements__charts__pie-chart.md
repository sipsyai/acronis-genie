---
title: "Pie chart form element"
source: "https://developer.acronis.com/doc/cyberapps/versions/ui-builder/build-form/selecting-elements/charts/pie-chart.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:05:08.641410"
---

# Pie chart form element

Pie chart
A pie chart displays a data set as sectors of a circle, which represent a proportion of the data set total. You must supply the data set in a callback response, and map the callback response to the pie chart element in the Data initializer callback section of the form’s PROPERTIES tab. For more information, see Specifying a data initializer callback.

Pie charts have a default appearance. You can set some of the appearance properties in the element PROPERTIES tab.
You can dynamically override properties (including the color scheme, but excluding the element size) in the pie chart callback response. For more information, see JSON schema of pie chart callback response.

Note
You can periodically refresh the pie chart data (and appearance, should you wish to) by specifying the appropriate callback in the Refresh callback section of the form PROPERTIES tab, and mapping the response data to the pie chart element properties. For more information, see Refresh callback.


PROPERTIES



ID
Element identifier.



Label
Text displayed at the upper-left corner of the chart element.
Default = null.



Data Type
The type of data being represented in the pie chart. If unspecified, values are treated as generic numbers, and the numbers are rounded according to the Precision property.



Size
Speed
Speed in bits
Temperature (Celsius)




Options
The properties in this section can be changed by mapping the chart callback response data.




Show legend
Default = True.



Precision
Maximum data decimal points displayed.
Default = 0. Maximum = 10.



Show summary
A summary of the data can be displayed in the centre of the pie chart.
Default = False.








JSON schema of line chart callback response

{
"$schema": "http://json-schema.org/draft-07/schema#",
"type": "object",
"properties": {
"data": {
"type": "object",
"properties": {
"dataType": {
"type": "string",
"description": "Type of data being represented. If omitted, values are treated as generic numbers and rounded according to precision property.",
"enum": ["size", "speed", "speed_bits", "temperature"]
},
"sets": {
"type": "array",
"items": {
"type": "object",
"properties": {
"name": { "type": "string" },
"value": { "type": "number" },
"color": {
"type": "string",
"description": "Hex color code for the set. If omitted, a default color from the palette will be assigned."
}
},
"required": ["name", "value"]
}
}
},
"required": ["sets"]
},
"summary": {
"type": "boolean",
"description": "Toggles visibility of summary",
"default": true
},
"precision": {
"type": "integer",
"description": "Number of digits to be shown after decimal point",
"default": 0
},
"legend": {
"type": "boolean",
"description": "Toggles visibility of legend",
"default": true
}
},
"required": ["data"]
}