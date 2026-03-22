# File Restore Linux with LVM - doesn't work if exist multiple LVM volumes on same VM

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/file-restore-linux-lvm-doesnt-work-if-exist-multiple-lvm-volumes-same-vm

## Original Post
**Author:** Unknown

File Restore Linux with LVM - doesn't work if exist multiple LVM volumes on same VM

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Nicola Damonti
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Dear support,
We backup a lot of Linux Debian Virtual Machines with Acronis Cloud Backup. We do backup in "agentless" mode using VMWare Agent.
In this way we can do file level restore only if virtual machines have only 1 LVM partition.
In case of multiple LVM partitions on same server, we can't see browse files and we can only perform full VM restore.
See 2 images in attach that clarify problem.
Do you know about this issue?
Could you fix it in next releases? 
Kind regards

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      VM with multiple LVM partitions - file restore screen.png

                      22.28 KB
                  
              
                      VM with 1 LVM partition - file restore screen.png

                      25.64 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Mon, 10/01/2018 - 14:00

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Evgeny Ryuntyu
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 56
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Nicola,
It's Evgeny from Acronis Service Provider Support.
 
As far as I understand you are facing an issue with the backup browsing in a particular scenario - when a VM backed up agentlessly contains more than 1 LVM partition, they don't appear in the slice's contents.
To confirm when exactly the fix is going to be brought to you within Acronis Data Cloud I would like to ask you to raise a support ticket while specifying the details per our template
This way we will be able to check the version of the product you have, some details about the LVM partitioning for particular machines and suggest on a fix version.
If you have any questions, please feel free to ask. 
 
------------------------------------------------------------------------------------------------
Evgeny Ryuntyu | Senior Support Engineer
Acronis Backup Cloud | #1 Cloud Service Provider Backup

      
                
                
                    
                                                    Tue, 10/02/2018 - 14:15
