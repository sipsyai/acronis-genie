# Quota not properly adjusted

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/quota-not-properly-adjusted

## Original Post
**Author:** Unknown

Quota not properly adjusted

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Global-e | CS   
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 17
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Some of our customers excperience problems after adjusting the quota for the accounts.
Example:
We have a customer who has 100GB of quota but is at 95% of quota reached.
We then upgrade the quota to 150GB to get more space.
But the error messages about the quota nearly being reached keep popping up.
So it seems the adjusted quota is not completely activated or something.
 
Are we missing some step in the process?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 04/18/2016 - 12:01

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fredrik
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 8
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            We hade the same problem
If you dont know the workaround already this seems to do the trick
1. Go to:
C:\Programdata\Acronis\BackupandRecovery\OnlineBackup
2. Remove the CRT file from this location
3. Restart Acronis Managed Machine Service
4. Run a backup
5. This will generate a new certificate
The new certificate will resolve the issue with storage quota.
Dont know if there is a real solution for this problem yet. The workaround is a shitload of work.....
Have seen some other bad stuff
Clinets where it says XX GB used
but when you browse the cloud its way less
 
 

      
                
                
                    
                                                    Sat, 04/23/2016 - 18:03
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Global-e | CS   
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 17
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            This work-around solves the problem yes.
But indeed its a lot of work for a function that simply should be working fine.
Lets just use the work around for now and hope there will be a fix soon.

      
                
                
                    
                                                    Tue, 05/10/2016 - 10:19
