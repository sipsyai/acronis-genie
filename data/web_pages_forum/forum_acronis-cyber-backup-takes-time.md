# Acronis cyber backup takes time

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/acronis-cyber-backup-takes-time

## Original Post
**Author:** Unknown

Acronis cyber backup takes time

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Leo
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi all,
I have a client with Hyper-V and virtual file server, the file server has Acronis agent installed, the agent is connected with a protection plan that controls when backup is taken (time, date, etc.).
The servers are Windows Server 2019 Standard, it’s a local AD environment.
The data is located on a virtual drive that is attached to file VM. It’s large, about 4TB.
I have shadow copies enabled on this data drive.
The agent is the most recent version.
Issue being sometimes it takes forever to complete backup job; I receive email saying that job had stalled. But, it always finishes but it may take at least 12 hours!
I ran Acronis VSS doctor, and it found a few issues:
VSS shadow storage status, it says that I set 10% for this volume, which is about 10%.
Disk I/O load, says that disk is overloaded.
I see nothing in particular regarding logs in system even viewer, unless there is something you can point out to look for.
Please let me know what I can do to improve its performance!
TIA.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 11/04/2024 - 19:03

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Cyber Protect
            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Welcome to the forum.
The speed of backups is typically influenced by various factors on the user’s end and is not related to the VSS (Volume Shadow Copy Service). VSS simply creates a snapshot of the disk for the backup, which usually only takes a few minutes.
Backup speed can be affected by factors such as backup size, connection quality, hardware performance, and system load. To improve backup performance, I suggest scheduling backups during non-peak hours—like overnight—when machines are less overloaded.
Increasing the RAM of VMs may also help. Additionally, splitting backups into separate plans, such as backing up individual disks instead of the entire machine at once, can improve speed.
If you have any questions, please reach out to our support team at Acronis Support.
Best regards.

      
                
                
                    
                                                    Tue, 11/05/2024 - 09:22
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Leo
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Yes, the job runs at 2 AM with minimal host activity, the system has 16 GB of RAM and quad core allocation. I can bump up memory at least twice with no impact on the host.
It also backs up only one disk with folders, no boot disk or an entire machine.
What do you think is the best approach?

      
                
                
                    
                                                    Tue, 11/05/2024 - 18:17
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Cyber Protect
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Leo wrote:

Yes, the job runs at 2 AM with minimal host activity, the system has 16 GB of RAM and quad core allocation. I can bump up memory at least twice with no impact on the host.
It also backs up only one disk with folders, no boot disk or an entire machine.
What do you think is the best approach?


Hello!
Backing up folders doesn’t necessarily mean the backup size will be small—speed largely depends on the total data size. For example, backing up hundreds of gigabytes or even 1 TB will always take time. This is primarily influenced by the local hardware and the capacity of the disks to read and write data to the destination.
I recommend reviewing the connections between the machine and the backup destination. You might also try splitting the backup plan into two tasks to potentially speed up the process (testing this approach first could show if it makes a difference).
Best regards.

      
                
                
                    
                                                    Wed, 11/06/2024 - 09:00
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Leo
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I recommend reviewing the connections between the machine and the backup destination. - How?
The upload speed is about 200Mb/s for this server.
You might also try splitting the backup plan into two tasks to potentially speed up the - What's going to happen with existing data on Acronis cloud if I split and make to plans?
Any way to extend that alert setting that send me email that job stalled?
Thanks.

      
                
                
                    
                                                    Thu, 11/07/2024 - 00:17
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Cyber Protect
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Leo wrote:

I recommend reviewing the connections between the machine and the backup destination. - How?
The upload speed is about 200Mb/s for this server.
You might also try splitting the backup plan into two tasks to potentially speed up the - What's going to happen with existing data on Acronis cloud if I split and make to plans?
Any way to extend that alert setting that send me email that job stalled?
Thanks.


The upload speed of your bandwidth doesn’t affect backup speed unless you're backing up to the cloud. The primary factor is the read and write capacity of your hardware and disks.
Ensure that the machines with the backup agent installed can access the location where you store the backups (assuming backups are being run locally). If the connections are unstable it's expected the backups will be always slow.
If you create new backup plans and split the backups, you’ll end up with two separate backup files instead of one. Previous backups will remain available for recovery but won’t be used in new backup cycles.
As for the alarms, they are triggered when the program detects that a task is frozen and isn’t progressing for an extended period. Unfortunately, this behavior cannot be changed.
If you need further assistance, I recommend reaching out to our support team for guidance.
Best regards.

      
                
                
                    
                                                    Thu, 11/07/2024 - 08:57
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Leo
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            The backup destination is Acrons cloud.
Can you help me to contact the backup support team or open the case?

      
                
                
                    
                                                    Thu, 11/07/2024 - 23:06
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Cyber Protect
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Leo wrote:

The backup destination is Acrons cloud.
Can you help me to contact the backup support team or open the case?


Hello!
As far as I can see in the records, your account is under PAX8.
You will need to contact PAX8 so they can raise a ticket with us.
Regarding your comments, since the backups are stored in the cloud, that does change the situation.
You will be asked to execute this test: https://care.acronis.com/s/article/47678-Acronis-Cyber-Protect-Cloud-Acronis-Cyber-Protect-15-and-Acronis-Cyber-Backup-12-5-Connection-Verification-Tool?language=en_US
Once you’ve executed it, you need to compare the average write speed with the amount of data to see if it matches the backup time.
Best regards.

      
                
                
                    
                                                    Mon, 11/11/2024 - 11:58
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
