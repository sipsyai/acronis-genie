# My ISP use Acronis. But don't work. No valid assistance on it. Please Help

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/my-isp-use-acronis-dont-work-no-valid-assistance-it-please-help

## Original Post
**Author:** Unknown

My ISP use Acronis. But don't work. No valid assistance on it. Please Help

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    andsec
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi guys! My isp use Acronis for backup service to his customer.
No valid assistance. Please Help Me.
I have a Dedicated Server.
With Acronis software gived from ISP is all backup ok. 
But when i try recovey, don't work properly:
The service can't reboot machine (i think) and this error:
recovery blocked to 1% and after give me this error:
{"reason":"internalError","date":"2019-04-01T17:14:35.575942+00:00","troubleshoot":null,"effect":"ZmqGw::JobRunner","cause":"TOL: Activity with ID = 'BE95679C-6834-4243-A46E-F364BFD2E7EC' has no associated worker.","context":{"effect_str":"ZmqGw::JobRunner","operation":"unknown","_internal":"0:0:-1","cause_str":"TOL: Activity with ID = 'BE95679C-6834-4243-A46E-F364BFD2E7EC' has no associated worker."},"serCode":"0x00F90004+0x01350014","origin":{"text":"ZmqGw::JobRunner","linetag":"0x0000000000000000","code":4,"fields":{"$module":"zmq_infra_lxa64_10790"},"module":249,"suberror":{"text":"TOL: Activity with ID = 'BE95679C-6834-4243-A46E-F364BFD2E7EC' has no associated worker.","linetag":"0x6708BE0A5B5D3D67","code":20,"fields":{"$module":"mms_lxa64_10790","TraceLevel":"1"},"module":309,"suberror":null}}}
Internal server error.
Codice errore 100011
01 Apr, 2019, 19:14
 
***********************************
Port are open. Please help me or suggest me where i must see
Thanks a lot!!
andsec
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 04/02/2019 - 11:05

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Agata Serebrennikova
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello andsec,
as quick solution I can suggest you to try the recovery via Bootable Media, please check the following KB:
https://kb.acronis.com/content/54596
However to understand the root cause of the issue we need:
1) account ID- so we can check the logs on our side
2) I suggest verify the connection via the  tool you can find: https://kb.acronis.com/content/47678

      
                
                
                    
                                                    Mon, 04/08/2019 - 03:53
                                                                            
                                
                            
                                            
                                            
    
                    
                Agata Serebrennikova | Senior Support Team Manager, Cloud Team
Acronis Backup Cloud | #1 Cloud Service Provider Backup

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

Customer Service and Support
http://www.acronis.com
