# Failed to copy the volume error

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/failed-copy-volume-error

## Original Post
**Author:** Unknown

Failed to copy the volume error

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Alexis Van Zeveren
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
I am an end user of the Acronis Cloud Protected solution by Infomaniak and have a "Failed to copy the volume" error when trying to restore the full backup of a Windows 2019 physical server to a new VM (following the instructions in https://www.acronis.com/en-us/support/documentation/CyberProtectionServ…)
This succeeds without problem for another physical server running Windows 2012R2.
The problematic server has a disk with a basic EFI system partition and 2 Dynamic NTFS partitions.
The server for which the restore is succeeding has just 2 basic NTFS partitions and no EFI.
Unfortunately Infomaniak support is of no help since more than 2 weeks.
Can anybody help ? 
 
{
    "code": "error",
    "error": {
        "domain": "Common",
        "code": "InternalError",
        "reason": "InternalError",
        "context": {
            "$module": "disk_bundle_vsa64_31771",
            "_src": {
                "code": 20250646,
                "fields": {
                    "$module": "mms_vsa64_31771",
                    "AgentName": "",
                    "CommandID": "08FF37D8-FB90-49A3-828B-B9A8CDA417B3"
                },
                "src": {
                    "file": "d:\\1108\\enterprise\\common\\tol\\command\\command.cpp",
                    "func": "Tol::`anonymous-namespace'::MakeFailResultWitnName",
                    "line": 503,
                    "tag": "0x8d165e86fb8195c5"
                },
                "suberror": {
                    "code": 20250646,
                    "fields": {
                        "$module": "disk_bundle_vsa64_31771",
                        "AgentName": "",
                        "CommandID": "08FF37D8-FB90-49A3-828B-B9A8CDA417B3"
                    },
                    "src": {
                        "file": "d:\\1108\\enterprise\\common\\tol\\command\\command.cpp",
                        "func": "Tol::`anonymous-namespace'::MakeFailResultWitnName",
                        "line": 503,
                        "tag": "0x8d165e86fb8195c5"
                    },
                    "suberror": {
                        "code": 7503969,
                        "fields": {
                            "$module": "disk_bundle_vsa64_31771"
                        },
                        "src": {
                            "file": "d:\\1108\\enterprise\\migration\\commands\\group_restore\\src\\group_restore_logic.cpp",
                            "func": "MigrationManagement::GroupRestore::GroupRestoreCommandLogic::RunLogic",
                            "line": 389,
                            "tag": "0x8cf6eec01474e20f"
                        },
                        "suberror": {
                            "code": 20250646,
                            "fields": {
                                "$module": "mms_vsa64_31771",
                                "AgentName": "",
                                "CommandID": "4504F8D4-2727-42AB-BB4F-A42EDBB790A0"
                            },
                            "src": {
                                "file": "d:\\1108\\enterprise\\common\\tol\\command\\command.cpp",
                                "func": "Tol::`anonymous-namespace'::MakeFailResultWitnName",
                                "line": 503,
                                "tag": "0x8d165e86fb8195c5"
                            },
                            "suberror": {
                                "code": 20250646,
                                "fields": {
                                    "$module": "service_process_vsa64_31771",
                                    "AgentName": "",
                                    "CommandID": "6F80C46F-90AC-4F6F-9578-3CAEF754A637"
                                },
                                "src": {
                                    "file": "d:\\1108\\enterprise\\common\\tol\\command\\command.cpp",
                                    "func": "Tol::`anonymous-namespace'::MakeFailResultWitnName",
                                    "line": 503,
                                    "tag": "0x8d165e86fb8195c5"
                                },
                                "suberror": {
                                    "code": 20250646,
                                    "fields": {
                                        "$module": "disk_bundle_vsa64_31771",
                                        "AgentName": "",
                                        "CommandID": "6F80C46F-90AC-4F6F-9578-3CAEF754A637"
                                    },
                                    "src": {
                                        "file": "d:\\1108\\enterprise\\common\\tol\\command\\command.cpp",
                                        "func": "Tol::`anonymous-namespace'::MakeFailResultWitnName",
                                        "line": 503,
                                        "tag": "0x8d165e86fb8195c5"
                                    },
                                    "suberror": {
                                        "code": 7503972,
                                        "fields": {
                                            "$module": "disk_bundle_vsa64_31771"
                                        },
                                        "src": {
                                            "file": "d:\\1108\\enterprise\\migration\\impl\\manager_group_restore.cpp",
                                            "func": "MigrationManagement::MigrationManagerImpl::RestoreEntireVm",
                                            "line": 342,
                                            "tag": "0x2b2c9ed481007bde"
                                        },
                                        "suberror": {
                                            "code": 7503975,
                                            "fields": {
                                                "$module": "disk_bundle_vsa64_31771"
                                            },
                                            "src": {
                                                "file": "d:\\1108\\enterprise\\virtualization\\features\\convert_to_vm\\manager_convert.cpp",
                                                "func": "MigrationManagement::MigrationManagerImpl::CopyToNewVM",
                                                "line": 908,
                                                "tag": "0xfde974fd2ebcff55"
                                            },
                                            "suberror": {
                                                "code": 7471122,
                                                "fields": {
                                                    "$module": "disk_bundle_vsa64_31771"
                                                },
                                                "src": {
                                                    "file": "d:\\1108\\enterprise\\migration\\impl\\disk_utils.cpp",
                                                    "func": "MigrationManagement::`anonymous-namespace'::ConfigDrivenDisksCopier::CopyVolumes",
                                                    "line": 317,
                                                    "tag": "0xcc2eaae51c84579d"
                                                },
                                                "suberror": {},
                                                "text": "Failed to copy the volume.",
                                                "types": {
                                                    "$module": "A"
                                                }
                                            },
                                            "text": "Failed to copy source disks to a new virtual machine.",
                                            "types": {
                                                "$module": "A"
                                            }
                                        },
                                        "text": "Failed to recover the entire virtual machine.",
                                        "types": {
                                            "$module": "A"
                                        }
                                    },
                                    "text": "TOL: Failed to execute the command. Recovering the entire virtual machine",
                                    "types": {
                                        "$module": "A",
                                        "AgentName": "W",
                                        "CommandID": "A"
                                    }
                                },
                                "text": "TOL: Failed to execute the command. Recovering the entire virtual machine",
                                "types": {
                                    "$module": "A",
                                    "AgentName": "W",
                                    "CommandID": "A"
                                }
                            },
                            "text": "TOL: Failed to execute the command. Tol::IsolateCommand",
                            "types": {
                                "$module": "A",
                                "AgentName": "W",
                                "CommandID": "A"
                            }
                        },
                        "text": "Failed to recover a virtual machine.",
                        "types": {
                            "$module": "A"
                        }
                    },
                    "text": "TOL: Failed to execute the command. Recovering a virtual machine",
                    "types": {
                        "$module": "A",
                        "AgentName": "W",
                        "CommandID": "A"
                    }
                },
                "text": "TOL: Failed to execute the command. Recovering a virtual machine",
                "types": {
                    "$module": "A",
                    "AgentName": "W",
                    "CommandID": "A"
                }
            },
            "agentname": "",
            "cause_str": "Failed to copy the volume.",
            "commandid": "6F80C46F-90AC-4F6F-9578-3CAEF754A637",
            "effect_str": "TOL: Failed to execute the command. Recovering a virtual machine"
        },        "kbLink": {
            "build": 20567,
            "lineTag": "0xCC2EAAE51C84579D",
            "os": "Windows",
            "product": "cloud",
            "serCode": "0x01350016+0x01350016+0x00728061+0x01350016+0x01350016+0x01350016+0x00728064+0x00728067+0x00720012",
            "version": "15.0"
        },
        "debug": {
            "msg": "Failed to copy the volume."
        }
    },
    "payload": null
}
      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 03/22/2023 - 19:26

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello.
The recovery process is different from physical to virtual machines. First of all 
Please try the following solutions:
1- Create the virtual machine with the same disk configuration as the physical machine.
2- On the virtual machine (you are looking to restore to), install the operating system an agent and register. Browse the backup from the agent of the VM in the backup storage tab (click on change for machine location and select the new machine).
3- Try the recovery with bootable media ( this one should resolve the issue ): https://www.acronis.com/en-us/support/documentation/CyberProtectionServ…
Let me know if that resolved the issue.

      
                
                
                    
                                                    Thu, 03/23/2023 - 13:53
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Alexis Van Zeveren
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Solution 3 (with the bootable media) finally solved the issue.
(that was already back in 2023, but I forgot to inform you at that time. I just update it now because maybe it can help others)
 

      
                
                
                    
                                                    Thu, 11/20/2025 - 13:30
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Alexis Van Zeveren wrote:

Solution 3 (with the bootable media) finally solved the issue.
(that was already back in 2023, but I forgot to inform you at that time. I just update it now because maybe it can help others)
 


Thank you for updating.
Best regards. 

      
                
                
                    
                                                    Thu, 11/20/2025 - 13:33
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
