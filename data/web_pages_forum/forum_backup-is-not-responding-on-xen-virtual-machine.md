# Backup is not responding on Xen virtual machine

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/backup-not-responding-xen-virtual-machine

## Original Post
**Author:** Unknown

Backup is not responding on Xen virtual machine

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                
                    
                        
            Hello,
Happy New Year!
I installed the agent on a CentOS server running cPanel yesterday (Xen based virtual machine), and while the first and second backup runs were successful, any further backups would fail. The backup process would go to 20% and stop there, after an hour or so I would get an alert that:
Backup is not responding
The running backup has not shown any progress for some time and may be frozen.

I stopped/started acronis_mms, rebooted the server, and even reinstalled the agent software after first deleting the device/agent and backups from the Backup Management Console. After reinstalling the cPanel plugin, the device appeared in BMC as expected but again, the backup process went up until 20% and stopped there.
I suspect this happens because of the dkms module's status: installed-weak
snapapi26, 0.7.117, 2.6.32-696.23.1.el6.x86_64.ksplice-updates, x86_64: installed-weak from 2.6.32-696.23.1.el6.x86_64
snapapi26, 0.7.117, 2.6.32-696.23.1.el6.x86_64, x86_64: installed-weak from 2.6.32-696.23.1.el6.x86_64

 This doesn't explain how/why the first 2 backup runs were successful though.
I have collected system information both before reinstalling the agent (ie when the first two runs were successful and only the following would fail) as well as after.
I'm also attaching part of the /var/lib/Acronis/BackupAndRecovery/MMS/mms.0.log file, from the time the backup job was initiated.
Anybody has any ideas?
Thanks,
George

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      acronis_mms.log

                      11.51 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Tue, 01/01/2019 - 15:38

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi George
Do you have a single backup plan or are there more than one backup plan for this machine?
Regards

      
                
                
                    
                                                    Mon, 01/07/2019 - 06:43
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products
