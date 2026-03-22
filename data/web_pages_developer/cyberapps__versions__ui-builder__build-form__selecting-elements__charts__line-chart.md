---
title: "Line chart form element"
source: "https://developer.acronis.com/doc/cyberapps/versions/ui-builder/build-form/selecting-elements/charts/line-chart.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:05:04.448067"
---

# Line chart form element

Line chart
A line chart plots one or more historical data sets as points on one or more graphs. You must supply the chart data in a callback response, and map the callback response to the line chart element in the Data Initializer callback section of the form’s PROPERTIES tab.
For more information, see Specifying a data initializer callback.
In the example below, you can see a line chart with a label, a single data set rendered in red, X axis time unit of hours, data points shown on user hover, and data point tooltips. For more information, see PROPERTIES.

Line charts have a default appearance, but you can override the appearance defaults in the element PROPERTIES tab.
You can also dynamically override the properties in the line chart callback response. For more information, see JSON schema of line chart callback response.

Note
You can periodically refresh the line chart data (and appearance, should you wish to) by specifying the appropriate callback in the Refresh callback section of the form PROPERTIES tab, and mapping the response data to the line chart element properties. For more information, see Refresh callback.


PROPERTIES



ID
Element identifier.



Label
Text displayed at the upper-left corner of the chart element.
Default = null.



Width



Default
This is for backward compatibility purposes only.



Fit



Fill
Uses all of the available width.




For more information, see Element distribution.
Default = Fit.



Height
The height of the chart element. The minimum height of the chart container is 150, but the chart displayed within the container can be as small as you want.
Default = 200.



Time unit
The unit of time for the X axis.
Options are:



Second
Minute
Hour
Day
Week
Month
Year



Default = Hour.



Options
The properties in this section - with the exception of Colors - can be changed by mapping the chart callback response data. Most are standard chart controls and the meanings are therefore intuitive. Explanations for less intuitive properties are included, below.



Colors
Specifies the color of the data object datasets. Enter the colors as a comma-separated list.
Default = default-primary (a standard Acronis platform color).



Note
This property cannot be controlled using chart callback reponse data.




Show legend
Default = True.



Show data point on hover
Default = False.



Precision
Maximum data decimal points displayed.
Default = 0. Maximum = 10.



Show data type unit
Default = False.



Stepped nature of line
Display graph as step form.
Default = False.



Show tooltip
Tooltip is a popup which displays data details when the user hovers over a data point.
Default = True.



Tooltip Time Format
Default = dd MMM, yyyy, hh:mm:ss.



Pass variable threshold values
Default = False.



Show X axis
Default = True.



Show X grid
Default = True.



Show Y axis
Default = True.



Y axis step size
Default = null.



Y axis ticks upper limit
Default = 5.



Show Y axis in %
Default = False.



Show Y grid
Default = True.







JSON schema of line chart callback response

{
"title": "Line Chart",
"description": "Line Chart data payload",
"type": "object",
"properties": {
"data": {
"type": "object",
"properties": {
"series": {
"type": "array",
"items": {
"type": "object",
"properties": {
"name": {
"type": "string"
},
"points": {
"type": "array",
"items": {
"type": "number"
}
}
}
}
},
"labels": {
"type": "array",
"items": {
"type": "string"
}
}
}
},
"legend": {
"type": "boolean",
"default": true,
"description": "Toggle visibility of legend"
},
"dataPointOnHover": {
"type": "boolean",
"default": false,
"description": "Show data points on hover"
},
"precision": {
"type": "integer",
"default": 0,
"description": "Number of digits to be shown after decimal point"
},
"showDataTypeUnit": {
"type": "boolean",
"default": false,
"description": "Show data type unit with time unit"
},
"stepped": {
"type": "boolean",
"default": false,
"description": "Toggles stepped nature of line"
},
"tooltip": {
"type": "boolean",
"default": true,
"description": "Toggles visibility of tooltip"
},
"tooltipTimeFormat": {
"type": "string",
"default": "dd MMM, yyyy, hh:mm:ss",
"description": "Format of time displayed in tooltip"
},
"variableThreshold": {
"type": "boolean",
"default": false,
"description": "Toggles if variable threshold values are passed"
},
"xAxis": {
"type": "boolean",
"default": true,
"description": "Toggle visibility of x-axis"
},
"xGrid": {
"type": "boolean",
"default": true,
"description": "Toggles visibility of vertical grid lines"
},
"yAxis": {
"type": "boolean",
"default": true,
"description": "Toggle visibility of y-axis"
},
"yGrid": {
"type": "boolean",
"default": true,
"description": "Toggles visibility of horizontal grid lines"
},
"yAxisStepSize": {
"type": "integer",
"description": "Defines the step size on the Y axis"
},
"yAxisTicksUpperLimit": {
"type": "integer",
"default": 5,
"description": "Upper limit for the number of ticks displayed on the Y axis"
},
"yPercent": {
"type": "boolean",
"default": false,
"description": "Toggles if values are to be rendered as percentages"
}
},
"required": [
"data"
]
}