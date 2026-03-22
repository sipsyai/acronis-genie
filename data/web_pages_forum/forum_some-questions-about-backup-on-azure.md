# Some questions about backup on Azure

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/some-questions-about-backup-azure

## Original Post
**Author:** Unknown

Some questions about backup on Azure

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Luca Ortolan
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi everyone, I have a Vmware infrastructure and I was considering Acronis as backup solution for my virtual machine (the other backup solution we are considering is Veeam). I would to backup my virtual machine on my on-premise repository (it is a NAS) and after, in a second shot, send data to the cloud (in order to respect the 3-2-1 rule). My question is: is it possible to send the backup data to an azure subscription and then (1) recover a single file,or application data, from Azure to my datacenter, without importing all the backup file in advance (in other word, read from my on prem datacenter, the backup file which is on Azure); (2) is it possible to convert the backup (which is stored on Azure) into a virtual machine directy on Azure in order to power it on?
Thank you
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 02/14/2017 - 09:20

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Luca,
Thank you for your question. I'll be glad to answer.
Yes, your scenario is supported. Let me describe which steps are required.
1. Set up Cloud Storage on Azure using Acronis Storage Gateway with Azure backend and register it in you Acronis Backup Cloud partner group.
2. Create a new Customer group and associate it with the new Azure Cloud Storage. Create a new account within the new Customer group.
3. Install an Agent for VMware using account from the new Customer group.
4. Configure a VM backup with following settings:
Entire machine backup
Application-aware feature enabled > specify application credentials for later application-level recovery
Destination: network storage on NAS
Replication enabled: to Cloud Storage
 
Once you complete the first backup, data will become available on you local storage and in Azure. Then you can perform following recovery operations by selecting the required recovery point:
single file recovery
application data recovery
recovery to new VM on a local hypervisor / to new physical machine
run as VM
 
In order to recover a backup into a VM on Azure EC2, do the following, as described in the documentation:
Create a new VM in Azure with Windows/Linux OS installed in it. Make sure to preserve the disk layout as in the source VM that you previously protected
Install an agent for Windows/Linux into the new VM
Using the newly installed Agent, select the backup that you would like to recover, and proceed with "Recover to physical machine" procedure
 
Let me know if you have additional questions.
Best regards,

      
                
                
                    
                                                    Tue, 02/14/2017 - 11:55
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.
