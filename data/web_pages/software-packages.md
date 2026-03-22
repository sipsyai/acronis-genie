# Working with software repositories and software packages

RMM > Managing software > Working with software repositories and software packages
Working with software repositories and software packages

The availability of this feature depends on the license that you have.

With software deployment by using DeployPilot, you can:

Perform fresh software installations on remote devices.

Update custom applications that are not supported by the Vulnerability assessment and Patch management feature. To support this function, the uploaded installer must be preconfigured to support upgrades.

Software packages

Software packages are installer files (.msi or .exe) that you can use to remotely deploy (install or uninstall) software to Windows workloads. To check the supported versions of Windows, see Supported Windows versions.

A software package is defined by the software version and some custom settings, such as language and architecture type.

Software repositories

Software repositories are depots where software packages are stored.

There are two software repositories: Library and My packages.

Library

The Library repository contains 40 of the most frequently used software applications. The content of this repository is predefined and maintained by the system. You can see the complete list of these applications in this knowledge base article.

You cannot edit or delete packages from this repository. Also, you cannot directly deploy a package from here. To deploy a package, you must first add it to the My packages repository.

My packages

The My packages repository contains all software packages that you can deploy and include in software deployment plans. Initially, this repository is empty, even if there are packages in the Library repository. You can add packages to My packages in the following ways:

By adding a package from the Library repository. For more information, see Adding software packages from the library.
By manually uploading a software package. For more information, see Uploading software packages.

After you add a package to My packages, you can deploy it by using a quick deploy action or by including it in a software deployment plan. For more information, see Installing software, Uninstalling software, and Creating a software deployment plan.

DeployPilot distinguishes between packages that were added from the Library repository and manually uploaded packages. For packages that were added from the Library repository, DeployPilot checks before deployment if the software is already installed on the device and, if so, prevents unnecessary reinstallation.

The maximum storage capacity of the My packages repository is 5 GB for customer tenants and 20 GB for partner tenants.

Supported Windows versions

Browsing the software repositories

Adding software packages from the library

Uploading software packages

Editing software packages

Deleting software packages

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.