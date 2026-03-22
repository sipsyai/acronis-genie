---
title: "group alignment"
source: "https://developer.acronis.com/doc/cyberapps/versions/ui-builder/build-form/selecting-elements/layout-management/group/alignment.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:05:57.182307"
---

# group alignment

Aligning group contained elements

Note
UI builder uses standard CSS terminology and concepts for group contained elements alignment.

The alignment of the contained elements in a group container element depends on the Justify and Align properties:



The Align property is analogous with the CSS align-content property: it sets the distribution of space between and around contained elements along the cross axis.
For more information, see the developer.mozilla.org page on ``align-content``.



The Justify property is analogous with the CSS justify-content property: it sets the distribution of space between and around contained elements along the main axis
For more informatrion, see the developer.mozilla.org page on ``justify-content``.





Note
For more information on CSS axis definitions and explanations, see the developer.mozilla.org page discussing the main axis and the developer.mozilla.org page discussing the cross axis.

Whether the main and cross axes are vertical or horizontal depends on the Mode property:


When the Mode property is set to Column, the main axis is vertical, and the cross axis is horizontal.
When the Mode property is set to Row, the main axis is horizontal, and the cross axis is vertical.


Therefore, alignment is controlled as follows:


When the Mode property is set to Column, Justify controls the vertical axis and Align controls the horizontal axis.
When the Mode property is set to Row, Justify controls the horizontal axis and Align controls the vertical axis.



Alignment property options


Justify content
When Mode = Column, this property has no effect.
See examples for Mode=Row



Default
Start
Center
End
Space between - distribute the group contained elements evenly.
Space - distribute the group contained elements evenly, including spaces to the left and right.




Align items
See examples for Mode=Column
See examples for Mode=Row



Default
Start
Center
End






Examples

Mode = Column : Align item examples
Since Mode = Column, Align items controls the horizontal positioning of the contained elements.



Mode = Row : Justify content examples
Since Mode = Row, Justify content controls the horizontal positioning of the contained elements.



Mode = Row : Align items examples
Since Mode = Row, Align items controls the vertical positioning of the contained elements.