# Register 2 partitions in Acronis Storage Gateway within 1 server

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/register-2-partitions-acronis-storage-gateway-within-1-server

## Original Post
**Author:** Unknown

Register 2 partitions in Acronis Storage Gateway within 1 server

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    net
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I can register the Acronis Storage Gateway fine already.
The problem is, our server has 2 raid arrays with partitions /backup and /backup2 .
How can I register these in Acronis Storage Gateway so that both partitions can be used?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 01/09/2019 - 23:34

                                                          
                                                            
                                                                                        
    
                    
                We love Acronis

            
                    
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Jones,
The possible options would be creating NFS shares on your partitions or connecting them via iSCSI to Acronis Storage cluster (see 2.13 Connecting Remote iSCSI Devices to Storage Cluster Nodes of the userguide)
thank you, 

      
                
                
                    
                                                    Fri, 02/01/2019 - 12:48
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
