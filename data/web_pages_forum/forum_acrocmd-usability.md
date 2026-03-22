# acrocmd usability

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/acrocmd-usability

## Original Post
**Author:** Unknown

acrocmd usability

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Tom
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 37
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Quite new to this, but isn't it very queer by engeneering to design this:
myhost:~ # acrocmd sysinfo
An error occurred while executing the command.
    Error: 0x1510008
    $module = "acrocmd_lxa64_39376"
    PrintPerformingResult : d:/925/enterprise/command_line/engine/impl/engine.cpp(65)
Parameter 'loc' is not defined.
    Error: 0x1510027
    $module = "abr11cli_lxa64_39376"
    ValidateOption : d:/925/enterprise/command_line/abr11/commands/sysinfo/sysinfo_command.cpp(93)
myhost:~ # 

acrocmd is outputting seven error lines, just to tell me that a command line parameter is missing.
Acronis engineers: is usability a concern for you?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 03/10/2025 - 07:29

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Cyber Protect 15
            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Tom,
Which process are you trying to execute exactly?
Best regards.
 

      
                
                
                    
                                                    Mon, 03/10/2025 - 08:10
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Tom
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 37
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            just getting warm with acrocmd, but this command is, as shown throwing so many errors, that I can't see the forest for the trees.
Like another example:
 
alocalhost:~ # acrocmd list disks
An error occurred while executing the command.
    Error: 0x1510008
    $module = "acrocmd_lxa64_39376"
    PrintPerformingResult : d:/925/enterprise/command_line/engine/impl/engine.cpp(65)
    Error: 0x151002B
    $module = "acrocmd_lxa64_39376"
    RequestItems : d:/925/enterprise/command_line/engine/impl/remote_access_impl.cpp(507)
Dml::AsyncServer::State::JobPool
    Error: 0xF90004
    $module = "mms_lxa64_39376"
    State : d:/925/enterprise/common/dml/messaging/async_server.cpp(241)
ASYNC: Action sequence pending action job.
    Error: 0xF90004
    $module = "mms_lxa64_39376"
    Describe : d:/925/enterprise/common/async/semaphore.cpp(154)
ASYNC: Full barrier action job.
    Error: 0xF90004
    $module = "mms_lxa64_39376"
    Describe : d:/925/enterprise/common/async/full_barrier.cpp(227)
The SnapAPI kernel module is not loaded for the kernel 4.12.14-122.216-default that is running in this system. Install the module for this kernel version, and then retry the backup.
    Error: 0x950065
    $module = "disk_bundle_lxa64_39376"
    GetDisks : d:/925/enterprise/disk_manager/daapi1/addon/impl/dm_browser_impl.cpp(669)
alocalhost:~ #


      
                
                
                    
                                                    Mon, 03/10/2025 - 08:16
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect 15
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Tom wrote:

just getting warm with acrocmd, but this command is, as shown throwing so many errors, that I can't see the forest for the trees.
Like another example:
 
alocalhost:~ # acrocmd list disks
An error occurred while executing the command.
    Error: 0x1510008
    $module = "acrocmd_lxa64_39376"
    PrintPerformingResult : d:/925/enterprise/command_line/engine/impl/engine.cpp(65)
    Error: 0x151002B
    $module = "acrocmd_lxa64_39376"
    RequestItems : d:/925/enterprise/command_line/engine/impl/remote_access_impl.cpp(507)
Dml::AsyncServer::State::JobPool
    Error: 0xF90004
    $module = "mms_lxa64_39376"
    State : d:/925/enterprise/common/dml/messaging/async_server.cpp(241)
ASYNC: Action sequence pending action job.
    Error: 0xF90004
    $module = "mms_lxa64_39376"
    Describe : d:/925/enterprise/common/async/semaphore.cpp(154)
ASYNC: Full barrier action job.
    Error: 0xF90004
    $module = "mms_lxa64_39376"
    Describe : d:/925/enterprise/common/async/full_barrier.cpp(227)
The SnapAPI kernel module is not loaded for the kernel 4.12.14-122.216-default that is running in this system. Install the module for this kernel version, and then retry the backup.
    Error: 0x950065
    $module = "disk_bundle_lxa64_39376"
    GetDisks : d:/925/enterprise/disk_manager/daapi1/addon/impl/dm_browser_impl.cpp(669)
alocalhost:~ #



Hello!
Resolution Steps:

Check if your OS is supported:
	Ensure that you are using a supported version of SUSE Linux Enterprise Server (SLES): 10, 11, 12, or 15.Supported Operating Systems and Environments


Verify Kernel Version:
	Confirm that the kernel version you are using is 4.12.14-122.216-default.


Install SnapAPI Kernel Module:
	You need to install the SnapAPI kernel module for the current kernel version. If you're using a Linux-based system, you can typically do this via the following steps:
Download and install the SnapAPI kernel module specific to your kernel version.
This may require using the installation package for your system or kernel module repository.
Once the SnapAPI module is installed, load it into the kernel.


Retry the Backup.

If the issue persists, please raise a ticket with the team so we can help troubleshoot the issue.
Best regards.

      
                
                
                    
                                                    Mon, 03/10/2025 - 09:25
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Tom
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 37
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            The issue initially was about the verbosity of the error messages in a command like "acrocmd sysinfo" where just one parameter is missing. This appears to be OS independent, as we also see it on the mgmt server with its deployed CentOS Linux.
About the OS support of "acrocmd list disks": in this example we are looking at a SLES12 SP5 system. This should be supported.
Now in the URL provided by you I see "Configurations with Btrfs are not supported for SUSE Linux Enterprise Server 12 and SUSE Linux Enterprise Server 15."
Seriously? Btrfs is the default root FS for SLES12 and SLES15 installs since about 10 years!

      
                
                
                    
                                                    Mon, 03/10/2025 - 09:58
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect 15
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Tom wrote:

The issue initially was about the verbosity of the error messages in a command like "acrocmd sysinfo" where just one parameter is missing. This appears to be OS independent, as we also see it on the mgmt server with its deployed CentOS Linux.
About the OS support of "acrocmd list disks": in this example we are looking at a SLES12 SP5 system. This should be supported.
Now in the URL provided by you I see "Configurations with Btrfs are not supported for SUSE Linux Enterprise Server 12 and SUSE Linux Enterprise Server 15."
Seriously? Btrfs is the default root FS for SLES12 and SLES15 installs since about 10 years!


Yes, that's correct. Unfortunately, Btrfs is currently unsupported for SUSE.

      
                
                
                    
                                                    Tue, 03/11/2025 - 07:32
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
