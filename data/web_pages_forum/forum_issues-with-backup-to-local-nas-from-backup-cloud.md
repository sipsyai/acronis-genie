# Issues with backup to local NAS from Backup Cloud

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/issues-backup-local-nas-backup-cloud

## Original Post
**Author:** Unknown

Issues with backup to local NAS from Backup Cloud

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Daniel Hayes
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I have a server that is trying to backup to a NAS locally.
 
I updated the credentials because it was giving an error stating the credentials were invalid:
 
The credentials for network share '\\?\UNC\192.168.0.141\share\[OMITTED].local-EBB803DC-9B4A-49DD-890E-F13287005CE7-7FCB88EC-BB23-43C3-BB13-C0BCB2AEB7EFA.TIB' are incorrect.
 
Once the credentials were updated and the services were restarted I attempted to run a backup again and it states it can't reach the share. After that if I try to browse the backup again it states the credentials are invalid.
 
Things I have found:
1. I can ping the NAS device just fine.
2. I can browse to the UNC path sometimes, by this I mean when navigating to the share it will sometimes come up and show items, other times it will not show items, then sometimes it will state the share can't be accessed.
3. When navigating to the NAS via web ui it gives a 404 error.
 
So from what I am finding I believe this may be a issue with the NAS, most likely some services hung up on it. I am currently investigating that issue, but I want to make sure that I am not going down a unnecessary rabbit hole.
Has anyone experienced this before and am I going about this the right way?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 07/24/2018 - 15:33

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Daniel
I have previously had some issues with backing up to local NAS and there are a few things you can check:
1. The user you are authenticating with needs to have administrative rights on the NAS (So basically read/write)
2. You can try using the IP address instead and if that does not work try the full name of the NAS, but in my experience the IP address does work the best. (So basically try IP address and then hostname of the NAS)
3. You can try and flush dns settings on your local machines (This could resolve the issue of sometimes the share being available and sometimes not)
4. And then lastly you can browse to the NAS from your local machine and add permissions to the parent folder\share
Properties > Security > Add authenticated user with full access to the share.
I do hope that this helps you out.
Best regards

      
                
                
                    
                                                    Thu, 07/26/2018 - 06:51
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products
