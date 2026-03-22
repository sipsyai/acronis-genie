# Restore of full device from cloud is very too slow

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/restore-full-device-cloud-very-too-slow

## Original Post
**Author:** Unknown

Restore of full device from cloud is very too slow

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Emilio Bruna
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 7
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                
                    
                        
            

Hi, after some testing our side, i notices that cloud restore of full device is WAAAAY TOO SLOW. For example I started one restore from cloud 2 days ago (with tibx of178gb), and after over 40hours is only at 76%!
Local backup of same device/archive was restored in less than 45 minutes.
We also noticed that with the cloud restore the connection bandwidth is not fully used, same for disk and cpu usage.
Calculated download time of the tibx based on www.speedtest.net/it should be 11 hours and half, and based on https://cloud-wr-eu2.acronis.com/speedtest/ 17 hours, but after over 40 hours the restore is still at 76%...
We also did acronis speed test with different connections and noticed that is always near half of the other speed test (that is near effective speed instead). Maybe acronis datacenters have limited resources or maybe there are some routing issues to italy...
I also thinked to workaround this problem by downloading the tibx and restoring it locally but it seems not possible.
For critical cases where only cloud backup is available, lasting 2-3 days to make a cloud restore of 170GB is litterarly UNACCEPTABLE.
This issue seems to be present with both windows and linux, with different acronis version, with both tib and tibx (even for previous restore cases I've not taken exact time). Restore times seem to be always N times higher of (computed) download time for the archive's backup size...
Anyone on this?
Thanks for any reply.



      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 11/22/2018 - 11:38

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Evgeny Ryuntyu
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 56
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Emilio,
 
It's Evgeny from Acronis Service Provider Support. 
As far as I understand you have faced an issue with the slow recovery of a disk-level backup (entire machine) from Cloud.
 
I would like to begin with the confirmation that the recovery from the Cloud is expected to be slower than the local recovery that you have observed. Having said that, I understand that 2-3 days compared to 45 minutes cannot be used as a proof that the situation was expected. We need to find the bottleneck of this issue to state any assumptions on the root cause. 
The speedtest results basically show you the connection speed and it is a good measure in terms of general connectivity or file download, but in case of an entire machine backup the speed is always going to be lower than the speedtest result. Take into account the I/O operations, the latency through all the network hops. 
Still 178GB over 40+ hours is not an expected result. The tibx (format 12) has large improvements to the speed of backup/recovery operations than the TIB type (format 11). It is sad that you don't have the results of previous restores, but I am sure the tibx recovery is faster. 
To understand why the slowness is present, I suggest you check the bootable media recovery:
https://www.acronis.com/en-us/support/documentation/BackupService/index… 
Knowing the results of the recovery speed from the bootable media might give us an idea whether the issue's bottleneck is within the OS way of managing the recovery (you wrote that similar results are both on Linux or Windows, bootmedia is a busybox system and is an alternative to try).
If the speed is relatively slow too, we might need to take a look at the logs collected after the recovery was running for some time. 
Additionally, once you contact us with the logs through the standard support process, we will be able to suggest on how to download the file in case of urgent recovery need.
It can be  done by yourself with LSR tool - it requires some reading + installation of the tool, so please take a look.
 
We will be glad to help you with the issue investigation, in case you collect the sysinfo report and share the details with us per the template 
 
Have a nice day in the meantime. 
-----------------------------------------------------------------------------------------------
Evgeny Ryuntyu | Senior Support Engineer
Acronis Backup Cloud | #1 Cloud Service Provider Backup

      
                
                
                    
                                                    Thu, 11/22/2018 - 18:13
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Emilio Bruna
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 7
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi, thanks for reply.
Even if backup is in tibx format was completed in 2 days and 8 hours.
Here connection test with acronis: https://acronis.speedtestcustom.com/result/38749900-f160-11e8-95c7-dd56… - Around 70mbps is  the usual speed for other uses outside of acronis.
Here the restore log (restore was done from default bootable recovery media based on linux downloaded from acronis cloud backup web interface, like near all):
<log build="12110" version="12" product="Acronis Backup Management Console">
  <event id="1" type="Information" time="11/20/18 11:36:12 AM" policy="[None]" task="[None]" InstanceType="[None]" Instance="[None]" Machine="[None]" message="User is running command. Command=Recovering volumes/Managing ASZ/Applying AUR; User=; clientProfileID=; clientSessionID=2F4437EB-38BD-4962-818B-7513DE2808AA" code="20,250,682(0x135003A)" module="309" Owner=""/>
  <event id="2" type="Information" time="11/20/18 11:36:13 AM" policy="[None]" task="[None]" InstanceType="[None]" Instance="[None]" Machine="[None]" message="Data recovery From avfs:/online?account%3d*******%26computer%3d1%26provider%3dAcronis%26stream%3dServer2016-280DFA48-4A08-4CF6-AA88-6A53CBD994E2-0389E716-7715-48B6-9F09-422B75CF4846A.tibx|Backup type: Image Recovery of: Disks &#32;&#32;" code="0(0x0)" module="0" Owner=""/>
  <event id="3" type="Information" time="11/20/18 11:36:13 AM" policy="[None]" task="[None]" InstanceType="[None]" Instance="[None]" Machine="[None]" message="Pending operation 53 started: 'Clearing disk (Hard disk 1)'." code="66,040(0x101F8)" module="1" Owner=""/>
  <event id="4" type="Information" time="11/20/18 11:36:13 AM" policy="[None]" task="[None]" InstanceType="[None]" Instance="[None]" Machine="[None]" message="Pending operation 14 started: 'Copying and merging partitions ()'." code="66,040(0x101F8)" module="1" Owner=""/>
  <event id="5" type="Information" time="11/20/18 11:41:44 AM" policy="[None]" task="[None]" InstanceType="[None]" Instance="[None]" Machine="[None]" message="Pending operation 14 started: 'Copying and merging partitions ()'." code="66,040(0x101F8)" module="1" Owner=""/>
  <event id="6" type="Information" time="11/20/18 11:41:56 AM" policy="[None]" task="[None]" InstanceType="[None]" Instance="[None]" Machine="[None]" message="Pending operation 53 started: 'Clearing disk (Hard disk 2)'." code="66,040(0x101F8)" module="1" Owner=""/>
  <event id="7" type="Information" time="11/20/18 11:41:56 AM" policy="[None]" task="[None]" InstanceType="[None]" Instance="[None]" Machine="[None]" message="Pending operation 14 started: 'Copying and merging partitions ()'." code="66,040(0x101F8)" module="1" Owner=""/>
  <event id="8" type="Information" time="11/21/18 3:06:00 PM" policy="[None]" task="[None]" InstanceType="[None]" Instance="[None]" Machine="[None]" message="Pending operation 61 started: 'Recovering MBR (Hard disk 1)'." code="66,040(0x101F8)" module="1" Owner=""/>
  <event id="9" type="Information" time="11/21/18 3:06:00 PM" policy="[None]" task="[None]" InstanceType="[None]" Instance="[None]" Machine="[None]" message="Pending operation 14 started: 'Copying and merging partitions ()'." code="66,040(0x101F8)" module="1" Owner=""/>
  <event id="10" type="Information" time="11/22/18 8:29:13 PM" policy="[None]" task="[None]" InstanceType="[None]" Instance="[None]" Machine="[None]" message="Pending operation 61 started: 'Recovering MBR (Hard disk 2)'." code="66,040(0x101F8)" module="1" Owner=""/>
  <event id="11" type="Information" time="11/22/18 8:29:14 PM" policy="[None]" task="[None]" InstanceType="[None]" Instance="[None]" Machine="[None]" message="Analyzing partition 'D:'..." code="66,039(0x101F7)" module="1" Owner=""/>
  <event id="12" type="Information" time="11/22/18 8:29:14 PM" policy="[None]" task="[None]" InstanceType="[None]" Instance="[None]" Machine="[None]" message="Analyzing partition 'E:'..." code="66,039(0x101F7)" module="1" Owner=""/>
  <event id="13" type="Information" time="11/22/18 8:29:14 PM" policy="[None]" task="[None]" InstanceType="[None]" Instance="[None]" Machine="[None]" message="Analyzing partition 'F:'..." code="66,039(0x101F7)" module="1" Owner=""/>
  <event id="14" type="Information" time="11/22/18 8:29:14 PM" policy="[None]" task="[None]" InstanceType="[None]" Instance="[None]" Machine="[None]" message="Fixing operating system bootability." code="1,900,544(0x1D0000)" module="29" Owner=""/>
  <event id="15" type="Information" time="11/22/18 8:29:14 PM" policy="[None]" task="[None]" InstanceType="[None]" Instance="[None]" Machine="[None]" message="Error 0x0|| trace level: information|| channel: tol-activity#34B8AB7A-7DCC-4626-807C-F05E76BFA935|| line: 0x0" code="0(0x0)" module="0" Owner=""/>
  <event id="16" type="Information" time="11/22/18 8:29:14 PM" policy="[None]" task="[None]" InstanceType="[None]" Instance="[None]" Machine="[None]" message="Error 0x0|| trace level: information|| channel: tol-activity#34B8AB7A-7DCC-4626-807C-F05E76BFA935|| line: 0x0" code="0(0x0)" module="0" Owner=""/>
  <event id="17" type="Information" time="11/22/18 8:29:14 PM" policy="[None]" task="[None]" InstanceType="[None]" Instance="[None]" Machine="[None]" message="Error 0x0|| trace level: information|| channel: tol-activity#34B8AB7A-7DCC-4626-807C-F05E76BFA935|| line: 0x0" code="0(0x0)" module="0" Owner=""/>
  <event id="18" type="Information" time="11/22/18 8:29:14 PM" policy="[None]" task="[None]" InstanceType="[None]" Instance="[None]" Machine="[None]" message="Error 0x0|| trace level: information|| channel: tol-activity#34B8AB7A-7DCC-4626-807C-F05E76BFA935|| line: 0x0" code="0(0x0)" module="0" Owner=""/>
  <event id="19" type="Information" time="11/22/18 8:29:14 PM" policy="[None]" task="[None]" InstanceType="[None]" Instance="[None]" Machine="[None]" message="Error 0x0|| trace level: information|| channel: tol-activity#34B8AB7A-7DCC-4626-807C-F05E76BFA935|| line: 0x0" code="0(0x0)" module="0" Owner=""/>
  <event id="20" type="Information" time="11/22/18 8:29:14 PM" policy="[None]" task="[None]" InstanceType="[None]" Instance="[None]" Machine="[None]" message="Error 0x0|| trace level: information|| channel: tol-activity#34B8AB7A-7DCC-4626-807C-F05E76BFA935|| line: 0x0" code="0(0x0)" module="0" Owner=""/>
  <event id="21" type="Information" time="11/22/18 8:29:14 PM" policy="[None]" task="[None]" InstanceType="[None]" Instance="[None]" Machine="[None]" message="Error 0x0|| trace level: information|| channel: tol-activity#34B8AB7A-7DCC-4626-807C-F05E76BFA935|| line: 0x0" code="0(0x0)" module="0" Owner=""/>
  <event id="22" type="Information" time="11/22/18 8:29:14 PM" policy="[None]" task="[None]" InstanceType="[None]" Instance="[None]" Machine="[None]" message="Error 0x0|| trace level: information|| channel: tol-activity#34B8AB7A-7DCC-4626-807C-F05E76BFA935|| line: 0x0" code="0(0x0)" module="0" Owner=""/>
  <event id="23" type="Information" time="11/22/18 8:29:14 PM" policy="[None]" task="[None]" InstanceType="[None]" Instance="[None]" Machine="[None]" message="The operating system bootability has been fixed." code="1,900,544(0x1D0000)" module="29" Owner=""/>
  <event id="24" type="Information" time="11/22/18 8:29:14 PM" policy="[None]" task="[None]" InstanceType="[None]" Instance="[None]" Machine="[None]" message="Fixing operating system bootability." code="1,900,544(0x1D0000)" module="29" Owner=""/>
  <event id="25" type="Information" time="11/22/18 8:29:14 PM" policy="[None]" task="[None]" InstanceType="[None]" Instance="[None]" Machine="[None]" message="The operating system bootability has been fixed." code="1,900,544(0x1D0000)" module="29" Owner=""/>
  <event id="26" type="Information" time="11/22/18 8:29:14 PM" policy="[None]" task="[None]" InstanceType="[None]" Instance="[None]" Machine="[None]" message="Command has completed successfully. Command=Recovering volumes/Managing ASZ/Applying AUR;&#32;" code="20,250,683(0x135003B)" module="309" Owner=""/>
</log>

Only account name replaced with "*" for security/privacy.
I not have time to do other tests now but for future ones any advice is welcome, thanks.

      
                
                
                    
                                                    Mon, 11/26/2018 - 14:38
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Emilio,
Please submit a support ticket at https://www.acronis.com/support/contact-us/ (select Support for Service providers), so that our engineers can conduct more in-depth investigation. 

      
                
                
                    
                                                    Tue, 12/04/2018 - 13:58
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
