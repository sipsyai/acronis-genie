# Registration error windows client

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/registration-error-windows-client

## Original Post
**Author:** Unknown

Registration error windows client

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Rafael Frias
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi, i'm trying to install cyber protect on a windows server and i'm getting this every time, if someone can help me to resolve this. After registration fails it says run this command on the RegisterAgentTool.

Thanks,

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 07/24/2020 - 21:26

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    David Cocke
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Not sure if this will help, but this looks similar to something I recently encountered.  My previous instructions that used to work are like yours in that I specified https://cloud.acronis.com but registration would fail.  But when I tried using our assigned datacenter of https://us5-cloud.acronis.com/ then it worked.

      
                
                
                    
                                                    Mon, 07/27/2020 - 20:33
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Rafael Frias
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            David Cocke wrote:

Not sure if this will help, but this looks similar to something I recently encountered.  My previous instructions that used to work are like yours in that I specified https://cloud.acronis.com but registration would fail.  But when I tried using our assigned datacenter of https://us5-cloud.acronis.com/ then it worked. 


Thanks for your answer but having the same result 

      
                
                
                    
                                                    Tue, 07/28/2020 - 13:53
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ivaylo Tsvetkov
                            

                            
                    
                        Acronis engineer
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 85
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Rafael,
Please make sure ports 443 and 8443 are open in Firewall. These ports are used for agent registration, data center selection, user authorization, certificate download. Then try again the same steps:
1. Open Command prompt and navigate to C:\Program Files\BackupClient:
cd "%ProgramFiles%\BackupClient\RegisterAgentTool"
2. Issue below command to register the client machine using account and password:
register_agent.exe -o register -t cloud -a https://DC-cloud.acronis.com -u <account> -p <password>
where -u <account> -p <password> are login and password for the backup user account, and also replace DC with your datacenter address prefix like advised by David Cocke.
If it still fails we would suggest opening a support case, providing all details of the issue, your DC and affected Cloud account login used in the above command.
Hope this helps.

      
                
                
                    
                                                    Fri, 07/31/2020 - 08:39
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ivaylo Tsvetkov | API Platform Senior Support Engineer 

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                            
                Products: 
                Acronis Cyber Protect Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Stephan Reis
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello, I also have the problem that I cannot register a machine. Ports tested via telnet and are open. But when trying to register a port using the register_agent, I get error 500 with the text "cant open pipe". I have several machines running and they could register without any problem.


      
                
                
                    
                                                    Mon, 08/03/2020 - 08:24
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Stephan Reis wrote:

Hello, I also have the problem that I cannot register a machine. Ports tested via telnet and are open. But when trying to register a port using the register_agent, I get error 500 with the text "cant open pipe". I have several machines running and they could register without any problem.


Hello Stephan,
if the suggestion shared by my colleague in the earlier comments didn't help to solve the issue, we'd strongly recommend raising a support ticket. When opening a case with Acronis Customer Central please collect and provide System Report from the affected machine https://kb.acronis.com/content/54608 (see the part "Acronis Agent is not installed or machine is offline")

      
                
                
                    
                                                    Fri, 08/07/2020 - 11:41
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Stephan Reis wrote:

Hello, I also have the problem that I cannot register a machine. Ports tested via telnet and are open. But when trying to register a port using the register_agent, I get error 500 with the text "cant open pipe". I have several machines running and they could register without any problem.


Hi, 
Not sure if you've fixed it already, but can you check if you have anything running on port 9999?
Run:netstat -ano | findstr 9999
	to find the PID of the process listening on 9999
Run:tasklist /svc /fi "pid eq <PID>"
	where <PID> is the process ID found in step 1.
If yes, head over to C:\ProgramData\Acronis\Agent\etc\aakore.yaml and change port 9999 in linehttp: 127.0.0.1:9999
to another port that is not currently in use.
Finally restart aakore service and try again.
Reference: https://kb.acronis.com/content/64771

      
                
                
                    
                                                    Wed, 08/12/2020 - 14:15
