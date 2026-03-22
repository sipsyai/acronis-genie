# Creating the transform file and extracting the installation packages

Installing and deploying Cyber Protection agents > Deploying protection agents through Group Policy > Creating the transform file and extracting the installation packages
Creating the transform file and extracting the installation packages

To deploy protection agents via Windows Group Policy, you need a transform file (.mst), and the installation packages (.msi and .cab files).

The procedure below uses the default registration option, which is registration by token. To learn how to generate a registration token, refer to Generating a registration token.

To create the .mst file and extract the installation packages (.msi and .cab files)

Log in as an administrator on any machine in the Active Directory domain.
Create a shared folder that will contain the installation packages. Ensure that domain users can access the shared folder—for example, by leaving the default sharing settings for Everyone.
Run the agent setup program.
Click Create .mst and .msi files for unattended installation.
In What to install, select the components that you want to include in the installation, and then click Done.

In Registration settings, click Specify, enter a registration token, and then click Done.

You can change the registration method from Use registration token (default) to Use credentials or Skip registration. The Skip registration option presumes that you will register the workloads manually later.

Review or modify the installation settings, which will be added to the .mst file, and then click Proceed.
In Save the files to, specify the path to the shared folder that you created.
Click Generate.

As a result, the .mst file, the .msi file, and the .cab files are created and copied to the shared folder that you specified.

Next, set up the Windows Group Policy object. To learn how to do it, refer to Setting up the Group Policy object.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.