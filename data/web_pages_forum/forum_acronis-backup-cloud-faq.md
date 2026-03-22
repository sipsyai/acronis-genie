# Acronis Backup Cloud: FAQ

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/acronis-backup-cloud-faq

## Original Post
**Author:** Unknown

Acronis Backup Cloud: FAQ

        
  



    
  


  
              
          
        Thread needs solution      
      
      





    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Anna Trifonova [Inactive]
                            

                            
                    
                        Forum Star
                    
                
            
                        
                
                    Posts: 121
                
            
            
                
                    Comments: 2663
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Installation
Do clients update automatically?
Automatic update is to be implemented in the next release. Nor are there automatic notifications about the update. Currently, you have to manually run the setup program of the new version and click "Update"
 How can I change the credentials of the backup account under which the backup client is installed?
Run the setup program again, click Install Backup Client, and then click Modify. Specify the new credentials when asked about the login and password.
  When installing the backup client, should I create a new Windows user account for the service or use an existing one?
In most cases, keep the default option of creating a new account. You only need to specify an existing account in two cases: if the machine is a domain controller, or if you are installing Client for Hyper-V on a failover cluster node (you need to provide the same account on all nodes of the cluster, so that each client can back up virtual machines that migrate between nodes).
  I have installed the backup client from an .msi file instead of the GUI-based setup program. How can I specify the backup account for it?
With the backup client installed, please go to the C:\Program Files (x86)\BackupClient\BackupAndRecovery folder and run the register_msp_mms.exe tool as follows:
register_msp_mms.exe register “https://baas.acronis.com” “<your email address> “<your password>”
Note the quotation marks around each of the parameters. When specifying the password, ensure that you escape certain special characters according to http://www.robvanderwoude.com/escapechars.php (for example, if the password contains a % sign, specify %% instead). The @ sign in the email address need not be escaped.
 The Acronis Backup Cloud Admin Guide states that Windows 7 Home and Starter Editions are not supported by BaaS. Is that actually the case?
That is correct, these systems are unsupported both by Acronis Backup Cloud backup client and Acronis Backup Advanced backup agents.
 Can the agent for Acronis Backup Cloud and the regular Acronis backup agent (including Acronis True Image) live together on the same machine?
The agents cannot be installed alongside each other. The reason is that the BaaS client is in a way a customized version of the ABA backup agent, and installing them both is somewhat similar to installing two copies of the same program, with resulting conflicts in accessing resources and services.
  Why does Acronis Storage require DHCP servers to be installed?
Current Acronis Storage requires DHCP mostly due to the way how product simplifies building HA and update procedure from version to version without deep IT staff involvement. We suggest to build private VLAN with internal DHCP enabled between the VMs which are used to run Acronis Storage.
  How are BaaS agents uninstalled from the systems once loaded?
On a Windows machine use Add or Remove Programs in Control Panel.  For Client for Linux, run these two commands as the root user (or by using sudo):
/usr/lib/Acronis/BackupAndRecovery/uninstall/uninstall
rm -rf /usr/src/snapapi*"
  Client machines are in a private network behind NAT. Will they be able to communicate with the management part placed at Acronis or at the service provider?
Yes, the client machines will be able to communicate with the management part.
Setup
 Which ports need to be open?
TCP ports 443, 44445, and 55556 (used in Acronis Backup Advanced and inherited by Acronis Backup Cloud), in addition: 80, 7770, 7786, 7787, and 8443 (Acronis Backup Cloud-specific). Future releases may use other ports from the range 7770–7800. You can use this tool to verify that verifies that all the necessary ports are open: Acronis Backup Cloud: Connection Verification Tool.
  Are there maintenance hours when I can expect being unable to access the service?
The BaaS team reserves the time interval from 6:00am until 7:00am UTC every Tuesday for maintenance operations. These operations include delivering service updates.
  I have problems working with the service by using Internet Explorer 9. Is this a supported browser?
No. The currently supported browsers are: Internet Explorer 10 , Safari 5.1.7, Mozilla Firefox 23, Google Chrome 29, Opera 16, or their later versions.
Backup
 Can I back up databases such as Microsoft SQL Server?
Yes, Backup clients use Microsoft Volume Shadow Copy Service to back up applications, including SQL Server, in a consistent state. A further release of Acronis Backup Cloud will include dedicated backup clients for Microsoft Exchange, Microsoft Active Directory, Microsoft SQL Server, and Microsoft SharePoint to provide granular restore options.
 Can I back up databases inside virtual machines?
Backup clients for VMware and Hyper-V back up the virtual machines in a consistent state, provided that VMware Tools (for VMware) or Integration Tools (for Hyper-V) are running on the machine.
  Is there a way to limit network usage for backups?
Yes, bandwidth limitation is an option of each backup plan.
Recovery
Is it possible to do file-level recovery from the (image) backups in the local storage?
Yes, it is possible
Billing
 If a virtual machine is running with a Workstation operating system (WinXP/7/8), is it considered a Workstation or VM in the billing?
A virtual machine is considered a virtual machine regardless of the operating system it runs and regardless of whether it is backed up by a client installed inside or agentlessly.
  If a physical Linux machine is running a Desktop/Workstation OS, is it considered a workstation or server in the billing?
Any physical machine running Linux is considered a server machine.
Third-party integration
 Are there plans to integrate Acronis Backup Cloud with PSAs such as ConnectWise and Kaseya?
There is no such point in the roadmap yet. We will be tracking such requests and plan accordingly.
A current solution is to use the API provided by Acronis Backup Cloud to integrate the product with your third-party software.
 Is Acronis Backup Cloud integrated with Parallels Automation?
Yes, via an APS package. We have packages for two APS versions: APS 2.0 and APS 1.2

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 03/16/2015 - 11:00

                                                          
                                                            
                                                                                        
    
                    
                Anna Trifonova

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials.

 

Check our Corporate and Consumer Handbooks and Online Documentation for help on managing your account, products and support.

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful
