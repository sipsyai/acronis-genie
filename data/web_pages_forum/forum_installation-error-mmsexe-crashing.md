# Installation Error - mms.exe Crashing

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/installation-error-mmsexe-crashing

## Original Post
**Author:** Unknown

Installation Error - mms.exe Crashing

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    nickct
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
We have recently experienced an issue with the mms.exe service crashing after the software has been installed on a physical server endpoint.
I narrowed down the cause and noticed that mms.exe was trying to listen on port 8090. There was another service running on this particular server which also needed 8090.
Is there any way we can change the port the Acronis endpoint mms.exe can listen on? As 8090 is a fairly common secondary port in the scheme of things.
We have so far come across this issue on 2-3 separate machines and I am expecting to come across this much more also.
Is this a known issue, and are there any workarounds?
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 06/29/2016 - 14:53

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Backup Cloud
            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Vyacheslav Bykov
                            

                            
                    
                        Cloud SP Trainer
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 10
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Nickct,
Please be informed that port 8090 is used by Acronis Backup Monitor by default. So the product has detected the port is occupied and then crashed unexpectedly.
In order to fix the issue please proceed the following way:
1) On the client machine, navigate to "Services" and make sure 'Acronis Managed Machine Service" is stopped. If not - stop it.
2) Navigate to the following folder: C:\Program Files\BackupClient\BackupAndRecovery\
3) Rename "mms.exe" to "mms_old.exe".
4) Copy the following file from the FTP to the folder: 
5) Start Acronis Managed Machine Service. Check if machine has appeared in backup console (https://baas.acronis.com) under "Home Run Auto Group" organization. In case it is missing, please register machine manually according to the following KB article: https://kb.acronis.com/content/55244.
Please let me know if the solution above helps to resolve the issue.

      
                
                
                    
                                                    Wed, 06/29/2016 - 18:45
                                                                            
                                
                            
                                            
                                            
    
                    
                Vyacheslav Bykov
Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    nickct
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Vyacheslav,
 
Thank you for providing that updated file, that has fixed the issue with the mms.exe service starting up and the server has now shown up in the management console.
My next question is that naturally after installing this fix the Backup Monitor shows 'An internal error has occured'.
Is there also a fix for this so that it can see the data from the mms.exe service?

      
                
                
                    
                                                    Wed, 06/29/2016 - 23:56
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Backup Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Vyacheslav Bykov
                            

                            
                    
                        Cloud SP Trainer
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 10
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            The custom version of  mms.exe you've been provided  has mms http server disabled. Backup Monitor will not work with it.
The original problem you were facing is oing to be fixed in one of the future updates of Acronis Backup Cloud  - v 7.0

      
                
                
                    
                                                    Thu, 06/30/2016 - 21:22
                                                                            
                                
                            
                                            
                                            
    
                    
                Vyacheslav Bykov
Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                     dialedin
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I am unsure whether this is related, but when attempting to install the Backup 12 client on a Windows workstation, it tells me 443 is closed to outbound traffic, yet I can navigate to https:\\cloud.acronis.com and login.  Registering the client through the command line and the Backup Monitor also errs out.

      
                
                
                    
                                                    Sun, 12/11/2016 - 01:09
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Raphael
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 37
                
            
            
                
                    Comments: 352
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi dialedin,
it might be related to 55944: (Fixed) Acronis Backup Cloud / Acronis Backup Service: Installation Fails with "Enable outgoing connections to the following ports: https://baas.acronis.com:443".
There are different settings for your Acronis Account and Backup Account.

      
                
                
                    
                                                    Sat, 12/17/2016 - 11:30
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect
