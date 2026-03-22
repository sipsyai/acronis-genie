# Using a project administrator account

Installing and deploying Cyber Protection agents > Deploying virtual appliances > Deploying Agent for Virtuozzo Hybrid Infrastructure (Virtual Appliance) > Using a project administrator account
Using a project administrator account

With this account, the virtual appliance will be able to back up and recover only the virtual machines in the project in which the account is created. No information about other projects in the domain will be available to the virtual appliance.

If you want to protect multiple projects, you must deploy a separate virtual appliance for each project.

Each virtual appliance must use a separate project administrator account that is created in the corresponding project. The appliance can be deployed anywhere in the Virtuozzo Hybrid Infrastructure cluster, even outside the protected project.

You can use the project administrator account only with Virtuozzo Hybrid Infrastructure 6.2 and later.

For more information about domains and projects, see Multitenancy in the Virtuozzo Hybrid Infrastructure documentation.

Prerequisite

You must be able to connect to the Virtuozzo Hybrid Infrastructure cluster by using the OpenStack Command-Line Interface. For more information, see Connecting to OpenStack command-line interface in the Virtuozzo Hybrid Infrastructure documentation.

To use the project administrator account

In the admin panel of Virtuozzo Hybrid Infrastructure, go to Settings > Projects and users.

Choose a domain and create a project in it.

In the same domain, create a user account. Assign the Project member role to this account, select the Image uploading check box, and then assign the user to the project that you created.

In the command-line interface, the Project member role is called project_admin.

Connect to the Virtuozzo Hybrid Infrastructure cluster by using the OpenStack Command-Line Interface.

Run the following script to create an environment file.

su - vstoradmin
kolla-ansible post-deploy
exit


Use the environment file to authorize further OpenStack commands.

. /etc/kolla/admin-openrc.sh

Assign the compute role to the user account that you created in the admin panel.

openstack --insecure role add --project <project name> --user <user name> --project-domain <project domain name> --user-domain <user domain name> compute

Here and below, <project name> is the name of the project, <user name> is the Virtuozzo Hybrid Infrastructure account, <project domain name> is the parent domain of the project, and <user domain name> is the parent domain of the user account.

If a name contains spaces, enclose it in quotation marks.

Assign the quota_manager role to the account.

openstack --insecure role add --project <project name> --user <user name> --project-domain <project domain name> --user-domain <user domain name> quota_manager

Check the roles that are assigned to the account.

openstack --insecure role assignment list --names --user <user name> --user-domain <user domain name>

Check the effective roles of the account.

The effective roles include assigned roles, inherited roles, and implied roles.

openstack --insecure role assignment list --names --effective  --user <user name> --user-domain <user domain name>
Examples

In the examples, the user account is johndoe and the project is Project A. Both the user account and the project are created in Domain A.

Assigning roles
Checking the assigned roles
Checking the effective roles
su - vstoradmin
kolla-ansible post-deploy
exit
. /etc/kolla/admin-openrc.sh
openstack --insecure role add --project "Project A" --user johndoe --project-domain "Domain A" --user-domain "Domain A" compute
openstack --insecure role add --project "Project A" --user johndoe --project-domain "Domain A" --user-domain "Domain A" quota_manager
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.