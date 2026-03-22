# Problem with Installation Agent on Windows 2012 R2 Hyper-V Edition

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/problem-installation-agent-windows-2012-r2-hyper-v-edition

## Original Post
**Author:** Unknown

Problem with Installation Agent on Windows 2012 R2 Hyper-V Edition

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Toufic Saghbini
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
We are trying to install Acronis agent on a windows 2012 R2 Hyper-V Edition (It is a core edition with Hyper-V role installed on it).
We created an msi and mst files and selected to install Windows Agent and Hyper-V agent.
When we deploy the agent using the msi package, an error shows in the log 'Microsoft Active Directory is not installed on the machine' knowing that we did not choose to install the active directory agent when creating the msi.
Can you please help us on this issue.
Thank you.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 12/02/2016 - 07:32

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Toufic Saghbini
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Attached is the installation log

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      399574-135505.log

                      947.04 KB
                  
          
    

                    
    
                
                
                    
                                                    Fri, 12/02/2016 - 07:36
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Raphael
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 37
                
            
            
                
                    Comments: 352
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi,
Not on Server Core here (and different locale) but when installing Backup Agent for Hyper-V (Backup Agent for Windows is automatically selected during MSI create phase) it succeeds deploying.
I can reproduce your error when selecting Backup Agent for Active Directory during MSI create phase and deploying to the Hyper-V Host.
You can try to re-create the MSI package and deploy again. Maybe it is a Server Core related issue.

      
                
                
                    
                                                    Fri, 12/02/2016 - 16:33
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect
