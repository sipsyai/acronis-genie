# Missing/Needed functionality + Bugs

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/missingneeded-functionality-bugs

## Original Post
**Author:** Unknown

Missing/Needed functionality + Bugs

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Cody Poncsak
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello, I had a chance to play with the cloud backup and have a few issues.
1. As its been mentioned before, How is it not possible to rename endpoints? Being a developer of SaaS platforms myself, I don't buy the whole "architecture limitations" excuse. It should be as simple as adding a database column to store a friendly name.
2. How is it not possible to organize endpoints? We image over 100 systems out of our office and its ridiculous that there is no way to organize endpoints. It looks like the only way to do this would be to create separate users for organizational units and use those user accounts to activate endpoints. This is crazy. Why can't we just move endpoints to other organizational units?!
3. There is a bug where the Hyper-V endpoint can not properly detect VM IP addresses in server 2016. It throws the following error: The following Msvm_KvpExchangeDataItem.Name keys are deprecated: NetworkAddressIPv4, NetworkAddressIPv6, RDPAddressIPv4, and RDPAddressIPv6. Please configure guest IP addresses using Msvm_GuestNetworkAdapterConfiguration.
4. When an endpoint is deleted from the system and then re-added, it retains all the previous logs. Which means that the data isn't deleted and uses identifying information from the system to re-link it back to its previous data. Why/how is it doing this? Should the endpoint not be assigned a new ID if its reinstalled with the option to manually link it back to an existing configuration set?
5. Not sure if this bug is related, but I uninstalled and endpoint and then deleted it from the system. Upon reinstall it, I wasn't able to apply the backup policy to the agent. It just got stuck on a spinning "Applying" message. Deleting the policy and re-making it allowed it to be added to the agent. Obviously this is a problem if you have a default policy that applies in most cases.
6. Not sure if this applies to Windows yet but on Linux, the agent doesn't properly detect its own backup destination path and so every image includes the previous images causing backups to increase exponentially.
7. There is no way to request support. Like a previous thread stated, requesting support requires that you activate a product key.
Overall I'm extremely disappointed in the experience I've had so far with the platform. Do you have a road-map or change-log that people can monitor for fixes?
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sat, 12/23/2017 - 04:10

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Evgeny Ryuntyu
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 56
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Cody,
 
My name is Evgeny, I am from Acronis Service Provider Support. 
I would like to respond to the points you raised:
1) This is true that the feature is obvious and we have it on the roadmap - the Program Management team has collected the feedback from multiple Service Providers/Partners, so right now we are working on implementing it within the code of Acronis Data Platform. The ETA is not public at this moment, but we aim to one of the major versions 
2) We are going to introduced such functionality within the version Acronis Data Cloud 8.0 when the funtionality of the on-premise product Acronis Backup Advanced 12.5 is merged. The exact requirements are still discussed, so I cannot commit it will be present as you described your need, but your feedback has been acknowledged by the Program Management team.
3) Could you please elaborate on this point and involve our Support if the issue is reproduced on constant basis? 
4) This is something which can be fixed by removing the logs upon the uninstallation. Depending on the OS the checkbox differs, please take a look at the Web-help article:
https://www.acronis.com/en-us/support/documentation/BackupService/index…
On the other hand the Customer may need to preserve the ID to be able to back up to the same archive. In that case the solution will be to change the MMSCurrentMachineID and InstanceID
https://kb.acronis.com/content/56493
5) This issue requires the investigation from the developers' side, so I would like to suggest you open a ticket with our Service Provider Support team by shooting an email to mspsupport@acronis.com with the description and the ProcessMonitor log gathered while you reproduce the behavior. 
6) If I understood correctly you may fix the behavior by setting up the file filters per the Web-help article below:
https://www.acronis.com/en-US/support/documentation/BackupService/#4080…
7) Generally, you can contact support by the following procedure  but if your account is not registered with the related MSP product, then you can send us an email at mspsupport@acronis.com
 
Best regards,
Evgeny Ryuntyu | Senior Support Engineer
Information provided AS-IS with no warranty of any kind.

      
                
                
                    
                                                    Tue, 12/26/2017 - 13:38
