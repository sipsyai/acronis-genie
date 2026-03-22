# Acronics Cyber Protect 16 - Backup Server Machine Itself

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/acronics-cyber-protect-16-backup-server-machine-itself

## Original Post
**Author:** Unknown

Acronics Cyber Protect 16 - Backup Server Machine Itself

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Himanshu Dwivedi
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
 
I have recently deployed an Acronics Cyber Protect Cloud  solution, and everything is running fine. It also has the local HDD as local storage. I can see the backup machine in Device List itself. I just want to know that, how to take the backup of the backup machine it self, removing the backup drive, and also what is the best approach to achieve this.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 08/18/2025 - 16:11

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
That’s not possible.
If you run a backup and select your local HDD as the storage, the backup will remain there. There’s no way to remove it without losing all the data.
If you need to move backups between nodes, please follow this guide:
? How to move backups between storage nodes
Alternatively, you can create a new backup plan from scratch and select a different storage location.
If you have any questions, please contact our support team or your service provider so we can guide you properly.
Best regards.

      
                
                
                    
                                                    Wed, 08/20/2025 - 19:16
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Himanshu Dwivedi
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            José P. Magalhães wrote:

Hello!
That’s not possible.
If you run a backup and select your local HDD as the storage, the backup will remain there. There’s no way to remove it without losing all the data.
If you need to move backups between nodes, please follow this guide:
? How to move backups between storage nodes
Alternatively, you can create a new backup plan from scratch and select a different storage location.
If you have any questions, please contact our support team or your service provider so we can guide you properly.
Best regards.


FYI I am using on prem management server not managed by cloud. Customer is asking, if the backup machine it self get corrupted, they mean the C drive, how to recover, we should have something. 

      
                
                
                    
                                                    Thu, 08/21/2025 - 16:41
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Himanshu Dwivedi wrote:

José P. Magalhães wrote:

Hello!
That’s not possible.
If you run a backup and select your local HDD as the storage, the backup will remain there. There’s no way to remove it without losing all the data.
If you need to move backups between nodes, please follow this guide:
? How to move backups between storage nodes
Alternatively, you can create a new backup plan from scratch and select a different storage location.
If you have any questions, please contact our support team or your service provider so we can guide you properly.
Best regards.


FYI I am using on prem management server not managed by cloud. Customer is asking, if the backup machine it self get corrupted, they mean the C drive, how to recover, we should have something. 


This thread is intended for Acronis Cyber Protect Cloud, not for Acronis Cyber Protect 15/16.
If the backup machine becomes corrupted, it is important to ensure that backups are stored on different disks or in the cloud. Otherwise, the data may be lost, which is expected in such cases.
It is not advisable to keep backups in a single location. We recommend adding backups to secondary storage locations (additional disks, cloud, etc.) for better protection.
Best regards.

      
                
                
                    
                                                    Mon, 09/01/2025 - 09:28
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
