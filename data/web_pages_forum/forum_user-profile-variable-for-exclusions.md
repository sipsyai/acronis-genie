# User Profile Variable for Exclusions

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/user-profile-variable-exclusions

## Original Post
**Author:** Unknown

User Profile Variable for Exclusions

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Anthony Brabrook
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            How can I exclude a folder within all user's profiles in a Protection Plan? I have tried %userprofile%\FOLDERNAME with no success. 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 11/13/2024 - 16:49

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Welcome to the forum.
You can try using wildcards within the path, such as C:\Users\*\AppData\folder\. This will exclude that folder for all users, so please check if it works for your needs.
For more details, you can refer to our documentation here: https://www.acronis.com/en-us/support/documentation/AcronisCyberProtect_16/#file-filters.html#kanchor1070.
If you have any further questions, please contact our support team at https://support.acronis.com/.
Best regards.

      
                
                
                    
                                                    Thu, 11/14/2024 - 14:33
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Anthony Brabrook
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you, that does work!

      
                
                
                    
                                                    Mon, 11/18/2024 - 16:30
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Anthony Brabrook wrote:

Thank you, that does work!


You are welcome! 

      
                
                
                    
                                                    Mon, 11/18/2024 - 21:56
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
