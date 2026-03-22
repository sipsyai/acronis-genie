---
title: "Complex mapping scenarios"
source: "https://developer.acronis.com/doc/cyberapps/versions/ui-builder/mapping/manual-map/complex-mapping/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:08:18.983281"
---

# Complex mapping scenarios

Complex mapping scenarios

Mapping provides the ability to map form model and callback request/response properties that - at first sight - are not compatible.
When electing which properties to map (one from each side of the mapping tool), a variety of scenarios exist, with set rules.





General rules


Left-side properties can be selected multiple times for multiple mappings.

Right-side properties can be used only once.
The parents and children of a right-side property are disabled after they are mapped.
For instance, if you choose an object’s head on the right side, the child properties are not selectable, since the whole object is already being mapped.






Mapping scenarios

Scenario 1: Both left and right properties are single values
Scenario 2: Both left and right properties are arrays
Scenario 3: Both left and right properties are arrays
Scenario 4: Both left and right properties are array properties
Scenario 4.1: Left property is a primitive or an object at root level, and right property is an array property
Scenario 5: Left property is an array and right properties is a single value
Scenario 6: Left property is an array property and right properties is a single value


Scenario availability

Note
Not all mapping scenarios are possible all the time.

Some scenarios are disabled after a scenario is used. This depends on whether we are request or response mapping a callback request or a callback response.

Request mapping

Scenario 1 is always enabled for request mapping. However, there are two scenario ‘branches’: Single request mapping and Multiple request mapping.
If any scenario from either branch is performed, then none of the scenarios in the other branch are viable any more.




Response mapping

Note
Scenario 5 and scenario 6 do not make sense when mapping a callback response payload to a form model, because a single response payload is mapped to a single form model.


Response mapping is even simpler.
Since there is only one branch, it is always referred to as response mapping.





In this section

Scenario 1: Both left and right properties are single values
Scenario 2: Both left and right properties are arrays
Scenario 3: Both left and right properties are arrays
Scenario 4: Both left and right properties are array properties
Scenario 4.1: Left property is a primitive or an object at root level, and right property is an array property
Scenario 5: Left property is an array and right properties is a single value
Scenario 6: Left property is an array property and right properties is a single value