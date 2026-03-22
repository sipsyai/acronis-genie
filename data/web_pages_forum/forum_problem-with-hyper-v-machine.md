# Problem with Hyper-v Machine

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/problem-hyper-v-machine

## Original Post
**Author:** Unknown

Problem with Hyper-v Machine

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Toufic Saghbini
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                
                    
                        
            We have a problem with one Hyper-V Host machine. We have installed the Hyper-V agent on the host server, however the virtual machines running on the host are not showing up in the portal. The Host machine is showing.
It is to note:
- That this machine was previously assigned to another account, we deleted the agent and reinstalled it in order to assign the machine to a new account.  
- A previous backup job, created on the previous account, is showing in the warning, with an error message: Agent is offline.
Any ideas on how to rectify the situation?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 08/18/2016 - 15:56

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Vyacheslav Bykov
                            

                            
                    
                        Cloud SP Trainer
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 10
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Toufic,
First of all, please make sure you have the latest version of backup client installed on hyper-v host -  build 12.0.3539. If not - please install it:
http://dl2.acronis.com/u/baas/4.0/12.0.3539/Backup_Agent_for_Windows_x6…
Next, check if Hyper-V host  has no connection issues between itself and cloud servers. Use the utility  attached to the KB article below:
http://dl2.acronis.com/u/baas/4.0/12.0.3539/Backup_Agent_for_Windows_x6…
 
If there are no connection problems please provide us with the following information for further investigation:
-name of the Hyper-V machine
-account name it is registered under
-screenshot of connection verifications utility's output
 
 
 

      
                
                
                    
                                                    Thu, 08/18/2016 - 16:51
                                                                            
                                
                            
                                            
                                            
    
                    
                Vyacheslav Bykov
Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Toufic Saghbini
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
Thank you for your prompt reply. Please note the following:
1- Backup client build installed is 12.0.3539
2- No connection problems with the cloud servers
3- Hyper-V machine name is IX-Host-1.entelligence.cloud
4- Account currently registered under is support@entelligence365.com
Thank you again for your support.
Toufic 

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      384390-132619.jpg

                      32.47 KB
                  
          
    

                    
    
                
                
                    
                                                    Thu, 08/18/2016 - 17:38
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Vyacheslav Bykov
                            

                            
                    
                        Cloud SP Trainer
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 10
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I've created a support request # 02773714  in our system.
Soon one of the support representatives will get in touch with you and assist further.
Thank you for your cooperation.

      
                
                
                    
                                                    Thu, 08/18/2016 - 18:53
                                                                            
                                
                            
                                            
                                            
    
                    
                Vyacheslav Bykov
Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.
