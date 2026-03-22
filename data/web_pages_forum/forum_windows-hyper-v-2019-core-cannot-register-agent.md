# Windows Hyper-v 2019 core - cannot register agent

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/windows-hyper-v-2019-core-cannot-register-agent

## Original Post
**Author:** Unknown

Windows Hyper-v 2019 core - cannot register agent

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Jerry Siemek
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
 
I'm using Acronis Cyber Cloud for server backups.
I have recently installed a Hyper-v 2019 core on a server and I want to register that host with Acronis cloud.
I have successfully installed the agent, tried to register with a token, but the portal says
"Check if the machine is online, connected to the network, and the agent setup program displays the registration window. If this is the case and the machine has not appeared under 'Devices', repeat the registration. To obtain a new code, click 'Show registration info' in the agent setup program that is running on the device. Alternatively, click 'Register the machine' in the setup program or Cyber Protect Monitor to directly register the machine."
I tried registering it using command line:
C:\Program Files\BackupClient\RegisterAgentTool>register_agent.exe -a https://eu-cloud.acronis.com --token BAE5-2136-41BD -o register -t cloud
level=err; message=akk error: Internal server error has occured (rc=15), http = {.httpCode = 500, .domain = AGENT_CORE, .code = UNKNOWN_CA}
Failed.
500
{
   "code" : "UNKNOWN_CA",
   "debug" :
   {
      "msg" : "ensure agent registration: test registration with agent manager: Post https://eu-cloud.acronis.com/api/agent_manager/v2/agent_registrations?d…: x509: certificate signed by unknown authority"
   },
   "domain" : "AGENT_CORE"
}
 
I tried to find a solution on https://kb.acronis.com, but couldn't find anything useful.
Anyone tried that in the past and knows any working solution? Please?
 
Thanks
Jerry

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 12/01/2022 - 15:02

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jerry Siemek
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi,
I found the solution described on the website below:
theserverside.technology/2020/06/16/acronis-agent-not-registered-windows-server-core-and-ssl-issues/
 
The problem is with the certificate that Windows core is using, or actually not using. Following the article you can use CMD and/or PowerShell to update Hyper-V core certificate database on your server and then you can register your host with regular command:
register_agent.exe -o register -t cloud -a https://cloud.acronis.com -u <account> -p <password> 
Hope this will help someone :)
Thanks
Jerry

      
                
                
                    
                                                    Fri, 12/02/2022 - 17:26
                                                                            
                                
                            
                                            
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dear Jerry,
thank you for taking the time to share the solution with the community! ⭐️

      
                
                
                    
                                                    Mon, 12/12/2022 - 19:50
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
