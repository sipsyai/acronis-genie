# You do not have access rights to this file - VMware Appliance Backup / Restore

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/you-do-not-have-access-rights-file-vmware-appliance-backup-restore

## Original Post
**Author:** Unknown

You do not have access rights to this file - VMware Appliance Backup / Restore

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    ESX_appliance_user
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I have an ESXi with 43 VM's backed up using "Green" (Acronis-Cloud) in switzerland.
Now I updated the VMware Appliance thorugh removing (also from Acronis-Cloud) and deploy a fresh one usign the same machine-name. I can't backup or Update any VM.
I always get this error:
"You do not have access rights to this file"
 
edit:
I use ESXi 7.0 Enterprise Plus.
 
more detailed error while Backup (was cut because of size):
{
    "code": "error",
    "error": {
        "domain": "Common",
        "code": "InternalError",
        "reason": "InternalError",
        "context": {
            "$module": "esx_srv_glxa64_22750",
            "_src": {
                "code": 20250646,
                "fields": {
                    "$module": "mms_bundle_glxa64_22750",
                    "CommandID": "D332948D-A7A9-4E07-B76C-253DCF6E17FB"
                },
                "src": {
                    "file": "e:/274/enterprise/common/tol/command/command.cpp",
                    "func": "MakeFailResult",
                    "line": 464,
                    "tag": 10166417142673676000
                },
                "suberror": {
                    "code": 20250646,
                    "fields": {
                        "$module": "mms_bundle_glxa64_22750",
                        "CommandID": "D332948D-A7A9-4E07-B76C-253DCF6E17FB"
                    },
                    "src": {
                        "file": "e:/274/enterprise/common/tol/command/command.cpp",
                        "func": "MakeFailResult",
                        "line": 464,
                        "tag": 10166417142673676000
                    },
                    "suberror": {
                        "code": 20119593,
                        "fields": {
                            "$module": "mms_bundle_glxa64_22750"
                        },
                        "src": {
                            "file": "e:/274/enterprise/managers/gtob/protection/agent_engine/protect_command.cpp",
                            "func": "SafeExecute",
                            "line": 234,
                            "tag": 16607351687905075000
                        },
                        "suberror": {
                            "code": 20250677,
                            "fields": {
                                "$module": "mms_bundle_glxa64_22750",
                                "FailCount": 2
                            },
                            "src": {
                                "file": "e:/274/enterprise/common/tol/replica/event_processor.cpp",
                                "func": "CreateCumulativeError",
                                "line": 105,
                                "tag": 3350288995759143000
                            },
                            "suberror": {
                                "code": 20250646,
                                "fields": {
                                    "$module": "service_process_glxa64_22750",
                                    "CommandID": "8F01AC13-F59E-4851-9204-DE1FD77E36B4"
                                },
                                "src": {
                                    "file": "e:/274/enterprise/common/tol/command/command.cpp",
                                    "func": "MakeFailResult",
                                    "line": 464,
                                    "tag": 10166417142673676000
                                },
                                "suberror": {
                                    "code": 20250646,
                                    "fields": {
                                        "$module": "gtob_backup_command_addon_glxa64_22750",
                                        "CommandID": "8F01AC13-F59E-4851-9204-DE1FD77E36B4"
                                    },
                                    "src": {
                                        "file": "e:/274/enterprise/common/tol/command/command.cpp",
                                        "func": "MakeFailResult",
                                        "line": 464,
                                        "tag": 10166417142673676000
                                    },
                                    "suberror": {
                                        "code": 7503931,
                                        "fields": {
                                            "$module": "disk_bundle_tape_off_glxa64_22750"
                                        },
                                        "src": {
                                            "file": "e:/274/enterprise/managers/gtob/backupers/vm_instance_backuper/impl/vm_instance_backuper.cpp",
                                            "func": "Execute",
                                            "line": 485,
                                            "tag": 14077130956673188000
                                        },
                                        "suberror": {
                                            "code": 7503950,
                                            "fields": {
                                                "$module": "disk_bundle_tape_off_glxa64_22750"
                                            },
                                            "src": {
                                                "file": "e:/274/enterprise/managers/gtob/backupers/vm_instance_backuper/impl/vm_instance_backuper.cpp",
                                                "func": "BackupMachines",
                                                "line": 552,
                                                "tag": 14077130956673188000
                                            },
                                            "suberror": {
                                                "code": 7503949,
                                                "fields": {
                                                    "$module": "disk_bundle_tape_off_glxa64_22750"
                                                },
                                                "src": {
                                                    "file": "e:/274/enterprise/managers/gtob/backupers/vm_instance_backuper/impl/vm_instance_backuper.cpp",
                                                    "func": "BackupMachine",
                                                    "line": 620,
                                                    "tag": 14077130956673188000
                                                },
                                                "suberror": {
                                                    "code": 7503890,
                                                    "fields": {
                                                        "$module": "disk_bundle_tape_off_glxa64_22750"
                                                    },
                                                    "src": {
                                                        "file": "e:/274/enterprise/migration/impl/manager_vmbackup.cpp",
                                                        "func": "Backup",
                                                        "line": 2613,
                                                        "tag": 2896180243006478300
                                                    },
                                                    "suberror": {
                                                        "code": 10551548,
                                                        "fields": {
                                                            "$module": "disk_bundle_tape_off_glxa64_22750",
                                                            "account": "187625",
                                                            "tenantName": "187625"
                                                        },
                                                        "src": {
                                                            "file": "e:/274/enterprise/mms/managers/archive/utils/uri_utils.cpp",
                                                            "func": "AddStreamNameToErrForOnlineBackup",
                                                            "line": 633,
                                                            "tag": 11512307002430466000
                                                        },
                                                        "suberror": {
                                                            "code": 21561347,
                                                            "fields": {
                                                                "$module": "disk_bundle_tape_off_glxa64_22750"
                                                            },
                                                            "src": {
                                                                "file": "e:/274/enterprise/managers/gtob/util/impl/convert_batch_result.cpp",
                                                                "func": "ConvertBatchResult",
                                                                "line": 58,
                                                                "tag": 2078845185228547300
                                                            },
                                                            "suberror": {
                                                                "code": 66596,
                                                                "fields": {
                                                                    "$module": "disk_bundle_tape_off_glxa64_22750"
                                                                },
                                                                "src": {
                                                                    "file": "e:/274/enterprise/disk_manager/daapi1/virt_op.cpp",
                                                                    "func": "Execute",
                                                                    "line": 1056,
                                                                    "tag": 15108309708260166000
                                                                },
                                                                "suberror": {
                                                                    "code": 9764877,
                                                                    "fields": {
                                                                        "$module": "disk_bundle_tape_off_glxa64_22750"
                                                                    },
                                                                    "src": {
                                                                        "file": "e:/274/enterprise/disk_manager/daapi1/virt_op.cpp",
                                                                        "func": "OpenVm",
                                                                        "line": 1350,
                                                                        "tag": 15108309708260166000
                                                                    },
                                                                    "suberror": {
                                                                        "code": 7503875,
                                                                        "fields": {
                                                                            "$module": "disk_bundle_tape_off_glxa64_22750"
                                                                        },
                                                                        "src": {
                                                                            "file": "e:/274/enterprise/migration/impl/computer_browser.cpp",
                                                                            "func": "OpenDisks",
                                                                            "line": 119,
                                                                            "tag": 17682004429578813000
                                                                        },
                                                                        "suberror": {
                                                                            "code": 5439582,
                                                                            "fields": {
                                                                                "$module": "esx_srv_glxa64_22750"
                                                                            },
                                                                            "src": {
                                                                                "file": "e:/274/enterprise/virtualware/raw/vmware/vixdisklib/vixdisklib.cpp",
                                                                                "func": "VixDiskHolder",
                                                                                "line": 714,
                                                                                "tag": 14273442096096860000
                                                                            },
                                                                            "suberror": {
                                                                                "code": 13,
                                                                                "fields": {
                                                                                    "$module": "esx_srv_glxa64_22750"
                                                                                },
                                                                                "src": {
                                                                                    "file": "e:/274/enterprise/virtualware/raw/vmware/vixdisklib/vixdisklib.cpp",
                                                                                    "func": "Open",
                                                                                    "line": 497,
                                                                                    "tag": 14273442096096860000
                                                                                },
                                                                                "suberror": {},
                                                                                "text": "You do not have access rights to this file",
                                                                                "types": {
                                                                                    "$module": "A"
                                                                                }
                                                                            },
                                                                            "text": "Failed to open virtual disk file '[datastore1] StackStorm/StackStorm.vmdk'.",
                                                                            "types": {
                                                                                "$module": "A"
                                                                            }
                                                                        },
                                                                        "text": "Failed to prepare for backup.",
                                                                        "types": {
                                                                            "$module": "A"
                                                                        }
                                                                    },
                                                                    "text": "Failed to perform the requested operation.",
                                                                    "types": {
                                                                        "$module": "A"
                                                                    }
                                                                },
                                                                "text": "",
                                                                "types": {
                                                                    "$module": "A"
                                                                }
                                                            },
                                                            "text": "Backup has failed.",
                                                            "types": {
                                                                "$module": "A"
                                                            }
                                                        },
                                                        "text": "Stream name: 'StackStorm-4745717A-E092-4B1D-808F-2036D14663E2-52FB754D-035D-4F85-C96E-8A45ABEDF963A.tibx'.",
                                                        "types": {
                                                            "$module": "A",
                                                            "account": "W",
                                                            "tenantName": "W"
                                                        }
                                                    },
                                                    "text": "Failed to prepare for backup.",
                                                    "types": {
                                                        "$module": "A"
                                                    }
                                                },
                                                "text": "Failed to back up virtual machine 'StackStorm'.",
                                                "types": {
                                                    "$module": "A"
                                                }
                                            },
                                            "text": "Not all virtual machines have been backed up.",
                                            "types": {
                                                "$module": "A"
                                            }
                                        },
                                        "text": "Backup of virtual machines has failed.",
                                        "types": {
                                            "$module": "A"
                                        }
                                    },
                                    "text": "TOL: Failed to execute the command. Backing up",
                                    "types": {
                                        "$module": "A",
                                        "CommandID": "A"
                                    }
                                },
                                "text": "TOL: Failed to execute the command. Backing up",
                                "types": {
                                    "$module": "A",
                                    "CommandID": "A"
                                }
                            },
                            "text": "2 activities have not succeeded. One of them is displayed.",
                            "types": {
                                "$module": "A",
                                "FailCount": "N"
                            }
                        },
                        "text": "Failed to execute the command.",
                        "types": {
                            "$module": "A"
                        }
                    },
                    "text": "TOL: Failed to execute the command. Backup plan '7_Tage_2*Täglich'",
                    "types": {
                        "$module": "A",
                        "CommandID": "A"
                    }
                },
                "text": "TOL: Failed to execute the command. Backup plan '7_Tage_2*Täglich'",
                "types": {
                    "$module": "A",
                    "CommandID": "A"
                }
            },
            "account": "187625",
            "cause_str": "You do not have access rights to this file",
            "commandid": "8F01AC13-F59E-4851-9204-DE1FD77E36B4",
            "effect_str": "TOL: Failed to execute the command. Backup plan '7_Tage_2*Täglich'",
            "failcount": 2,
            "tenantname": "187625"
        },
        "kbLink": {
            "build": 20227,
            "lineTag": "0xC61573F663F5D80A",
            "os": "Windows",
            "product": "cloud",
            "serCode": "0x01350016+0x01350016+0x01330029+0x01350035+0x01350016+0x01350016+0x0072803B+0x0072804E+0x0072804D+0x00728012+0x00A100FC+0x01490003+0x00010424+0x0095000D+0x00728003+0x0053005E+0x0000000D",
            "version": "12.5"
        },
        "debug": {
            "msg": "You do not have access rights to this file"
        },
        "type": "error",
        "startTime": "2020-06-23T08:10:36.000Z",
        "parentActivityId": "965833653907095552",
        "isRoot": true,
        "cause": "You do not have access rights to this file",
        "effect": "You do not have access rights to this file",
        "index": 0,
        "origin": {
            "code": 20250646,
            "fields": {
                "$module": "mms_bundle_glxa64_22750",
                "CommandID": "D332948D-A7A9-4E07-B76C-253DCF6E17FB"
            },
            "src": {
                "file": "e:/274/enterprise/common/tol/command/command.cpp",
                "func": "MakeFailResult",
                "line": 464,
                "tag": 10166417142673676000
            },
            "suberror": {
                "code": 20250646,
                "fields": {
                    "$module": "mms_bundle_glxa64_22750",
                    "CommandID": "D332948D-A7A9-4E07-B76C-253DCF6E17FB"
                },
                "src": {
                    "file": "e:/274/enterprise/common/tol/command/command.cpp",
                    "func": "MakeFailResult",
                    "line": 464,
                    "tag": 10166417142673676000
                },
                "suberror": {
                    "code": 20119593,
                    "fields": {
                        "$module": "mms_bundle_glxa64_22750"
                    },
                    "src": {
                        "file": "e:/274/enterprise/managers/gtob/protection/agent_engine/protect_command.cpp",
                        "func": "SafeExecute",
                        "line": 234,
                        "tag": 16607351687905075000
                    },
                    "suberror": {
                        "code": 20250677,
                        "fields": {
                            "$module": "mms_bundle_glxa64_22750",
                            "FailCount": 2
                        },
                        "src": {
                            "file": "e:/274/enterprise/common/tol/replica/event_processor.cpp",
                            "func": "CreateCumulativeError",
                            "line": 105,
                            "tag": 3350288995759143000
                        },
                        "suberror": {
                            "code": 20250646,
                            "fields": {
                                "$module": "service_process_glxa64_22750",
                                "CommandID": "8F01AC13-F59E-4851-9204-DE1FD77E36B4"
                            },
                            "src": {
                                "file": "e:/274/enterprise/common/tol/command/command.cpp",
                                "func": "MakeFailResult",
                                "line": 464,
                                "tag": 10166417142673676000
                            },
                            "suberror": {
                                "code": 20250646,
                                "fields": {
                                    "$module": "gtob_backup_command_addon_glxa64_22750",
                                    "CommandID": "8F01AC13-F59E-4851-9204-DE1FD77E36B4"
                                },
                                "src": {
                                    "file": "e:/274/enterprise/common/tol/command/command.cpp",
                                    "func": "MakeFailResult",
                                    "line": 464,
                                    "tag": 10166417142673676000
                                },
                                "suberror": {
                                    "code": 7503931,
                                    "fields": {
                                        "$module": "disk_bundle_tape_off_glxa64_22750"
                                    },
                                    "src": {
                                        "file": "e:/274/enterprise/managers/gtob/backupers/vm_instance_backuper/impl/vm_instance_backuper.cpp",
                                        "func": "Execute",
                                        "line": 485,
                                        "tag": 14077130956673188000
                                    },
                                    "suberror": {
                                        "code": 7503950,
                                        "fields": {
                                            "$module": "disk_bundle_tape_off_glxa64_22750"
                                        },
                                        "src": {
                                            "file": "e:/274/enterprise/managers/gtob/backupers/vm_instance_backuper/impl/vm_instance_backuper.cpp",
                                            "func": "BackupMachines",
                                            "line": 552,
                                            "tag": 14077130956673188000
                                        },
                                        "suberror": {
                                            "code": 7503949,
                                            "fields": {
                                                "$module": "disk_bundle_tape_off_glxa64_22750"
                                            },
                                            "src": {
                                                "file": "e:/274/enterprise/managers/gtob/backupers/vm_instance_backuper/impl/vm_instance_backuper.cpp",
                                                "func": "BackupMachine",
                                                "line": 620,
                                                "tag": 14077130956673188000
                                            },
                                            "suberror": {
                                                "code": 7503890,
                                                "fields": {
                                                    "$module": "disk_bundle_tape_off_glxa64_22750"
                                                },
                                    
                      

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      2020-06-22 17_15_41-Cyber Protection-Konsole.png

                      46.71 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Mon, 06/22/2020 - 15:06

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Maria Belinskaya
                            

                            
                    
                        Forum Support specialist 
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2012
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello ESX_appliance_user,
Welcome to Acronis forums!
We recommend that you open a case with your Service Provider for investigating this issue. You will need to collect VMware VDDK Logs from your Virtual Appliance as instructed in this KB article:https://kb.acronis.com/content/46575

      
                
                
                    
                                                    Tue, 06/23/2020 - 12:34
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Maria Belinskaya | Acronis Forum Support Specialist

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support/

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    ESX_appliance_user
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I have an open Ticket "AW: [04490431] "You do not have access rights to this file"    [ ref:_00D30Zcb._5001T1Nvq44:ref ]"
 
but I don't get any response since a week now and we just ran into a Problem with a customer not able to restore a lost file..
I uploaded the files -> FTP-Server.
 
 
 

      
                
                
                    
                                                    Thu, 07/02/2020 - 12:15
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Maria Belinskaya
                            

                            
                    
                        Forum Support specialist 
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2012
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello ESX_appliance_user.
Thank you for providing details of your support case.
We are sorry about your negative experience with Acronis Support Team. 
I have escalated your case to a higher level.

      
                
                
                    
                                                    Thu, 07/02/2020 - 15:38
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Maria Belinskaya | Acronis Forum Support Specialist

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support/

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    ESX_appliance_user
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Maria Belinskaya
Sadly this issue isn't fixed yet! And we don't get any response from support since over 2 weeks now!

      
                
                
                    
                                                    Thu, 08/06/2020 - 11:29
