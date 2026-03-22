# Creating application-consistent (VSS) hypervisor snapshot' failed

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/creating-application-consistent-vss-hypervisor-snapshot-failed

## Original Post
**Author:** Unknown

Creating application-consistent (VSS) hypervisor snapshot' failed

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    om team
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            There are 2 notifications:
Activity Failed:
Activity 'Creating application-consistent (VSS) hypervisor snapshot' failed. Operation failed because the Virtuozzo API returned an error 'Virtuozzo Hybrid Server failed to begin a backup. Error message: Please try again. If the problem persists, contact your system administrator for assistance.'

Backup failed:
Operation failed because the Virtuozzo API returned an error 'Virtuozzo Hybrid Server failed to begin a backup. Error message: Please try again. If the problem persists, contact your system administrator for assistance.'

 
How to solve this problem?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sat, 07/08/2023 - 03:54

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
The issue is described in the following KB: https://kb.acronis.com/content/62369 .
Please apply the solutions suggested there.
Please consider to fix the tools of the VM if it can't make the snapshots. Also the issue may happen if there is overloading so consider to change the backup schedule to a non productive hour.
If the issue persists, please contact our support with the logs from the troubleshooting steps: https://kb.acronis.com/content/8153
Thanks!

      
                
                
                    
                                                    Mon, 07/10/2023 - 10:09
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    kinoue     
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            we had this issue, and funnily enough, with one of our Linux VMs too ! not even Windows - so not sure why would it mention VSS in this error message ...
good old have you tried turning it off and on again helped yet again
after trying to understand what is happening (and failing), reinstalling Virtuozzo Tools in the VM (that did not help), we concluded that it was some sort of glitch or stale process or snapshot (or whatever)
so we rebooted the VM (which was in fact quite mature - 300+ days uptime) and voila ! after reboot, it finally was backed up by Acronis
black magic, no less

      
                
                
                    
                                                    Wed, 08/21/2024 - 05:04
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            kinoue wrote:

we had this issue, and funnily enough, with one of our Linux VMs too ! not even Windows - so not sure why would it mention VSS in this error message ...
good old have you tried turning it off and on again helped yet again
after trying to understand what is happening (and failing), reinstalling Virtuozzo Tools in the VM (that did not help), we concluded that it was some sort of glitch or stale process or snapshot (or whatever)
so we rebooted the VM (which was in fact quite mature - 300+ days uptime) and voila ! after reboot, it finally was backed up by Acronis
black magic, no less


Hello!
In fact, sometimes rebooting those VMs can help, as it will also reboot the internal snapshot tools.
You can test if they are working by creating a manual snapshot and then deleting it manually. If that doesn’t work, it could mean that some component is either stuck (which the reboot can fix) or broken.
Best regards.

      
                
                
                    
                                                    Wed, 08/21/2024 - 09:26
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
