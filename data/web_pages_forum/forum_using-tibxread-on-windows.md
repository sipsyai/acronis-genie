# Using TIBXRead on Windows

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/using-tibxread-windows

## Original Post
**Author:** Unknown

Using TIBXRead on Windows

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Bill Bach
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I am trying to get the TIBXREAD command line tool working on my Windows Server 2019 installation of CP16. The Explorer plugin seems to work OK, but I am looking to do some validation scripting that can be automated, so I really need the command line version working.  
When I run this from the C:\Program Files\Acronis\BackupAndRecovery folder, it spits back DLL errors for files not in the path.  I tried copying the first two DLL's into the BackupAndRecovery folder (astor_client.dll and winpthreads4.dll, which were both in the C:\Program Files\Acronis\ArchiveServer folder), but then I get to pcs_stats.dll, and this file is found in a completely different location of  C:\Program Files\Common Files\Acronis\BackupAndRecovery\Common.  It seems silly to have to copy a bunch of files around to get a basic tool working, so what am I missing?
We have already tried a "Repair" to no avail.  The Windows path is currently set up as the following:
Path=C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\WINDOWS\System32\OpenSSH\;C:\Program Files\Acronis\CommandLineTool\;C:\Program Files\Acronis\PyShell\bin\;C:\Program Files (x86)\Common Files\Acronis\SnapAPI\;C:\Program Files (x86)\Common Files\Acronis\VirtualFile\;C:\Program Files (x86)\Common Files\Acronis\VirtualFile64\;C:\Users\Administrator.EMPIRE\AppData\Local\Microsoft\WindowsApps
Note that ArchiveServer was not in the path, and neither is C:\Program Files\Common Files\Acronis\BackupAndRecovery\Common.  What other folders are needed in the path for this tool to function?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 10/08/2025 - 20:09

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi,
Thanks for reaching out. A few points to clarify:

Could you confirm which Acronis product you are using? We don’t have any tool officially named TIBXREAD.


What is your goal with this tool? Are you trying to automate validation of backups? Understanding what you’re trying to achieve will help us guide you properly.

Regarding the DLL errors: Acronis command-line tools rely on specific folders being in the system path, but manually copying DLLs is not recommended, as it can cause unexpected issues. Once we know exactly which product/version you are using and what you want to accomplish, we can provide the correct instructions for using the command-line tool without breaking dependencies.
Could you provide:

The exact product name and version (e.g., Acronis Cyber Protect 16, Build XXX)


The task or script you’re aiming to run

Best regards.

      
                
                
                    
                                                    Thu, 10/09/2025 - 15:23
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Bill Bach
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            1) As you might imply from the Forum I posted in, this is Acronis Cyber Protect 16.  The exact Build numbers are Console Version 16.0.4622 and Server Version 16.4.40354.  You DO actually have a tool called TIBXREAD, which is documented here: https://www.acronis.com/en-us/support/documentation/AcronisCyberProtect…
2) My goal is to leverage additional scripting to confirm the data stored within any given series of backup images.  Our previous system with v12.5 replicates backups from the primary NAS to a secondary NAS, and then onwards to 6 external USB drives once per week, in a rotation that includes 4 drives on the shelf, one in a fireproof safe, and one in a bank safe deposit box (40 miles away).  We do this to improve over the 3/2/1 backup strategy to actually provide a deeper level of restore with literally MONTHS of fallback capability should a disaster occur, with the added geographic protection for that last line of defense. Anyway, this automatic replication needs some additional validation, too, so I want to be able to "list backups" from the source data set and from the target copy and confirm identical results (and perhaps calculate a hash on at least one volume), which will help ensure that backups are not mangled in any way during the replication cycle.  I didn't need any extra validation under the v11 TIB format, as each incremental and full backup file was immutable and each file had the proper date stamp right in the name. 
I agree that copying DLL's around is a silly idea, which is why I am posting this question here.

      
                
                
                    
                                                    Thu, 10/09/2025 - 16:13
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Bill Bach wrote:

1) As you might imply from the Forum I posted in, this is Acronis Cyber Protect 16.  The exact Build numbers are Console Version 16.0.4622 and Server Version 16.4.40354.  You DO actually have a tool called TIBXREAD, which is documented here: https://www.acronis.com/en-us/support/documentation/AcronisCyberProtect…
2) My goal is to leverage additional scripting to confirm the data stored within any given series of backup images.  Our previous system with v12.5 replicates backups from the primary NAS to a secondary NAS, and then onwards to 6 external USB drives once per week, in a rotation that includes 4 drives on the shelf, one in a fireproof safe, and one in a bank safe deposit box (40 miles away).  We do this to improve over the 3/2/1 backup strategy to actually provide a deeper level of restore with literally MONTHS of fallback capability should a disaster occur, with the added geographic protection for that last line of defense. Anyway, this automatic replication needs some additional validation, too, so I want to be able to "list backups" from the source data set and from the target copy and confirm identical results (and perhaps calculate a hash on at least one volume), which will help ensure that backups are not mangled in any way during the replication cycle.  I didn't need any extra validation under the v11 TIB format, as each incremental and full backup file was immutable and each file had the proper date stamp right in the name. 
I agree that copying DLL's around is a silly idea, which is why I am posting this question here.


Thank you for sharing the context.
Indeed, the TIBXREAD (under forensic tools) utility exists and is primarily designed for internal verification and analysis of .tibx archives.
However, it’s not a standalone tool, which is why you’re encountering missing dependency errors when running it outside its expected environment. The dependencies are dynamically loaded from several Acronis service paths, and manually copying DLLs is not recommended, as it can cause version mismatches.
What you’re trying to achieve — automated validation and comparison of replicated backups — is possible, but not through TIBXREAD directly.
I’ve raised a ticket with our team to confirm if your specific use case can be supported or if a workaround can be provided.
You can expect an email update as soon as possible.
Best regards,

      
                
                
                    
                                                    Fri, 10/10/2025 - 10:38
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
