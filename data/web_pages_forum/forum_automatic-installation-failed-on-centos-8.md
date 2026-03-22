# Automatic installation failed on CentOS 8

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/automatic-installation-failed-centos-8

## Original Post
**Author:** Unknown

Automatic installation failed on CentOS 8

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Morris M
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 10
                
            
            
                
                    Comments: 21
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
The SnapAPI kernel module is not loaded for the kernel 4.18.0-147.5.1.el8_1.x86_64 that is running in this system. Install the module for this kernel version, and then retry the backup.
When will CentOS 8 be supported?
We have many customers that does go over to CentOS 8 from CentOS 6.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 10/27/2020 - 13:21

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Mikhail Rozhkov
                            

                            
                    
                        Support Engineer 
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 21
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Morris.
As per userguide - https://www.acronis.com/en-us/support/documentation/CyberProtectionServ… CentOS 8 is supported.
Before installing the agent please make sure to install all needed Linux packages - https://www.acronis.com/en-us/support/documentation/CyberProtectionServ…
 

      
                
                
                    
                                                    Fri, 11/06/2020 - 07:54
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            No problem with CentOS 8 here, when you already have the kernel-devel package installed before you install the agent.
If you have already installed the agent but don't have kernel-devel, then do the following:
# dnf install kernel-devel
# service acronis_mms stop
# dkms {build,install} -m snapapi26 -v 0.7.135
# service acronis_mms start

      
                
                
                    
                                                    Wed, 03/10/2021 - 12:26
