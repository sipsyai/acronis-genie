# Backup SQL database but fails with noti :" Failed to create snapshot because VSS provider returned error 'Request is unsuppored"

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/backup-sql-database-fails-noti-failed-create-snapshot-because-vss-provider-returned-error-request-unsuppored

## Original Post
**Author:** Unknown

Backup SQL database but fails with noti :" Failed to create snapshot because VSS provider returned error 'Request is unsuppored"

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    hiep tran
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            
cause


Failed to create snapshot because VSS provider returned error 'Request is unsuppored'.

code


MemoVssProviderDoesNotSupportVolume

context


{
    "_src": {
        "code": 22873777,
        "fields": {
            "$module": "ArsDbBackupProvider_vsa64_28503"
        },
        "src": {
            "file": "d:\\391\\enterprise\\applications\\technology\\snapapi\\src\\backup_session.cpp",
            "func": "AppBackup::SnapApi::SnapapiBackupSession::CreateVssSnapshot",
            "line": 268,
            "tag": "0xe821934a13fc0262"
        },
        "suberror": {
            "code": 458785,
            "fields": {
                "$module": "ArsDbBackupProvider_vsa64_28503"
            },
            "src": {
                "file": "d:\\391\\core\\resizer\\generic\\snapinit.cpp",
                "func": "InitSnapshotBitmap",
                "line": 157,
                "tag": "0xe24f93d0b8d8c99f"
            },
            "suberror": {
                "code": 1098824,
                "fields": {
                    "$module": "ArsDbBackupProvider_vsa64_28503"
                },
                "src": {
                    "file": "d:\\391\\core\\fdisk\\win_snapshot.cpp",
                    "func": "win_snapshot_core::AppendVolumesToSnapshot",
                    "line": 1360,
                    "tag": "0x3fec04e376b8a246"
                },
                "suberror": {
                    "code": 9,
                    "fields": {
                        "$module": "ArsDbBackupProvider_vsa64_28503",
                        "code": 50
                    },
                    "src": {
                        "file": "d:\\391\\core\\fdisk\\ver2\\arch\\windows\\win_errors.cpp",
                        "func": "Fdisk::AddKstatusError",
                        "line": 40,
                        "tag": "0x2aacb7b2ab852ac"
                    },
                    "suberror": {
                        "code": 65520,
                        "fields": {
                            "$module": "ArsDbBackupProvider_vsa64_28503",
                            "code": 2147942450
                        },
                        "src": {
                            "file": "d:\\391\\core\\common\\error.cpp",
                            "func": "Common::Error::AddWindowsError",
                            "line": 314,
                            "tag": "0xbd28fdbd64edb8f8"
                        },
                        "suberror": {},
                        "text": "The request is not supported",
                        "types": {
                            "$module": "A",
                            "code": "N"
                        }
                    },
                    "text": "Unknown status.",
                    "types": {
                        "$module": "A",
                        "code": "N"
                    }
                },
                "text": "Failed to add the volume to the snapshot.",
                "types": {
                    "$module": "A"
                }
            },
            "text": "Failed to create volume snapshot.",
            "types": {
                "$module": "A"
            }
        },
        "text": "Failed to process the shadow copy operation.",
        "types": {
            "$module": "A"
        }
    },
    "cause_str": "The request is not supported",
    "effect_str": "Failed to process the shadow copy operation.",
    "os_error_code": "0x80070032"
}

domain


environment

effect


Failed to create snapshot because VSS provider returned error 'Request is unsuppored'.

index


0

isRoot


false

kbLink


{
    "build": 20463,
    "lineTag": "0xBD28FDBD64EDB8F8",
    "os": "Windows",
    "product": "",
    "serCode": "0x015D06B1+0x00070021+0x0010C448+0x00000009+0x00000032+0x0000FFF0+0x80070032",
    "version": "15.0"
}

origin


