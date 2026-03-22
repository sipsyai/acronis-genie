# Moving the AMS to a different machine - still no easy way ?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/moving-ams-different-machine-still-no-easy-way

## Original Post
**Author:** Unknown

Moving the AMS to a different machine - still no easy way ?

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    SvenT
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 68
                
            
            
                
                    Comments: 232
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hey there,
we have to do some refactoring on our servers and also migrate from Win2019 to Win2022.
The management server is currently installed on a Win10 virtual machine and shall be moved to a virtual Win Server 2022 machine.
Is there any chance to do so or will I lose all history as I have to do a reinstall from scratch?
There is a feature request "RM-366 Integration of AMS migration tool from one system to another" but this is open since July 2020 (!), and still no plan to implement this although for administration this would be quite helpful....
Well...I use Acronis tools since >10 years and my experience with most of the RMs is...."noted" but not more...sad but true.
I also saw Acronis Cyber Backup, Acronis Cyber Protect: Moving Management Server
but if I then dig into the instructions, the prerequisites are 
"The management server uses an external Microsoft SQL Server database. The Microsoft SQL Server instance is running on a dedicated machine."
So it seems as if an on premise installation that uses the built-in SQLite database cannot be moved in that way.
The simple question:
The only the method to move an on premise AMS that uses SQLite to another machine in the year 2025 is still a complete reinstallation and complete reconfiguration?
S.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 10/30/2025 - 08:29

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Cyber Protect Backup Advanced 15/16 in professional usecases


            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Sven,
If you need to move the Acronis Management Server to a different machine, you must install the Management Server on the new system and configure it from scratch.
Migrating a Backup Management Server is complex because it involves multiple linked components, such as databases, certificates, and agent registrations, that are tied to the original server’s ID and network settings.
Best regards.

      
                
                
                    
                                                    Thu, 10/30/2025 - 09:14
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Javier
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 52
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
             
 

      
                
                
                    
                                                    Thu, 10/30/2025 - 09:20
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    SvenT
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 68
                
            
            
                
                    Comments: 232
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hm okay, 
so Acronis still sees it as "state-of-the-art" to do a full reinstall and reconfig....hmm okay.
The RM-366 seems also to be some black hole: Freature Request in, ande never seen again.
Sorry for the sarcasm bit am I the only one who no longer finds this appropriate, since it is a step that is needed from time to time?
And sorry.....complexity is not argument as other companys are able to manage such procedures.
There it is no problem to export all settings and databases and import them on another machine and....just go on....
Well...is it as it is and maybe the developers should also take the SMEs into account in their doing and not only the big players with hundreds of machines...
S.
 

      
                
                
                    
                                                    Thu, 10/30/2025 - 09:43
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Backup Advanced 15/16 in professional usecases


            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            SvenT wrote:

Hm okay, 
so Acronis still sees it as "state-of-the-art" to do a full reinstall and reconfig....hmm okay.
The RM-366 seems also to be some black hole: Freature Request in, ande never seen again.
Sorry for the sarcasm bit am I the only one who no longer finds this appropriate, since it is a step that is needed from time to time?
And sorry.....complexity is not argument as other companys are able to manage such procedures.
There it is no problem to export all settings and databases and import them on another machine and....just go on....
Well...is it as it is and maybe the developers should also take the SMEs into account in their doing and not only the big players with hundreds of machines...
S.
 


Hello again, Sven,
I understand what you mean, your points are perfectly valid. I was just trying to explain the complexity of the matter. In the past, Acronis did have a tool like that (I can’t say much about it since I wasn’t with the company at the time), but it was discontinued because such migration tools often caused malfunctions when moving between environments.
There is indeed a feature request for this, and I’ve forwarded your message to the team. However, to be honest, there’s currently no ETA for its implementation.
Best regards.

      
                
                
                    
                                                    Thu, 10/30/2025 - 11:05
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    SvenT
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 68
                
            
            
                
                    Comments: 232
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            There is indeed a feature request for this, and I’ve forwarded your message to the team. However, to be honest, there’s currently no ETA for its implementation.

To be honest, I do not believe that this feature request will ever be implemented.
It was created at least 5 years ago, and the team seems to see no need for that. 
A security solution that cannot be easily transferred to another machine is somewhat critical.
Is it as it is, and I have to live with it.
The annoying point in the reinstallation and reconfiguring from scratch is, that it is hard to transfer the settings manually and test the plans on the new AMS as the licensing becomes an issue.
The licenses are either bound to the old OR the new AMS and therefore a testing is quite hard....
S.

      
                
                
                    
                                                    Thu, 10/30/2025 - 15:11
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Backup Advanced 15/16 in professional usecases
