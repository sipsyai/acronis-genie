# How to backup a VM on a ESXi Server with Cpanel

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/how-backup-vm-esxi-server-cpanel

## Original Post
**Author:** Unknown

How to backup a VM on a ESXi Server with Cpanel

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Michael Brunner
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 21
                
            
            
                
                    Comments: 33
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi
We have a lot of virtual machines on ESXi servers which use the controllpanel solution Cpanel. What is the best solution to backup such a VM?
- Installing the agent and the cpanel plugin for easy restore inside cpanel
- backup the vm on vmware level
As I understood, the first solution gives the enduser the possitbility to restore files and databases by him self. But in case of a node failure I have to restore the machine with the boot cd and restore vm by vm.
With the second solution I don't have the enduser restore and also no possibility to restore mysql databases. I can only restore on file level. But this solution has the benefit to restore the complete vm in case of a desaster.
What is the recommended way to backup such VM's?
Regards
Michael
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 05/31/2018 - 05:22

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Mikaela Yu
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I am a user of a <a href="http://guidesformarketingautomation.com/">computer backup software</a> and i love it.

      
                
                
                    
                                                    Thu, 05/31/2018 - 09:27
                                                                            
                                
                            
                                            
                                            
    
                    
                SPAM

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Evgeny Ryuntyu
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 56
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Michael!
 
Thanks for reaching out to our Forum. My name is Evgeny, I am from Acronis Service Provider Support.
As far as I understand you would like to know the recommended way of backing up VMs that are also using the cPanel.
You have described the benifits correctly, the Acronis Data Cloud plugin for cPanel allows :
• Back up an entire cPanel server to the cloud storage with the disk-level backup
• Recover the entire server including all of the websites
• Perform granular recovery of websites, individual files, mailboxes, mail filters, mail forwarders or databases
• Enable self-service recovery for cPanel accounts
 
The standard backup with the Agent for VMware allows to use such functions as Run the backup as VM, create replicas of VMs. 
https://www.acronis.com/en-us/support/documentation/BackupService/index…
 
It is up to the End-User to decide which option to choose that covers their business need :)
 
Best regards,
------------------------------------------------------------------------------------------------
Evgeny Ryuntyu | Senior Support Engineer
Acronis

      
                
                
                    
                                                    Thu, 05/31/2018 - 09:40
