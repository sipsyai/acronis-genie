# Acronis Cyber Protect Cloud: Backups fail with "The cloud storage is temporarily unavailable" on EU2 and EU8 DCs

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/acronis-cyber-protect-cloud-backups-fail-cloud-storage-temporarily-unavailable-eu2-and-eu8-dcs

## Original Post
**Author:** Unknown

Acronis Cyber Protect Cloud: Backups fail with "The cloud storage is temporarily unavailable" on EU2 and EU8 DCs

        
  



    
  


  
          





    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Symptoms
The customer is located on EU2 or EU8 DC and uses the abgw-fra2-arp1 storage.
Starting the last week, backups to Cloud have been failing with "The cloud storage is temporarily unavailable. Please try again later."
Example of full error:
| error 0x29b1398: Network operation timed out
| linea: 0xc3bc4c1eb2299c1a
| archivo: d:\1531\enterprise\applications\archiving\storages\archive3\src\archive3.cpp:624
| funcion: `anonymous-namespace'::CoOpenArchive
| function: archive_open
| $module: common_archive_addon_vsa64_35320
|
| error 0x29b000d: Peer did not respond or did not hold deadline
| linea: 0xc3bc4c1eb2299c1a
| archivo: d:\1531\enterprise\applications\archiving\storages\archive3\src\archive3.cpp:624
| funcion: `anonymous-namespace'::CoOpenArchive
| function: astor_file_open
| $module: common_archive_addon_vsa64_35320
Solution
The issue is fixed. 

      
                                            
                
            
                            
                    
                        
                            
                              Mon, 05/08/2023 - 10:13

                                                          
                                                            
                                                                                        
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful
