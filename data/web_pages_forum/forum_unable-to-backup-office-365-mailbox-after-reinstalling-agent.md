# Unable to backup office 365 mailbox after reinstalling agent

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/unable-backup-office-365-mailbox-after-reinstalling-agent

## Original Post
**Author:** Unknown

Unable to backup office 365 mailbox after reinstalling agent

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    MargaretPap
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 25
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I had installed the Acronis backup agent for office 365 and configured backups for mailboxes in the cloud console which was working.
I subsequently had an issue with the machine on which the agent was installed on and had to rebuild it and re-install the agent and re-register the agent.
I am now no longer able to backup any mailboxes. The console is still displaying all my mailboxes but the "backup now" button is greyed out.
How can I correct this? 
Margaret

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 02/09/2017 - 22:49

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Eugene Tanasiev
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 20
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello, Margaret
Generally I would start from checking if same agent instance is still listed in backup console.
It's a normal behavior, that reinstalled agent appear duplicated in backup console, since it receive a different instance & installation ID.
The solution in this case is easy: delete offline agent, wait some minutes.
An alternative here is to use KB https://kb.acronis.com/content/56493 and preserve original Machine & Instance IDs. However I would recommend using it in very rare occasions.
"Backup now" button should become active.
If problem persist, then please contact Service Provider Support for detailed investigation on subject.
 
Regards,
Eugene

      
                
                
                    
                                                    Fri, 02/10/2017 - 07:32
