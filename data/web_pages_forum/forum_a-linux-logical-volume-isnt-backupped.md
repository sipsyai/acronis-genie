# A Linux logical volume isn't backupped

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/linux-logical-volume-isnt-backupped

## Original Post
**Author:** Unknown

A Linux logical volume isn't backupped

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Vittorio Faraoni
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello, I have a weird problem with a server that previously hadn't this strange behavior.
I recently reinstalled agents after a datacenter migration and what is happening is that the backup policy just backups the boot partition and the swap logical volume as well, but it completely skips the main logical volume, where all the root file system is located.
I already tried to completely uninstall the backup agent, including the removal of every snapapi26 module versions and I reinstalled agent from scratch, but nothing changed.
Here are the relevant infos:
# uname -r
3.13.0-88-generic
# lsmod|grep snap
snapapi26              45335  3
root@cdlan:~# modinfo snapapi26
filename:       /lib/modules/3.13.0-88-generic/updates/dkms/snapapi26.ko
supported:      external
version:        0.7.88
license:        Proprietary
description:    Acronis Snapshot kernel API module
author:         Acronis
srcversion:     1395824A5987E7C5E5E4719
depends:        
vermagic:       3.13.0-88-generic SMP mod_unload modversions
# mount
/dev/mapper/ubuntu--vg-root on / type ext4 (rw,errors=remount-ro)
proc on /proc type proc (rw,noexec,nosuid,nodev)
sysfs on /sys type sysfs (rw,noexec,nosuid,nodev)
none on /sys/fs/cgroup type tmpfs (rw)
none on /sys/fs/fuse/connections type fusectl (rw)
none on /sys/kernel/debug type debugfs (rw)
none on /sys/kernel/security type securityfs (rw)
udev on /dev type devtmpfs (rw,mode=0755)
devpts on /dev/pts type devpts (rw,noexec,nosuid,gid=5,mode=0620)
tmpfs on /run type tmpfs (rw,noexec,nosuid,size=10%,mode=0755)
none on /run/lock type tmpfs (rw,noexec,nosuid,nodev,size=5242880)
none on /run/shm type tmpfs (rw,nosuid,nodev)
none on /run/user type tmpfs (rw,noexec,nosuid,nodev,size=104857600,mode=0755)
none on /sys/fs/pstore type pstore (rw)
/dev/sda1 on /boot type ext2 (rw)
systemd on /sys/fs/cgroup/systemd type cgroup (rw,noexec,nosuid,nodev,none,name=systemd)
 
# swapon -s
Filename                Type        Size    Used    Priority
/dev/mapper/ubuntu--vg-swap_1           partition    1044476    89124    -1
 
In the attached image you may see that the backup policy completely ignores the /dev/mapper/ubuntu--vg-root logical volume.
 
Regards.
 

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      cdshr.png

                      11.85 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Thu, 06/23/2016 - 16:24

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Vittorio,
Thank you for your posting! I would suggest to raise a support ticket, so that we can investigate the issue.
Thank you,

      
                
                
                    
                                                    Mon, 06/27/2016 - 14:51
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Vittorio Faraoni
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Ekaterina.
Thank you for replying.
I have some troubles in rasing a support ticket; when I choose "Technical issues/Question" and "I am using Service Provider solutions", the support site answers "There are no Service provider products associated with your account". However there's no way for me to register the product, since there's no serial number associated with the Acronis Backup Cloud service.
Could you kindly tell me if there's another way to open a support ticket?
Kind regards.

      
                
                
                    
                                                    Mon, 06/27/2016 - 15:11
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Vittorio,
I've sent you PM ragarding the issue.
Thank you,

      
                
                
                    
                                                    Mon, 06/27/2016 - 16:24
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
