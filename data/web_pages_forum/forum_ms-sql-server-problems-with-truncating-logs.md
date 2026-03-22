# MS SQL Server problems with truncating logs

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/ms-sql-server-problems-truncating-logs

## Original Post
**Author:** Unknown

MS SQL Server problems with truncating logs

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Alexander Fabech
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello.
 
We have a customer, there are running Microsoft Dynamics AX on a Server 2012 R2 with MS SQL Server 2014 and have a heavy load of data (270 GB DB). Currently they have the primary DB, but we have some issue with truncating logs (transaction logs) which is grooving too fast/big.
DB size: 278 GB (D:\)
DB log: (E:\ Currently 190 GB which should be.. 10 GB?)
We are having a backup plan:
Every day repeat every 4 hour(s) from 06:00 until 22:00
With truncating logs enabled.
 
Why it doesnt truncate/remove the logs when running backup? I have to change the DB til simple mode, for making log file like zero again..
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 06/18/2019 - 06:29

                                                          
                                                            
                                                                                        
    
                    
                HP EliteBook 840 G5 8GB i5 8250U 256 GB SSD

            
                            
                Products: 
                Acronis Cloud (Reseller)
            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Alexander Fabech
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I doesnt get any errors in backup jobs.

      
                
                
                    
                                                    Tue, 06/18/2019 - 06:29
                                                                            
                                
                            
                                            
                                            
    
                    
                HP EliteBook 840 G5 8GB i5 8250U 256 GB SSD

            
                            
                Products: 
                Acronis Cloud (Reseller)
