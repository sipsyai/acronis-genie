# Agent on Azure Linux VM with Secure Boot

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/agent-azure-linux-vm-secure-boot

## Original Post
**Author:** Unknown

Agent on Azure Linux VM with Secure Boot

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Chris Notley
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I am trying to get the CyberProtect agent installed on an Ubuntu 20.04 VM inside a customer's Azure environment.
The agent installs, but warns me at the end that I need to enroll the MOK certificate due to SecureBoot running..
After a bit of digging, I can see that the enrollment certificate is there, but when I reboot the instance I have no way of accessing the shim uefi key management menu that's displayed at boot, obviously I can't see this on the Azure instance..
Does this mean I can't use CyberProtect on a cloud machine running SecureBoot??

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 02/07/2022 - 18:08

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Georgi Dimitrov
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 10
                
            
            
                
                    Comments: 49
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Chris. 
This appears like it needs a bit more investigation. 
Please open a case with our support team and someone will be happy to investigate and provide a solution. 
Thank you for your time.

      
                
                
                    
                                                    Tue, 02/15/2022 - 08:21
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Georgi Dimitrov | Support Engineer

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daria Sorokina
                            

                            
                    
                        Acronis Support
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 487
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dear Chris Notley,
Please let us know was your problem that you presented here resolved if yes, what helped you?

      
                
                
                    
                                                    Tue, 09/27/2022 - 22:31
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards, Daria Sorokina | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Chris Notley
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Apologies - I'd logged in a couple of forums but obviously hadn't responded on all.
So in the end what I discovered was that the MOK boot menu appears sometimes but not others - I repeatedly re-created machines and only around 30% of the time did it appear!
My assumption is that it's a problem in Azure..
To conclude, I got to the bottom of it, but didn't get a successful result.

      
                
                
                    
                                                    Fri, 09/30/2022 - 14:42
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daria Sorokina
                            

                            
                    
                        Acronis Support
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 487
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dear Chris Notley,
Thank you for your response. Do not hesitate contacting us and our support if necessary. 

      
                
                
                    
                                                    Wed, 10/05/2022 - 11:05
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards, Daria Sorokina | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
