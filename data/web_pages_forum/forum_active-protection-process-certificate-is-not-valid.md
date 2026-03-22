# active protection - Process certificate is not valid

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/active-protection-process-certificate-not-valid

## Original Post
**Author:** Unknown

active protection - Process certificate is not valid

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Darko Bazulj
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                
                    
                        
            active protection
agent : 12.5.15300
how to exclude network process or folder?
If I set network trusted process or folder I get this error [The list of trusted processes must not contain network paths.] and if I set only process name I get [Ensure that the paths in the list of trusted processes are valid and do not contain reserved characters: <>:"|]
I need this because I'm receiving error in screen shoot 


      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      2020-02-16_9-11-57.png

                      45.95 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Sun, 02/16/2020 - 08:09

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ivaylo Tsvetkov
                            

                            
                    
                        Acronis engineer
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 85
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Darko,
Double-check that you have specified the full path to the process executable and the exclusions are set correctly, starting with the drive letter. For example for Windows it would be: C:\Windows\Temp\example.exe
If done correctly you could experience an issue caused by an empty string in Active Protection exclusions/trusted processes list. Empty filter could not be applied so the Agent re-applies exclusions indefinitely which results in new unexpected activities.
In Folder exclusions, specify a list of folders where file changes will not be monitored, and then click Done.
If you still face an issue, I would suggest opening a support case, so our engineers could investigate what's causing the issue.

      
                
                
                    
                                                    Wed, 02/19/2020 - 09:32
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ivaylo Tsvetkov | API Platform Senior Support Engineer 

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                            
                Products: 
                Acronis Cyber Protect Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Darko Bazulj
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Ivaylo,
exclusion with local path is working normal but problem is with with network paths like
\\some-server\some-share\folder1
If I enter network path I get error [The list of trusted processes must not contain network paths.]
Do you have some idea how to exclude network file/folder?
Regards,
Darko Bazulj

      
                
                
                    
                                                    Thu, 02/20/2020 - 17:04
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ivaylo Tsvetkov
                            

                            
                    
                        Acronis engineer
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 85
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Darko,
As I discussed it and verified with RnD, excluding network paths is not supported with Acronis Backup Cloud 8.0
Meaning that getting the error [The list of trusted processes must not contain network paths.] is expected as this is developed by design. You can't exclude network files/folders at this stage.
Regards,
Ivaylo

      
                
                
                    
                                                    Wed, 03/04/2020 - 00:00
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ivaylo Tsvetkov | API Platform Senior Support Engineer 

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                            
                Products: 
                Acronis Cyber Protect Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Darko Bazulj
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            is there plan to add this option in ver. 9 ?
Regards,
Darko Bazulj

      
                
                
                    
                                                    Tue, 08/18/2020 - 15:52
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ivaylo Tsvetkov
                            

                            
                    
                        Acronis engineer
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 85
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Darko,
There is no current plan to make this functionality available for Cyber Protect Cloud v.9.
I will check with the Product Improvement team for if it could be added for future versions.
I will post back when I get a reply.

      
                
                
                    
                                                    Thu, 08/20/2020 - 19:21
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ivaylo Tsvetkov | API Platform Senior Support Engineer 

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                            
                Products: 
                Acronis Cyber Protect Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ivaylo Tsvetkov
                            

                            
                    
                        Acronis engineer
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 85
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Darko,
Epic was added to future Roadmap and backlog, to support network drives as a source.
There is no ETA time for implementation while in backlog, for now it is planned.
Thank you.

      
                
                
                    
                                                    Fri, 08/21/2020 - 08:00
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ivaylo Tsvetkov | API Platform Senior Support Engineer 

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                            
                Products: 
                Acronis Cyber Protect Cloud
