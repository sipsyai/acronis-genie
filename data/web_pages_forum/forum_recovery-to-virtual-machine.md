# Recovery to Virtual Machine

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/recovery-virtual-machine

## Original Post
**Author:** Unknown

Recovery to Virtual Machine

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    David Pitt
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 7
                
            
            
                
                    Comments: 15
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Is there an option to recover ABC (Cloud or On-Premise) backups of a physical machine to a virtual machine? Like we could with B&R.

I can't see the option within the BaaS console and can't access the .tib directly any more through Acronis Backup & Recovery Console.

Thanks

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 08/27/2015 - 11:09

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi David,
Thanks for posting your question here.
In Acronis Backup Advanced (formerly Acronis Backup & Recovery) you could convert a disk backup to a virtual machine, this was a common recovery to a virtual machine which would automatically apply the Universal Restore with necessary drivers for supported hypervisor.
Acronis Backup Cloud does not yet provide the conversion/recovery to VM functionality, so there is only one way to recover a physical machine to VM:
Start the VM with a bootable media 
In the bootable media interface connect to the cloud or local storage and select the backup of your physical machine
Restore the backup with Universal Restore or apply Universal Restore after recovery, providing necessary drivers for the selected hypervisor. You can copy the folder with them from a machine with installed Acronis Backup Advanced Agent (C:\Program Files\Common Files\Acronis\UniversalRestore\DriversPack)
Please note that you can recover a machine A to machine B within the web console provided machine B has an agent installed and is online, but no Universal Restore would be applied then, and also disk configuration should be similar so that disk and volume mapping can succeed. This is why you cannot recover a physical machine into a VM even if you have and agent running inside the VM as the drivers would not match and the machine will not boot afterwards.
Let me know if you have more questions.

      
                
                
                    
                                                    Thu, 08/27/2015 - 11:39
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.
