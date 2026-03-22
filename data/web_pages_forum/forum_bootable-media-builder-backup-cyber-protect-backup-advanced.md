# Bootable media builder - backup? Cyber protect - Backup Advanced

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/bootable-media-builder-backup-cyber-protect-backup-advanced

## Original Post
**Author:** Unknown

Bootable media builder - backup? Cyber protect - Backup Advanced

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Johnny Wallinder
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi
We have a license for "Acronis Cyber Protect - Backup Advanced"
I'm trying to figure out how to create a Bootable media with both backup and restore capabilities. 
We are in the situation that we have an industrial PC with windows 10, that is controlling a robot. 
We would rather not want to install any software on this PC, and this PC is not network connected for security reasons. But we want to make a backup/clone of the entire system. 
The thought we had was to boot up the system from a bootable USB and create a backup/clone this way. 
We want to be able to restore the clone/backup to a new hard drive OS and all, in the same way with bootable USB if the hard drive in the PC gets corrupted.
We also have a spare industrial PC of the same model/brand we can exchange to if the actual PC stops working.
So we would want to use the same backup created from the running computer to restore to the spare PC.
Is there any potential problems restoring clone to the spare computer, slight dissimilar hardware?
Is this possible, what do i need to do?
I downloaded the 'Bootable media builder' and was able to create and boot from the USB on the spare PC. But there is only the "Restore" option. Not the backup. 
Is the 'Backup Advanced' License enough to be able to do this?
Regards,
Johnny. W

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 11/06/2024 - 11:56

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Welcome to the forum.
Regarding your query, it is possible to execute backups using only the Bootable Media, with the following pre-requisites:
1- Make sure to specify a license key during bootable media creation, otherwise backup will not be available ( I guess this is missing in your bootable media )
2- It is not possible to back up a macOS system using Bootable media.
How to create a bootable media
How to back up with bootable media
Alternatively, you can download an ISO image from your account at Acronis Account.
I wouldn’t recommend restoring clones to dissimilar hardware, as it may cause conflicts. Backups are a better option.
The best approach is to perform regular backups and, if needed, recover them on dissimilar hardware using Universal Restore: Restoring to Dissimilar Hardware with Universal Restore
Best regards.

      
                
                
                    
                                                    Wed, 11/06/2024 - 14:48
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    IT Dep
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
 
Yes what Jose said, i had the same use case at my place. With even the standard license i made a bootable key, plugged that and a ssd into the machine, booted on acronis, made the backup  and restored into to another compatible machine
 
No fuss

      
                
                
                    
                                                    Fri, 01/31/2025 - 12:13
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Standard
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Mykhaylo Romaniv
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I have the same error after upgrade from 16.0.37482 to 16.3.39376. Bootable Media "Windows PE 64 bit" does not automatically register on management server, not assign licence key and no Backup option available even manual registered and assigned the key. Bootable Media "Linux based" work fine but this is not a solution.
 
Regards,
Mykhaylo

      
                
                
                    
                                                    Mon, 03/10/2025 - 07:37
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Mykhaylo Romaniv wrote:

I have the same error after upgrade from 16.0.37482 to 16.3.39376. Bootable Media "Windows PE 64 bit" does not automatically register on management server, not assign licence key and no Backup option available even manual registered and assigned the key. Bootable Media "Linux based" work fine but this is not a solution.
 
Regards,
Mykhaylo


Hello Mykhaylo,
I recommend reporting the issue to the team and raising a ticket.
I've noticed some issues with the latest WinPE build in other products as well, so it's a good idea to escalate it. This way, they can test it and provide you with a reliable solution.
Best regards.

      
                
                
                    
                                                    Mon, 03/10/2025 - 08:13
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
