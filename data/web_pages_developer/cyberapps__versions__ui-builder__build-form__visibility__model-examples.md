---
title: "Model condition type examples"
source: "https://developer.acronis.com/doc/cyberapps/versions/ui-builder/build-form/visibility/model-examples.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:06:49.213702"
---

# Model condition type examples

Model condition type examples

In these examples, the visibility of a button is controlled by Model condition types for three input elements.
A second button with no visibility conditions is included as a contrast.


Note
Here, we are demonstrating visibility control through user input. A data initializer callback or input parameter mapping from a parent form can assign values to elements, and the visibility logic would apply without user interaction.


Example 1

Button1 is only visible when all three input elements are not null. If one field is null, Button1 is not visible.
For this, we use an And as the Condition block modifier.


Note
Button1 becomes visible as soon as the first letter of the email is typed. Model condition type does not check the validity of the email field contents.


The logic is:
IF (FirstName <> NULL AND SecondName <> NULL AND Email <> NULL) THEN Button1.Visible = TRUE




Example 2

Button1 is visible when any of the three input elements is not null. If all are null, Button1 is not visible.
For this, we use an Or as the Condition block modifier. Notice that the conditions are identical to Example 1. All we had to do was change the Condition block modifier from And to Or.


Note
In this example, we demonstrate the dynamic nature of visibility logic by deleting all the field content to show Button1 becoming not visible again.


The logic is:
IF (FirstName <> NULL OR SecondName <> NULL OR Email <> NULL) THEN Button1.Visible = TRUE




Example 3

In this sightly more complex example, Button1 becomes visible when both the FirstName and SecondName elements are not null or the Email element is not null.
For this, we must define two blocks: one for the name elements conditions and one for the Email element condition, and combine them within a parent block with an Or condition block modifier.

The logic is:
IF ((FirstName <> NULL AND SecondName <> NULL) OR Email <> NULL) THEN Button1.Enabled = TRUE




Example 4

In this example, Button1 becomes visible when any of the input elements is not null, as in example 2, above.
However, Button1 is enabled only when all three input elements are not null.
For this, we must define two dependencies: one for the Visible state and one for the Enabled state .

The logic is:
IF (FirstName <> NULL OR SecondName <> NULL OR Email <> NULL) THEN Button1.Visible = TRUE
IF (FirstName <> NULL AND SecondName <> NULL AND Email <> NULL) THEN Button1.Enabled = TRUE