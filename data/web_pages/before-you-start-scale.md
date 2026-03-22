# Before You Start Scale

Installing and deploying Cyber Protection agents > Deploying virtual appliances > Deploying Agent for Scale Computing HC3 (Virtual Appliance) > Before you start
Before you start

This appliance is a pre-configured virtual machine that you deploy in a Scale Computing HC3 cluster. It contains a protection agent that enables you to administer cyber protection for all virtual machines in the cluster.

System requirements for the agent

By default, the virtual machine with the agent uses 2 vCPUs and 4 GiB of RAM. These settings are sufficient for most operations but you can change them by editing the virtual machine in the Scale Computing HC3 web interface.

To improve the backup performance and avoid failures related to insufficient RAM memory, we recommend that you increase these resources to 4 vCPUs and 8 GiB of RAM in more demanding cases. For example, increase the assigned resources when you expect the backup traffic to exceed 100 MB per second (for example, in 10-Gigabit networks) or if you back up simultaneously multiple virtual machines with large hard drives (500 GB or more).

The size of the appliance virtual disk is about 9 GB.

How many agents do I need?

One agent can protect the entire cluster. However, you can have more than one agent in the cluster if you need to distribute the backup traffic bandwidth load.

If you have more than one agent in a cluster, the virtual machines are automatically evenly distributed between the agents, so that each agent manages a similar number of machines.

Automatic redistribution occurs when the load imbalance among the agents reaches 20 percent. This may happen after you add or remove a machine or an agent. For example, you realize that you need more agents to help with throughput and you deploy an additional virtual appliance to the cluster. The management server will assign the most appropriate machines to the new agent. The old agents' load will reduce. When you remove an agent from the management server, the machines assigned to the agent are redistributed among the remaining agents. However, this will not happen if an agent gets corrupted or is deleted manually from the Scale Computing HC3 cluster. Redistribution will start only after you remove such an agent from the Cyber Protect console.

To check which agent manages a specific machine

In the Cyber Protect console, click Devices, and then select Scale Computing.
Click the gear icon in the upper right corner of the table, and under System, select the Agent check box.
Check the name of the agent in the column that appears.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.