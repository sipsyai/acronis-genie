---
title: "Copying and pasting elements"
source: "https://developer.acronis.com/doc/cyberapps/versions/ui-builder/build-form/copy-paste.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:04:30.337855"
---

# Copying and pasting elements

Copying and pasting elements
You can use keyboard shortcuts to cut and paste elements on a single form, across related forms, across extension points in the same CyberApp, or even across CyberApps.
The copy and paste functionality works for individual elements; for containers, such as groups, tables, tooltips, etc.; and for the entire contents of a form.
When you copy and paste an element, all settings are also copied, incuding the element name. Therefore, you should change the name of the copied element and any nested child elements. Otherwise, the pasted elements will act as clones of the original.

To copy and paste elements


Select an element on the canvas.
You can select individual elements container elements, or the form itself.


Note
If you select a form, you will not copy the form, only the elements contained in the form.


Copy your selection by pressing Ctrl+C (Windows/Linux) or Command-C (macOS).

Select the target element on the form.
When you paste an element, its location depends on the selected target element.


If you select a target that is a simple element, the copied element is pasted right after the selected element.
If you select a target that is a container element, the copied element is pasted inside that container, as the final child element. To locate the pasted element in a specific location within a target element, select the child element immediately before the desired location.


Note
Tables are an exception to the container rule. If a table is the selected target element when you paste, the element is pasted under the table (not inside it). This is because UI Builder does not know which column to paste into.





Paste the element by pressing Ctrl+V (Windows/Linux) or Command-V (macOS).



Cutting elements and undo
You can also cut an element, by pressing Ctrl+X (Windows/Linux) or Command-X (macOS). You can then paste the cut element, as you would a copied element.
If you cut an element by mistake, you can undo the cut by pressing Ctrl+Z (Windows/Linux) or Command-Z (macOS).

Note
Undo works only until you make another change in the form. If you cut elements and then change the form structure, you will not be able to undo the cut.



Copy and paste via a text editor
When you copy an element (including a container element with nested child elements) you are actually copying its JSON representation. This means that you can paste the JSON into a text editor, edit it, and then paste the modified JSON.
In this way, you can create a library of element JSON to reuse over multiple forms, extension points or CyberApps.