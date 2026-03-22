# Acronis backup agent failing

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/acronis-backup-agent-failing

## Original Post
**Author:** Unknown

Acronis backup agent failing

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Ravi Mukti
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
We have installed Acronis backup agent (64-bit) version 12.5.12960 on Centos 7 with Plan: Entire machine to Cloud storage. When trying to run the entire system backup it is failing. 
We see the following errors in the logs: 
The activity has failed due to a restart of the service.

Additional info:
------------------------
Error code: 78
Module: 309
LineInfo: 0x7564DA35B0F1EAF5
Fields: {"$module":"mms_lxa64_12960"}
Message: The activity has failed due to a restart of the service.
------------------------
Error code: 205
Module: 309
LineInfo: 0x7564DA35B0F1EAFD
Fields: {"$module":"mms_lxa64_12960"}
Message: The activity has failed due to an unexpected machine reboot or the backup process was terminated.
We then checked and confirmed that the backup agent service is crashing with the following details: 
================
Aug 19 13:59:49 localhost journal: Acronis Backup and Recovery[20864]: Error 0x294000d: Socket bind error | trace level: error | line: 0x18073c0bca1ee95e | file: E:/bs_hudson/workspace/mod-ht806 | function: Run | Address: 127.0.0.1 | Port: 43234 | $module: http_lxa64_304
Aug 19 13:59:49 localhost systemd: acronis_mms.service: main process exited, code=exited, status=125/n/a
Aug 19 13:59:49 localhost systemd: Unit acronis_mms.service entered failed state.
================
Please suggest. 
Regards,
Ravi M
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 08/19/2019 - 06:11

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Good day Ravi
Can you please confirm the current state of the MMS service?
Is it running, in a stopping state, in a stopped state or does it stop as soon as you start it?
Regards

      
                
                
                    
                                                    Tue, 08/20/2019 - 13:07
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ravi Mukti
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Jason,
When we initiate the backup from the portal the service acronis_mms.service fails. Here is the output we see: 
Aug 19 13:59:49 localhost.localdomain systemd[1]: Unit acronis_mms.service entered failed state.
Aug 19 13:59:49 localhost.localdomain systemd[1]: acronis_mms.service failed.
After sometime when the backup portal reports that the backup operation has failed the service  acronis_mms.service is again in running state. 
I have also re-installed the backup agent on the server but it didn't help. I have also ensured that it is not a firewall issue. Below is the output for your reference: 
 
[root@localhost ver]# ./linux_port_checker_en-US_x86_64 -u=xxxxxxxx
Enter password: ****
Check for au1-cloud.acronis.com 443 Ok
Check for au1-cloud.acronis.com 7787 Ok
Check for baas-fes-au1.acronis.com 44445 Ok
Check for au1-baas.acronis.com 8443 Ok
Any suggestion or help would be appreciated.
 
Regards,
Ravi M

      
                
                
                    
                                                    Wed, 08/21/2019 - 05:44
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Ravi
This seems to be a service crash, can you check the following log for me:
Check /var/log/messages for segfault messages of mms proces, you should see something like this:
Aug 22 08:39:32 localhost kernel: mms[15295]: segfault at 0 ip 00007ffe6210fa79 sp 00007fff87d2a7e0 error 4 in libDiskBundle.so[7ffe6143c000+240f000]
Please let me know what you find
Regards

      
                
                
                    
                                                    Thu, 08/22/2019 - 10:00
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ravi Mukti
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Jacob,
Thank you for your reply.
I have already tried to check this by following the mentioned forums https://kb.acronis.com/content/61650. However, there is nothing related found in the error logs. 
/var/log/messages for segfault
The only log I can find related to 'mms' is as mentioned below: 
 
cat /var/log/messages | grep 'mms'
Aug 19 13:54:47 localhost systemd: acronis_mms.service: main process exited, code=killed, status=9/KILL
Aug 19 13:54:47 localhost systemd: Unit acronis_mms.service entered failed state.
Aug 19 13:54:47 localhost systemd: acronis_mms.service failed.
Aug 19 13:59:47 localhost systemd: acronis_mms.service holdoff time over, scheduling restart.
Aug 19 13:59:49 localhost systemd: acronis_mms.service: main process exited, code=exited, status=125/n/a
Aug 19 13:59:49 localhost systemd: Unit acronis_mms.service entered failed state.
Aug 19 13:59:49 localhost systemd: acronis_mms.service failed.
Aug 19 14:04:49 localhost systemd: acronis_mms.service holdoff time over, scheduling restart.
Regards,
Ravi M

      
                
                
                    
                                                    Thu, 08/22/2019 - 10:11
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ravi Mukti
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Jacob,
I would also like to add some more details about the issue. When we initiate the backup from console it starts and shows 20% complete and then fails to load after it.
This has one of the behaviours I have notified when I run the backup from the console. 
Hope this helps in your investigation. 
Regards,
Ravi M

      
                
                
                    
                                                    Thu, 08/22/2019 - 10:14
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Ravi
Since there are no logs  pertaining to segfault mms I would not be able to further investigate.
I would strongly recommend logging a support case with Acronis as this will most likely require a remote session to troubleshoot. When logging the case with Acronis support team please ensure that you provide them with the:
System information log:
https://kb.acronis.com/content/54608
As well as the process monitor log:
https://kb.acronis.com/content/2295
And lastly just add the Strace logs aswell:
https://kb.acronis.com/content/37659
The above will help speed up the troubleshooting process
Regards
 

      
                
                
                    
                                                    Fri, 08/23/2019 - 12:56
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Any chance you're running out of RAM and the OOM killer is killing the acronis_mms process?

      
                
                
                    
                                                    Thu, 08/29/2019 - 09:12
