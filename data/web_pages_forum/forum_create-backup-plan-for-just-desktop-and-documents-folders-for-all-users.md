# Create Backup Plan for Just Desktop And Documents Folders for All Users

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/create-backup-plan-just-desktop-and-documents-folders-all-users

## Original Post
**Author:** Unknown

Create Backup Plan for Just Desktop And Documents Folders for All Users

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Maury Macdonald
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi there,  new to Acronis,  have integrated with Connectwise, and im wondering how i would go about creating a backup plan to apply to some machines that backed up any Documents and Desktop folders in every users profile, excluding all the rest of the data.  I wasn't sure if i used a variable such as %USERPROFILE% if it would only backup the data in the currently logged in users profile.
Thanks
Maury

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 05/01/2018 - 20:51

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi, Maury
 
This works exactly as you described, you can specify the inclusion rules by either selecting the files directly or by using policies. Please refer to the following article on the matter -> https://www.acronis.com/en-us/support/documentation/BackupService/#3305…
Check out the " Selection rules for Windows" section of the guide.
 
I'm sure that would solve your questions, but if you would like to clarify something else, please let us know in a reply.

      
                
                
                    
                                                    Wed, 05/02/2018 - 13:01
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Rodrigo Cruz
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Fedor Kondrashov wrote:

Hi, Maury
 
This works exactly as you described, you can specify the inclusion rules by either selecting the files directly or by using policies. Please refer to the following article on the matter -> https://www.acronis.com/en-us/support/documentation/BackupService/#3305…
Check out the " Selection rules for Windows" section of the guide.
 
I'm sure that would solve your questions, but if you would like to clarify something else, please let us know in a reply.


Hello Fedor, how are you doing?
I have a similar question, instead of creating a backup plan for all users within a workstation, I need to backup Documents and Desktop files for current logged user where agent is running.
I have tried to use %HOMEPATH% and created an environment variable but it is not working.
Do you have a clue on how to do that?
 

      
                
                
                    
                                                    Tue, 10/09/2018 - 02:19
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Rodrigo Cruz wrote:
I have a similar question, instead of creating a backup plan for all users within a workstation, I need to backup Documents and Desktop files for current logged user where agent is running.
I have tried to use %HOMEPATH% and created an environment variable but it is not working.
Do you have a clue on how to do that?
 


hi Rodrigo!
I have a question first - you say it is not working - does it fail with an error message or the result is not satisfactory? how exactly does it not work?)
 
in general. for the environment variables to work on all machines, they have to be created in those machines. certain variables are predefined such as %ALLUSERSPROFILE% for example.
 
Perhaps with a combination of rules and paths you can achieve what you seek?
like this:
%HOMEPATH%\<user>
If you would like to have a rule that would use consitions, like, to back up ONLY data of a user that is currently logged on, this is not implemented.
On the other hand, why do you have such specific requirements? Why not back up data of All the users or just some of them?

      
                
                
                    
                                                    Thu, 10/11/2018 - 12:08
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud
