# Acronis Backup Cloud Feature Request

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/acronis-backup-cloud-feature-request

## Original Post
**Author:** Unknown

Acronis Backup Cloud Feature Request

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Nick
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 24
                
            
            
                
                    Comments: 22
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Good day,
We have two feature requests (perhaps these features exists but I haven't been able to figure out how to find them).
1: Rename devices in the cloud console - We would like to be able to change the name from the machine hostname to a different name in the cloud console. Sometime our customers find their hostname convention results in machines with unfriendly names and we would like to rename the devices in the cloud console to ease administration. Is this possible?
2: Change the time that daily alert recaps are send - Would it be possible to add the ability to change when the alert notifications are sent to the users in the cloud management console
Thank you very much for all your efforts.
Nick

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 11/20/2019 - 14:33

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dear Nick
thank you for taking the time to share your suggestions! Passed to the product manager for review

      
                
                
                    
                                                    Mon, 12/09/2019 - 06:34
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Nick,
an update to the requests:
1. This one is in our roadmap (internal ID for ref RM-743), but no ETA so far
For now, you may want using the comments on devices https://www.acronis.com/en-us/support/documentation/BackupService/#39148.html
Comment for a device.
Default value:
-          For physical machines running Windows, the computer description taken from the computer properties in Windows.
-          Empty for other devices.
To view the comment, under Devices, select the device, click Details, and then locate the Comment section.
So, if you have windows machines, you can populate this option by running a script on boot or set this value using Active Directory.
2. Regarding the second question, you can configure active alerts reports in dashboards. In this case, you can configure the scope of customers to include (it can be single report for all customers or separate reports per customer). The report can be scheduled and send to any emails specified.
Thank you! 

      
                
                
                    
                                                    Mon, 12/23/2019 - 09:16
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
