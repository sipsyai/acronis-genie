# Using a system administrator account

Installing and deploying Cyber Protection agents > Deploying virtual appliances > Deploying Agent for Virtuozzo Hybrid Infrastructure (Virtual Appliance) > Using a system administrator account
Using a system administrator account

With the system administrator account, the virtual appliance can back up and recover all virtual machines in the Virtuozzo Hybrid Infrastructure domain.

For more information about domains and projects, see Multitenancy in the Virtuozzo Hybrid Infrastructure documentation.

Prerequisite

You must be able to connect to the Virtuozzo Hybrid Infrastructure cluster by using the OpenStack Command-Line Interface. For more information, see Connecting to OpenStack command-line interface in the Virtuozzo Hybrid Infrastructure documentation.

To use the system administrator account

Connect to the Virtuozzo Hybrid Infrastructure cluster by using the OpenStack Command-Line Interface, and then run the following script to create an environment file for the system administrator.

su - vstoradmin
kolla-ansible post-deploy
exit


Use the environment file to authorize further OpenStack commands.

. /etc/kolla/admin-openrc.sh


Create an administrator account in the Default domain.

openstack --insecure user set --project admin --project-domain Default --domain Default <user name>


Here and below, <user name> is the Virtuozzo Hybrid Infrastructure account. The virtual appliance will use this account in order to back up and recover the virtual machines in any child project in the Default domain.

Assign the admin role to the account.

openstack --insecure role add --domain Default --user <user name> --user-domain Default admin --inherited

Allow the account to access additional domains in the Virtuozzo Hybrid Infrastructure.

openstack --insecure role add --domain <domain name> --inherited --user <user name> --user-domain Default admin

Here, <domain name> is the domain to which this account will have access. If the domain name contains spaces, enclose the name in quotation marks.

Repeat this step for each additional domain that you want to make accessible.

Check the roles that are assigned to the account.

openstack --insecure role assignment list --user <user name> --names

Check the effective roles of the account.

The effective roles include assigned roles, inherited roles, and implied roles.

openstack --insecure role assignment list --user <user name> --names --effective
Examples
Granting access to the Default domain
Granting access to the Default and an additional domain
Checking the assigned roles
Checking the effective roles
su - vstoradmin
kolla-ansible post-deploy
exit
. /etc/kolla/admin-openrc.sh
openstack --insecure user set --project admin --project-domain Default --domain Default johndoe
openstack --insecure role add --domain Default --user johndoe --user-domain Default compute --inherited
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.