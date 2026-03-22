# Linux system freeze on every backup

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/linux-system-freeze-every-backup

## Original Post
**Author:** Unknown

Linux system freeze on every backup

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Malte Kiefer
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
we have 12 Linux VM's at Netcup, all of which we back up with Acronis.
One machine is giving us significant problem here, so we had to disable Acronis for now.
Namely, every time we try to make a file & folder backup, the VM freezes, our monitoring systems report that it is offline and in the console we see the following picture:
 

We have already updated the system, rebooted, reinstalled Acronis several times, however, the error comes again and again.
I can't find anything specific in the KB about this, does anyone have a tip for me.
Here is some more information about the server
Kernel:  Linux XXX 5.10.0-18-amd64 #1 SMP Debian 5.10.140-1 (2022-09-02) x86_64 GNU/Linux
Memory Size: 16 GB
CPU: AMD EPYC 7702P 64-Core Processor
fs.inotify.max_user_watches = 8192

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 10/10/2022 - 06:28

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daria Sorokina
                            

                            
                    
                        Acronis Support
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 487
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dear Malte Kiefer,
Thank you for reaching out. We have forwarded your question to a dedicated support engineer who will review and respond soon.

      
                
                
                    
                                                    Thu, 10/13/2022 - 10:30
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards, Daria Sorokina | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Georgi Dimitrov
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 10
                
            
            
                
                    Comments: 49
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Malte. 
In order to troubleshoot the stuck backup, please use https://kb.acronis.com/content/45992 . 
If the issue persists - please open a case with our support team and provide the information as described in - https://kb.acronis.com/content/45992 
Thank you for your time. 

      
                
                
                    
                                                    Thu, 10/20/2022 - 10:53
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Georgi Dimitrov | Support Engineer

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
