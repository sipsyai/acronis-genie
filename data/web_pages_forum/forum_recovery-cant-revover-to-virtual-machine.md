# [Recovery] Can't Revover to Virtual Machine

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/recovery-cant-revover-virtual-machine

## Original Post
**Author:** Unknown

[Recovery] Can't Revover to Virtual Machine

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Doddy  Listyo
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Dear Master,
I would like to ask, why i can't do recover my backup to virtual machine..
I created virtual machine white vmware, that machine was detected on Acronis mapping. But when i want to recover my backup to that vmware it always appear error 
TOL: Failed to execute the command. Recovery::VM::Assistant::Commands::SetVmRestoreDestination
Cannot recover the virtual machine to the target host because this host is managed by another agent. Only virtual machines whose backups are located in the cloud storage or on a network share can be recovered to a host managed by another agent.
Error code 0x01350016+0x01350016+0x021F001F+0x021F001E
What should i do to recover backup from my PC to VMware, Please kindly your support.
 
Thanks and Regards,
Doddy Listyo

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      capture_failed_machine_to_vmware.png

                      49.7 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Fri, 03/10/2017 - 09:55

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Doddy,
Thanks for posting your question here.
According to the error message, the agent that should perform recovery, cannot connect to the location with the backup. This can happen if the backup was created in a local folder or in an isolated network folder.
To succeed with the recovery, you have to make sure that the Agent for VMware can browse the specified backup location.
Detect the Agent for VMware that is managing the host with target VM Doddy-Win7(64).
Go to Backups tab and in "Machine to browse from" select the Agent for VMware from step 1.
In Locations detect the folder where your backup is located or click + Browse and add respective location. If the location or backup file are not available, make sure the folder is shared and permissions are granted.
Once you detect the backup file with the Agent for VMware, from the same page to to Show backups tab and start recovery to the existing VM.
Looking forward to your reply whether this was helpful.
Best regards,

      
                
                
                    
                                                    Fri, 03/10/2017 - 10:48
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.
