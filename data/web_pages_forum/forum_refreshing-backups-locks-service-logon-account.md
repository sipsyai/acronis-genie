# Refreshing backups locks service logon account

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/refreshing-backups-locks-service-logon-account

## Original Post
**Author:** Unknown

Refreshing backups locks service logon account

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Mykhaylo Romaniv
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Refreshing backups locks service logon account (only if from "All devices" menu).
- mentioned account has full access to all backup locations;
- all jobs (backup, restore) are completing successfully;
- from "backup storage" menu refreshing works great.
- problem appear after migration to new hardware and upgrade from v.15 to v.16
Acronis Cyber Protect 16.0.37482.
result:
{
    "code": "error",
    "payload": "{\n   \"agent_result\" : {\n      \"completionResult\" : \"{\\\"code\\\":20250646,\\\"fields\\\":{\\\"$module\\\":\\\"Amms_vsa64_37482\\\",\\\"CommandID\\\":\\\"AEB4DED5A-19BD-4CB7-8D37-BB2C429B286D\\\"},\\\"src\\\":{\\\"file\\\":\\\"d:\\\\\\\\107\\\\\\\\enterprise\\\\\\\\common\\\\\\\\tol\\\\\\\\command\\\\\\\\command.cpp\\\",\\\"func\\\":\\\"Tol::`anonymous-namespace'::MakeFailResult\\\",\\\"line\\\":495,\\\"tag\\\":\\\"0x8d165e86fb8195bd\\\"},\\\"suberror\\\":{\\\"code\\\":20250646,\\\"fields\\\":{\\\"$module\\\":\\\"Adms_provider_vsa64_37482\\\",\\\"CommandID\\\":\\\"AEB4DED5A-19BD-4CB7-8D37-BB2C429B286D\\\"},\\\"src\\\":{\\\"file\\\":\\\"d:\\\\\\\\107\\\\\\\\enterprise\\\\\\\\common\\\\\\\\tol\\\\\\\\command\\\\\\\\command.cpp\\\",\\\"func\\\":\\\"Tol::`anonymous-namespace'::MakeFailResult\\\",\\\"line\\\":495,\\\"tag\\\":\\\"0x8d165e86fb8195bd\\\"},\\\"suberror\\\":{\\\"code\\\":22741008,\\\"fields\\\":{\\\"$module\\\":\\\"Adms_provider_vsa64_37482\\\"},\\\"src\\\":{\\\"file\\\":\\\"d:\\\\\\\\107\\\\\\\\enterprise\\\\\\\\dms\\\\\\\\gst\\\\\\\\providers\\\\\\\\common\\\\\\\\impl\\\\\\\\archive_info_accessor.cpp\\\",\\\"func\\\":\\\"`anonymous-namespace'::ArchiveInfoAccessorOverInternalManager::GetArchivesInfo\\\",\\\"line\\\":197,\\\"tag\\\":\\\"0xdc03ecc21410e65e\\\"},\\\"suberror\\\":{\\\"code\\\":10551497,\\\"fields\\\":{\\\"$module\\\":\\\"Adisk_bundle_vsa64_37482\\\",\\\"IsReturnCode\\\":1},\\\"src\\\":{\\\"file\\\":\\\"d:\\\\\\\\107\\\\\\\\enterprise\\\\\\\\mms\\\\\\\\managers\\\\\\\\archive\\\\\\\\impl\\\\\\\\private_manager.cpp\\\",\\\"func\\\":\\\"ArchiveManagement::PrivateArchiveManager::GetArchivesInfo\\\",\\\"line\\\":1814,\\\"tag\\\":\\\"0xb320396adfe41bb\\\"},\\\"suberror\\\":{\\\"code\\\":10551329,\\\"fields\\\":{\\\"$module\\\":\\\"Adisk_bundle_vsa64_37482\\\"},\\\"src\\\":{\\\"file\\\":\\\"d:\\\\\\\\107\\\\\\\\enterprise\\\\\\\\mms\\\\\\\\managers\\\\\\\\archive\\\\\\\\impl\\\\\\\\local\\\\\\\\local_manager_impl.cpp\\\",\\\"func\\\":\\\"ArchiveManagement::LocalArchiveManagerImpl::GetArchivesInfo\\\",\\\"line\\\":327,\\\"tag\\\":\\\"0xa0f87a51d6f9cceb\\\"},\\\"suberror\\\":{\\\"code\\\":10551497,\\\"fields\\\":{\\\"$module\\\":\\\"Adisk_bundle_vsa64_37482\\\"},\\\"src\\\":{\\\"file\\\":\\\"d:\\\\\\\\107\\\\\\\\enterprise\\\\\\\\mms\\\\\\\\managers\\\\\\\\archive\\\\\\\\meta_info_cache\\\\\\\\meta_info_cache.cpp\\\",\\\"func\\\":\\\"ArchiveManagement::MetaInfoCache::GetArchivesInfo\\\",\\\"line\\\":125,\\\"tag\\\":\\\"0xd5796a33131eeb73\\\"},\\\"suberror\\\":{\\\"code\\\":262145,\\\"fields\\\":{\\\"$module\\\":\\\"Adisk_bundle_vsa64_37482\\\",\\\"function\\\":\\\"ANtOpenFile\\\",\\\"path\\\":\\\"W\\\\\\\\\\\\\\\\?\\\\\\\\UNC\\\\\\\\nts4132\\\\\\\\main\\\\\\\\\\\"},\\\"src\\\":{\\\"file\\\":\\\"d:\\\\\\\\107\\\\\\\\core\\\\\\\\file\\\\\\\\windows\\\\\\\\winnt_dir.cpp\\\",\\\"func\\\":\\\"winnt_dir::iterator::iterator\\\",\\\"line\\\":1389,\\\"tag\\\":\\\"0xf35f747b3b21fc76\\\"},\\\"suberror\\\":{\\\"code\\\":65520,\\\"fields\\\":{\\\"$module\\\":\\\"Adisk_bundle_vsa64_37482\\\",\\\"code\\\":2147944309},\\\"src\\\":{\\\"file\\\":\\\"d:\\\\\\\\107\\\\\\\\core\\\\\\\\common\\\\\\\\error.cpp\\\",\\\"func\\\":\\\"Common::Error::AddWindowsError\\\",\\\"line\\\":314,\\\"tag\\\":\\\"0xbd28fdbd64edb8f8\\\"},\\\"suberror\\\":{},\\\"text\\\":\\\"Wywoływane konto jest obecnie zablokowane i nie można logować się za jego pomocą\\\"},\\\"text\\\":\\\"Error occurred while reading the file.\\\"},\\\"text\\\":\\\"Failed to get information about the archives.\\\"},\\\"text\\\":\\\"Failed to read backup information. The specified vault is probably unavailable.\\\"},\\\"text\\\":\\\"Failed to get information about the archives.\\\"},\\\"text\\\":\\\"Failed to access the backups.\\\"},\\\"text\\\":\\\"TOL: Failed to execute the command. Refreshing recovery points\\\"},\\\"text\\\":\\\"TOL: Failed to execute the command. Refreshing recovery points\\\"}\\n\",\n      \"result\" : \"\"\n   }\n}\n"
}
Please help.
Regards, Mykhaylo

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 06/18/2024 - 07:54

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Mihaylo,
The issue is unexpected and must be investigated, as there aren't any similar issues found in our internal resources.
Please raise a ticket with the team so we can investigate it at https://kb.acronis.com/content/8153.
Feel free to update this thread with any progress or if you face any issues during the process of getting support.
Best regards.

      
                
                
                    
                                                    Tue, 06/18/2024 - 14:34
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Andrey Sh
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Same with our setup
Using dedictated domain account since day 1 when version 12.5 was installed.
this year updated to v15 then 2 weeks later to v16.
password hasn't been changed
When refresh storages using different Agents where account was used to deploy this agent, account becomes  locked.
Does Acronis v16 store credentials globally somewhere? or once entered wrong password Agent will keep it and will lock account?

      
                
                
                    
                                                    Fri, 07/12/2024 - 19:22
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Andrey Shlyonov wrote:

