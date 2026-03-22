# Agent not showing up in cloud

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/agent-not-showing-cloud

## Original Post
**Author:** Unknown

Agent not showing up in cloud

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Tomas Björn
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi!
I am an MSP that is taking my first steps using Acronis.
Have problems with customers servers not showing up in the dashboard under devices.
Have installed the software on the clients windows-server, and registrered correctly, but the devices does not show up in the dashboard. When i try to "Apply protection plan" in the Windows-agent it says "Cannot connect to server"
I have used the "Connection verification tool"  to test Connection and all is ok.
I have disabled antivirus webroot that i use, and even uninstalled it without solution.
I have uninstalled and reinstalled the agent and reregistered without luck.
I have  tried at different customers (separate tenants) with different servers but get the same problem.
I can see the agents under Settings, Agents, but not under devices.
 
Does anyone have any suggestion about how to move on?
The strange thing is that i have managed to get two servers running (two different tenants), and i can´t see what i did differently with them. 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 07/15/2020 - 07:36

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                MSP using Acronis Cyber Backup
            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Tomas,
thank you for your posting! I'd start with instructions from the article https://kb.acronis.com/content/62569
The general troubleshooting\localization steps also include:
Check for firewalls or anti-virus software
https://kb.acronis.com/content/46430
https://kb.acronis.com/content/36429

Check connectivity to DC with msp_port_checker.
Try telnet to AMS (Acronis Management Server) port received on previous step (e.g. telnet us-cloud.acronis.com 7780).
. If everything is OK, collect Acronis system info report and check MMS log for errors about registration.
You can also check the troubleshooting between the Agent and the Cloud Management Server https://kb.acronis.com/content/59057
6. Check activities in Cyber Protection console to see if the "Adding machine" events were successful. 
If the above steps don't give any clue about the root cause, I'd recommend raising a support ticket, so that our engineers can assist you right away.  

      
                
                
                    
                                                    Wed, 07/15/2020 - 19:43
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Tomas Björn
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you.
All steps seem ok in your tips, but the error remains.
but i see this in the mms-log that i cant seem to figure out why i get?
Can this be the problem?
2020-07-15T23:12:28:533+02:00 16672 I00000000: Using SecurePersistentCredentialStore.
2020-07-15T23:12:30:790+02:00 16672 I00000000: Request to AMS failed with status: 400, body: {"troubleshoot":null,"kb_link":"https://kb.acronis.com/errorcode?ser=0x01350016%2B0x01350016%2B0x00FC00…","origin":{"fields":{"$module":"management_server_lxa64_15900","CommandID":"6D9472EE-5D47-4107-9C6F-43A4273D2EA7"},"suberror":{"fields":{"$module":"ams_backup_assistant_addon_lxa64_15900","CommandID":"6D9472EE-5D47-4107-9C6F-43A4273D2EA7"},"suberror":{"fields":{"$module":"ams_backup_assistant_addon_lxa64_15900","TraceLevel":"4"},"suberror":null,"module":252,"linetag":"0x5B0018A6E6937F50","code":56,"text":"Cannot find an object by the following criteria: ' Root (Composite)\n   [Is (Common::String) = InstanceManagement::Instance]\n   ID (Common::Guid) = E6381DD3-4537-4243-B892-1A07103E29B4\n   Type (j) = 1\n'."},"module":309,"linetag":"0x8D165E86FB8196E0","code":22,"text":"TOL: Failed to execute the command. Backup::Assistant::Commands::ApplyDefaultPlan"},"module":309,"linetag":"0x8D165E86FB8196E0","code":22,"text":"TOL: Failed to execute the command. Backup::Assistant::Commands::ApplyDefaultPlan"},"stacktrace":null,"cause":"Cannot find an object by the following criteria: ' Root (Composite)\n   [Is (Common::String) = InstanceManagement::Instance]\n   ID (Common::Guid) = E6381DD3-4537-4243-B892-1A07103E29B4\n   Type (j) = 1\n'.","context":{"operation":"unknown","cause_str":"Cannot find an object by the following criteria: ' Root (Composite)\n   [Is (Common::String) = InstanceManagement::Instance]\n   ID (Common::Guid) = E6381DD3-4537-4243-B892-1A07103E29B4\n   Type (j) = 1\n'.","_internal":"0:0:-1","effect_str":"TOL: Failed to execute the command. Backup::Assistant::Commands::ApplyDefaultPlan"},"reason":"internalError","effect":"TOL: Failed to execute the command. Backup::Assistant::Commands::ApplyDefaultPlan","date":"2020-07-15T21:12:31.140792+00:00","serCode":"0x01350016+0x01350016+0x00FC0038"}

      
                
                
                    
                                                    Wed, 07/15/2020 - 21:11
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                MSP using Acronis Cyber Backup
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ivaylo Tsvetkov
                            

                            
                    
                        Acronis engineer
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 85
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            



Hello Tomas,
I would suggest opening a Support case as it requires deeper investigation, collection of system information logs and read-only access to your Backup Console from a Support engineer. Provide your Acronis Cyber Cloud account login name, DC of your account, affected tenant group, affected machine, and our Support engineers will investigate it.
We need to take a look on the complete system report from the affected machines, checking the full set of logs.
Thank you.





      
                
                
                    
                                                    Tue, 07/21/2020 - 11:47
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ivaylo Tsvetkov | API Platform Senior Support Engineer 

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                            
                Products: 
                Acronis Cyber Protect Cloud
