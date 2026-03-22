# Agent Install Failure

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/agent-install-failure

## Original Post
**Author:** Unknown

Agent Install Failure

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    James Burns
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Windows 10 PC. 64bit. 
I am unable to register the agent.   The install hangs at 96% and when trying to register is locks up.  This lock up causes the internet on the entire PC to crash.  After about 5 mins it says it cant register and to do it manually.  After I hit ignore the agent install completes and the internet comes back online.   When trying to manual register using the command prompt I get:
 
Microsoft Windows [Version 10.0.14393]
(c) 2016 Microsoft Corporation. All rights reserved.
C:\Users\James>cd c:\program files\backupclient\backupandrecovery
c:\Program Files\BackupClient\BackupAndRecovery>register_msp_mms.exe register https://cloud.acronis.com XXXXX XXXXXXX
check credentials:  Root (Composite)
   [Is (Common::String) = Msp::Agent::Dto::CheckCredentialsResponse]
   IsValid (bool) = 1
Error 0x1350016: TOL: Failed to execute the command. Setting the registration server address in the backup service
| line: 0x8d165e86fb819595
| file: k:\3917\enterprise\common\tol\command\command.cpp:455
| function: Tol::`anonymous-namespace'::MakeFailResult
| CommandID: BD897884-9F47-4DC0-BC02-DA8DA2BBBD48
| $module: mms_vsa64_3917
|
| error 0x1350016: TOL: Failed to execute the command. Setting the registration server address in the backup service
| line: 0x8d165e86fb819595
| file: k:\3917\enterprise\common\tol\command\command.cpp:455
| function: Tol::`anonymous-namespace'::MakeFailResult
| CommandID: BD897884-9F47-4DC0-BC02-DA8DA2BBBD48
| $module: zmq_infra_vsa64_3917
|
| error 0x2760002: Cannot modify user profile.
| line: 0x8f84435ae6490414
| file: k:\3917\enterprise\msp\agent\commands\set_registration_server_address_logic.cpp:83
| function: Msp::Agent::Commands::SetRegistrationServerAddressLogic::RunLogic
| $module: zmq_infra_vsa64_3917
|
| error 0x273000d: Access violation in module 'zmq_infra.dll' at line '0x8f84435ae6490414', executable: 'mms.exe'.
| line: 0xe839411589f18a1f
| file: k:\3917\enterprise\managers\access\impl\profile_vault_component.cpp:1254
| function: AccessManagement::ProfileVaultComponent::AddAccountToSystemProfile
| $module: access_manager_vsa64_3917
|
| error 0x2730016: Failed to add account in user profile.
| line: 0x53cbdf900173a0cc
| file: k:\3917\enterprise\managers\access\impl\persistent_storage_logic.cpp:735
| function: AccessManagement::Impl::PersistentStorageLogic::AddAccount
| ResourceType: location
| ResourceAddress: jburns@mylitech.com
| ProfileID: 23002D64-E4A6-493D-AA18-BEC82B304E98
| $module: access_manager_vsa64_3917
|
| error 0x26a0014: Failed to encrypt data.
| line: 0x36e942e8021f4b68
| file: k:\3917\enterprise\common\security\core\impl\scrambler_winapi.cpp:61
| function: Scrambler::EncryptData
| CurrentUserName: Office-PC\Acronis Agent User 2
| CurrentUserSID: S-1-5-21-1429379698-1775114435-495884488-1016
| $module: security_core_vsa64_3917
|
| error 0xfff0: The system cannot find the file specified
| line: 0x36e942e8021f4b68
| file: k:\3917\enterprise\common\security\core\impl\scrambler_winapi.cpp:61
| function: Scrambler::EncryptData
| code: 0x80070002
| $module: security_core_vsa64_3917
 
When trying to manually register the agent with the app on the system tray the error is:  An Internal Error has occurred.
 
Please advise.  I have disabled firewall and antivirus ect.   Cant get it to go.
 
Thank you!

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sun, 03/26/2017 - 16:55

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Evgeny Ryuntyu
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 56
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
 
Thanks for contacting Acronis Support via our Forum.
 
It's Evgeny from Acronis Service Providers Support. Your ticket has been assigned to me and I will allocate the appropriate resources in order to lead the ticket to resolution. 
As far as I understand you are facing two issues with the installation of the Agent for Windows of Acronis Backup Cloud: the installation stalls at 96% and the manual registration of the agent is failing with an error.
I will be glad to provide a solution. If the solution below doesn't resolve the issues you observe, please feel free to submit a Support ticket for further investigation by sending an email to mspsupport@acronis.com
 
Based on the error message and internal research, the issue with the registration is related to the fact that WINAPI calls related to encryption doesn't work for the given Windows user in some specific environments. 
Could you please remove the product from the PC, run the executable as administrator and also specify the Administrator in the acccount to run the service (this can be done on the step prior to the actual installation)?
The issue with the installation hanging at 96% is known and will be fixed in one of the next build versions. 
For the moment, I would like to suggest you use the following workaround:
 
Before starting installation create SYSTEM (  IMPORTANT to create system variable, not user one) environment variable EV_BYPASS_ACCEPT_PORT_SANITY_CHECK and set is to any value (eg. "1")
You may create it by running the following command in PowerShell window running with elevated privileges (for example when dealing with core-mode windows with no GUI installed
 [Environment]::SetEnvironmentVariable("EV_BYPASS_ACCEPT_PORT_SANITY_CHECK", "1", "Machine")
Start setup
Please apply the solution and confirm that the issue is resolved. 
If the issue persists, please submit the support request while attaching the logs of the installation.
 
With warm regards,
Evgeny Ryuntyu
Senior Support Specialist – Service Provider Support team | Acronis
Office: +1 781 79 14 486
 

      
                
                
                    
                                                    Mon, 03/27/2017 - 12:31
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    James Burns
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you for the reply.  
I was able to complete the install by running the exe as Administrator and in the install settings I selected "Use Local Account" to register the service.   
With the above settings I was able to complete the install.   I did not have to use Power Shell or any commands to get passed the 96%.  It went to 100% and completed on its own.
 
Thanks again,
 
Jim
 

      
                
                
                    
                                                    Mon, 03/27/2017 - 13:31
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jeremy Wright
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I am still having this same issue. I ran the powershell command but got no where. Running the service as domain admin but it still wont process.

      
                
                
                    
                                                    Fri, 10/20/2017 - 03:05
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jeremy Wright
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            If i hit ignore it completes but i cant login to the services for further setup.

      
                
                
                    
                                                    Fri, 10/20/2017 - 03:09
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi James,
If you are using Acronis Backup Cloud you can always try to manually register the account:
Windows OS
1.
Open Command prompt and navigate to C:\Program Files\BackupClient\BackupAndRecovery: 
cd "C:\Program Files\BackupClient\BackupAndRecovery"
2.
Issue this command to register the client machine: 
register_msp_mms.exe register https://cloud.acronis.com <account> <password>
(Please note to change the values of the "https://cloud.acronis.com, account and password to match what you are using)
If you are using Linux OS:
1.
Open terminal as root user
2.
Type in the following command to register the agent:
/usr/lib/Acronis/BackupAndRecovery/AmsRegisterHelper register https://cloud.acronis.com <username> <password>
(Please note to change the values of the "https://cloud.acronis.com, account and password to match what you are using)
If you are using  OS X:
1.
Open terminal.
2.
Execute:
sudo -u root "/Library/Application Support/BackupClient/Acronis/BackupAndRecovery/AmsRegisterHelper" register https://cloud.acronis.com <login> <password>
(Please note to change the values of the "https://cloud.acronis.com, account and password to match what you are using)
I do hope that this helps you.
Regards

      
                
                
                    
                                                    Wed, 10/25/2017 - 14:55
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Stephan Gaspary
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello
 
I have got the same issue.
I want to install the "Cloud Agent for Windows Server Backup" or "Cloud Backup Agent for ESX" on Windows 2008R2.
First i got error with Port 443:

When i press 'sign in' the installation starts until 97%.
Then the following error occurs:
 

I tried both agents with the same error.
I opened the firewall, but this does not worked.
I tried to register manualy, but the same error as of the treatstarter accurs.
I tried telnet connection to some servers with port 4445, that worked.  
I also set the system variable as mentioned above. That didn't helped.
 
Could you please open a ticket and provide a solution ? 
 
kind regards and greetings from Germany.
Stephan Gaspary
 
 
 
 

      
                
                
                    
                                                    Thu, 11/02/2017 - 17:02
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
                    In reply to Hello… by Stephan Gaspary
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Stephan Gaspary
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello
 
>>>>>>>>>>>>>> I solved this problem !!! <<<<<<<<<<<<<<
 
The problem was, that i configured a 'client' but not a corresponding 'user' in the client section.
I tried to install an agent of a client configuration with the 'superadmin' credentials. That doesen't worked.
 
So i am lucky and my client has a working cloud backup solution.
 
so long....
Stephan Gaspary
 

      
                
                
                    
                                                    Fri, 11/03/2017 - 15:22
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Stephan, thank you for posting back with the solution, this might help other users 

      
                
                
                    
                                                    Tue, 11/07/2017 - 12:12
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Samuyel Alan
                            

            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
we get the same Port error like Stephan Gaspary


After "Sign in" the Installation is Hanging on 97 %
The Error Massege is:
lost Ceonection to Backup Service
 
We used the Domain Admin as Service User and even the Local Admin User.
Nothing would Change the Problem.
 

      
                
                
                    
                                                    Wed, 03/28/2018 - 10:05