Same with our setup
Using dedictated domain account since day 1 when version 12.5 was installed.
this year updated to v15 then 2 weeks later to v16.
password hasn't been changed
When refresh storages using different Agents where account was used to deploy this agent, account becomes  locked.
Does Acronis v16 store credentials globally somewhere? or once entered wrong password Agent will keep it and will lock account?


Hello!
The credentials should be typed manually. The agent tries to connect with the vault, and if they are correct, it manages to access it. That's how the process works.
If you are sure the credentials are correct when you type them but it gives you errors of "wrong user/password," I advise you to raise a ticket with the team. In the past, there were some similar issues, and it is possible the issue is within the product. Therefore, an investigation is needed to review the root cause.
Best regards.

      
                
                
                    
                                                    Mon, 07/15/2024 - 14:04
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Mykhaylo Romaniv
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Andrey Sh wrote:

Same with our setup
Using dedictated domain account since day 1 when version 12.5 was installed.
this year updated to v15 then 2 weeks later to v16.
password hasn't been changed
When refresh storages using different Agents where account was used to deploy this agent, account becomes  locked.
Does Acronis v16 store credentials globally somewhere? or once entered wrong password Agent will keep it and will lock account?


Andrey,
I also suspect that the problem is related to the upgrade to v.16 (in v.15 everything worked fine). Now my support request has been terminated due to my absence but last suggestions was: 
- change service account's password
- clean GPO's related to account by moving account to another folder in AD without any assigned GPOs.
IMHO, this is snake oil to my problem but I will try to change service account to new one and will keep topic in touch in 1-2 weeks.
 

      
                
                
                    
                                                    Sun, 07/28/2024 - 09:54
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Mykhaylo Romaniv wrote:

Andrey Sh wrote:

Same with our setup
Using dedictated domain account since day 1 when version 12.5 was installed.
this year updated to v15 then 2 weeks later to v16.
password hasn't been changed
When refresh storages using different Agents where account was used to deploy this agent, account becomes  locked.
Does Acronis v16 store credentials globally somewhere? or once entered wrong password Agent will keep it and will lock account?


Andrey,
I also suspect that the problem is related to the upgrade to v.16 (in v.15 everything worked fine). Now my support request has been terminated due to my absence but last suggestions was: 
- change service account's password
- clean GPO's related to account by moving account to another folder in AD without any assigned GPOs.
IMHO, this is snake oil to my problem but I will try to change service account to new one and will keep topic in touch in 1-2 weeks.
 


Hello,
Please reply to the email. By doing so, the case will be re-opened.
Best regards.

      
                
                
                    
                                                    Mon, 07/29/2024 - 16:22
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
