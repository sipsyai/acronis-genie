---
title: "Custom Content Detectors"
section: "Data Loss Prevention"
subsection: "Custom Content Detectors"
page_range: "1474-1477"
tags: [dlp, content-detectors, file-type, keywords, pattern, regex, complex-detector, data-classifiers]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#advanced-dlp-custom-content-detectors.html"
---

# Custom Content Detectors

Content detectors provide the ability to centrally define types of content for which access control is desired. Content detectors specify content filtering criteria for identifying data to which content-aware rules should be applied.

## File Type Content Detector

### To Create a File Type Content Detector

1. Log in to the Cyber Protect console as an administrator.
2. Navigate to **Protection** > **Data Loss Prevention** > **Data classifiers**.
3. Click **Content detectors**. The list of content detectors opens.
4. In the upper-right corner of the window, click **Add new**.
5. In the dropdown list, select **File type**.
6. Configure the content detector:
   a. Enter a name and description for the content detector.
   b. (Optional) Select a sensitivity category from the list.
   c. In the **Supported file types** list, click the plus icon to move the selected type to the **Selected file types** list. By clicking a "plus" icon to the right of the supported file type you will move it to the Selected file types list. You can also select multiple supported file types by clicking on the checkmarks next to their names and then using **Add selected** button in the upper-right corner.
   d. To remove a file type from the **Selected file types** list, click on the trashcan icon to the right of its name. You can also remove multiple file types using the check boxes and **Remove selected** button.
7. In the lower-right corner, click **Save**.

## Keywords Content Detector

### To Create a Keywords Content Detector

1. Log in to the Cyber Protect console as an administrator.
2. Navigate to **Protection** > **Data Loss Prevention** > **Data classifiers**.
3. Click **Content detectors**. The list of content detectors opens.
4. In the upper-right corner of the window, click **Add new**.
5. In the dropdown list, click **Keywords**.
6. Configure the content detector:
   a. Enter keywords manually, one at a time, or import them from a CSV or TXT file. Each keyword or phrase in the file must be specified on a new line. After successfully importing the keywords, you can either merge the new keywords with the existing list or replace the existing list with the imported keywords.
   b. Configure if the content detector should match all keywords from the list, any keyword from the list, or a custom number of keywords.
7. In the lower-right corner, click **Save**.

## Pattern Content Detector

### To Create a Pattern Content Detector

1. Log in to the Cyber Protect console as an administrator.
2. Navigate to **Protection** > **Data Loss Prevention** > **Data classifiers**.
3. Click **Content detectors**. The list of content detectors opens.
4. In the upper-right corner of the window, click **Add new**.
5. In the dropdown list, click **Pattern**.
6. Configure the content detector:
   a. **Name** -- Specify the name of the group.
   b. **Description** -- Specify a description for the group.
   c. **Regular expression** -- enter a regular expression.
   d. **Validate** -- Check the syntax of the regular expression.
   e. **Check now** -- Enter test strings and view the result. DLP supports real-time color highlighting of test results. All matches are highlighted.
   f. **Validation** -- When configured to perform validation, the group detects a match only in case of a match to the selected validation type in addition to the expression specified. To match the group, data needs to match the expression and additionally pass the validation. If **No validation** is selected, the group does not perform validation -- data only needs to match the expression specified. To configure validation, select the desired type from the drop-down list in this field.
   g. **Minimum matches count** -- enter the number of matches that will trigger the content inspection rule.

   > **Important:** The detector checks for an exact match no more than the first megabyte of the content provided for inspection. If the content exceeds 1MB, the rule with the **Exact match** condition is not triggered even if the first megabyte of the content matches the regular expression of the detector.

   h. **Case sensitive** -- When this check box is selected, the group distinguishes between lowercase and uppercase characters. For example, the words `Term` and `term` will be treated differently, so the group can be configured to match the word `Term` but not `term`. When this check box is cleared, the group does not differentiate between uppercase and lowercase characters.
   i. **Count identical matches as one match** -- Combine duplicate matches returned by the regular expression into a single match.
7. In the lower-right corner, click **Save**.

## Complex Content Detector

### To Create a Complex Content Detector

1. Log in to the Cyber Protect console as an administrator.
2. Navigate to **Protection** > **Data Loss Prevention** > **Data classifiers**.
3. Click **Content detectors**. The list of content detectors opens.
4. In the upper-right corner of the window, click **Add new**.
5. In the dropdown list, click **Complex**.
6. Configure the content detector. Complex content detector allows you to create logical combinations of two or more content detectors. You can browse through the database of available detectors and combine them using logical operators AND, OR, and NOT.
7. In the lower-right corner, click **Save**.

## Cloning an Existing Content Detector

Instead of creating a new content detector from scratch, you can also clone an existing built-in or custom content detector and adjust its parameters.

1. In the list of content detectors, select the one that you want to clone, and then click **Clone** from the dropdown list at the end of its row.
2. Edit the cloned content detector to add or remove parameters as needed and click **Done** to save your changes.

> **Note:** Cloning a built-in content detector creates a custom content detector.
