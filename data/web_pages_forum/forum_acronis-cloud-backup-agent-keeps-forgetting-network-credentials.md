# Acronis Cloud Backup Agent keeps forgetting network credentials

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/acronis-cloud-backup-agent-keeps-forgetting-network-credentials

## Original Post
**Author:** Unknown

Acronis Cloud Backup Agent keeps forgetting network credentials

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    René Haus
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I Have a strange Problem on one of our Servers that uses Acronis Cloud backup.
The Server itself is an old SBS 2008 Server. The Backup to Cloud works fine, althouth we do a second backup to a local NAS Server for redundancy purposes.
Regularly (almost daily now). i get the error that the backup could not create the file in the backup location.
The workaround i figured out for this is : Modify the backup job. copy the network path and browse for it again.
Reenter the Credentials and save the job. after that the job works fine again, untill the next sheduled job / 1-2 days later.
I tried to delete all Network credentials on the machine itself but i cant seem to find the issue. Any insight where the problem could lie? any further information needed? it drives me nuts to redo the same steps every day without finding a real solution

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 07/28/2017 - 06:20

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daniel Delaney
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            René Haus; we have seen this issue at our locations as well. Its annoying but takes less time to reenter than to try and fix. :(

      
                
                
                    
                                                    Wed, 08/02/2017 - 14:28
                                                                            
                                
                            
                                            
                                            
    
                    
                Daniel Delaney | Support Technician - Guardian operations and support

Deerwood Technologies, inc.

This message transmitted on 100% recycled electrons.

            
                            
                Products: 
                Acronis Cloud
