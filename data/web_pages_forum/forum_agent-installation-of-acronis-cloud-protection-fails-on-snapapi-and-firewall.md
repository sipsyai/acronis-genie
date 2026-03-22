# Agent installation of Acronis Cloud protection fails on Snapapi and firewall

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/agent-installation-acronis-cloud-protection-fails-snapapi-and-firewall

## Original Post
**Author:** Unknown

Agent installation of Acronis Cloud protection fails on Snapapi and firewall

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    dxxSDZX
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                
                    
                        
            So my company needs a couple of VPS's to backup in the cloud but the installation of the Acronis agent presents an error on the first VM I try to install it on. Something that should take 15 min, now keeps me busy for half a day already:
Automatic installation of the kernel module has failed.

After that, the installation continues normally and registration succeeds (the VPS is visible in the cloud console). At the end of the installation the following errors are presented:

So two problems:
- Firewall error.
- SnapAPI error.
I tried to figure out what ports to which ip addresses Acronis needs (no idea which datacenter I'm on so don't present me the KB with ports) because for some IDIOTIC reason neither the agent nor my cloud console can tell me this. Fine, I install Acronis's Connection Verification Tool but ofcourse this thing doesn't work (WHAT A FUCKING SURPRISE):

root@vm:/home/user/connectiontool# ./linux_port_checker_en-US_x86_64 -u=user@company -p=password
Error 0x640002: The credentials are incorrect. Make sure you use backup account credentials, not administrator ones.
line info: 0xe71b9a1528b1baa8
$module: msp_port_checker_lxa64_215

Censored the user/pass above but the credentials are correct and are the same I'm using to log in to the portal. Also, no special characters in the password. Well maybe the mandatory 2FA is preventing the tool to work? Fine, I'll create a new account and mark it as service account. Easy peasy...nopes I have to do the activation, and mandatory 2FA registration procedure for the new account because I can't mark it as service account rightaway. Fine, I'll do that. Nopes still not working. Let's look at the KB: https://kb.acronis.com/content/47678
where <login>, depending on the product you use, is:
- your Backup Account belonging to Acronis Cyber Protect Cloud's Customer(!) group (not Partner admin account).
- your Backup Account email address for Acronis Cyber Backup
[..]

What the fuck does this even mean?!!!! I only have one account, the adminstrator account I'm using the login to the portal.
Well this firewall shit isn't going nowhere. Let's move on to Snapapi problem first, how do I fix this? The VM seems to meet all the requirements (see console output below) as per this KB: https://kb.acronis.com/content/55052 but https://www.acronis.com/en-us/support/documentation/AcronisCyberProtect… seems to indicate the kernel is not supported. Is this correct? Do I need to create the SnapApi manually as per this KB? https://kb.acronis.com/content/1556
If that's the case than apparently I need to follow the instructions in: /usr/lib/Acronis/BackupAndRecovery/HOWTO.INSTALL - for Acronis Backup (Acronis Backup & Recovery)?
To which I'll say....screw this I'm using another provider and another product because considering this is Linux, I'm a 1000% sure that AT LEAST one step in the HOWTO.INSTALL doc doesn't work and/or doesn't match my distro, kernel, depency, installed software....you name it, besides the obvious Linux manual ambiguity and requires me to Google for hours on how to make one step work only to be presented with other crap that doesn't work in the next step.
(I'm sorry for being pisted off)

cat /proc/version
Linux version 5.10.0-10-cloud-amd64 (debian-kernel@lists.debian (gcc-10 (Debian 10.2.1-6) 10.2.1 20210110, GNU ld (GNU Binutils for Debian) 2.35.2) #1 SMP Debian 5.10.84-1 (2021-12-08)
#make -v
GNU Make 4.3
Built for x86_64-pc-linux-gnu
Copyright (C) 1988-2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
#gcc --version
gcc (Debian 10.2.1-6) 10.2.1 20210110
Copyright (C) 2020 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#dpkg --get-selections | grep linux-headers
linux-headers-5.10.0-10-cloud-amd64             install
linux-headers-5.10.0-10-common                  install
#dpkg --get-selections | grep linux-image
linux-image-5.10.0-10-cloud-amd64               install
linux-image-5.10.0-11-cloud-amd64               install
linux-image-cloud-amd64                         install
#perl --version
This is perl 5, version 32, subversion 1 (v5.32.1) built for x86_64-linux-gnu-thread-multi
(with 47 registered patches, see perl -V for more detail)
Copyright 1987-2021, Larry Wall
Perl may be copied only under the terms of either the Artistic License or the
GNU General Public License, which may be found in the Perl 5 source kit.
Complete documentation for Perl, including FAQ lists, should be found on
this system using "man perl" or "perldoc perl".  If you have access to the
Internet, point your browser at , the Perl Home Page.
#sudo apt-get install -y libelf-dev  
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
libelf-dev is already the newest version (0.183-1).
0 upgraded, 0 newly installed, 0 to remove and 1 not upgraded.


      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 02/16/2022 - 16:18

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Georgi Dimitrov
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 10
                
            
            
                
                    Comments: 49
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi, dxxSDZX . 
Please open a case with our support team and we will happily assist.

      
                
                
                    
                                                    Mon, 02/21/2022 - 10:38
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Georgi Dimitrov | Support Engineer

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daria Sorokina
                            

                            
                    
                        Acronis Support
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 487
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dear dxxSDZX,
Please let us know was your problem that you presented here resolved if yes, what helped you?

      
                
                
                    
                                                    Tue, 09/27/2022 - 22:29
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards, Daria Sorokina | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
