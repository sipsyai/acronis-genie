# Updating agent version from the server's side

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/updating-agent-version-servers-side

## Original Post
**Author:** Unknown

Updating agent version from the server's side

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                
                    
                        
            Hello,
We've seen that sometimes the agent update functionality in the backup management console doesn't work.
In the attached screenshot for example is a case where we selected all 6 servers to have their agent version updated from 12210 to 12420 yesterday, and when we logged back into the account today, only two of them were updated successfully.
There are also no alerts or other information to see why they didn't get updated. 
Is there a way to update the agent version via SSH in Linux, instead of using the backup management console?
Thanks in advance,
George Tasioulis

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      [fdfa174644226a52407237a057d81a59]_Screenshot%202019-02-14%20at%2010.45.19.png

                      79.66 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Thu, 02/14/2019 - 08:43

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello George,
Thank you for your posting! The described behavior needs to be investigated with the help of the support engineers.  In order to start investigation, I would ask you to contact your Service Provider for creating a support ticket. 
Regarding your question on the update procedure: 
To update Acronis Agents via command line, you can follow one of the following ways
Download and update agents locally. Here the links to the latest builds:
Agent for Linux (32-bit) http://dl.managed-protection.com/u/baas/4.0/12.5.12420/Backup_Agent_for_Linux_x86.bin
Agent for Linux (64-bit) http://dl.managed-protection.com/u/baas/4.0/12.5.12420/Backup_Agent_for_Linux_x86_64.bin
Here you'll find the documentation on Updating Linux agents which might be useful  https://www.acronis.com/en-us/support/documentation/BackupService/index.html#32961.html
 
Via mass-update script provided in the Acronis Knowledge Base article which is available at https://kb.acronis.com/content/61049.
Installation of Python 3.6 is required.
To perform the operation, please do the following:
Download the script (https://access.acronis.com/node_share_links/15357?token=ac8b10bd-1fbd-4ea5-988f-07bb593b5a28)
Open command prompt
Navigate to the folder you have downloaded the script to
Run the script: python agent_update.py --username <username> --password <password> --hostname <hostname> --group <group ID> --justreport
Limitations: script does not update agents on offline machines. If the amount of agents to update is large (>100), the script pauses for 1 hour after each 100 updated agents.
***
Сonsider switching to the new backup archive to have all the benefits of Acronis Backup software: https://dl.acronis.com/u/PP_TIBX_Archive_Overview_in_Acronis_Backup_Cloud_EN-US_180607.pdf
Check our monthly digests and support best practices at https://forum.acronis.com/digests-and-support-best-practices 
Find most viewed and most recent knowledge base articles at https://kb.acronis.com/backup-cloud-known-solutions 

      
                
                
                    
                                                    Tue, 02/19/2019 - 09:59
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I noticed the same problem.
 
1 of 5 servers did not update.
Download the script (https://access.acronis.com/node_share_links/15357?token=ac8b10bd-1fbd-4ea5-988f-07bb593b5a28)

Does not work...

      
                
                
                    
                                                    Wed, 12/09/2020 - 22:44
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Mikhail Rozhkov
                            

                            
                    
                        Support Engineer 
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 21
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Please try the following link https://access.acronis.com/t/b1t9lhz6

      
                
                
                    
                                                    Mon, 12/14/2020 - 14:43