{
    "code": 22873777,
    "fields": {
        "$module": "ArsDbBackupProvider_vsa64_28503"
    },
    "src": {
        "file": "d:\\391\\enterprise\\applications\\technology\\snapapi\\src\\backup_session.cpp",
        "func": "AppBackup::SnapApi::SnapapiBackupSession::CreateVssSnapshot",
        "line": 268,
        "tag": "0xe821934a13fc0262"
    },
    "suberror": {
        "code": 458785,
        "fields": {
            "$module": "ArsDbBackupProvider_vsa64_28503"
        },
        "src": {
            "file": "d:\\391\\core\\resizer\\generic\\snapinit.cpp",
            "func": "InitSnapshotBitmap",
            "line": 157,
            "tag": "0xe24f93d0b8d8c99f"
        },
        "suberror": {
            "code": 1098824,
            "fields": {
                "$module": "ArsDbBackupProvider_vsa64_28503"
            },
            "src": {
                "file": "d:\\391\\core\\fdisk\\win_snapshot.cpp",
                "func": "win_snapshot_core::AppendVolumesToSnapshot",
                "line": 1360,
                "tag": "0x3fec04e376b8a246"
            },
            "suberror": {
                "code": 9,
                "fields": {
                    "$module": "ArsDbBackupProvider_vsa64_28503",
                    "code": 50
                },
                "src": {
                    "file": "d:\\391\\core\\fdisk\\ver2\\arch\\windows\\win_errors.cpp",
                    "func": "Fdisk::AddKstatusError",
                    "line": 40,
                    "tag": "0x2aacb7b2ab852ac"
                },
                "suberror": {
                    "code": 65520,
                    "fields": {
                        "$module": "ArsDbBackupProvider_vsa64_28503",
                        "code": 2147942450
                    },
                    "src": {
                        "file": "d:\\391\\core\\common\\error.cpp",
                        "func": "Common::Error::AddWindowsError",
                        "line": 314,
                        "tag": "0xbd28fdbd64edb8f8"
                    },
                    "suberror": {},
                    "text": "The request is not supported",
                    "types": {
                        "$module": "A",
                        "code": "N"
                    }
                },
                "text": "Unknown status.",
                "types": {
                    "$module": "A",
                    "code": "N"
                }
            },
            "text": "Failed to add the volume to the snapshot.",
            "types": {
                "$module": "A"
            }
        },
        "text": "Failed to create volume snapshot.",
        "types": {
            "$module": "A"
        }
    },
    "text": "Failed to process the shadow copy operation.",
    "types": {
        "$module": "A"
    }
}

parentActivityId


1198193926964510720

reason


MemoVssProviderDoesNotSupportVolume

startTime


Tue Apr 26 2022 23:18:52 GMT+0700 (Giờ Đông Dương)

type


error

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      Untitled.png

                      66.82 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Wed, 04/27/2022 - 03:11

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello hiep tran,
thank you for your posting! Have you tried selecting "Automatically select snapshot provider" as suggested in the error message? If the issue persists after that, we'd recommend starting the troubleshooting with the steps outlined in https://kb.acronis.com/content/36200 and open a support ticket, if the more in-depth investigation is needed.

      
                
                
                    
                                                    Thu, 04/28/2022 - 10:22
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Sid Payne
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I have this same issue. Was this ever resolved?
Sid

      
                
                
                    
                                                    Thu, 11/24/2022 - 13:48
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daria Sorokina
                            

                            
                    
                        Acronis Support
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 487
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dear Sid Payne,
Thank you for reaching out. Have you tried the workaround from the Ekaterina's message? 
"Have you tried selecting "Automatically select snapshot provider" as suggested in the error message? If the issue persists after that, we'd recommend starting the troubleshooting with the steps outlined in https://kb.acronis.com/content/36200 and open a support ticket, if the more in-depth investigation is needed."

      
                
                
                    
                                                    Thu, 11/24/2022 - 16:39
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards, Daria Sorokina | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    hiep tran
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            you can go to " HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{71a27cdd-812a-11d0-bec7-08002be2092f} " check vaule and changed to "volsnap" , close it restart computer and try backup again ?

      
                
                
                    
                                                    Thu, 12/01/2022 - 07:58
                                                                            
                                
                            
                                            
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dear hiep tran,
thank you for taking the time to share your solution with the community! 

      
                
                
                    
                                                    Tue, 12/13/2022 - 14:01
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
