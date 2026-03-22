# Install client without logging in with each customers account info

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/install-client-without-logging-each-customers-account-info

## Original Post
**Author:** Unknown

Install client without logging in with each customers account info

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Chris Toews
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I'm finding installing Acronis painful to install on clients. I am able to create the customer in the portal, I'm able to setup the protection plans, and I make a user for the customer.
BUT,
when I install the Acronis client on windows, it then wants to setup the client in a webpage, and that page is logged in as me, and it won't let me add the computer to the customer. I need to login as each customer to add computers.
So,
it seems like I need to make a user for each customer that I will be able to login with when I want to install Acronis anywhere. I just want to be able to install the client using MY authentication on the website.
 
Am I missing something?
Is there a step I'm not doing that would make my life easier?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 01/26/2022 - 19:05

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Alphonso Burger
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Sorry for digging up an old thread but I figured i'd answer this since I had the same issue and im sure others would also want to know this answer. Not sure if you actually figured this out:
You can go into the customer portal with your partner account and the select add devices, scroll to the bottom and choose generate registration token.  

You can then pre-select the customer user or service account that will be used for registration when installing the agent (I prefer using 1 single "service" account to register the agents against on each customer eg customername.acronis). You dont need to select a plan here but you can if you want to.

Now when you install the Agent you need to choose CUSTOMIZE INSTALLATION OPTIONS, under registration options change this to TOKEN and then paste the generated token value that you generated above. Then you can install as normal and the Agent will auto register on that account. 
Doing it this way means you never have to log into that customer account directly after the initial activation. This seems to be a really good method if you are the service provider for the customer.
Hope this helps!
 
 
 

      
                
                
                    
                                                    Thu, 11/03/2022 - 23:23
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daria Sorokina
                            

                            
                    
                        Acronis Support
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 487
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dear Alphonso Burger,
Thank you for sharing the solution, really appreciate your cooperation!

      
                
                
                    
                                                    Fri, 11/04/2022 - 16:02
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards, Daria Sorokina | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
