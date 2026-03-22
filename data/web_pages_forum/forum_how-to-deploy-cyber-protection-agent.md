# How to Deploy Cyber Protection Agent

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/how-deploy-cyber-protection-agent

## Original Post
**Author:** Unknown

How to Deploy Cyber Protection Agent

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Rob Sickler
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Forgive my ignorance; I've not used anything from Acronis for about 10 years and I've just recently been assigned this task.
I'm new to a company who has just started using this product.  I've been tasked with deploying this to a bunch of users.  Historically, they've always sent out the registration emails to the individual users.  I'm told this was to make it easier to find and recover data if/when the time came because it was under the individual user.  My problem is that, in my mind, this doesn't scale well.  While I've found the offline installer and know how I can create and MSI and an MST, It seems very tedious to generate/deploy an MST for every user in the org.  Are we doing it wrong?  What's the recommended way of deploying this software to groups of users while still keeping things clean when it comes time to recover data from the cloud?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 06/03/2021 - 20:55

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Good day,
So methods that I have personally used for mass deployment are as follows:
1. Deployed the software using the customers own software deployment solution (I have used GFI, Panda etc) and then registering via tokens. This did have some headaches in the beginning but was quick to sort out.
2. The MSI method also worked well with pre-registering the agent before hand during the setup of the agent, this is in my opinion the best way of mass deploying as it can also be pushed out via GPO or a software deployment solution
3. One of the newer ways of deploying (But only works on Windows) is to use the "Multiple Devices" deployment within the console. This will allow you to search AD, scan the local network or specify manually or import from a file. I have not used this method a lot but the times I have used it it also works very well.
It becomes more complex if you want each user to have their own tenant/folder but the way I deploy is I have a admin account for the customer which gets assigned to the technical lead (generally the technical manager) and then sub admin accounts for the technical staff which they can login and manage the backups.
I hope this helps you a little bit,
Regards
 

      
                
                
                    
                                                    Wed, 06/09/2021 - 09:02
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Rob Sickler
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            So, with #3, we are indeed working with Windows.  Problem is, we don't have a central server at each of our customers' sites.  At best, they all have AzureAD-joined Win10 machines so, there's no PCD on-site.  Because of this, we use the Acronis Cyber Cloud portal.  So, I don't think that we can use this new method anyway.
#2 looks like our best option.  It's what I was looking at anyway.  I can deploy it, with a vanilla MST that is set up without any user info, and during our typical setup, we can have the user open the agent and register the machine under their account.

      
                
                
                    
                                                    Wed, 06/09/2021 - 16:46
