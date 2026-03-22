# How to clone Linux OS on RAID 5 to a VM with non-RAID

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/how-clone-linux-os-raid-5-vm-non-raid

## Original Post
**Author:** Unknown

How to clone Linux OS on RAID 5 to a VM with non-RAID

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    The Immortal
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Dear Sirs,
I'm not sure if this is the right section to create a topic, so I apologize in advance.
I need to clone a Linux OS running on a RAID 5 array (3 disks) to a virtual machine with a non-RAID setup (1 disk).
Most YouTube tutorials cover only simple cases, such as copying one entire disk to another, but my situation is more complex.
Here is the configuration of my source Fedora 32-bit system:
# df -h
Filesystem      Size  Used Avail Use% Mounted on
devtmpfs        3.9G     0  3.9G   0% /dev
tmpfs           3.9G     0  3.9G   0% /dev/shm
tmpfs           3.9G  992K  3.9G   1% /run
tmpfs           3.9G     0  3.9G   0% /sys/fs/cgroup
/dev/md0         50G   43G  3.8G  93% /
tmpfs           3.9G  8.0K  3.9G   1% /tmp
/dev/sdc2       194M  163M   22M  89% /boot
/dev/md4        1.8T  614G  1.1T  37% /home
/dev/md1         59G   24G   33G  42% /var/log
/dev/md2        148G   60M  140G   1% /backup
/dev/md5        3.1T  811G  2.1T  28% /var/samba
/dev/md3        394G  374G     0 100% /var/lib/mysql
tmpfs           798M     0  798M   0% /run/user/0

# lsblk -o NAME,FSTYPE,MOUNTPOINT,LABEL,PARTTYPE,PARTLABEL
NAME    FSTYPE            MOUNTPOINT     LABEL                   PARTTYPE                             PARTLABEL
sda
├─sda1                                                           21686148-6449-6e6f-744e-656564454649 BIOS boot partition
├─sda2  ext2                                                     0fc63daf-8483-4772-8e79-3d69d8477de4 Linux filesystem
├─sda3  linux_raid_member                localhost.localdomain:0 a19d880f-05fc-4d3b-a006-743f0f84911e Linux RAID
│ └─md0 ext4              /
├─sda4  swap                                                     0657fd6d-a4ab-43c4-84e5-0933c84b4f4f Linux swap
├─sda5  linux_raid_member                localhost.localdomain:1 a19d880f-05fc-4d3b-a006-743f0f84911e Linux RAID
│ └─md1 ext4              /var/log
├─sda6  linux_raid_member                localhost.localdomain:2 a19d880f-05fc-4d3b-a006-743f0f84911e Linux RAID
│ └─md2 ext4              /backup
├─sda7  linux_raid_member                localhost.localdomain:3 a19d880f-05fc-4d3b-a006-743f0f84911e Linux RAID
│ └─md3 ext4              /var/lib/mysql
├─sda8  linux_raid_member                localhost.localdomain:4 a19d880f-05fc-4d3b-a006-743f0f84911e Linux RAID
│ └─md4 ext4              /home
└─sda9  linux_raid_member                localhost.localdomain:5 a19d880f-05fc-4d3b-a006-743f0f84911e Linux RAID
  └─md5 ext4              /var/samba
sdb
├─sdb1                                                           21686148-6449-6e6f-744e-656564454649 BIOS boot partition
├─sdb2  ext2                                                     0fc63daf-8483-4772-8e79-3d69d8477de4 Linux filesystem
├─sdb3  linux_raid_member                localhost.localdomain:0 a19d880f-05fc-4d3b-a006-743f0f84911e Linux RAID
│ └─md0 ext4              /
├─sdb4  swap                                                     0657fd6d-a4ab-43c4-84e5-0933c84b4f4f Linux swap
├─sdb5  linux_raid_member                localhost.localdomain:1 a19d880f-05fc-4d3b-a006-743f0f84911e Linux RAID
│ └─md1 ext4              /var/log
├─sdb6  linux_raid_member                localhost.localdomain:2 a19d880f-05fc-4d3b-a006-743f0f84911e Linux RAID
│ └─md2 ext4              /backup
├─sdb7  linux_raid_member                localhost.localdomain:3 a19d880f-05fc-4d3b-a006-743f0f84911e Linux RAID
│ └─md3 ext4              /var/lib/mysql
├─sdb8  linux_raid_member                localhost.localdomain:4 a19d880f-05fc-4d3b-a006-743f0f84911e Linux RAID
│ └─md4 ext4              /home
└─sdb9  linux_raid_member                localhost.localdomain:5 a19d880f-05fc-4d3b-a006-743f0f84911e Linux RAID
  └─md5 ext4              /var/samba
