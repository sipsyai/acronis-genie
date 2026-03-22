# Failed Acronis Cyber Cloud O365 mail backup

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/failed-acronis-cyber-cloud-o365-mail-backup

## Original Post
**Author:** Unknown

Failed Acronis Cyber Cloud O365 mail backup

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Lemoning
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 52
                
            
            
                
                    Comments: 75
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello.
This is a cloud product inquiry.
My client uses Acronis Cyber ​​Cloud to back up O365 mail.
I have had no problems for several months getting my mail backups using Acronis Cyber ​​Cloud.
However, since recently, more than 3 to 10 random mail backups fail every day as the following error message is displayed.
------------------------
Thrown .NET exception 'System.Net.WebException': The underlying connection was closed. Send unexpected error. Exception stack trace: Location: System.Web.Services.Protocols.WebClientProtocol.GetWebResponse(WebRequest request) Location: System.Web.Services.Protocols.HttpWebClientProtocol.GetWebResponse(WebRequest request) Location: System.Web.Services.Protocols.SoapHttpClientProtocol. Invoke(String methodName, Object[] parameters) Location: ComEwsAdapter.ExchangeWebService.ExchangeServiceBinding.GetFolder(GetFolderType GetFolder1) Location: MsExchange.Ews.ReTryStrategy.DoTry[TReturn,TArg](TCallDelegate`2 call, TArg arg) Location: MsExchange.Ews.ReTryStrategy.DoTry[TReturn,TArg](TCallDelegate`2 call, TArg arg). Ews.ReTryExchangeServicePoint.GetFolder(GetFolderType getFolder) Location: MsExchange.Ews.ExchangeConnectionEngine.CheckConnection(IExchangeServicePoint service, RootObjectServicesProvider root) Location: MsExchange.Ews.ExchangeServiceFactory.GetService() Location: MsExchangeConnection..ctor() Location: MsExchange.Ews. NetworkCredential user, RootObject root, ConnectionOptions options) Location: MsExchange.Ews.ExchangeConnection..ctor(String url, Credentials user, RootObject root, ConnectionOptions options) Location: MsExchange.Ews.Exchang eClient.ConnectToAsUser(String url, Credentials user, RootObject root, ConnectionOptions options, IExchangeConnection& connection)
Additional information:-----------
Error code: 20250646
Field: {"$module":"service_process_vsa64_27904","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"}
Message: TOL: Failed to execute the command. back up
------------------------
Error code: 20250646
Field: {"$module":"gtob_backup_command_addon_vsa64_27904","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"}
Message: TOL: Failed to execute the command. back up
------------------------
Error code: 40829031
Field: {"$module":"arx_agent_fork_vsa64_27904","IsReturnCode":1}
Message: A generic error of Microsoft Exchange backup component.
------------------------
Error code: 5963794
Field: {"$module":"arx_agent_fork_vsa64_27904","IsReturnCode":1}
Message: Failed to back up document container.
------------------------
Error code: 5964060
Field: {"$module":"arx_agent_fork_vsa64_27904"}
Message: Nothing was backed up. See log for details. Last error:
------------------------
Error code: 5963787
Field: {"$module":"arx_agent_fork_vsa64_27904"}
Message: Could not open public folder or mailbox 'example@customer.com'.
------------------------
Error code: 1
Field: {"$module":"arx_agent_fork_vsa64_27904","uri":"https-outlook.office365.com-EWS-Exchange.asmx"}
Message: Failed to connect to Microsoft Exchange API using the following URL 'https-outlook.office365.com-EWS-Exchange.asmx'
------------------------
Error code: 5966877
Field: {"$module":"arx_agent_fork_vsa64_27904"}
Message: Error within COM EWS adapter.
------------------------
Error code: 5966892
Field: {"$module":"arx_agent_fork_vsa64_27904"}
Message: Thrown .NET exception 'System.Net.WebException': The underlying connection was closed. Send unexpected error.
Exception stack trace: Location: System.Web.Services.Protocols.WebClientProtocol.GetWebResponse(WebRequest request)
Location: System.Web.Services.Protocols.HttpWebClientProtocol.GetWebResponse(WebRequest request)
Location: System.Web.Services.Protocols.SoapHttpClientProtocol.Invoke(String methodName, Object[] parameters)
Location: ComEwsAdapter.ExchangeWebService.ExchangeServiceBinding.GetFolder(GetFolderType GetFolder1)
Location: MsExchange.Ews.ReTryStrategy.DoTry[TReturn,TArg](TCallDelegate`2 call, TArg arg)
Location: MsExchange.Ews.ReTryExchangeServicePoint.GetFolder(GetFolderType getFolder)
Location: MsExchange.Ews.ExchangeConnectionEngine.CheckConnection(IExchangeServicePoint service, RootObjectServicesProvider root)
Location: MsExchange.Ews.ExchangeServiceFactory.GetService()
Location: MsExchange.Ews.ExchangeConnection..ctor(String url, NetworkCredential user, RootObject root, ConnectionOptions options)
Location: MsExchange.Ews.ExchangeConnection..ctor(String url, Credentials user, RootObject root, ConnectionOptions options)
Location: MsExchange.Ews.ExchangeClient.ConnectToAsUser(String url, Credentials user, RootObject root, ConnectionOptions options, IExchangeConnection& connection)
------------------------
(All forward slashes were changed to hyphens because hyperlinks should not be included in the content.)
I googled the error message, but couldn't find it.
What actions are needed to resolve this issue?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 10/14/2021 - 00:59

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Olaf Engelke
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 22
                
            
            
                
                    Comments: 42
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I can confirm this issue for multiple customers using Acronis Cyber Backup for local Office 365 backups.
If you repeat the same task, the issue may happen again on other mailboxes. Started to pop up around Monday or Tuesday last week.
Best greetings from Germany
Olaf

      
                
                
                    
                                                    Mon, 10/18/2021 - 13:34
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Lemoning
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 52
                
            
            
                
                    Comments: 75
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
As a temporary workaround, we spread the backup window.
(For example, the existing schedule backed up the mail of 90 people at 1 o'clock. Now, the schedule has been changed to backup 30 people at 1 o'clock, 30 people at 2 o'clock, and 30 people at 3 o'clock.)
It's been about 3 days since the change, and so far no issues have occurred.
We will have to wait a few more days to see if the same problem occurs again.
Thank you.

      
                
                
                    
                                                    Wed, 10/20/2021 - 00:40
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Lemoning
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 52
                
            
            
                
                    Comments: 75
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
When I checked the condition today, I still have the same symptoms.
Thank you.

      
                
                
                    
                                                    Thu, 10/21/2021 - 03:43
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Olaf Engelke
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 22
                
            
            
                
                    Comments: 42
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            The same still here - and an increasing number of fails.
Best greetings from Germany
Olaf

      
                
                
                    
                                                    Tue, 10/26/2021 - 05:58
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Lemoning
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 52
                
            
            
                
                    Comments: 75
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I don't know if this is the correct workaround.
However, since October 30, after taking the action, there have been no problems.
I solved the problem by adding below registry value in CMD window. (TLS 1.2 Activation Registry)
> reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Client" /v Enabled /t REG_DWORD /d 1 /f > reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\ Protocols\TLS 1.2\Client" /v DisabledByDefault /t REG_DWORD /d 0 /f > reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Server" /v Enabled /t REG_DWORD /d 1 /f > reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Server" /v DisabledByDefault /t REG_DWORD /d 0 /f
thank you.

      
                
                
                    
                                                    Mon, 11/01/2021 - 23:56
                                                                            
                                
                            
                                            
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Olaf Engelke
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 22
                
            
            
                
                    Comments: 42
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            The issue had been fixed for a while (I assume on the MS side) but is now back since 24th January for insite backups with Acronis Cyber Backup 15.
Best greetings from Germany
Olaf

      
                
                
                    
                                                    Fri, 02/04/2022 - 07:47
