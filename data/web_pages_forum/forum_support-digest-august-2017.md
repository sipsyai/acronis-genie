# Support Digest: August 2017

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/digests-and-support-best-practices/support-digest-august-2017

## Original Post
**Author:** Unknown

Support Digest: August 2017

        
  



    
  


  
          





    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello Colleagues!
Here is some news on Acronis Cloud Products for August that will help you with your daily support routine:
Hot topics
New KB articles
New training materials
New features
Datacenter updates
Release notes
 
Hot topics
Here are the top 3 questions in August:
  #1 ►Cloud storage quota exceeded and space does not get freed after deleting slices, why?
To understand how quotas work, you need to remember some facts about cloud backup technology and the archive format. Here are the most important ones:
Cloud archives are always incremental and their size cannot decrease. When you remove a recovery point, cloud archive size remains the same, but the freed up space will be re-used by future backups
To free up cloud space you have to remove the entire archive
Cloud console will show updated cloud storage space after 4-6 hours: KB59979
Incomplete cloud backups are not deleted automatically. If you know that some incomplete backups are not needed, you can delete them manually as explained in KB59015
When agent quota is exceeded, the agent download link disappears from the web console. See more here: KB57328
  #2 ►Which ports and IP addresses should be available from agent side?
There is a list of ports and hostnames that you should make available from all agents for successful operation with the cloud components:
Ports 443, 8443, 7770-7800, 44445, 80 will open automatically on the agent during installation, but you should make sure no network firewalls block them
Proxy and NAT can be setup during or after agent installation
Agent will automatically get required hostnames and IP addresses during installation
All hostnames, IP addresses and ports are available here: KB47189
Check that all ports are open with the Connection Verification Tool: KB47678
  #3 ►What to do with slow internet connection? How to upload a large backup?
If the estimated backup time is too long, you can either restart the backup at a later time, or use the Physical Data Shipping service:
Measure the upload speed using the speedtest utility: KB59690
Stop and restart a backup to cloud at any time: KB56049
Offer the Physical Data Shipping service to your Customers: KB56070
Help your Customers to start using the Physical Data Shipping service: KB57604
 
New and hot KB articles
KB59047: Acronis Backup 12.5/12 and Acronis Backup Cloud: "The storage quota is exceeded"
KB60132: Acronis Backup Cloud: incorrect partition is mounted
KB60114: Acronis Backup Cloud: incremental to an initial seeding backup fails with "Failed to create an incremental backup in backup archive"
KB60112: Acronis Backup Cloud: 'An internal error has occurred' in Backup Monitor
See all new KB articles here: https://kb.acronis.com/new
 Did you know that all product related articles are grouped under one URL and organized by relevant topics? Check out this Acronis Backup Cloud link: https://kb.acronis.com/acronis-backup-cloud

 
New training materials
Website backup in Acronis Backup Cloud Product Training
Estimating backup to Cloud Storage in Acronis Backup Cloud Troubleshooting Training
Acronis VSS Doctor in Acronis Backup Cloud Troubleshooting Training
See all training materials here: https://kb.acronis.com/MSPtraining
 Still haven't got certified for support of Acronis Cloud Products? Attend one of our webinars and master the technical side of our cloud products!

 
New features
Website backup. The static contents of websites can be backed up via SFTP/SSH. MySQL databases are backed up either by using a direct connection to the database or over an SSH tunnel.
 Did you know that website backup is the first cloud-to-cloud backup technology to appear in Acronis Service Provider products?

 
Datacenter updates
Datacenter
Platform version
Available services
St. Luis (BETA2)
7.5 Beta
Backup Cloud, Files Cloud
London (EU3)
7.0 Hotfix 3
Backup Cloud
 
Release notes:
7.0 Hotfix 3
 
Share your experience!
What were the things you found easy and what was hard in your experience while supporting Acronis Cloud Products? What do your Customers usually request from you? How do you think we can make your support life easier? Share below your experience and your questions.

      
                                            
                
            
                            
                    
                        
                            
                              Wed, 08/23/2017 - 15:33

                                                          
                                                            
                                                                                        
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                    
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful
