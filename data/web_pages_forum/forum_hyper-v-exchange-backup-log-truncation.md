# Hyper V Exchange Backup - Log truncation

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/hyper-v-exchange-backup-log-truncation

## Original Post
**Author:** Unknown

Hyper V Exchange Backup - Log truncation

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Neil_L
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 7
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
We're backing up a customer's exchange server by taking a full Hyper V backup. This works fine and the restore has been tested.
 
However, it's not truncating the logs for obvious reasons. Is there a way to make this type of backup application aware, or will I have to enable circular logging?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 02/12/2018 - 14:06

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Neil_L
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 7
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Just to update I have VSS aware enabled on the Hyper V backup, so I would have thought that this would truncate the logs automatically.

      
                
                
                    
                                                    Mon, 02/12/2018 - 14:22
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi,
According to https://www.acronis.com/en-us/support/documentation/BackupService/#3550… Application-aware disk-level backup is available for physical machines and for ESXi virtual machines. If you want to back up Hyper-V virtual machines with Exchange databases and remove transaction logs after every backup, install Agent for Windows and Agent for Exchange onto the VM with Exchange and create a separate backup plan with enabled VSS full backup option. The server should be selected as VM with Agent to be backed up with the help of components installed within the guest OS of the VM. 


      
                
                
                    
                                                    Wed, 02/14/2018 - 09:56
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
