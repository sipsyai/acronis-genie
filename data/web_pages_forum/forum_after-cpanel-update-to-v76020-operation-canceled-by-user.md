# After Cpanel update to v76.0.20 -> Operation canceled by user.

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/after-cpanel-update-v76020-operation-canceled-user

## Original Post
**Author:** Unknown

After Cpanel update to v76.0.20 -> Operation canceled by user.

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Michael Brunner
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 21
                
            
            
                
                    Comments: 33
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi
Last night some servers updated cpanel to version v76.0.20. Since then, I have failed backups for a lot of servers. In cloud.acronis.com I only see "Operation canceled by user."
In the /usr/local/cpanel/base/3rdparty/acronisbackup/srv/log/cpanel_meta.log I found the following error:
[2019-02-26 08:12:33] [ERROR] Fail collecting accounts, cannot make metadata for "customer-username".
[2019-02-26 08:12:33] [ERROR] Generating metadata has been failed
Traceback (most recent call last):
  File "/usr/local/cpanel/base/3rdparty/acronisbackup/python/site-packages/acronis_backup_srv/scripts/generate_cpanel_meta.py", line 287, in generate_metadata
    cpanel_meta_collector.collect()
  File "/usr/local/cpanel/base/3rdparty/acronisbackup/python/site-packages/acronis_backup_srv/scripts/generate_cpanel_meta.py", line 276, in collect
    self.collect_accounts()
  File "/usr/local/cpanel/base/3rdparty/acronisbackup/python/site-packages/acronis_backup_srv/helpers.py", line 196, in wrapped
    res = fn(*args, **kwargs)
  File "/usr/local/cpanel/base/3rdparty/acronisbackup/python/site-packages/acronis_backup_srv/scripts/generate_cpanel_meta.py", line 177, in collect_accounts
    self.meta['accounts'][account['uid']] = _make_metadata_for_account(account)
  File "/usr/local/cpanel/base/3rdparty/acronisbackup/python/site-packages/acronis_backup_srv/scripts/generate_cpanel_meta.py", line 162, in _make_metadata_for_account
    emails, filters = self._get_account_emails_and_filters(account_name, home_dir)
  File "/usr/local/cpanel/base/3rdparty/acronisbackup/python/site-packages/acronis_backup_srv/scripts/generate_cpanel_meta.py", line 67, in _get_account_emails_and_filters
    quota = 0 if quota == 'unlimited' else int(quota)
ValueError: invalid literal for int() with base 10: '104857.6'
 

 
Any idea how I can fix this?
Michael

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 02/26/2019 - 07:18

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Michael Brunner
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 21
                
            
            
                
                    Comments: 33
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I was able to fix the problem. Some users had strange values in the email quota file:
/home/*/etc/*/quota
Some users used " unlimited" instead of "unlimited" and some had no values. Both does acronis not handle well.

      
                
                
                    
                                                    Sat, 03/02/2019 - 19:58
