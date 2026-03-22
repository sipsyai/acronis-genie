# PowerShell Scripting Dell Command Update

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/powershell-scripting-dell-command-update

## Original Post
**Author:** Unknown

PowerShell Scripting Dell Command Update

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    D8taSlay3r
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                
                    
                        
            We have a lot a Dell machines and I wanted to be able to utilize the Dell Command Update utility to automatically update Dell software and firmware through a Scripting Plan. I ran into a LOT of issues and it seems like many are the way PowerShell is executed by the Aconis agent vs running PowerShell interactively.
I'm not a developer but I got this thing working. You will notice that there are some repetitive sections of the script and many places that appear to be able to optimized by functions and so forth. However, when I attempted to write the script in a more optimized manner, it would always error out in Acronis - even though it worked fine just running the script in a PowerShell session locally on a machine.
The script will check to see if the machine is a Dell or not before continuing to check for any incompatible software like the universal version of DCU or any version of Dell Update. It will then uninstall those, download a specific version of DCU using a user agent of Chrome instead of PowerShell so it doesn't get blocked by the web server, install DCU, then run DCU via command line, and reboot if needed. You can check local logs on the device in the C:\source\DCU directory or download the script stdout from the Activity in the Acronis console.
I am attaching the script as a text file to the post. I hope this will be helpful and that it will be improved upon.
 

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      dcu.txt

                      11.23 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Wed, 11/08/2023 - 04:29

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Cyber Protect Cloud
            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
In this situation, I would suggest that you raise a ticket with our support or contact your Service Provider to do so. This way, we can check the script for possible incompatibilities and guide you through the best option: https://kb.acronis.com/content/8153
Best regards.

      
                
                
                    
                                                    Wed, 11/08/2023 - 08:26
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    D8taSlay3r
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I don't need support on this. This was just me posting to help others potentially. I will say that Support was completely unable or unwilling to troubleshoot scripting. They basically just said, "The problem is your script." While "technically" correct that the script needed to change to run, the reason is BECAUSE of the constraints imposed by Acronis and the way the Acronis agent executes scripts.
If PowerShell scripts have to be written a special way to execute through Acronis when they work just fine without Acronis, then Acronis ought to actually publish documentation on how to do it correctly instead of just making people go figure it out.

      
                
                
                    
                                                    Wed, 11/08/2023 - 15:17
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud
