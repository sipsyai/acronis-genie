# Agent Installation

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/agent-installation

## Original Post
**Author:** Unknown

Agent Installation

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Lesha30
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi All,
I'm trying to install an agent on a Windows 7 workstation, but it fails everytime no matter what I try. Please see the log file attached.
Please help!

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      backupclient.txt

                      3.47 MB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Thu, 11/19/2015 - 21:53

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Evgeny Ryuntyu
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 56
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
 
My name is Evgeny, I am from Acronis Service Providers Support.
As far as I understand you have faced an issue with the installation of Acronis Backup Cloud (v4.2 - Agent build - 1588).
The error message indicates that there was a fatal error during the installation:
 
MSI (s) (9C:F0) [13:37:12:731]: Executing op: CustomActionSchedule(Action=MsiRemoteAgCoreInstall_AgentCore__I,
ActionType=3073,Source=BinaryData,Target=MsiRemoteAgCoreInstall,
CustomActionData=C:\Users\SMBCLO~1\AppData\Local\Temp\tmp9824.tmp)
MSI (s) (9C:70) [13:37:13:557]: Invoking remote custom action. DLL: C:\Windows\Installer\MSI78EA.tmp, 
Entrypoint: MsiRemoteAgCoreInstall
1: MsiRemoteAgCoreInstall: started. 
1: Install certificate at 'file:///C:\Program Files (x86)\Common Files\Acronis\Agent\certificate.pem' 
1: MSIGEN:AgentCore install::Install, res=2 
1: MSIGEN:AgentCore install error code 2 
1: MSIGEN:CommonError: code:3113460, message:, linetag:0431AC2339A572BB6h
CommonError: code:65520, message:Fatal error during installation, linetag:0BD28FDBD64EDB8BCh 
1: MSIGEN:SendMessageToInstaller: started 
1: MSIGEN:SendMessageToInstaller: MsiCreateRecord succeeded 
1: MSIGEN:SendMessageToInstaller: MsiRecordSetStringW succeeded 
{09FC4C04-FD7F-4f4c-967A-62597EBA9218} Common::Error (Base64) = 77u/PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiID8+
DQo8WE1MX1NFUklBTElaRVI+DQoJPFNlcmlhbGl6ZWRPYmplY3Q+DQoJCUFmU0JMd0MySzFlYU04SWFRd0FrYlc5a2RXeGxBRmRET2x4WGFXNWtiM2R6WEVsd
WMzUmhiR3hsY2x4TlUwazNPRVZCTG5SdGNBQUE4UDhBQUx5NDdXUzkvU2k5Um1GMFlXd2daWEp5YjNJZ1pIVnlhVzVuSUdsdWMzUmhiR3hoZEdsdmJnQmpi
MlJsQUU1REJnZUFBQUFBQUFBPQ0KCTwvU2VyaWFsaXplZE9iamVjdD4NCjwvWE1MX1NFUklBTElaRVI+DQo=
1: MSIGEN:SendMessageToInstaller: message sent 
CustomAction MsiRemoteAgCoreInstall_AgentCore__I returned actual error code 1603 (note this may not be 100% accurate 
if translation happened inside sandbox)
Action ended 13:38:01: InstallFinalize. Return value 3. 
We have seen such an error when the Acronis Cleanup Utility was used prior to installing the Agent.
If this is true, please go to services.msc and remove any Acronis services left with commands:
sc delete <servicename>
like
sc delete AcronisAgent
sc delete mmsThen please retry the installation from the .exe installer.
If the issue persists, please create a support ticket by sending an email with the fresh installation log to mspsupport@acronis.com
 
With regards,
Evgeny Ryuntyu
Acronis Service Providers Support

      
                
                
                    
                                                    Fri, 11/20/2015 - 10:48
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Pat Young
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            And I'm trying to just find the link to download the backup agent so I can get my server to show up on the cloud backup. Where is that???? It won't let me get beyond the opening page. I've clicked on the agreement page but nothing.

      
                
                
                    
                                                    Tue, 11/01/2016 - 13:11
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Pat,
Welcome to Acronis forums! First of all we'll need to know what product are you attempting to install. Is it Acronis Backup Cloud or Acronis Backup 12? Under your account I see a trial version of Acronis Backup 12 only. To install a trial version of Acronis Backup 12 please follow the steps from this article. You'll need to log in to your Acronis account at https://account.acronis.com/auth/login, find Acronis Backup under Products tab and choose whether you want to use cloud management (with all management components located in Acronis data centers and only backup agents installed in your environment) or install all components on-premises, and then start your free trial. I've attached screenshots.
Thank you, 

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      397664-135019.png

                      129.19 KB
                  
              
                      397664-135022.png

                      34.64 KB
                  
              
                      397664-135025.png

                      69.2 KB
                  
              
                      397664-135028.png

                      66.13 KB
                  
          
    

                    
    
                
                
                    
                                                    Mon, 11/07/2016 - 11:26
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jeetendra Kumar
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I had added an agent but deleted during test. Now when I am trying to add, it gives message, "Agent already exists" and does not allow to add.
 
Please help.
 
 

      
                
                
                    
                                                    Mon, 02/13/2017 - 09:36
