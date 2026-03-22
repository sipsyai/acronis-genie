# Service Account For Windows

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/service-account-windows

## Original Post
**Author:** Unknown

Service Account For Windows 

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    A TARO
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 7
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I am deploying Acronis Cyber Protect 16 in Windows domain environment. As per the article to install the software on domain controller, we need to specify a service account who is member of domain admin which is a security risk.
Service logon account – Acronis Cyber Protect 16 Update 4 – Web Help
I have following queries
a) Is it mandatory to add the service account in Domain Admin Group? 
b) Is it not possible to run it under local systems just like other agent services? 
c) Why service account is specified only for “Acronis Managed Machine Service” and not for other Acronis services?
d) Can we use MSA (Managed Service Account) account to run this service?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 06/24/2025 - 06:15

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
Thank you for your questions regarding the deployment of Acronis Cyber Protect 16 in a Windows domain environment. Let me address your concerns one by one:
a) Is it mandatory to add the service account to the Domain Admin group?
While it is recommended to use a Domain Admin account for installation on a Domain Controller due to required permissions (e.g., registry access, service control, etc.), it is not strictly mandatory. However, limited permissions may result in failed operations or incomplete functionality. If you choose to use a custom account, ensure it has the necessary rights as outlined in our documentation.
b) Is it not possible to run it under Local System like other agent services?
On domain controllers, running under Local System may not provide the required privileges to perform certain backup/restore operations or access protected system components. This is why a service account with elevated rights is recommended in these cases. On non-DC systems, Local System is usually sufficient.
c) Why is the service account specified only for "Acronis Managed Machine Service" and not for other Acronis services?
The "Acronis Managed Machine Service" (MMS) is responsible for key operations such as communication with the management server, task execution, and some system-level activities. It requires broader access compared to other services, which is why it specifically allows customization of the service account.
d) Can we use an MSA (Managed Service Account) to run this service?
Currently, Managed Service Accounts (MSAs) are not officially supported for Acronis services. Using an MSA may work in some scenarios, but we cannot guarantee full compatibility or support. We recommend using a dedicated service account with the appropriate permissions for best results.
If you need help configuring a minimal-permission account or have additional questions, please don’t hesitate to reach out to our support team:
? https://support.acronis.com/
Best regards,

      
                
                
                    
                                                    Tue, 06/24/2025 - 11:17
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    A TARO
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 7
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you for the detailed answers.
My customer is not accepting domain admin as service account. Is it inline with best practices? 

      
                
                
                    
                                                    Tue, 06/24/2025 - 13:37
                                                                            
                                
                            
                                            
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            A TARO wrote:

Thank you for the detailed answers.
My customer is not accepting domain admin as service account. Is it inline with best practices? 


Hello!
As long as the necessary permissions are granted it should work.
Best regards. 

      
                
                
                    
                                                    Wed, 06/25/2025 - 10:20
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
