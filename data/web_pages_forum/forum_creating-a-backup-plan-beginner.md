# Creating a backup plan (Beginner)

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/creating-backup-plan-beginner

## Original Post
**Author:** Unknown

Creating a backup plan (Beginner)

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Alvin
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
I'm starting to create a backup plan using Acronis Cyber Cloud for our machines 1 host, 2 VM. Currently, our backup plan is :
1. Backup for entire host server + SAP server(VM) + AD server(VM)
2. Backup for SAP server(VM)
3. Backup for AD server(VM)
Total of 3 backup plans.
Can you suggest simple and better way on how to take backup of the machines? 
Additional question, one of the 2 VMs is a SAP server that runs SQL for backup and stored in NAS. Is it best to enable Application aware backup for this scenario?
Thank you in advance for the suggestions!

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 10/14/2020 - 06:35

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Mikhail Rozhkov
                            

                            
                    
                        Support Engineer 
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 21
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Alvin.
Can you suggest simple and better way on how to take backup of the machines? 

The following table summarizes the available protection plan parameters. Use the table to create a protection plan that best fits your needs:
https://www.acronis.com/en-us/support/documentation/CyberProtectionServ…
Additional question, one of the 2 VMs is a SAP server that runs SQL for backup and stored in NAS. Is it best to enable Application aware backup for this scenario?

If you are backing up the entire machine it is better to enable application-aware backup.
Additional information about application-aware backup can be found by the following link:
https://www.acronis.com/en-us/support/documentation/CyberProtectionServ…

      
                
                
                    
                                                    Mon, 10/26/2020 - 13:25
