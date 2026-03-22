# Types of conversion to virtual machine

Working with plans > Off-host data protection plans > Conversion to a virtual machine > Types of conversion to virtual machine
Types of conversion to virtual machine

When you convert a backup to a virtual machine, you can choose one of the following conversion types:

Save the resulting virtual machine as a set of files

With this option, the conversion process creates one or more virtual disk files without requiring access to a hypervisor. You can save the files to a local or network folder and, later, manually use them on a hypervisor.

The resulting files depend on the selected type, as follows:

VMware Workstation creates VMDK files

VHDX files creates VHDX and VMX files

The following table shows which agents you can use to create a virtual machine as a set of files.

Conversion to a virtual machine

(as a set of files)

Agent that performs conversion
Agent for VMware	Agent for Hyper-V	Agent for Windows	Agent for Linux
VMware Workstation

+



+



+



+


VHDX files

+



+



+



+

With this conversion type, each conversion recreates the virtual machine from scratch.

Cyber Protect temporarily renames the existing machine, and then creates a new virtual machine with the original name. If conversion is successful, the old machine is deleted. If conversion fails, the old machine is restored. Additional temporary storage is required, because both an old and a new machines exist during processing.

Create the resulting virtual machine directly on a virtualization server

With this option, the conversion process creates a virtual machine directly on the selected virtualization server. Unlike conversion as a set of files, this method supports incremental updates.

During the first conversion, Cyber Protect creates a new virtual machine.

For subsequent conversions:

If no full backup has occurred since the last conversion, an incremental update is performed, and only changed data are transferred to the virtual machine. Incremental updates are faster and reduce network and CPU usage on the host that is used for this conversion.
If a full backup has occurred, or if an incremental update is not possible (for example, due to missing intermediate snapshots), the virtual machine is created from scratch.

This approach avoids temporary duplication of full virtual machines, and minimizes processing overhead when incremental updates are available.

The following table shows which agents you can use to create a virtual machine on a specific type of virtualization server.

Conversion to a virtual machine	Agent that performs conversion
Agent for VMware	Agent for Hyper-V	Agent for Scale Computing HC3

Agent for Virtuozzo Hybrid Infrastructure

Agent for Proxmox
VMware ESXi

+



–

–	–	–
Microsoft Hyper-V

–



+

–	–	–
Scale Computing HC3	–	–	+	–	–


Virtuozzo Hybrid Infrastructure

–	–	–	+	–
Proxmox	–	–	–	–	+
Intermediate snapshots

To enable incremental updates of the resulting virtual machine, Cyber Protect stores an intermediate snapshot named Replica. This snapshot captures the state of the virtual machine after the most recent successful conversion. You can revert the virtual machine to this snapshot if you want to discard any subsequent changes, and return to the last converted state.

For conversions to Scale Computing HC3 virtual machines, an additional snapshot named Utility Snapshot is created. This snapshot is used only by Cyber Protect and must remain intact to ensure proper operation.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.