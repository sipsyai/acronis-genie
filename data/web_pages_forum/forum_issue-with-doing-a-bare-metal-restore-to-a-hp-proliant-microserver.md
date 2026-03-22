# Issue with doing a bare metal restore to a HP Proliant Microserver

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/issue-doing-bare-metal-restore-hp-proliant-microserver

## Original Post
**Author:** Unknown

Issue with doing a bare metal restore to a HP Proliant Microserver

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Michael Valencia
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I recently had to replace the drives on a HP Proliant Microserver Gen8.  We use Acronis Cloud as the backup solution for that physical server. 
 
When I tried to use the bootable ISO that comes with Acronis Cloud,  I can't see the RAID array of the server.  It uses the B120i RAID Controller.  The bootable ISO can read the backup data but it does not see the RAID array so I can't restore the data.
I referred to this article as part of my troubleshooting:https://kb.acronis.com/content/6495
I created a bootable WinPE media to use as an alternative boot media.  ( See https://kb.acronis.com/content/59611)
 
 When I use the bootable WinPE media,  I get an error when trying to read the backup data. "Failed to obtain backup contents".
I have also tried the custom boot media from Acronis that supposedly has B120i RAID driver.  But it also gets the "Failed to obtain backup contents"  error when trying to read the backup data. 
If there is anyone out there that may know what to do. Please let me know. 
 
 
 
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sun, 02/24/2019 - 02:10

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Michael!
 
"Failed to obtain backup contents" message comes up because the build number of Acronis Data Cloud is higher that of Acronis Backup 12.5 - 12420 vs 11010
And with the higher build number comes a slightly updated version of the archive that an older build does not recognise.
 
We will update the Knowledge Base article with this info, but in the meantime I have sent a link to download the newer installer.
I cannot post links as such out in the open to avoid users with other problems downloading the build and making things worse :)
 
Let me know if you got it!

      
                
                
                    
                                                    Mon, 02/25/2019 - 19:50
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud
