# SBS 2008 won't boot after recovery to new VM

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/sbs-2008-wont-boot-after-recovery-new-vm

## Original Post
**Author:** Unknown

SBS 2008 won't boot after recovery to new VM

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Nick
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 24
                
            
            
                
                    Comments: 22
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi all,
 
I have a partner who was doing a test recovery of a Hyper-V VM of SBS 2008 to a new Hyper-V VM (same host, just new VM).
The backups work fine, no errors or warnings, but when they boot the new VM they get a Blue screen with the error:

They tried to run the DSRM and that does not seem to have solved the issue.
This machine is running the clients exchange, AD etc.
Has anyone else come across this issue and is there anything you would suggest I try?
Thank in advance.
Nick

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 09/20/2018 - 13:37

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Nick. sorry to hear that you have faced the BSOD after the recovery.
Unfortunately, the screenshot was not added to your post, can you please upload it again?
 
In the meantime, may I share the general troubleshooting article on the matter -> Acronis Software: Troubleshooting Universal Restore and Bootability Issues (direct link, in case the text is not clickable - https://kb.acronis.com/content/45432)
The article covers both troubleshooting steps and contains the list of info that Acronis Support team would need in case all steps fail.
 
 

      
                
                
                    
                                                    Wed, 09/26/2018 - 07:24
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Nick
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 24
                
            
            
                
                    Comments: 22
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Fedor,
 
Thank you for your help, this issue seems be be an isolated case and has to do with the machine itself rather with the Acronis restore.

      
                
                
                    
                                                    Thu, 10/11/2018 - 11:41
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Nick, alright. Let me know if you would need further assistance or guidance!

      
                
                
                    
                                                    Thu, 10/11/2018 - 11:58
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud
