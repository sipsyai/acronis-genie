# Compression level

Managing the backup and recovery of workloads and files > Backup options > Compression level
Compression level
This option is not available for cloud-to-cloud backups. Compression for these backups is enabled by default with a fixed level that corresponds to the Normal level below.

The option defines the level of compression applied to the data being backed up. The available levels are: None, Normal, High, Maximum.

The preset is: Normal.

A higher compression level means that the backup process takes more time, but the resulting backup occupies less space. Currently, the High and Maximum levels work similarly.

The optimal data compression level depends on the type of data being backed up. For example, even maximum compression will not significantly reduce the backup size if the backup contains essentially compressed files, such as .jpg, .pdf or .mp3. However, formats such as .doc or .xls will be compressed well.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.