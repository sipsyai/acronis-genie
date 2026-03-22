# Constantly failed backups

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/constantly-failed-backups

## Original Post
**Author:** Unknown

Constantly failed backups

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    rutger@praetoria-consulting.be
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
 
System Centos 7* with Plesk. Installed and configured the Acronis according to the Plesk Manual. Installation is succesful. 
Opened the needed FW-ports.
But the back-ups keep failing. I have checks the .config file (Virtuozzo set-up) and all is good.
 
It is set-up as default webcp backup, backing up the entire machine.
 
Codes I get returned:
None of the items selected for backup were found.
DATE AND TIME
Feb 09, 2018, 11:25:30
CODE
70
MODULE
309
MESSAGE
Backup failed

Additional info:
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"CommandID":"D332948D-A7A9-4E07-B76C-253DCF6E17FB","$module":"mms_lxa64_4560"}
Message: TOL: Failed to execute the command. Backup plan 'webcp'
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"CommandID":"D332948D-A7A9-4E07-B76C-253DCF6E17FB","$module":"agent_protection_addon_lxa64_4560"}
Message: TOL: Failed to execute the command. Backup plan 'webcp'
------------------------
Error code: 41
Module: 307
LineInfo: 0xE6792A5EE190DDE7
Fields: {"$module":"agent_protection_addon_lxa64_4560"}
Message: Failed to execute the command.
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"CommandID":"FD79C554-B363-4DB2-97BC-1E5A94094A94","$module":"mms_lxa64_4560"}
Message: TOL: Failed to execute the command. Resolving items to back up
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"CommandID":"FD79C554-B363-4DB2-97BC-1E5A94094A94","$module":"agent_protection_addon_lxa64_4560"}
Message: TOL: Failed to execute the command. Resolving items to back up
------------------------
Error code: 43
Module: 307
LineInfo: 0xE873A234106E3486
Fields: {"$module":"agent_protection_addon_lxa64_4560"}
Message: Failed to execute an internal command while resolving items selected for backup.
------------------------
Error code: 68
Module: 307
LineInfo: 0x071E35C26B78D644
Fields: {"$module":"agent_protection_addon_lxa64_4560"}
Message: Cannot resolve any of the following inclusion rules: '[Fixed Volumes]'.
------------------------
Error code: 67
Module: 307
LineInfo: 0x071E35C26B78D5FC
Fields: {"$module":"agent_protection_addon_lxa64_4560"}
Message: Cannot resolve inclusion rule '[Fixed Volumes]'.
------------------------
Error code: 6
Module: 377
LineInfo: 0x20E8C00E3FF3FA4F
Fields: {"$module":"agent_protection_addon_lxa64_4560"}
Message: No volumes have been found while processing the 'Fixed Volumes' template.
 
Did I miss something in the set-up?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 02/09/2018 - 10:35

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    rutger@praetoria-consulting.be
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Allright,
 
I have been digging into this. The config from Plesk says in the .config file key Webcp
Acronis sees webcp
When trying to back-up the entire machine this fails. When backing up files / folders (all) the backup runs without a problem.
 
Why does the entire machine fail? Is this because of the above lying VM?

      
                
                
                    
                                                    Fri, 02/09/2018 - 14:08
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Evgeny Ryuntyu
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 56
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Rutger,

It's Evgeny from Acronis Service Provider Support. 
As far as I understood the disk level backups (entire machine) of one of your Plesk servers is failing with Message: No volumes have been found while processing the 'Fixed Volumes' template.
I will be glad to assist you.
 
According to the trueimage-setup.log from the machine configo.* the SnapAPI module was not loaded, although it has been built.
 
2018-02-09T11:41:35+0000:Failed to find directory '/lib/modules/3.10.0-514.6.1.el7.x86_64/build' that contains the kernel source code.
The kernel source code or kernel headers require installing. For more information, refer to http://kb.acronis.com/content/1556.
2018-02-09T11:41:35+0000:- failed to load the SnapAPI kernel module.
 
Could you please make sure the system packages are updated and the required one are present per the following web-help article?
https://www.acronis.com/en-US/support/documentation/BackupService/#2261…
I actually checked further and found that 514 build of your CentOS has a problem https://bugzilla.redhat.com/show_bug.cgi?id=1463241 and you will need to update the kernel to the latest stable release to have it fixed, then verify if the snapapi26 module is loaded 
# modprobe snapapi26and if all is OK - run the backup.
 
If you require any assistance with our product after following the suggestions above, please feel free to contact our Support team per the SLA. 
 
Best regards,
Evgeny Ryuntyu | Senior Support Engineer
Acronis  | Dolgoprudnenskoe shosse 3, Moscow, Russia 141700

      
                
                
                    
                                                    Mon, 02/12/2018 - 08:46
