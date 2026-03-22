# Failed to build the SnapAPI kernel module

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/failed-build-snapapi-kernel-module

## Original Post
**Author:** Unknown

Failed to build the SnapAPI kernel module

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    dxxSDZX
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
Trying to install Acronis Cloud backup agent on a Ubuntu 16.04.5 LTS VPS (no gui, console only) but I get the following error:
Installation of the Backup Agent packages has finished.
The following problems occurred:
- failed to build the SnapAPI kernel module. Operations with disk-level backups will not be available.
- failed to load the SnapAPI kernel module.
See 'HOWTO.INSTALL' for further instructions.
Fine, I read the HOWTO.INSTALL. Ran some commands but stuck now:
 
root@vps:~# uname -r
3.13.0-042stab130.1
root@vps:~# sudo apt install linux-headers-`uname -r`
Reading package lists... Done
Building dependency tree
Reading state information... DoneE: Unable to locate package linux-headers-3.13.0-042stab130.1
E: Couldn't find any package by glob 'linux-headers-3.13.0-042stab130.1'
E: Couldn't find any package by regex 'linux-headers-3.13.0-042stab130.1'

apt-cache search linux-headers doesn't show any 3.x, only a long list of different 4.x
How do I solve this problem, how do I get this SnapAPI going?
 
 
           
 

 
 
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 07/23/2018 - 09:12

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    dxxSDZX
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Anyone?

      
                
                
                    
                                                    Fri, 07/27/2018 - 06:57
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Marcin Pikula
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Did you solved the problem?
I had the same problem too. Solution was to install following packages:
"linux-headers-3.16.0-6-amd64" and "linux-headers-3.16.0-6-common"

      
                
                
                    
                                                    Wed, 08/29/2018 - 16:24
