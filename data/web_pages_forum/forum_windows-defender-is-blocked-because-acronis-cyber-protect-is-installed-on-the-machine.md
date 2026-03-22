# Windows Defender is blocked because Acronis Cyber Protect is installed on the machine.

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/windows-defender-blocked-because-acronis-cyber-protect-installed-machine

## Original Post
**Author:** Unknown

Windows Defender is blocked because Acronis Cyber Protect is installed on the machine.

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                
                    
                        
            After enabling "Windows Defender Antivirus" in a Cyber Protect Essentials plan on a Windows 10 workstation, I got an alert that "Windows Defender is blocked by a third-party antivirus software: Windows Defender is blocked because Acronis Cyber Protect is installed on the machine."
In Windows Security > Virus and Thread protection whether Period Scanning under Microsoft Defender Antivirus options is turned On or Off doesn't make any difference.

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      Screenshot 2020-10-21 at 11.50.15 AM.png

                      88.8 KB
                  
              
                      Screenshot 2020-10-21 at 11.53.57 AM.png

                      99.99 KB
                  
              
                      Screenshot 2020-10-21 at 11.56.09 AM.png

                      192.19 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Wed, 10/21/2020 - 08:43

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi!
If your machine is already protected with a third-party antivirus at the moment of applying the Antivirus & Antimalware protection module to the machine, the system will generate an alert and will stop the on-access protection in order to prevent potential compatibility and performance issues. You will need to either disable or uninstall the third-party antivirus, in order to enable full-functional Antivirus & Antimalware protection.
If you want to keep using the third-party antivirus, disable Antivirus and Antimalware Protection in the protection plan or use a default protection plan Office Workers (third-party Antivirus).
If Antivirus & Antimalware protection is disabled but conflicts between antivirus software and Cyber Protection Agent still happen, contact Acronis Support to investigate the issue.   
Please refer to https://kb.acronis.com/content/65310 for more details.

      
                
                
                    
                                                    Wed, 10/28/2020 - 09:03
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
