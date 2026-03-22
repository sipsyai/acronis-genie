# device name

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/device-name

## Original Post
**Author:** Unknown

device name

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Suporte
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 24
                
            
            
                
                    Comments: 13
                
            
                                                        
    
    
        
    


                
                
                    
                        
            hello, i have 100 computers to install on cloud datacenter but when i installed 3 machines i realize that the name of machine on console wasn't the same windows name i think that name was the node on the datacenter. is there any way to put the name of the windows machine and not the datacenter node ?
 
Thanks.
 
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 10/17/2018 - 21:42

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Aconis Backup Cloud

            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi!
The names of the machines that you see in the Backup Console are taken from the machine properties. You can't change them from the Backup Console, however, if you change a name of the machine and then reboot the machine, the Console will show a new name for the same old device.
Additionally, since the devices are managed via their unique ID numbers and not the names, you would not need to re-create the backup plan, because only the name would change.
 
I future versions of the platform, we will add ability to add custom comments to each resource (devices, mailboxes, databases and so on)
 
Hope that helps!

      
                
                
                    
                                                    Fri, 10/19/2018 - 07:11
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Suporte
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 24
                
            
            
                
                    Comments: 13
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            thanks

      
                
                
                    
                                                    Sun, 10/21/2018 - 10:34
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Aconis Backup Cloud
