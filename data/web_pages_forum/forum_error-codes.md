# Error Codes

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/error-codes-0

## Original Post
**Author:** Unknown

Error Codes

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Rie Tsuruga
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
I'm new to this. Is there somewhere one can check what various error codes means? Right now I have a failing system state backup 
Don't know what or where to look for with this info:
DATE AND TIME
Nov 18, 2020, 11:07:08 AM
CODE
0x01350016+0x01350016+0x01C90009
MODULE
309
MESSAGE
TOL: Failed to execute the command. Remote registration

Additional info:
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819597
Fields: {"$module":"management_server_vsa64_16363","CommandID":"2B220C98-B8C2-428D-98B7-5C54AEBC8713"}
Message: TOL: Failed to execute the command. Remote registration
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819597
Fields: {"$module":"remote_installation_addon_vsa64_16363","CommandID":"2B220C98-B8C2-428D-98B7-5C54AEBC8713"}
Message: TOL: Failed to execute the command. Remote registration
------------------------
Error code: 9
Module: 457
LineInfo: 0x2485EABA0A7242FD
Fields: {"exitCode":"5","$module":"acroinst_vs_s_16363","httpBody":"{\"context\":{\"$module\":\"mms_rest_api_vsa64_16363\"},\"domain\":\"global\",\"origin\":{\"code\":92,\"fields\":{\"$module\":\"mms_rest_api_vsa64_16363\"},\"linetag\":\"0x487816542fd36b0a, d:\\\\235\\\\enterprise\\\\rest_api\\\\agent\\\\registration.cpp:1391, AgentRestApi::`anonymous-namespace'::Register\",\"module\":0,\"suberror\":{\"code\":1,\"fields\":{\"$module\":\"mms_rest_api_vsa64_16363\",\"curlResult\":\"\",\"host\":\"BACKUPSERVER\",\"port\":\"\",\"requestType\":\"GET\",\"uri\":\"BACKUPSERVER/api/resource_manager/v1/agents/DB9297E2-EA47-46AE-AB63-EF4B4BEC1A17/tenant\"},\"linetag\":\"0xcbd0886296318956, d:\\\\235\\\\enterprise\\\\common\\\\http\\\\curl_transport.cpp:417, Http::Curl::CurlDetails::RequestScope::MakeError\",\"module\":583,\"suberror\":{\"code\":28,\"fields\":{\"$module\":\"mms_rest_api_vsa64_16363\"},\"linetag\":\"0xcbd0886296318955, d:\\\\235\\\\enterprise\\\\common\\\\http\\\\curl_transport.cpp:416, Http::Curl::CurlDetails::RequestScope::MakeError\",\"module\":550,\"suberror\":null,\"text\":\"Connection timed out after 20000 milliseconds\"},\"text\":\"HTTP transfer error\"},\"text\":\"Server unavailable.\"},\"reason\":\"internalError\",\"serCode\":\"0x0000005c+0x02470001+0x0226001c\"}\r
\r
","httpStatus":"503"}
Message: Failed to connect to the management server.
 
 
Any help would be so much appreciated. Thank you.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 12/09/2020 - 03:03

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Mikhail Rozhkov
                            

                            
                    
                        Support Engineer 
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 21
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Rie.
In most cases such issues are caused by closed ports on the machine.
To check them - please follow https://kb.acronis.com/content/47678 
If all ports are open please submit a support ticket as described by the following link: https://kb.acronis.com/content/56079

      
                
                
                    
                                                    Mon, 12/14/2020 - 14:40
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Rie Tsuruga
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Mikhail Rozhkov wrote:

Hello Rie.
In most cases such issues are caused by closed ports on the machine.
To check them - please follow https://kb.acronis.com/content/47678 
If all ports are open please submit a support ticket as described by the following link: https://kb.acronis.com/content/56079


I see. Will try this. Thank you so much!
Happy holidays. 

      
                
                
                    
                                                    Mon, 12/28/2020 - 07:15
