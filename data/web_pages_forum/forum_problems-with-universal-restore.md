# Problems with Universal Restore

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/problems-universal-restore

## Original Post
**Author:** Unknown

Problems with Universal Restore

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Jim Becher
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Has anyone else had problems with universal restore? This goes back years and years and is even true today. Universal Restored just doesn't work. I can find the driver and point Universal Restore to that driver or even explicitly add the driver but it flat out doesn't work. I can add the same driver via DISM and it works great.. it's just nothing works with universal restore. Never has. Am I doing something wrong?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 02/24/2025 - 16:00

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
That is not expected behavior.
If you have the latest build of Universal Restore and are still experiencing issues, please raise a ticket with our support team. We can then schedule a remote session to assist you with the creation process.
Best regards.

      
                
                
                    
                                                    Tue, 02/25/2025 - 14:56
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jim Becher
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Yes I know it is not expected behavior but it is what happens and has been happening for 10 years. I have a feeling that no one uses Universal Restore. Not even Acronis. So no suggestions?

      
                
                
                    
                                                    Tue, 02/25/2025 - 16:53
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Jim,
I can assure you that it is used by many of our customers across a wide range of products, from consumers to corporate clients. It is a very reliable tool in general.
Here are a few tips to help:

Sometimes, Universal Restore may not automatically detect certain drivers during the restore process, even though DISM works fine. In Acronis Cyber Protect, ensure you select "Universal Restore" after booting into Acronis recovery mode and explicitly add the driver in the driver dialog. Sometimes, manually placing drivers in the Acronis boot media before initiating the restore can help.


When applying Universal Restore, try performing the restore step-by-step, including adding the driver explicitly during the setup phase. Ensure you are following the correct order: Restoring to Dissimilar Hardware with Universal Restore.


Verify that the driver you're trying to inject is for the correct OS architecture (32-bit vs. 64-bit) and is compatible with the hardware you're restoring to. Acronis Cyber Protect may not support certain proprietary drivers or uncommon hardware components.


Make sure you are using the latest build of Universal Restore. Sometimes, updates include fixes for driver compatibility.


Verify that the driver is in the correct format (e.g., INF files or a driver package recognized by Universal Restore). DISM may handle the driver installation more effectively because it works at a deeper system level.


Double-check that you're pointing Universal Restore to the correct driver path. Even though DISM may work, there could be a slight discrepancy in how Universal Restore references the driver.


In rare cases, adding or creating those drivers might not work. However, our support team has a process where, when that happens, our developers can assist in creating a tool adjusted to your environment and drivers. I understand you may not want to wait, but if this issue persists an investigation is required and a fix applied.

Best regards.

      
                
                
                    
                                                    Tue, 02/25/2025 - 17:32
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
