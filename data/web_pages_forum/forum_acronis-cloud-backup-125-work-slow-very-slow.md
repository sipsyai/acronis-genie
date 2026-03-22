# Acronis cloud Backup 12.5 work slow, very slow

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/acronis-cloud-backup-125-work-slow-very-slow

## Original Post
**Author:** Unknown

Acronis cloud Backup 12.5 work slow, very slow

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Avi Vaserman
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello Everyone,
 
I have some wired issue, Acronis cloud backup with one server works very very slow, 1 GB to cloud 1 takes one hour.
I tried switching to agentless and is the same thing, I have 100/100 symmetrical fiber, connection to Acronis data centers I get 90/90 so it perfect, What I found agents called MMS.exe and service_process.exe never get over 200kb.
Is there any way I can bump a speed of that agents maybe via registry or any another way

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sun, 03/01/2020 - 20:21

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ivaylo Tsvetkov
                            

                            
                    
                        Acronis engineer
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 85
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Avi,
In such cases we can suggest to increase the Archive3 cache that will boost the speed of processing the backups. Before applying the changes you might first check the current Archive3 cache in the MMS log:
- for Windows machines you can find it in: C:\ProgramData\Acronis\BackupAndRecovery\MMS\mms.0.log
- for Linux machines: /var/lib/Acronis/BackupAndRecovery/MMS/mms.0.log
Look for a line where the backup service_process has started, it should contain the message like:
service_process(5912): Using default page cache size 63 MB
63 MB is the default cache size. I would suggest you increase the cache size to 1 GB first, follow the instructions from this KB article, depending on the OS of the backed-up server: https://kb.acronis.com/content/61758
Hope this resolves the slowness of your backups.
Regards,
Ivaylo
 

      
                
                
                    
                                                    Tue, 03/10/2020 - 13:31
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ivaylo Tsvetkov | API Platform Senior Support Engineer 

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                            
                Products: 
                Acronis Cyber Protect Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    ullo project
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello! I installed Acronis Cyber Backup on VPS (Ubuntu 18.4). When I do something in the control panel https://185.233.119.35:9877 then the server freezes after a while and becomes inaccessible both in html and ssh. Such server freezes occur at the moment of opening the list of actions or changing the backup creation settings.
In the attachment, the log file /var/lib/Acronis/BackupAndRecovery/MMS/mms.0.log

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      540781-185792.log

                      127.92 KB
                  
          
    

                    
    
                
                
                    
                                                    Wed, 06/03/2020 - 15:07
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ivaylo Tsvetkov
                            

                            
                    
                        Acronis engineer
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 85
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            

Hello Ullo,
I would suggest you opening a Support case as it requires deeper investigation, collection of system information logs and read-only access to your Backup Console from a Support engineer.
Please, open a Support case, provide your Acronis Cyber Cloud account login name, DC of your account, affected tenant group, affected machine, and our Support engineers will investigate it.
Thank you.



      
                
                
                    
                                                    Thu, 06/04/2020 - 11:17
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ivaylo Tsvetkov | API Platform Senior Support Engineer 

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                            
                Products: 
                Acronis Cyber Protect Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Ivaylo Tsvetkov wrote:

63 MB is the default cache size. I would suggest you increase the cache size to 1 GB first, follow the instructions from this KB article, depending on the OS of the backed-up server: https://kb.acronis.com/content/61758


It looks like this link is password protected or not publicly accessible.

      
                
                
                    
                                                    Mon, 06/15/2020 - 15:53
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ivaylo Tsvetkov
                            

                            
                    
                        Acronis engineer
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 85
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello George,
Yes, you are correct it contains internal information and not publicly available.
The value <size suggested by the developer> can be either in MB or GB (1024M or 1G). Both ways are correct.
In Windows
To enable the cache perform the following steps:
Open Computer Properties -> Advanced system settings -> Environmental Variables.
Under System Variables click New.
Set Variable name to A3_CACHE_SIZE
Set Variable value to <size suggested by the developer>
Restart Acronis Managed Machine Service.
Alternatively, you can open the Command line prompt and issue:setx /M A3_CACHE_SIZE 2G

In macOS
To enable the cache perform the following steps:
Open Terminal and execute these commands:      sudo launchctl stop acronis_mms
	     cd /Library/Application\ Support/BackupClient/Acronis/Backup\ Agent.app/Contents/Library/sbin/
	     sudo cp acronis_mms acronis_mms.bak
Open the file acronis_mms for editing. For example, in nano editor: 
	     $ sudo nano acronis_mms
Input the export below ulimits     export A3_CACHE_SIZE=<size suggested by the developer>
Save changes and close the file.
Execute:      sudo launchctl start acronis_mms

In Linux
To enable the cache perform the following steps:
Open Terminal and execute these commands:      sudo service acronis_mms stop     cd /usr/sbin/     sudo cp acronis_mms acronis_mms.bak
Open the file acronis_mms for editing. For example, in nano editor: 
	     $ sudo nano acronis_mms
Input the export below ulimit     export A3_CACHE_SIZE=<size suggested by the developer>
Save changes and close the file.
Execute:      sudo service acronis_mms start

      
                
                
                    
                                                    Tue, 06/16/2020 - 10:09
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ivaylo Tsvetkov | API Platform Senior Support Engineer 

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                            
                Products: 
                Acronis Cyber Protect Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    andsec
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I try his solution, but not work for me.
2nd  line is export A3_CACHE_SIZE=2048M
 
Last month a backup in few minutes, max 1 hr
Now, 48/72 hour
Please help me.
Centos 7 on dedicated server ionos
Thanks a lot!
 

      
                
                
                    
                                                    Fri, 07/17/2020 - 11:15
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ivaylo Tsvetkov
                            

                            
                    
                        Acronis engineer
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 85
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            


Hello,
I would suggest opening a Support case as it requires deeper investigation, collection of system information logs and read-only access to your Backup Console from a Support engineer.
Please, open a Support case, provide your Acronis Cyber Cloud account login name, DC of your account, affected tenant group, affected machine, and our Support engineers will investigate it.
Currently we have few case where backup to NAS storage jumped from 1 hour to 16-17 hours after updating the backup agent, but there is still different root cause for them, some are network connectivity issue, some the agent itself, or just some kind of bad performance. Better open a case and provide all information so we can investigate it more deeply.
Thank you.




      
                
                
                    
                                                    Tue, 07/21/2020 - 11:41
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ivaylo Tsvetkov | API Platform Senior Support Engineer 

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                            
                Products: 
                Acronis Cyber Protect Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    ScottS
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 22
                
            
            
                
                    Comments: 46
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            DELETED

      
                
                
                    
                                                    Mon, 01/18/2021 - 15:20
                                                                            
                                
                            
                                            
                                            
    
                    
                Windows 10 x64 Pro (latest non-preview version); GIGABYTE Aorus Elite mobo; i7-8700; 64GB RAM; Samsung Evo 960 M.2 NVMe pcie

            
                            
                Products: 
                ATI 2021, Cloud storage
