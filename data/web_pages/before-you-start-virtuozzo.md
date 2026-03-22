# Before You Start Virtuozzo

Installing and deploying Cyber Protection agents > Deploying virtual appliances > Deploying Agent for Virtuozzo Hybrid Infrastructure (Virtual Appliance) > Before you start
Before you start

This appliance is a pre-configured virtual machine that you deploy in Virtuozzo Hybrid Infrastructure. It contains a protection agent that enables you to administer cyber protection for all virtual machines in a Virtuozzo Hybrid Infrastructure cluster.

To ensure that backups with enabled Volume Shadow Copy Service (VSS) for virtual machines backup option run properly and capture data in application-consistent state, verify that Virtuozzo Guest Tools are installed and up-to-date on the protected virtual machines.
System requirements for the agent

When deploying the virtual appliance, you can choose between different predefined combinations of vCPUs and RAM (flavors). You can also create your own flavors.

2 vCPUs and 4 GB of RAM (medium flavor) are optimal and sufficient for most operations. To improve the backup performance and avoid failures related to insufficient RAM memory, we recommend that you increase these resources to 4 vCPUs and 8 GB of RAM in more demanding cases. For example, increase the assigned resources when you expect the backup traffic to exceed 100 MB per second (for example, in 10-Gigabit networks) or if you back up simultaneously multiple virtual machines with large hard drives (500 GB or more).

How many agents do I need?

One agent can protect the entire cluster. However, you can have more than one agent in the cluster if you need to distribute the backup traffic bandwidth load.

If you have more than one agent in a cluster, the virtual machines are automatically evenly distributed between the agents, so that each agent manages a similar number of machines.

Automatic redistribution occurs when the load imbalance among the agents reaches 20 percent. This may happen after you add or remove a machine or an agent. For example, you realize that you need more agents to help with throughput and you deploy an additional virtual appliance to the cluster. The management server will assign the most appropriate machines to the new agent. The old agents' load will reduce. When you remove an agent from the management server, the machines assigned to the agent are redistributed among the remaining agents. However, this will not happen if an agent gets corrupted or is deleted manually from the Virtuozzo Hybrid Infrastructure node. Redistribution will start only after you remove such an agent from the Cyber Protection web interface.

To check which agent manages a specific machine

In the Cyber Protect console, click Devices, and then select Virtuozzo Hybrid Infrastructure.
Click the gear icon in the upper right corner of the table, and under System, select the Agent check box.
Check the name of the agent in the column that appears.
Limitations
Virtuozzo Hybrid Infrastructure appliance cannot be deployed remotely.
Application-aware backup of virtual machines is not supported.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.