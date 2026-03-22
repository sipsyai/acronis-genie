# Help with error code

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/help-error-code

## Original Post
**Author:** Unknown

Help with error code

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    artur.dekowski@lafargeholcim.com
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi
I have problem with use schedule backup plan on virtual machines. 
This is a strange situation becose last month ago i had no problem. I didnt change the settings, and now i have problem on all virtual machines.
Addtional info:
------------------------
Kod błędu: 22
Moduł: 309
LineInfo: 0x8D165E86FB81959B
Pola: {"$module":"mms_bundle_glxa64_7970","CommandID":"D332948D-A7A9-4E07-B76C-253DCF6E17FB"}
Komunikat: TOL: Failed to execute the command. Backup plan 'PLCKUJDIEPO Scheduled Full Backup'
------------------------
Kod błędu: 22
Moduł: 309
LineInfo: 0x8D165E86FB81959B
Pola: {"$module":"agent_protection_addon_glxa64_7970","CommandID":"D332948D-A7A9-4E07-B76C-253DCF6E17FB"}
Komunikat: TOL: Failed to execute the command. Backup plan 'PLCKUJDIEPO Scheduled Full Backup'
------------------------
Kod błędu: 41
Moduł: 307
LineInfo: 0xE6792A5EE190DE2C
Pola: {"$module":"agent_protection_addon_glxa64_7970"}
Komunikat: Failed to execute the command.
------------------------
Kod błędu: 53
Moduł: 309
LineInfo: 0x2E7E9E174F1FB719
Pola: {"$module":"agent_protection_addon_glxa64_7970","FailCount":"2"}
Komunikat: 2 activities have not succeeded. One of them is displayed.
------------------------
Kod błędu: 22
Moduł: 309
LineInfo: 0x8D165E86FB81959B
Pola: {"$module":"service_process_glxa64_7970","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"}
Komunikat: TOL: Failed to execute the command. Backing up
------------------------
Kod błędu: 22
Moduł: 309
LineInfo: 0x8D165E86FB81959B
Pola: {"$module":"gtob_backup_command_addon_glxa64_7970","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"}
Komunikat: TOL: Failed to execute the command. Backing up
------------------------
Kod błędu: 32827
Moduł: 114
LineInfo: 0xC35C04057128FEDC
Pola: {"$module":"disk_bundle_tape_off_glxa64_7970"}
Komunikat: Backup of virtual machines has failed.
------------------------
Kod błędu: 32846
Moduł: 114
LineInfo: 0xC35C04057128FF1F
Pola: {"$module":"disk_bundle_tape_off_glxa64_7970"}
Komunikat: Not all virtual machines have been backed up.
------------------------
Kod błędu: 32845
Moduł: 114
LineInfo: 0xC35C04057128FF66
Pola: {"$module":"disk_bundle_tape_off_glxa64_7970"}
Komunikat: Failed to back up virtual machine 'plckujdiepo'.
------------------------
Kod błędu: 32786
Moduł: 114
LineInfo: 0x28314C961DE7D668
Pola: {"$module":"disk_bundle_tape_off_glxa64_7970"}
Komunikat: Failed to prepare for backup.
------------------------
Kod błędu: 22
Moduł: 83
LineInfo: 0x41AA269C04905FD1
Pola: {"$module":"esx_srv_glxa64_7970"}
Komunikat: Failed to find registered virtual machine '5031441f-ae4d-3746-352f-0e3095238649'.
------------------------
Kod błędu: 122
Moduł: 83
LineInfo: 0x4F487166528D2928
Pola: {"$module":"esx_srv_glxa64_7970"}
Komunikat: Failed to obtain server object 'config.network.pnic' (ha-host).
------------------------
Kod błędu: 296
Moduł: 83
LineInfo: 0x4F487166528D2928
Pola: {"fault":"MethodFault","$module":"esx_srv_glxa64_7970"}
Komunikat: Method has failed.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 08/19/2019 - 09:18

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Good day 
Can you please confirm in the backup options if "Volume Shadow Copy Service (VSS) and "Volume Shadow Copy Service (VSS) for virtual machines is enabled"
If "Volume Shadow Copy Service (VSS)" is enabled can you please advise to which option is selected
Regards

      
                
                
                    
                                                    Tue, 08/20/2019 - 13:10
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    artur.dekowski@lafargeholcim.com
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you for reply.
I had "Volume Shadow Copy Service (VSS)" enebled with option : automatic selection of snapshot suppplier and "Volume Shadow Copy Service (VSS) for virtual machines" was disabled.
I changed option with VSS on virtual machines and now i have "Volume Shadow Copy Service (VSS) for virtual machines" is enable but still backup cant start.
 
Regards

      
                
                
                    
                                                    Mon, 08/26/2019 - 09:43
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Good day,
So generally when I experience this issue:
"Failed to find registered virtual machine" I have found the following to be the root cause:
The ID of the virtual machine in the backup plan does not correspond to the ID in the virtual infrastructure.
Can you please confirm if you are backing up from a virtual host level? (Installed the agent on the virtual host such as Hyper-V, VMware etc) OR are you backing up from the VM level (Agent installed directly on the VM?
Then can you also advise which virtual environment you are using? (VMWare, Hyper-V etc)
Regards
 

      
                
                
                    
                                                    Mon, 08/26/2019 - 11:17
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    artur.dekowski@lafargeholcim.com
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Good morning.
I have installed VMWare.
I am start the backup from schedulle plan and from "my hand" by acronis management console.
Best regards.

      
                
                
                    
                                                    Tue, 08/27/2019 - 06:11
