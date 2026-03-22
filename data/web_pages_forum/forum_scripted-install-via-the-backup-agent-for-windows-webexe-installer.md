# Scripted install via the Backup_Agent_for_Windows_web.exe installer

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-backup-cloud-forum/scripted-install-backupagentforwindowswebexe-installer

## Original Post
**Author:** Unknown

Scripted install via the Backup_Agent_for_Windows_web.exe installer

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Brian
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                
                    
                        
            We would like to deploy Acronis agents via our RMM.  The MSI method of installation requires the MSI and all the neccessary .CAB files to be first uploaded into the same folder.  We would prefer a more streamlined deployment method and so the 13MB web installer seems like the best choice.
From our experience in using the web installer, the EXE downloads the MSI and the necessary CAB files to the C:\Users\username\AppData\Local\TEMP folder and then installs the software.  If  we run Backup_Agent_for_Windows_web.exe with the '--help' parameter then all the commandline options are shown - including the parameter for silent install.  When we run the installer with the following parameters, the install fails.
Backup_Agent_for_Windows_web.exe --quiet --add-components=agentForWindows,commandLine,trayMonitor --reg-token==XXXX-XXXX-XXXX --agent-account=system

The error in the install log is:
1: [15:11:56:837]: PrepareUsers: an error has been thrown:
Error 0x450001: User for 'MMS' service is not specified. Specify 'MMS_SERVICE_USERNAME' and 'MMS_SERVICE_PASSWORD' to install the service on domain controller.
| line: 0x12171f3d4a7b3c9
| file: e:\594\inst_supp\msi_supp\custom_actions\users_and_groups\lib\impl\user_operations.cpp:113
| function: UsersAndGroups::PrepareUser::Execute
| $module: custom_actions_msp_vsa64_s_15300

I don't see a parameter for the "MMS" account, only the agent account, which I specified as 'system'.  Any ideas on how to resolve this? 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 03/11/2020 - 20:21

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ivaylo Tsvetkov
                            

                            
                    
                        Acronis engineer
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 85
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Brian,
I've seen that error for some provisioning systems integrated with Acronis Cyber Cloud. There were some statements that installing the service on a domain controller is not supported. Same 'MMS_SERVICE_USERNAME' and 'MMS_SERVICE_PASSWORD' parameters are not passed from those systems to the installer.
Since you are using your RMM system, I believe you could add values to those parameters and automate it. Here is the guide for unattended installation of a backup agent: https://kb.acronis.com/content/61525
See if that could be a good help for you. All parameters that could be used with the command for silent installation are explained under "Install using Windows Installer (msiexec.exe) and specify parameters manually". I think you can add it to the command itself and it should work. For all parameters you have reference from where the value comes.
Regards,
Ivaylo

      
                
                
                    
                                                    Tue, 03/17/2020 - 16:49
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ivaylo Tsvetkov | API Platform Senior Support Engineer 

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                            
                Products: 
                Acronis Cyber Protect Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Brian
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I found that I needed to specify an account for the "--agent-account" parameter and it worked.  Here is the command that I ultimately used:
Backup_Agent_for_Windows_web.exe --quiet --add-components=agentForWindows,commandLine,trayMonitor --reg-address=us5-cloud.acronis.com --reg-token=XXXX-XXXX-XXXX --agent-account=domain\username:password

 

      
                
                
                    
                                                    Fri, 04/17/2020 - 19:45
                                                                            
                                
                            
                                            
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Brian, thank you for the update\feedback on this topic! 

      
                
                
                    
                                                    Mon, 04/20/2020 - 10:50
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
