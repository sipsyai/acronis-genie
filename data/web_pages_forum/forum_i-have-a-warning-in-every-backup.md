# I have a warning in every backup

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/i-have-warning-every-backup

## Original Post
**Author:** Unknown

I have a warning in every backup

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    mvalenzuelab@grupogtd.com
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi I am new using Acronis, so I will need a little of help with common things about!
My first question is with a warning after every backup of a Linux Server. The backup is with the option Complete Machine and the warning is related with SWAP partition.
Here I put log register about;
Error 0x7002f: File exclusion is not supported.
| trace level: warning| channel: tol-activity#E982396C-DAC4-4E69-84CD-AAC84020F43A| line: 0xa5695862aaf8e7e3| file: d:/3957/resizer/backup/backup.cpp:1158| function: BackupPartitions| volume: webserver-swap_1| fstype: LINUXSWAP| $module: disk_bundle_lxa64_3957
 
I hope receive your help and solve soon this, because my costumer is coming back crazy!!
 
Best regards from Chile
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 08/29/2017 - 18:11

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi there
Can you please advise to which version of Acronis Backup Cloud you are on?
As an immediate recommendation you can try one of the following:
1. As workaround, you can make a file-level backup and specify exclusions.
2. You can try and write the exclusions as follows: C:\* + D:\*
I would also recommend that you check the proper drive letters by going to File Recovery and check the actual drive letters while browsing through the contents of the backup in this machine
Regards

      
                
                
                    
                                                    Wed, 08/30/2017 - 06:18
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Eugene Tanasiev
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 20
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello mvalenzuelab@grupogtd.com,
My name is Eugene.
I'm Sr. Support Engineer from Acronis Service Provider Support team.
According to out internal notes, the warning appear when a swap partition is included in 'Entire backup', while you have 'file exclusions' mentioned in backup options.
There are many ways to handle this:
1. ignore, since this warning is just an info.
2. go to backup options and clear 'file exclusions'
3. if you need file exclusions, then create a new disk/volume backup plan, but not include swap volume
4. follow Jay's recommendation creating file level backup, but not include all the volume ( this plan type is not designed for it)
By the way, warning 'File exclusion is not supported' in regards to swap partition and enabled file exclusion behavior, will be fixed in one of the next Acronis Backup Cloud releases. You can monitor for ABR-106383 in release notes.

      
                
                
                    
                                                    Wed, 08/30/2017 - 07:42
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
                    In reply to Hello mvalenzuelab@grupogtd… by Eugene Tanasiev
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    mvalenzuelab@grupogtd.com
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Спасибо мой друг!!

      
                
                
                    
                                                    Wed, 08/30/2017 - 14:07
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Eugene Tanasiev
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 20
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Всегда рад помочь!

      
                
                
                    
                                                    Wed, 08/30/2017 - 14:09
