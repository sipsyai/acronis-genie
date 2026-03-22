# Referencing credentials in Powershell script

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/referencing-credentials-powershell-script

## Original Post
**Author:** Unknown

Referencing credentials in Powershell script

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Preben Justesen
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi!
I'm new to Acronis Cyber Protect Cloud and is trying to utilize the Script repository to execute a Powershell script.
The script uses a credential and I have added the this as a credentials pair under the "Credentials." In the user interface it then says that "You can use these credentials in the script body with the names ”XXX_name and XXX_secret” given that I named the credential XXX.
But how do I actually reference them in the Powershell script? The obvious way was to assume that I could reference them as variables $XXX_name and $XXX_secret, but that doesn't work.
Just using the strings without $ doesn't work either.
I can find no documentation on how to reference the values.
Best regards
Preben

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 02/14/2024 - 17:18

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Preben Justesen
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi again!
One of my colleagues figured out that the credentials need to be referenced by $env: so $env:XXX_name and $env:XXX_secret gets the values.
This information could be nice to have in the documentation or in the text in the user interface.
Best regards,
Preben

      
                
                
                    
                                                    Thu, 02/15/2024 - 07:17
                                                                            
                                
                            
                                            
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Preben Justesen wrote:

Hi again!
One of my colleagues figured out that the credentials need to be referenced by $env: so $env:XXX_name and $env:XXX_secret gets the values.
This information could be nice to have in the documentation or in the text in the user interface.
Best regards,
Preben


Hello Preben,
The information is not available in the user guide because the product does, in fact, allow you to integrate scripts. However, we do not provide support for issues related to custom scripts. Users should refer to the information available in Microsoft manuals when creating them, for example: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables?view=powershell-7.4
Best regards.

      
                
                
                    
                                                    Thu, 02/15/2024 - 08:35
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Preben Justesen
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Jose,
I think at least the user guide could state that the credentials values will be presented as environment variables in order to point users to the right way to access the values.
Best regards,
Preben

      
                
                
                    
                                                    Thu, 02/15/2024 - 09:06
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Preben Justesen wrote:

Hello Jose,
I think at least the user guide could state that the credentials values will be presented as environment variables in order to point users to the right way to access the values.
Best regards,
Preben


Hello again,
We have forwarded your message to the team regarding your feedback, and we appreciate it. We are always striving to improve our processes.
Best regards.
. 

      
                
                
                    
                                                    Thu, 02/15/2024 - 09:16
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
