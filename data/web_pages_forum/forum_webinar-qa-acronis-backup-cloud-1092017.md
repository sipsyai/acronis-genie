# Webinar Q&A: Acronis Backup Cloud, 10/9/2017

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/digests-and-support-best-practices/webinar-qa-acronis-backup-cloud-1092017

## Original Post
**Author:** Unknown

Webinar Q&A: Acronis Backup Cloud, 10/9/2017

        
  



    
  


  
          





    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello Colleagues!
Here are the Q&A for the recent webinar:
Topic: [APAC] Acronis Backup Cloud Support Training
Date: October 9, 2017
 
Q: Do you now do website backups or is it just for IIS?
A: You can now protect any website available via SSH or SFTP (website file content), and a linked MySQL database. Protecting IIS works through protection of the hosting Windows server. See more here.
 
Q: What are the minimum permissions to set for user to be able to see backups and retrieve backups? Do they need agent to be deployed to their computers?
A: All partners and company administrators can see and retrieve backups withing the company. Backup Service users can only see their own backups. See more here.
 
Q: When do the business users receive their notifications about the errors, if setup via WHMCS or other integration service?
A: All users receive backup notifications immediately after the activity is finished. See more here.
 
Q: What is new about API integration in version 7.5?
A: APIv.1 is fully supported. For all new account management functionality new APIv.2 is introduced. See more in KB60486.
 
Q: Do you need a special VMware license for backing up? Like a vmware storage license or will just esxi license work?
A: Agent for VMware uses VMware vSphere Storage API to protect VMs on hypervisor level. VMware license should include this functionality. To protect Free VMware ESXi install the agent inside the guest OS. See more in KB21015.
 
Q: Is there any advantages/disadvantages installing agent inside the VM, and not backing up by the virtualization host level? It seems direct file restore on the VM and active protection is not available on the Host based backup.
A: Advantages of agentless backup: VM offloading, simpler installation, LAN-free backup. Disadvantages: no direct selection of files, no Active Protection. Direct file restore is possible in any scenario for all supported file systems. See more in KB16577.
 
Q: I noticed only "Entire Machine" backup are able to do application backup. If the machine is connected with USB external hard drive, and we don't want it to be backed up, how can we accomplish Application backup (eg. Active Directory)?
A Correct, Application Backup is available only for Entire Machine backup. To create a consistent backup of applications within the OS to an external drive, create Disk-level backup without external drive and ensure VSS option is enabled and provides no warnings or errors during backup. For granular restore of application data, protect applications with the respective agents.

      
                                            
                
            
                            
                    
                        
                            
                              Tue, 10/10/2017 - 07:11

                                                          
                                                            
                                                                                        
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                    
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful
