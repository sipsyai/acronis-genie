# Backup plan best practice

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/backup-plan-best-practice

## Original Post
**Author:** Unknown

Backup plan best practice

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Systems Operations Biznet GIO
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
I've been using Acronis Cyber Protect cloud to backup hundred VM inside VMware. I use one vmware agent (windows server) to backup all VM entire machine daily. All VMs have different size and spec.
Is there any best practice for backup plan to backup all this VM daily? Should I use only one backup plan and then apply it to all VM or make multiple backup plan and spread it within 1 day?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 10/09/2020 - 06:58

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Cyber Infrastructure, Acronis Cloud Backup
            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Mikhail Rozhkov
                            

                            
                    
                        Support Engineer 
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 21
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello.
You can create 10 plans for 100 machines and back up 10 machines at a time.
To increase number of simultaneously backed-up virtual machines, please follow:
https://www.acronis.com/en-us/support/documentation/CyberProtectionServ…

      
                
                
                    
                                                    Mon, 10/26/2020 - 15:19
