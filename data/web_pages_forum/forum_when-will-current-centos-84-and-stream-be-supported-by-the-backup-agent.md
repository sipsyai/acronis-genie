# When will current CentOS 8.4 and Stream be supported by the Backup Agent?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/when-will-current-centos-84-and-stream-be-supported-backup-agent

## Original Post
**Author:** Unknown

When will current CentOS 8.4 and Stream be supported by the Backup Agent?

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Manuel Haschke
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            The official documentation says that CentOS is supported to version 8.3 but not above and CentOS Stream.
As a Service Provider we naturally always try to keep our own and customers servers (most of them are VMs) up to date. For about half a year or so, there is no support for current CentOS-Versions with a current Kernel.
Problem seems to be the snapapi-module that somehow does not support current Kernel 4.18 and above. Mentioned e.g. here: https://kb.acronis.com/de/node/68870
Without the snapapi-module we are not able to backup and recover the full machine but only the most important files. Really annoying in case of a recovery since the whole OS setup and installation of services has to be done before you can recover the backed up files.
Other solutions like storapi on VMware/ESXi are no alternative because most customers are not willing to pay for it.
If this situation continues as is, from our perspective, Acronis can not be used for maintained CentOS VMs.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 07/07/2021 - 10:35

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Maria Belinskaya
                            

                            
                    
                        Forum Support specialist 
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2012
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Manuel,
Welcome to Acronis forums!
This kernel compatibility issue is described in this KB article: https://kb.acronis.com/de/node/68870
However, we have a new version of SnapAPI that provides support for all 4.18.-series and 5.8-series Linux kernels as well (NOT 5.9!!).
This new SnapAPI will be included in C21.07 agent release. Please download it at:
https://dl.acronis.com/u/kb/67243/snapapi26_modules-0.7.140-1.noarch.rpm
Then please follow this KB article with the detailed instructions on how to update SnapAPI module with the CentOS 8.4 + CentOS Stream 8 support: https://kb.acronis.com/content/41283
 

      
                
                
                    
                                                    Thu, 07/08/2021 - 11:13
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Maria Belinskaya | Acronis Forum Support Specialist

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support/

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Manuel Haschke
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you for the fast reply, Maria. 
I just tried to compile the new version from the .rpm as instructions told in https://kb.acronis.com/content/41283
First, I updated a CentOS8 Stream to the newest Version. Which seems to be 8.5 already...
[root@srv01-dc ~]# cat /proc/version 
Linux version 4.18.0-315.el8.x86_64 (mockbuild@kbuilder.bsys.centos.org) (gcc version 8.5.0 20210514 (Red Hat 8.5.0-2) (GCC)) #1 SMP Mon Jun 28 19:09:44 UTC 2021 
The steps from the instructions complete successfully until you start the building process.
[root@srv01-dc ~]# dkms ldtarball /usr/lib/Acronis/kernel_modules/snapapi26-0.7.140-all.tar.gz 
...
Loading /var/lib/dkms/snapapi26/0.7.140/4.18.0-147.13.2.el8_1.x86_64/x86_64...
Loading /var/lib/dkms/snapapi26/0.7.140/4.18.0-147.el8.x86_64/x86_64...
Loading /var/lib/dkms/snapapi26/0.7.140/4.18.0-193.6.3.el8_2.x86_64/x86_64...
Loading /var/lib/dkms/snapapi26/0.7.140/4.18.0-305.3.1.el8.x86_64/x86_64...
Loading /var/lib/dkms/snapapi26/0.7.140/4.18.0-80.el8.x86_64/x86_64...

DKMS: ldtarball completed.

Creating symlink /var/lib/dkms/snapapi26/0.7.140/source ->
                 /usr/src/snapapi26-0.7.140

DKMS: add completed.
[root@srv01-dc ~]# dkms build -m snapapi26 -v 0.7.140

Kernel preparation unnecessary for this kernel.  Skipping...

Building module:
cleaning build area...
make -j8 KERNELRELEASE=4.18.0-315.el8.x86_64 -C /lib/modules/4.18.0-315.el8.x86_64/build M=/var/lib/dkms/snapapi26/0.7.140/build...(bad exit status: 2)
Error! Bad return status for module build on kernel: 4.18.0-315.el8.x86_64 (x86_64)
Consult /var/lib/dkms/snapapi26/0.7.140/build/make.log for more information. 
Following line does probably show the most current version supportet by snapapi:
Loading /var/lib/dkms/snapapi26/0.7.140/4.18.0-305.3.1.el8.x86_64/x86_64...

 
I also tried the same steps on a VM with an older Kernel:
[root@srv01-dc ~]# cat /proc/version 
Linux version 4.18.0-277.el8.x86_64 (mockbuild@kbuilder.bsys.centos.org) (gcc version 8.4.1 20200928 (Red Hat 8.4.1-1) (GCC)) #1 SMP Wed Feb 3 20:35:19 UTC 2021The last command completes with warnings:
[root@srv01-dc ~]#  dkms install -m snapapi26 -v 0.7.140
...
depmod: WARNING: /lib/modules/4.18.0-269.el8.x86_64/weak-updates/snapapi26.ko.xz needs unknown symbol blk_mq_make_request
depmod: WARNING: /lib/modules/4.18.0-277.el8.x86_64/extra/snapapi26.ko.xz needs unknown symbol blk_mq_make_request
...Jobs with a full machine backup fail with the message that the snapapi-module is not installed for this kernel-version.

      
                
                
                    
                                                    Fri, 07/09/2021 - 07:19
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Georgi Dimitrov
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 10
                
            
            
                
                    Comments: 49
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi, Manuel. 
Please open a case with our support team so that we may investigate and provide you with a solution.

      
                
                
                    
                                                    Tue, 07/20/2021 - 13:30
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Georgi Dimitrov | Support Engineer

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
