# Support Digest: February-March 2018

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/digests-and-support-best-practices/support-digest-february-march-2018

## Original Post
**Author:** Unknown

Support Digest: February-March 2018

        
  



    
  


  
          





    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Vyacheslav Bykov
                            

                            
                    
                        Cloud SP Trainer
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 10
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello Colleagues!
Let me introduce to you the digest for February & March. In past two months, we have introduced several releases of Acronis Backup Cloud agent and Cloud software components with multiple fixes and improvements. You may perform a centralized update of all client machines using the live update feature. Here's what we have in the list to review:
Hot topics
New KB articles
New training materials
Datacenter and agent updates
Release notes and documentation
 
Hot topics
A big number of questions asked by Partners in February was related to URL branding of Acronis Backup Cloud's portal. Let’s review the prerequisites and necessary steps for this procedure. In addition, we will cover three more popular topics: automatic update of backup clients, dealing with “orphan” backup plans running on the machines in background and retention rules policies.
  #1 ► Branding Web Console URL
Instead of standard one - https://cloud.acronis.com - Acronis Backup Cloud provides a possibility for Partners to use their own URL to access Web Console. This feature is scalable, e.g. if the Partner has another Partner group under him,  the child Partner will also be able to customize the URL for his customers. Branding is performed by Acronis Datacenter team. There are two prerequisites needs to be met prior to contacting support:
Partner should register a DNS name he's going to use for accessing and create a CNAME that would resolve DNS name into default Acronis Backup Cloud's Web Console's URL.
Partner needs to generate a SSL certificate for his DNS name and get it signed by a certificate authority.
Once all preparations are done, Partner raises a support request with Acronis Service Providers support for further assistance (support page) sharing the following details:
The desired domain name
Certificate file in  .pem or .pfx format (+ password)
The name of your group in Acronis Backup Cloud and the datacenter in which Partner group is located.
A favicon picture (optional)
Step-by-step instructions for URL branding are available under KB58275.
It is not only the portal URL that can be branded, but also much more things: logo, web console's color scheme, mail server's settings and many others. Refer to the Acronis Backup Cloud user guide for more details about branding.
  #2 ► Updating backup clients
There are several ways how to update backup client to the latest version available. As soon as a new release of the agent software is published, Acronis Backup Cloud’s Backup Management console provides a possibility to perform a centralized update of all backup client running older version. Here are the possible update scenarios:
Updating backup agent manually: this is the easiest way to upgrade a single machine. All that needs to be done is to download the latest version of backup agent’s installation file and run it on the client machine. After clicking “Update” installer will automatically download latest version of the software and install it
Performing centralized update from Backup Console. This method does not require direct connection to the agent machines and allows to perform simultaneous update of up to 10 machines. Check this User Guide page for more details
Mass update using a python script. This option is applicable for huge number of agents and does not have a limitation for simultaneous update (unlike the previous option). For detailed guidance, please refer to KB61049. This method requires Python installed
  #3 ► Dealing with “orphan” backup plans
Some of our Partners were facing an issue with backup plans still running on the client PCs despite the fact they were revoked/deleted. One of the most common scenarios is agent machine’s migration from one customer account to another. The reason for that is the fact that backup plans are not only being kept on the backup agent’s side, but also at cloud backup management server (AMS). After machine’s migration to new customer, backup plan from old customer is still being automatically deployed from cloud AMS. It is a limitation of current Acronis Backup Cloud’s design. To bypass this, you may follow this scheme:
Revoke all backup plans from the machine you want to migrate to different customer account
Register machine under new customer account according to KB55244
Once device is shown under new customer, check if there are any old backup plans present. If so – delete them
Create new backup plan for the migrated machine
If the “orphan” plan is still running for some machine, please follow the guidance from KB6104
  #4 ► Retention rules
Since this queries on this topic remain ones of the most frequently asked, we've decided to review this theme once again. Check the digest for November 2017 that covers not only the question about retention rules, and also backup schedule and backup types.
https://forum.acronis.com/forum/digests-and-support-best-practices/supp…
 
New KB articles
Acronis Backup Cloud
KB61074: Acronis Backup Cloud: how to enable logs of Acronis Backup module for WHMCS
KB61049: Acronis Backup Cloud: mass update of Acronis Agents
KB61045: Acronis Backup Cloud: backup plan runs on the machine after registering it to a different user (tenant)
KB60983: Acronis Backup Cloud 7.7 Beta: how to export Office 365 archives from Cloud to local storage
KB60982: Acronis Backup: full backup is created on the first day of each month with "Weekly full, Daily incremental" scheme
KB60980: How to activate Acronis Backup Cloud subscription purchased from Plesk
KB60929: Acronis Backup Cloud 7.7 Beta: recovery of mailboxes fails with "The account does not have permission to impersonate the requested user"
KB60881: Acronis Backup: "The security database on the server does not have a computer account for this workstation trust relationship" error
Acronis Storage
KB61050: Acronis Storage: using SSH keys to access and manage Acronis Storage
KB61024: Acronis Storage: understanding node role icons
See all new KB articles here: https://kb.acronis.com/new
Did you know that Acronis Data Cloud v 7.7 BETA is now live and available for public testing? Use the following link to register: https://www.acronis.com/en-us/support/beta-cloud/register-reseller.html

 
New training materials
Acronis Files Cloud v.1.0 Support Training
Acronis Files Cloud v.1.0 Certification Exam
See all training materials here: https://kb.acronis.com/MSPtraining
Did you know that Acronis Files Cloud provides office and mobile users with safe file access, sync, and share in an easy-to-use, complete, and secure hosted cloud solution? See more at https://www.acronis.com/en-us/cloud/service-provider/files/
 

Datacenter and agent updates
Current agent versions:
Backup Agent for Windows (v.12.0.4670)
Backup Agent for Mac (v.12.0.4670)
Backup Agent for Linux (v.12.0.4670)

Datacenter


Platform version


Available services


Strasbourg (BETA)


7.5HF2


Backup
File Sync&Share


St. Luis (BETA2)


7.5HF2


Backup
Disaster Recovery
File Sync&Share


Strasbourg (EU1)


7.5HF2


Backup


Frankfurt (EU2)


7.5HF2


Backup


London (EU3)


7.5HF2


Backup
Disaster Recovery
File Sync&Share


Frankfurt (EU4)


7.5HF2


Backup


Zurich (EU5)


7.5HF2


Backup


Ashburn (US2)


7.5HF2


Backup


Ashburn (US5)


7.5HF2


Backup
Disaster Recovery
File Sync&Share


Nagano (JP1)


7.5HF2


Backup


Singapore (SG1)


7.5HF2


Backup


Sidney (AU1)


7.5HF2


Backup


Moscow (RU2)


7.5HF2


Backup

 
Release notes:
Acronis Data Cloud backup agent v 12.0.4670


      
                                            
                
            
                            
                    
                        
                            
                              Wed, 03/14/2018 - 13:02

                                                          
                                                            
                                                                                        
    
                    
                Vyacheslav Bykov
Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                    
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful
