# Bandwidth usage/requirements with overseas storage configured

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/bandwidth-usagerequirements-overseas-storage-configured

## Original Post
**Author:** Unknown

Bandwidth usage/requirements with overseas storage configured

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    D_Bean@hotmail.com
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
I am and end user of Acronis Cloud backup from Chile. My provider has a storage host here in Chile, but while looking at the backups I noticed there are active connections to the storage server, as well as to the Ashburn Va host us-cloud.acronis.com. The connections to Ashburn are on port 7793 and to the Chile based storage server on port 44445.
My questions are these:
Does the backup process transfer any significant amount of content to Ashburn or is this a control connection of some kind ?
Is our backup material proxied through the US ?
Our backup is for a service we offer our clients and there are privacy issues involved, but our key concern is simply that we have very limited international bandwidth. It probably sounds a bit backwards in this day and age, but in Chile domestic bandwidth is far cheaper than international, and as a result the service has much lower bandwidth internationally and that is capped by a restrictor. We are backing up a large amount of data so it is crucial that the actual backup not pass through an international connection.
Is there any technical information available on bandidth usage by the backup agent ?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 01/25/2019 - 11:02

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi,
thank you for your posting! 
Ports 443 and 8443 are used for agent registration, data center selection, user authorization, certificate download, Web Restore and Backup management console access.
Ports 5905, 7770-7800 are used for agent communication with Management server (backup plans creation and applying, status reports, activity logging, etc.).
Port 44445 is used backup read-write operations.
You can additionally open 80 port for your convenience, so any http requests from browser will be redirected to https. Please refer to Knowledge Base article about access ports and hostnames for detailed information at https://kb.acronis.com/content/47189
To limit Output speed during backup during backup go to the Performance tab of the Backup Options and find Output speed during backup. This option defines the priority of the backup process in the operating system. Detailed information is available here https://www.acronis.com/support/documentation/BackupService/index.html#36350.html
Regarding the security measures:
Acronis maintains a comprehensive information security and compliance program that includes administrative, physical, and technical controls based on ongoing risk assessment. Our information security policies and processes are based on broadly accepted international security standards, such as ISO 27001 and NIST.
Also Acronis has implemented an enterprise-wide access control policy to restrict access to information resources and data in accordance with official duties. 
More information about Acronis Cloud security and privacy is available herehttps://kb.acronis.com/content/14188
Let me know, if there are any questions or concerns. 

      
                
                
                    
                                                    Mon, 02/11/2019 - 12:12
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
