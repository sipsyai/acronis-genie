# How to restore MacOS device to VMWare ESXi (running on Mac Hardware)

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/how-restore-macos-device-vmware-esxi-running-mac-hardware

## Original Post
**Author:** Unknown

How to restore MacOS device to VMWare ESXi (running on Mac Hardware)

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Mischa Künzle
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi all
I'm in need of your help. We're currently evaluation Acronis Cyber Protect and are testing its capabilities for our clients using Apple products.
Where I'm struggling is to restore a backup of a physical iMac to a VMware ESXi host (5.1). The host is running on a MacMini, due to Apples terms of use.
We've create a virtual appliance agent and connected it to the Acronis Cloud (though this seems not to be necessary for the restore).
Next, we've created an empty VM to boot the Acronis Boot Image from. Connecting it to the Acronis Cloud, we can see all the backups, choose any of the iMac backups and chose to restore as disk.
The restore process only takes a few seconds and ends with "Succeeded with warnings", however nothing is restored:
"Failed to open the root directory of the original operating system"
Tried various different backups incl. the initial fullbackup of the machine.
 
Does anyone of you have an idea on how to do this recovery correctly?
 
Thank you in advance!

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      2021-01-27 14_19_40-bc_mku01 (Mischa Desktop) - TeamViewer.png

                      112.67 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Thu, 01/28/2021 - 08:16

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Cyber Cloud - Evaluation
            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Mischa,
thank you for your posting! I've discussed the issue with my colleagues from the support team and looks like the issue would need the more in-depth investigation, which is not possible on forum. Please submit a support ticket as described by the following link: https://kb.acronis.com/content/56079

      
                
                
                    
                                                    Wed, 02/03/2021 - 17:55
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
