# Unable to send initialseed with archive3 format backup

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/unable-send-initialseed-archive3-format-backup

## Original Post
**Author:** Unknown

Unable to send initialseed with archive3 format backup

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Emilio Bruna
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 7
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi, I already did successfull some initialseed send before the acronis cloud backup update but now I'm unable to do them.
I saw the part "Backup of archive3 format" in the kb https://kb.acronis.com/content/56070 but there isn't the new IS/LSR tool version to download (or at least in this kb that have both linux and windows link with same version installed).
Someone know where is the new version of the tool please?
Thanks for any reply.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 07/09/2018 - 08:49

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi, Emilio!
 
The newest tool is actually available in the same KB, here is the direct link to the build that is actual for the moment I write these lines - https://dl.acronis.com/u/kb/IS_LSR_Tool_Build3.1.132_Windows.zip
Type the following in the CMD to check out the current build:
is_tool --version
Initial Seeding tool version 3.1.125
 
Please note that the CMD calls for TIBX files are different, which is also reflected in the article..
 
I hope that help, but do let me know if you still have any questions/difficulties.
 
 

      
                
                
                    
                                                    Mon, 07/09/2018 - 13:00
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Emilio Bruna
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 7
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi, thanks for reply.
I already downloaded same version for linux (IS_LSR_Tool_Build3.1.132_Linux.zip), more exactly debian9 but seem already at the same version, already tried before:
rpm --install --nodeps InitialSeedingTool64.rpm
rpm: RPM should not be used directly install RPM packages, use Alien instead!
rpm: However assuming you know what you are doing...
        package InitialSeedingTool-12.0.5600-1.x86_64 is already installed
        file /usr/lib/Acronis/InitialSeedingTool/baas_lsr_support.py from install of InitialSeedingTool-12.0.5600-1.x86_64 conflicts with file from package InitialSeedingTool-12.0.5600-1.x86_64 ...

File is tibx created with updated agent and backup plan created after update.
is_tool and  archive_io_ctl are not present (checked also /usr/lib/Acronis/InitialSeedingTool/) but is_info and is_me is and already used for some successfull initialseed send on same system before acronis backup cloud update.

      
                
                
                    
                                                    Mon, 07/09/2018 - 14:55
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I have checked the RPM package, it does includes the necessary files, so this is Linux installation that fails.
try using "--replacepkgs" as an additional parameter to install a package with the same name anyway.
Let me know how it goes!
 
I am attaching a screenshot of the contents of the package so you could see that the necessary files are there:


      
                
                
                    
                                                    Tue, 07/10/2018 - 08:30
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud
