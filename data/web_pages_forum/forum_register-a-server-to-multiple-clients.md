# Register a Server to Multiple Clients

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/register-server-multiple-clients

## Original Post
**Author:** Unknown

Register a Server to Multiple Clients

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    George Xanthopoulos
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
We are an IT Consulting & Support Company. We have multiple clients have installed and use Acronis Cloud Backup Solution (especially server part).
We have also backup servers to our offices in the case that a client's server fault.
Can we have the option to Recover client backup to a server on our offices, ready to replace the fault server?
Can we register this server to a multiple clients Acronis Cloud Backup accounts?
 
Thank you

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 04/11/2019 - 13:11

                                                          
                                                            
                                                                                        
    
                    
                Multiple PC & Server Machines

            
                            
                Products: 
                Acronis Cloud Backup
True Image
            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi George
You can have a look at the large scale disaster recovery:
https://kb.acronis.com/content/14084
Alternatively if you have all of the login credentials you can recover to any server you wish by means of using the bootable ISO image or restoring to a physical machine granted that the machine you are restoring to can access the backed up data either via cloud or local
I hope this answers your question
Kind regards

      
                
                
                    
                                                    Fri, 04/12/2019 - 08:05
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George Xanthopoulos
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thanks for the reply.
Yes i have the login credentials and i try to Register a server in my office to a client account and i manage to recover some files.
I see the Large Scale Recovery but i need to pay for an extra license (for all of my clients). I will think about it while i make some offer to my clients.
My question is if i can register a server (that is in my office) to multiple customer accounts....
Thanks for advanced...

      
                
                
                    
                                                    Fri, 04/12/2019 - 10:06
                                                                            
                                
                            
                                            
                                            
    
                    
                Multiple PC & Server Machines

            
                            
                Products: 
                Acronis Cloud Backup
True Image
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi there
Can you please elaborate on exactly what you would like to achieve with the following:
"My question is if i can register a server (that is in my office) to multiple customer accounts"
My understanding is you have a server in your office which you use as a stand by server should your customers environment crash you will provide them with the server to minimize the RTO. But you would like to use one server for multiple customers.
If the above is correct then in theory yes it is possible to recover multiple customers data to a single server (Granted that you do not perform an entire machine backup) but then delivering the server to one customer will cause a security violation/GDPR violation as you will have other customers data on the same server
What I do for our customers is we have what is called a virtual data center located in South Africa which we can spin up a virtual machine for a customer for use until they repair their physical server or continue to use should they wish to and get rid of the physical server. We have the same in Azure for our customers who do not want their VM to reside in South Africa
I hope this guides you in the right path to what you would like to achieve
Regards

      
                
                
                    
                                                    Fri, 04/12/2019 - 11:38
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George Xanthopoulos
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you for your reply ... you cover me 100% (i not give a thought for GDPR matter having in a server varius client's data!).
I will create some VMs for my critical cituations (localy and on the cloud to)..
Thanks again

      
                
                
                    
                                                    Sat, 04/20/2019 - 09:45
                                                                            
                                
                            
                                            
                                            
    
                    
                Multiple PC & Server Machines

            
                            
                Products: 
                Acronis Cloud Backup
True Image
