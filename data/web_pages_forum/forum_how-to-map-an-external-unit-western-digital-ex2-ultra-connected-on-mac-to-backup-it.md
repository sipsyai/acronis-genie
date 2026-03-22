# How to map an external unit (Western Digital EX2 Ultra)  connected on Mac to backup it?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/how-map-external-unit-western-digital-ex2-ultra-connected-mac-backup-it

## Original Post
**Author:** Unknown

How to map an external unit (Western Digital EX2 Ultra)  connected on Mac to backup it?

        
  



    
  


  
          
  
    Tutorial
  


          






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Julio Divietro
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            My customer has a Mac and it connect a external storage unit from Western Digital (WD EX2 Ultra) via time machine.  I want to backup the data into this WD.  I understood that I cannot install an agent on this WD with MyCloud OS.   The unit appears that way on the mac.:
 
 

      
                                            
                
            
                            
                    
                        
                            
                              Tue, 07/16/2024 - 18:32

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Cyber Protect Cloud 
MSP Partner
            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  





            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Julio,
Thanks for posting.
Please check the following troubleshooting steps:

Verify Network Connection:
Make sure that the WD EX2 Ultra is properly connected to the network and is accessible from the Mac. You can verify this by opening Finder on the Mac and checking if the WD EX2 Ultra appears under the "Shared" section.


Check Share Permissions:
Create a new share (as a test) or use an existing share on the NAS where the backup will be stored. Ensure it has the necessary read/write permissions. This is very important; without proper permissions, it won't be possible to back up the files.


Set WD EX2 Ultra as the Backup Destination:
In the Acronis Cyber Protect 16 backup destination settings, select "Network Folder."
Browse to or enter the path to the WD EX2 Ultra share. This will typically be something like smb://[WD EX2 Ultra IP Address]/[Share Name].
Enter the username and password for accessing the share if prompted.

If the issue persists, please reply with a detailed explanation about what’s wrong.
Best regards.

      
                
                
                    
                                                    Wed, 07/17/2024 - 10:15
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
