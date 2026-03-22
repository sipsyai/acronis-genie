# Understanding the detection of bottlenecks

Managing the backup and recovery of workloads and files > Operations with backups > Understanding the detection of bottlenecks
Understanding the detection of bottlenecks

The bottleneck detection feature helps you understand where you can improve performance by highlighting which component in your system was the slowest during a backup or recovery process.

As bottlenecks always occur in any transmission event, it does not necessarily mean they need to be resolved. Your backups may be already fast enough and meet your backup windows perfectly, as well as meet your SLAs, so there is typically nothing you need to actually resolve.

You can easily view and track bottlenecks in the Activity details tab. To do this, in the Cyber Protect console, go to Monitoring > Activities, and then click the relevant activity. For more information about viewing bottlenecks, see Viewing bottleneck details and On what workloads, agents, and backup locations are bottlenecks shown?.

What is a bottleneck?

Bottlenecks are typically caused due to a slow component in the processing chain, in other words, a component that the other components wait for.

The bottleneck detection feature enables you to track these slow components during the backup and recovery process, helping you understand which of the following component types is the slowest:

Source: At a glance, you can determine if the reading speed from the backup/recovery source is causing a bottleneck.
Destination: Understand if the writing speed to the backup/recovery destination is affecting performance.
Agent: Understand if the agent is processing the data fast enough.

The bottleneck type, whether from the source, destination, or agent, can change at different times during the backup/recovery activity. The percentages shown in the Bottleneck section of the Activity details tab below (for example, Read data from source (workload): 63%), represent the percentage of time when this type of bottleneck was encountered. In this case, for 63% of the recovery activity time, the bottleneck type was reading data, in other words, the slow speed in reading data from the backup archive by the agent.

Similarly, for 30% of the time, the bottleneck was due to the slow speed in writing data to the recovery destination (Write data to destination: 30%).

It is normal behavior to see bottleneck statistics in the Activity details tab. These statistics are only available for tasks more than one minute long.
How to reduce bottlenecks

As mentioned above, the bottleneck detection feature highlights the read and write data flow between backup components. The read statistics refer to the data flow from the data source to the agent which performs the backup/recovery operation, and the write statistics refer to the data flow between the agent and the backup archive (the destination).

Тo reduce bottlenecks and improve the read/write data flow performance, you should analyze the channel between the agent and the data source/backup archive. For example, you can try benchmarking your hard disks if the agent is backing up some local files.

Viewing bottleneck details

On what workloads, agents, and backup locations are bottlenecks shown?

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.