sdc
├─sdc1                                                           21686148-6449-6e6f-744e-656564454649 BIOS boot partition
├─sdc2  ext2              /boot                                  0fc63daf-8483-4772-8e79-3d69d8477de4 Linux filesystem
├─sdc3  linux_raid_member                localhost.localdomain:0 a19d880f-05fc-4d3b-a006-743f0f84911e Linux RAID
│ └─md0 ext4              /
├─sdc4  swap                                                     0657fd6d-a4ab-43c4-84e5-0933c84b4f4f Linux swap
├─sdc5  linux_raid_member                localhost.localdomain:1 a19d880f-05fc-4d3b-a006-743f0f84911e Linux RAID
│ └─md1 ext4              /var/log
├─sdc6  linux_raid_member                localhost.localdomain:2 a19d880f-05fc-4d3b-a006-743f0f84911e Linux RAID
│ └─md2 ext4              /backup
├─sdc7  linux_raid_member                localhost.localdomain:3 a19d880f-05fc-4d3b-a006-743f0f84911e Linux RAID
│ └─md3 ext4              /var/lib/mysql
├─sdc8  linux_raid_member                localhost.localdomain:4 a19d880f-05fc-4d3b-a006-743f0f84911e Linux RAID
│ └─md4 ext4              /home
└─sdc9  linux_raid_member                localhost.localdomain:5 a19d880f-05fc-4d3b-a006-743f0f84911e Linux RAID
  └─md5 ext4              /var/samba/pre>

As I understand I have to clone the following 9 partitions:
> /dev/sdc1 — «BIOS boot partition» for Legacy Boot
> /dev/sdc2 — /boot
> /dev/sdc — swap partition
> /dev/md0 — /
> /dev/md1 — /var/log
> /dev/md2 — /backup
> /dev/md3 — /var/lib/mysql
> /dev/md4 — /home
> /dev/md5 — /var/samba<

So the main question is: does Acronis offer a suitable product (products) for this case?
 
Could you please advise on the correct way to proceed with minimum manual intervation?
 
Thank you very much!

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 03/31/2025 - 21:10

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Welcome to the forum.
Clone wouldn't be the best option to execute that.
You for example use Acronis Cyber Protect 16, execute a full backup of the machine and execute the recovery with a bootable media in the host and the new VM would be there or simply recover the machine directly in the hypervisor:
Please refer to the following user-guides: 
https://www.acronis.com/en-us/support/documentation/AcronisCyberProtect…
https://www.acronis.com/en-us/support/documentation/AcronisCyberProtect…
Best regards.

      
                
                
                    
                                                    Tue, 04/01/2025 - 10:10
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    The Immortal
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Jose,
Thank you for your response!
Could you please tell me if there is a way to directly transfer data from the source Linux machine to the VM using Acronis Cyber Protect 16 without creating an intermediate backup? I don’t have enough free space to first back up the source Linux system and then restore it. I need to perform the transfer in a single step.
Thanks!

      
                
                
                    
                                                    Tue, 04/01/2025 - 13:29
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            The Immortal wrote:

Hello Jose,
Thank you for your response!
Could you please tell me if there is a way to directly transfer data from the source Linux machine to the VM using Acronis Cyber Protect 16 without creating an intermediate backup? I don’t have enough free space to first back up the source Linux system and then restore it. I need to perform the transfer in a single step.
Thanks!


Hello!
This is a bit more complex, as a backup ensures that your data is protected and can be properly deployed afterward.
In this case, a replica might be a better solution. Please check the following link for more details:
? Replication of Virtual Machines
Best regards.

      
                
                
                    
                                                    Tue, 04/01/2025 - 13:40
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    The Immortal
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            But does the replica preserve the exact disk structure on the target machine as on the source? I mean, in my case, there are three disks of the same size as the source.
This doesn’t work for me either. :(

      
                
                
                    
                                                    Tue, 04/01/2025 - 14:13
