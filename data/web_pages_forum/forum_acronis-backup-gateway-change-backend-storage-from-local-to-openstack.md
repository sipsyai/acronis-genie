# Acronis backup gateway - change backend storage from local to OpenStack

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/acronis-backup-gateway-change-backend-storage-local-openstack

## Original Post
**Author:** Unknown

Acronis backup gateway - change backend storage from local to OpenStack

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Eric  Ngun
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
I have create a Acronis storage gateway with local backend storage, and have been working for a while. after that, we change it to OpenStack backend storage (from IBM softlayer). both configure file acronis-storage-gateway.xml and acornis-storage-backend-swift.xml has been modify as per implementation guide. after that, I have re-register it to the cloud backup console, restart both acronis-storage-gateway and acronis-storage-mds service. but the service acronis-storage-gateway are fail with status "active (exited)". below are the error log from journalctl and systemctl. please advise if anybody have an idea, thanks!
 systemctl -l status acronis-storage-gateway
● acronis-storage-gateway.service - SYSV: Acronis Storage Gateway
   Loaded: loaded (/etc/rc.d/init.d/acronis-storage-gateway)
   Active: active (exited) since Sun 2016-09-11 23:24:47 CDT; 20min ago
     Docs: man:systemd-sysv-generator(8)
  Process: 31956 ExecStop=/etc/rc.d/init.d/acronis-storage-gateway stop (code=exited, status=0/SUCCESS)
  Process: 31965 ExecStart=/etc/rc.d/init.d/acronis-storage-gateway start (code=exited, status=0/SUCCESS)
Sep 11 23:24:47 'undisclose_hostname' systemd[1]: Starting SYSV: Acronis Storage Gateway...
Sep 11 23:24:47 'undisclose_hostname' acronis-storage-gateway[31965]: acronis-storage-gateway is stopped
Sep 11 23:24:47 'undisclose_hostname' runuser[31968]: pam_unix(runuser:session): session opened for user acronis by (uid=0)
Sep 11 23:24:47 'undisclose_hostname' runuser[31968]: pam_unix(runuser:session): session closed for user acronis
Sep 11 23:24:47 'undisclose_hostname' acronis-storage-gateway[31965]: Starting acronis-storage-gateway: [  OK  ]
Sep 11 23:24:47 'undisclose_hostname' systemd[1]: Started SYSV: Acronis Storage Gateway.
 
journalctl -u acronis-storage-gateway.service
Sep 11 22:43:41 'undisclose_hostname' systemd[1]: Stopping SYSV: Acronis Storage Gateway...
Sep 11 22:43:42 'undisclose_hostname' acronis-storage-gateway[29743]: Stopping acronis-storage-gateway: [  OK  ]
Sep 11 22:43:42 'undisclose_hostname' systemd[1]: Starting SYSV: Acronis Storage Gateway...
Sep 11 22:43:42 'undisclose_hostname' acronis-storage-gateway[29754]: acronis-storage-gateway is stopped
Sep 11 22:43:42 'undisclose_hostname' runuser[29757]: pam_unix(runuser:session): session opened for user acronis by (uid=0)
Sep 11 22:43:42 'undisclose_hostname' runuser[29757]: pam_unix(runuser:session): session closed for user acronis
Sep 11 22:43:42 'undisclose_hostname' acronis-storage-gateway[29754]: Starting acronis-storage-gateway: [  OK  ]
Sep 11 22:43:42 'undisclose_hostname' systemd[1]: Started SYSV: Acronis Storage Gateway.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 09/12/2016 - 04:50

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Eric  Ngun
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Eugene,
the mentioned steps has been done but not work, I will share you the the ssh login to you through email.

      
                
                
                    
                                                    Tue, 09/13/2016 - 07:57
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Andrew Cho
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I have a question about this.  We have a similar wish to be able to move to a different backend.  For the sake of example, if we have a lot of data that has been backed up to a local storage (for example NFS or file share) and now we would like to migrate all of that to a cloud (for example S3), can that be done?  Please tell me yes or I will be very very sad...
I await your good news...

      
                
                
                    
                                                    Mon, 08/14/2017 - 22:21
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Andrew,
Good news are your wish is basically possible! We can use acrocmd commands to replicate backups from a local storage to a cloud-based location. To do so, you'll need
1. Create a Partner Account in Acronis Backup Cloud.
2. Install Acronis Storage Gateway on a Linux machine and register it in the same Partner group.
3. Tie Acronis Storage Gateway to Amazon S3 (Configuring the gateway).
4. Create a Customer group and a User account in this group.
5. Then install an Agent that will perform replication (you can install it to the same machine with Acronis Storage Gateway or to another machine in the same environment) and register it in the Customer group. The Agent should have access to the storage.
6. On the machine with the Agent find acrocmd and run the following command
acrocmd replicate backup --loc=\\server\share --credentials=netuser,netpassword --arc=archive_name --target=online:// --credentials=abclogin,abcpassword
Where archive_name — name of the archive in the local storage, netuser and netpassword — credentials for the local storage,  abclogin and abcpassword — login and password of User account, that we have registered in the Customer group earlier.
Not so good news are this command doesn't allow to replicate the whole archive, only the last backup in the chain..However, you can select which backup slice to replicate using the commands from https://www.acronis.com/en-gb/support/documentation/AcronisBackup_11.7/… 
I hope, this helps..We've also passed your scenario to the product team, so hopefully we'll have the ability to migrate data to Cloud in the future versions.

      
                
                
                    
                                                    Thu, 08/17/2017 - 14:26
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
