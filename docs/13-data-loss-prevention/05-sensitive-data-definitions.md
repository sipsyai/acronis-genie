---
title: "Sensitive Data Definitions"
section: "Data Loss Prevention"
subsection: "Sensitive Data Definitions"
page_range: "1465-1471"
tags: [dlp, sensitive-data, phi, pii, pci-dss, confidential, content-detection, logical-expressions, keywords]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#advanced-dlp-sensitive-data-definitions.html"
---

# Sensitive Data Definitions

This topic describes the logic of identifying sensitive data during content analysis. To reduce the number of false positives, identical matches are counted as one match for all groups of the described logical expressions.

> **Important:** The logical expressions used for content identification are provided for information only and do not describe the solution in full detail.

## Protected Health Information (PHI)

### Supported Languages

US, UK, English-International, Finnish, Italian, French, Polish, Russian, Hungarian, Norwegian, Spanish.

### Data Considered Protected Health Information

- First names and last names
- Address (street, city, county, precinct, zip code, and their equivalent geocodes)
- Phone numbers
- Email addresses
- Social security numbers
- Health plan beneficiary numbers
- Bank account numbers
- URLs
- IP address numbers
- ICD-10-CM codes
- ICD-10-PCS-and-GEMs
- HIPAA
- Other health-care related
- Credit card numbers

### Logical Expression Used for Content Detection

The logical expression consists of strings joined by the logical operator OR. The OR operator is used to join different data groups if the AND logical operator is not specified explicitly. The numbers in brackets represent the number of detected instances that would return a positive detection result.

- Social Security Numbers (5)
- (First names and Last names (3) OR Address (3) OR Phone Numbers (3) OR Email Address (3) OR Bank Account Numbers (3) OR Credit Card Numbers (3)) AND (Social security Numbers (3) OR Health plan beneficiary Numbers (3) * OR ICD-10-CM codes (3) OR ICD-10-PCS-and-GEMs (3) OR HIPAA (3) OR * Other Health-care related (3))

## Personally Identifiable Information (PII)

### Supported Languages

US, UK, English-International, Bulgarian, Chinese, Czech, Danish, Dutch, Finnish, French, German, Hungarian, Indonesian, Italian, Korean, Malay, Norwegian, Polish, Portuguese (Brazil), Portuguese (Portugal), Romanian, Russian, Serbian, Singapore, Spanish, Swedish, Taiwan, Turkish, Thai, Japanese.

### Data Considered Personally Identifiable Information

- First names and last names
- Address (street, city, county, zip code)
- Bank account numbers
- Personal and fiscal ID numbers
- Passport numbers
- Social security numbers
- Phone numbers
- Car plate numbers
- Driving license numbers
- Identifiers and serial numbers
- IP addresses
- Email addresses
- Credit card numbers

### Logical Expression for All Supported Languages Except Japanese

The logical expression consists of strings joined by the logical operator OR or AND. The numbers in brackets represent the number of detected instances that would return a positive detection result.

- Personal and fiscal ID numbers (5)
- First names and Last names (3) AND (Credit Card Number (3) OR Social Security Number (3) OR Bank Account Number (3) OR Personal and fiscal ID numbers (3) OR Driving license numbers (3) OR Passport Numbers (3) OR Social security numbers (3) OR IP Addresses (3) OR Car plate numbers (3) OR Identifiers and serial numbers)
- Phone Numbers (3) AND (Credit Card Number (3) OR Social Security Number (3) OR Bank Account Number (3) OR Address (3) OR Personal and fiscal ID numbers (3) OR Driving license numbers (3) OR Passport Numbers (3) OR Social security numbers (3) OR Car plate numbers (3) OR Identifiers and serial numbers (3))
- (First names and Last names (30) OR Address (30)) AND (Email Addresses (30) OR Phone Numbers (30) OR IP Addresses (30))
- Email Addresses (3) AND (Credit Card Number (3) OR Social Security Number (3) OR Bank Account Number (3) OR Personal and fiscal ID numbers (3) OR Driving license numbers (3) OR Passport Numbers (3) OR Social security numbers (3) OR Car plate numbers (3) OR Identifiers and serial numbers (3))
- Email Address (30) AND (Address (30) OR Phone Numbers (30))
- First names and Last names (30) AND Address (30)
- Phone Numbers (30) AND Address (30)
- First names and Last names (3) AND Bank Account Numbers (3)
- Phone Numbers (3) AND (Credit Card Number (3) OR Bank Account Number (3) OR Social security numbers (3) OR Personal and fiscal ID numbers (3) OR Driving license numbers (3) OR Passport Numbers (3))

### Logical Expression for Japanese

Only unique matches are counted by content detection. The logical expression consists of strings joined by the logical operator OR. The operator OR is used to join different groups if logical operator AND is not explicitly specified.

- Social security numbers (5)
- First names and Last names (3) AND (Credit Card Number (3) OR Bank Account Number (3) OR Driving license numbers (3) OR Passport Numbers (3) OR Social security numbers (3))
- First names and Last names (30) AND (Email Addresses (30) OR Phone Numbers (30) OR IP Addresses (30) OR Address (30))
- Address (3) AND (Credit Card Number (3) OR Bank Account Number (3) OR Driving license numbers (3) OR Passport Numbers (3) OR Social security numbers (3))
- Email Address (3) AND (Credit Card Number (3) OR Bank Account Number (3) OR Social security numbers (3) OR Driving license numbers (3))
- Address (5) AND (Email Address (5) OR First names and Last names (5) OR Phone Numbers (5) OR IP Addresses (5))
- First names and Last names (3) AND Bank Account Numbers (3)
- Phone Numbers (3) AND (Credit Card Number (3) OR Bank Account Number (3) OR Address (3) OR Social security numbers (3) OR Driving license numbers (3))

## Payment Card Industry Data Security Standard (PCI DSS)

### Supported Languages

This sensitivity group is language-independent. The PCI DSS data is in English in all countries.

### Data Considered PCI DSS

- **Cardholder data:** Primary Account Number (PAN), Cardholder Name, Expiration date, Service code
- **Sensitive Authentication Data:** Full track data (magnetic-stripe data or equivalent on a chip), CAV2/CVC2/CVV2/CID, PINs/PIN blocks

### Logical Expression Used for Content Detection

- Credit Card Number (5)
- Credit Card Number (3) AND (American Name (Ex) (3) OR American Name (3) OR PCI DSS Keywords (3) OR Date (month/year) (3))
- Credit Card Dump (5)

## Marked as Confidential

Data marked as confidential is detected through keywords group. The Match condition is weight-based, and every word has weight == 1. The content detection is considered positive when Match if weight > 3.

### Supported Languages

English, Bulgarian, Chinese Simplified, Chinese Traditional, Czech, Danish, Dutch, Finnish, French, German, Hungarian, Indonesian, Italian, Japanese, Korean, Malay, Norwegian, Polish, Portuguese - Brazil, Portuguese - Portugal, Russian, Serbian, Spanish, Swedish, Turkish.

### Keyword Groups

The keyword group for each language contains the country-specific equivalents of the following keywords that are used for the English language (case-insensitive):

- confidential
- internal distribution
- not for distribution
- do not distribute
- not for public
- not for external distribution
- for internal use only
- highly qualified documentation
- private
- privileged information
- for internal use only
- for official use only
