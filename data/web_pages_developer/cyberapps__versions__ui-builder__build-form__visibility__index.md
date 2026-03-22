---
title: "Element visibility and enablement"
source: "https://developer.acronis.com/doc/cyberapps/versions/ui-builder/build-form/visibility/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:06:40.420997"
---

# Element visibility and enablement

Element visibility and enablement
In the VISIBILITY tab of an element, you define logic to control the element visibility and enablement. This ability is available to you for all element types.
The visibility logic builder allows you to build extremely complex, recursive conditions, should your CyberApp UI require them. Technically, there are no limitations.
Element visibility logic adheres to a logical hierarchy of dependencies, conditions, and condition blocks.

Dependencies

The visibility logic consists of one or more dependencies. Each dependency controls either the visibility state or the enablement state of the element.
The result of the logic in each dependency is either True or False at any given time.



Note
If multiple dependencies control the same state (visible or enabled), then all of those dependencies must be True for the state to be True.




Condition blocks

Dependencies consist of one or more condition blocks.

If all condition blocks in a dependency result in True, the dependency is True.
If any condition blocks in a dependency results in False, the dependency is False.



Conditions

Condition blocks consist of one or more conditions, which are logically related by the Condition block modifier.

If all conditions in an And condition block are True, the condition block is True.
If any condition in an And condition block is False, the condition block is False.

If any condition in an Or condition block is True, the condition block is True.
If none of the conditions in an Or condition block are True, the condition block is False.


In this section

Building element visibility logic
Setting model condition types
Model condition type examples
Setting form-level condition types
Form-level condition type examples
Setting offering items condition types