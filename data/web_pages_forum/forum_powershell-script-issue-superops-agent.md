# Powershell Script Issue - SuperOps agent

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/powershell-script-issue-superops-agent

## Original Post
**Author:** Unknown

Powershell Script Issue - SuperOps agent

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Leandro Garcia
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello everyone!
I'm trying to deploy the SuperOps agent using a Powershell script from the Acronis Cyber Protect Cloud console using the following script from the SuperOps webpage:
 
Invoke-Command -ScriptBlock { param ($url) $fileName=Split-Path -Path "$url" -Leaf; invoke-WebRequest -Uri "$url" -Outfile "$fileName"; Start-Process -Wait -FilePath msiexec -ArgumentList /i,$fileName,/qn,LicenseAccepted=YES; } -ArgumentList "<MSI Download URL from site>"
 
when I add the script to the Acronis console, I use the following parameters:
Account to execute the script: System account
PowerShell execution policy: Bypass (I have tried almost all of the execution policies)
Maximum duration: 10 minutes
 
The script is successfully deployed but in the output file I get the following error:
 
invoke-WebRequest : Access to the path 'C:\ProgramData\Acronis\Agent\var\run\cyber-scripting-executor\11e5470c-6274-47a
a-915c-cc45af451ee4\LEMWV3R1VZ0G_1LSVPD4OM7S3K_windows_x64.msi' is denied.
At C:\ProgramData\Acronis\Agent\var\run\cyber-scripting-executor\11e5470c-6274-47aa-915c-cc45af451ee4\36ee4d50-f075-4bf
9-9f38-54d348765de0.ps1:1 char:85
+ ... url" -Leaf; invoke-WebRequest -Uri "$url" -Outfile "$fileName"; Start ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [Invoke-WebRequest], UnauthorizedAccessException
    + FullyQualifiedErrorId : System.UnauthorizedAccessException,Microsoft.PowerShell.Commands.InvokeWebRequestCommand
 
I attached the output, any recommendations to be able to deploy the superops agent from the Acronis console?
Thanks in advance!

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      0c1f9b87-d146-4a50-b2e7-642deaca0772_1383165346067775488.zip

                      646 bytes
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Fri, 10/13/2023 - 21:44

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Leandro.
Please reply to the email our support sent you on the 14th of October.
We are ready to help you and answer to all the questions you may have.
Best regards.

      
                
                
                    
                                                    Mon, 10/16/2023 - 13:36
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
