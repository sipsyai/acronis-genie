# CloudLinux 9 Support ETA?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/cloudlinux-9-support-eta

## Original Post
**Author:** Unknown

CloudLinux 9 Support ETA?

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                
                    
                        
            Hello,
With CloudLinux 9 + cPanel v118 ready for production as per https://blog.cloudlinux.com/cloudlinux-9-and-cpanel-118-integration-now… do you have any ETA for Cloudlinux 9 support for the Acronis cPanel Plugin?
Currently it fails:
Detecting OS type and version ...
ERROR: Only CentOS/CloudLinux 6, 7 and 8 are supported at the moment
Thanks in advance, George

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 03/14/2024 - 09:30

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Thank you for contacting us.
There is a feature request (CI-26620) for which I have voted on your behalf and added a comment.
As far as I can see, there is no ETA for this task, at least for now.
So far, the workaround is installing the Linux agent directly inside each machine (it should work). I advise you to contact the team if you have any questions about this process: https://kb.acronis.com/content/8153
Thanks in advance!
 

      
                
                
                    
                                                    Thu, 03/14/2024 - 11:42
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you Jose. 
I thought I'd give it a try on a test machine, and it appears that after overriding the OS check, the plugin installs fine and the agent as well.
Here's what I did:
cd ~
wget https://download.acronis.com/ci/cpanel/stable/install_acronis_cpanel.sh
sed -i 's/"${OS_VERSION}" -gt 8/"${OS_VERSION}" -gt 9/g' install_acronis_cpanel.sh
sh install_acronis_cpanel.sh
Obviously I understand that this is unsupported by Acronis, but at least backups appear to be working fine.
dkms also built fine without any manual intervention:
[root@demo-cl9 ~]# uname -r
5.14.0-362.18.1.el9_3.x86_64
[root@demo-cl9 ~]# dkms status | grep "5.14.0-362.18.1.el9_3"
file_protector/1.1-1522, 5.14.0-362.18.1.el9_3.x86_64, x86_64: installed
snapapi26/0.8.25, 5.14.0-362.18.1.el9_3.x86_64, x86_64: installed
One of the next few days I will also try restores of files, databases etc to see how things behave.

      
                
                
                    
                                                    Fri, 03/15/2024 - 11:00
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            George_Fusioned wrote:

Thank you Jose. 
I thought I'd give it a try on a test machine, and it appears that after overriding the OS check, the plugin installs fine and the agent as well.
Here's what I did:
cd ~
wget https://download.acronis.com/ci/cpanel/stable/install_acronis_cpanel.sh
sed -i 's/"${OS_VERSION}" -gt 8/"${OS_VERSION}" -gt 9/g' install_acronis_cpanel.sh
sh install_acronis_cpanel.sh
Obviously I understand that this is unsupported by Acronis, but at least backups appear to be working fine.
dkms also built fine without any manual intervention:
[root@demo-cl9 ~]# uname -r
5.14.0-362.18.1.el9_3.x86_64
[root@demo-cl9 ~]# dkms status | grep "5.14.0-362.18.1.el9_3"
file_protector/1.1-1522, 5.14.0-362.18.1.el9_3.x86_64, x86_64: installed
snapapi26/0.8.25, 5.14.0-362.18.1.el9_3.x86_64, x86_64: installed
One of the next few days I will also try restores of files, databases etc to see how things behave.


Hello George,
Thank you for sharing the information. This may be useful for other partners.
Feel free to update the thread if you want to share any other information.
Best regards.

      
                
                
                    
                                                    Fri, 03/15/2024 - 15:17
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Looks like the driver is not ready after all. In my dmesg I see thousands of these:
[167232.253770] session_init(mms,487949): OK. kdev=fb:1, len=2048 sect=512 s=00000000ce1747e9 pgrp=(487893).
[167232.256131] snumbd_open_blk(systemd-udevd,673199): Disable access (689,487893,487893)...
[167232.294447] snumbdctl_release(mms,487949): OK s=00000000ce1747e9
[167232.342018] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[167232.342024] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[167232.342026] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[167232.342028] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[167232.342031]  snumbd1d: unable to read partition table
[167280.460700] snumbdctl_open(TrueImageMount,673400): OK s=000000002bd449cc
[167280.461021] snumbdctl_release(TrueImageMount,673400): OK s=000000002bd449cc
[167399.363455] snumbdctl_open(TrueImageMount,673757): OK s=00000000ce1747e9
[167399.364458] snumbdctl_release(TrueImageMount,673757): OK s=00000000ce1747e9
[167580.901794] snumbdctl_open(TrueImageMount,675027): OK s=00000000363ad3ec
[167580.902130] snumbdctl_release(TrueImageMount,675027): OK s=00000000363ad3ec
[167700.127694] snumbdctl_open(TrueImageMount,675415): OK s=00000000a3ac3ca4
[167700.128016] snumbdctl_release(TrueImageMount,675415): OK s=00000000a3ac3ca4
[167881.359122] snumbdctl_open(TrueImageMount,676407): OK s=000000004a97f9d4
[167881.359543] snumbdctl_release(TrueImageMount,676407): OK s=000000004a97f9d4
[168000.853542] snumbdctl_open(TrueImageMount,676707): OK s=0000000091a24d4a
[168000.853964] snumbdctl_release(TrueImageMount,676707): OK s=0000000091a24d4a
[168132.458243] snumbdctl_open(mms,487949): OK s=0000000032c72f00
[168132.458737] snumbd_make_request(mms,487949): Session is in unusable state=0, bio=00000000fdaa92a4 dev=fb00001.
[168132.458742] buffer_io_error: 2 callbacks suppressed
[168132.458744] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[168132.458750] snumbd_make_request(mms,487949): Session is in unusable state=0, bio=00000000fdaa92a4 dev=fb00001.
[168132.458752] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[168132.458755] snumbd_make_request(mms,487949): Session is in unusable state=0, bio=00000000fdaa92a4 dev=fb00001.
[168132.458757] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[168132.458759] snumbd_make_request(mms,487949): Session is in unusable state=0, bio=00000000fdaa92a4 dev=fb00001.
[168132.458761] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[168132.458764] snumbd_make_request(mms,487949): Session is in unusable state=0, bio=00000000fdaa92a4 dev=fb00001.
[168132.458765] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[168132.458768] snumbd_make_request(mms,487949): Session is in unusable state=0, bio=00000000fdaa92a4 dev=fb00001.
[168132.458770] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[168132.458771]  snumbd1d: unable to read partition table
So for now I have removed the dkms modules and stopped the acronis_mms & aakore services. I guess I'll wait for the official release - hope it's soon! Thanks

      
                
                
                    
                                                    Fri, 03/15/2024 - 21:11
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Karl Austin
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 7
                
            
            
                
                    Comments: 15
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Another vote for this, it is currently holding up our migration away from CentOS 7, and the provisioning of some new systems.  If there isn't a resolution soon then we may have to think about moving away from Acronis completely, as this keeps happening.

      
                
                
                    
                                                    Fri, 03/22/2024 - 11:08
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Karl Austin wrote:

Another vote for this, it is currently holding up our migration away from CentOS 7, and the provisioning of some new systems.  If there isn't a resolution soon then we may have to think about moving away from Acronis completely, as this keeps happening.


Hello!
I have added the vote for you.
Best regards. 

      
                
                
                    
                                                    Fri, 03/22/2024 - 13:05
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Tino Andrijic
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello everyone, I have the same problem with CloudLinux 9.3 and cPanel 118.0.4 so another vote!
Acronis cPanel plugin cannot be installed:
Detecting OS type and version ...
ERROR: Only CentOS/CloudLinux 6, 7 and 8 are supported at the moment

If I install it as George_Fusioned wrote, everything seems fine but dmesg shows errors:
[45418.819371] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[45418.819375] snumbd_make_request(mms,74679): Session is in unusable state=0, bio=000000003823d637 dev=fc00001.
[45418.819377] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[45418.819380] snumbd_make_request(mms,74679): Session is in unusable state=0, bio=000000003823d637 dev=fc00001.
[45418.819381] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[45418.819383] snumbd_make_request(mms,74679): Session is in unusable state=0, bio=000000003823d637 dev=fc00001.
[45418.819384] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[45418.819387] snumbd_make_request(mms,74679): Session is in unusable state=0, bio=000000003823d637 dev=fc00001.
[45418.819388] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[45418.819390] snumbd_make_request(mms,74679): Session is in unusable state=0, bio=000000003823d637 dev=fc00001.
[45418.819391] Buffer I/O error on dev snumbd1d, logical block 0, async page read

This is also holding us back on migration and we need an urgent solution.
Best regards,
Tino Andrijic

      
                
                
                    
                                                    Tue, 04/02/2024 - 22:04
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Tino Andrijic wrote:

Hello everyone, I have the same problem with CloudLinux 9.3 and cPanel 118.0.4 so another vote!
Acronis cPanel plugin cannot be installed:
Detecting OS type and version ...
ERROR: Only CentOS/CloudLinux 6, 7 and 8 are supported at the moment

If I install it as George_Fusioned wrote, everything seems fine but dmesg shows errors:
[45418.819371] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[45418.819375] snumbd_make_request(mms,74679): Session is in unusable state=0, bio=000000003823d637 dev=fc00001.
[45418.819377] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[45418.819380] snumbd_make_request(mms,74679): Session is in unusable state=0, bio=000000003823d637 dev=fc00001.
[45418.819381] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[45418.819383] snumbd_make_request(mms,74679): Session is in unusable state=0, bio=000000003823d637 dev=fc00001.
[45418.819384] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[45418.819387] snumbd_make_request(mms,74679): Session is in unusable state=0, bio=000000003823d637 dev=fc00001.
[45418.819388] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[45418.819390] snumbd_make_request(mms,74679): Session is in unusable state=0, bio=000000003823d637 dev=fc00001.
[45418.819391] Buffer I/O error on dev snumbd1d, logical block 0, async page read

This is also holding us back on migration and we need an urgent solution.
Best regards,
Tino Andrijic


Hello Tino,
I have added your comments to the task and voted for you.
If you would like to know news about this task, feel free to contact our support at https://kb.acronis.com/content/8153.
Best regards.

      
                
                
                    
                                                    Wed, 04/03/2024 - 12:19
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Karl Austin
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 7
                
            
            
                
                    Comments: 15
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            This is where Acronis really falls down IMHO and just doesn't understand certain areas of the Service Provider market.  We really shouldn't be having to individually chase and bother your support for updates on issues such as these.
Right now you've got an issue where your product claims to support cPanel, but doesn't support an OS that is officially supported by cPanel.  CloudLinux 9.3 isn't a sudden surprise release, it logically follows from 9, 9.1 and 9.2 so it isn't like there's only been a couple of weeks to get on top of this.

      
                
                
                    
                                                    Wed, 04/03/2024 - 13:11
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Karl Austin wrote:

This is where Acronis really falls down IMHO and just doesn't understand certain areas of the Service Provider market.  We really shouldn't be having to individually chase and bother your support for updates on issues such as these.
Right now you've got an issue where your product claims to support cPanel, but doesn't support an OS that is officially supported by cPanel.  CloudLinux 9.3 isn't a sudden surprise release, it logically follows from 9, 9.1 and 9.2 so it isn't like there's only been a couple of weeks to get on top of this.


Hello Karl,
Thank you for your comments. I've taken note of them, and the thread has been forwarded to the team for further review. From what I can gather, the team is actively working on a solution, and it should be available as soon as possible.
Additionally, I recommend reaching out to your service provider to raise a ticket. This will ensure that the issue is properly registered and tracked.
Best regards.

      
                
                
                    
                                                    Wed, 04/03/2024 - 13:17
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    David Petruzzella
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I am experiencing the same thing with Alma Linux 9, but I found documentation on Acronis website saying it is supported.
 
Here is the information I found about it being supported. 
 
https://www.acronis.com/en-us/support/documentation/CyberProtectionServ…
I did check my kernel version and it is 5.14 
I will try to bypass the OS detection a little later, unless I see any other suggestions.

      
                
                
                    
                                                    Mon, 04/29/2024 - 17:17
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    David Petruzzella
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            George_Fusioned wrote:

Looks like the driver is not ready after all. In my dmesg I see thousands of these:
[167232.253770] session_init(mms,487949): OK. kdev=fb:1, len=2048 sect=512 s=00000000ce1747e9 pgrp=(487893).
[167232.256131] snumbd_open_blk(systemd-udevd,673199): Disable access (689,487893,487893)...
[167232.294447] snumbdctl_release(mms,487949): OK s=00000000ce1747e9
[167232.342018] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[167232.342024] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[167232.342026] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[167232.342028] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[167232.342031]  snumbd1d: unable to read partition table
[167280.460700] snumbdctl_open(TrueImageMount,673400): OK s=000000002bd449cc
[167280.461021] snumbdctl_release(TrueImageMount,673400): OK s=000000002bd449cc
[167399.363455] snumbdctl_open(TrueImageMount,673757): OK s=00000000ce1747e9
[167399.364458] snumbdctl_release(TrueImageMount,673757): OK s=00000000ce1747e9
[167580.901794] snumbdctl_open(TrueImageMount,675027): OK s=00000000363ad3ec
[167580.902130] snumbdctl_release(TrueImageMount,675027): OK s=00000000363ad3ec
[167700.127694] snumbdctl_open(TrueImageMount,675415): OK s=00000000a3ac3ca4
[167700.128016] snumbdctl_release(TrueImageMount,675415): OK s=00000000a3ac3ca4
[167881.359122] snumbdctl_open(TrueImageMount,676407): OK s=000000004a97f9d4
[167881.359543] snumbdctl_release(TrueImageMount,676407): OK s=000000004a97f9d4
[168000.853542] snumbdctl_open(TrueImageMount,676707): OK s=0000000091a24d4a
[168000.853964] snumbdctl_release(TrueImageMount,676707): OK s=0000000091a24d4a
[168132.458243] snumbdctl_open(mms,487949): OK s=0000000032c72f00
[168132.458737] snumbd_make_request(mms,487949): Session is in unusable state=0, bio=00000000fdaa92a4 dev=fb00001.
[168132.458742] buffer_io_error: 2 callbacks suppressed
[168132.458744] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[168132.458750] snumbd_make_request(mms,487949): Session is in unusable state=0, bio=00000000fdaa92a4 dev=fb00001.
[168132.458752] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[168132.458755] snumbd_make_request(mms,487949): Session is in unusable state=0, bio=00000000fdaa92a4 dev=fb00001.
[168132.458757] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[168132.458759] snumbd_make_request(mms,487949): Session is in unusable state=0, bio=00000000fdaa92a4 dev=fb00001.
[168132.458761] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[168132.458764] snumbd_make_request(mms,487949): Session is in unusable state=0, bio=00000000fdaa92a4 dev=fb00001.
[168132.458765] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[168132.458768] snumbd_make_request(mms,487949): Session is in unusable state=0, bio=00000000fdaa92a4 dev=fb00001.
[168132.458770] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[168132.458771]  snumbd1d: unable to read partition table
So for now I have removed the dkms modules and stopped the acronis_mms & aakore services. I guess I'll wait for the official release - hope it's soon! Thanks


I am seeing those errors as well and that was even before installing the Acronis cpanel plugin, my server already had the agent installed as part of my plan from my provider. 

      
                
                
                    
                                                    Tue, 04/30/2024 - 03:09
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    David Petruzzella
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            George_Fusioned wrote:

Looks like the driver is not ready after all. In my dmesg I see thousands of these:
[167232.253770] session_init(mms,487949): OK. kdev=fb:1, len=2048 sect=512 s=00000000ce1747e9 pgrp=(487893).
[167232.256131] snumbd_open_blk(systemd-udevd,673199): Disable access (689,487893,487893)...
[167232.294447] snumbdctl_release(mms,487949): OK s=00000000ce1747e9
[167232.342018] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[167232.342024] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[167232.342026] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[167232.342028] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[167232.342031]  snumbd1d: unable to read partition table
[167280.460700] snumbdctl_open(TrueImageMount,673400): OK s=000000002bd449cc
[167280.461021] snumbdctl_release(TrueImageMount,673400): OK s=000000002bd449cc
[167399.363455] snumbdctl_open(TrueImageMount,673757): OK s=00000000ce1747e9
[167399.364458] snumbdctl_release(TrueImageMount,673757): OK s=00000000ce1747e9
[167580.901794] snumbdctl_open(TrueImageMount,675027): OK s=00000000363ad3ec
[167580.902130] snumbdctl_release(TrueImageMount,675027): OK s=00000000363ad3ec
[167700.127694] snumbdctl_open(TrueImageMount,675415): OK s=00000000a3ac3ca4
[167700.128016] snumbdctl_release(TrueImageMount,675415): OK s=00000000a3ac3ca4
[167881.359122] snumbdctl_open(TrueImageMount,676407): OK s=000000004a97f9d4
[167881.359543] snumbdctl_release(TrueImageMount,676407): OK s=000000004a97f9d4
[168000.853542] snumbdctl_open(TrueImageMount,676707): OK s=0000000091a24d4a
[168000.853964] snumbdctl_release(TrueImageMount,676707): OK s=0000000091a24d4a
[168132.458243] snumbdctl_open(mms,487949): OK s=0000000032c72f00
[168132.458737] snumbd_make_request(mms,487949): Session is in unusable state=0, bio=00000000fdaa92a4 dev=fb00001.
[168132.458742] buffer_io_error: 2 callbacks suppressed
[168132.458744] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[168132.458750] snumbd_make_request(mms,487949): Session is in unusable state=0, bio=00000000fdaa92a4 dev=fb00001.
[168132.458752] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[168132.458755] snumbd_make_request(mms,487949): Session is in unusable state=0, bio=00000000fdaa92a4 dev=fb00001.
[168132.458757] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[168132.458759] snumbd_make_request(mms,487949): Session is in unusable state=0, bio=00000000fdaa92a4 dev=fb00001.
[168132.458761] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[168132.458764] snumbd_make_request(mms,487949): Session is in unusable state=0, bio=00000000fdaa92a4 dev=fb00001.
[168132.458765] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[168132.458768] snumbd_make_request(mms,487949): Session is in unusable state=0, bio=00000000fdaa92a4 dev=fb00001.
[168132.458770] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[168132.458771]  snumbd1d: unable to read partition table
So for now I have removed the dkms modules and stopped the acronis_mms & aakore services. I guess I'll wait for the official release - hope it's soon! Thanks


So I installed the plugin using the method that George recommended by bypassing the OS detection, but when I was looking at dmesg, I was seeing the same I/O errors even before the plugin was installed. 

      
                
                
                    
                                                    Wed, 05/01/2024 - 12:04
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            David Petruzzella wrote:

George_Fusioned wrote:

Looks like the driver is not ready after all. In my dmesg I see thousands of these:
[167232.253770] session_init(mms,487949): OK. kdev=fb:1, len=2048 sect=512 s=00000000ce1747e9 pgrp=(487893).
[167232.256131] snumbd_open_blk(systemd-udevd,673199): Disable access (689,487893,487893)...
[167232.294447] snumbdctl_release(mms,487949): OK s=00000000ce1747e9
[167232.342018] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[167232.342024] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[167232.342026] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[167232.342028] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[167232.342031]  snumbd1d: unable to read partition table
[167280.460700] snumbdctl_open(TrueImageMount,673400): OK s=000000002bd449cc
[167280.461021] snumbdctl_release(TrueImageMount,673400): OK s=000000002bd449cc
[167399.363455] snumbdctl_open(TrueImageMount,673757): OK s=00000000ce1747e9
[167399.364458] snumbdctl_release(TrueImageMount,673757): OK s=00000000ce1747e9
[167580.901794] snumbdctl_open(TrueImageMount,675027): OK s=00000000363ad3ec
[167580.902130] snumbdctl_release(TrueImageMount,675027): OK s=00000000363ad3ec
[167700.127694] snumbdctl_open(TrueImageMount,675415): OK s=00000000a3ac3ca4
[167700.128016] snumbdctl_release(TrueImageMount,675415): OK s=00000000a3ac3ca4
[167881.359122] snumbdctl_open(TrueImageMount,676407): OK s=000000004a97f9d4
[167881.359543] snumbdctl_release(TrueImageMount,676407): OK s=000000004a97f9d4
[168000.853542] snumbdctl_open(TrueImageMount,676707): OK s=0000000091a24d4a
[168000.853964] snumbdctl_release(TrueImageMount,676707): OK s=0000000091a24d4a
[168132.458243] snumbdctl_open(mms,487949): OK s=0000000032c72f00
[168132.458737] snumbd_make_request(mms,487949): Session is in unusable state=0, bio=00000000fdaa92a4 dev=fb00001.
[168132.458742] buffer_io_error: 2 callbacks suppressed
[168132.458744] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[168132.458750] snumbd_make_request(mms,487949): Session is in unusable state=0, bio=00000000fdaa92a4 dev=fb00001.
[168132.458752] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[168132.458755] snumbd_make_request(mms,487949): Session is in unusable state=0, bio=00000000fdaa92a4 dev=fb00001.
[168132.458757] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[168132.458759] snumbd_make_request(mms,487949): Session is in unusable state=0, bio=00000000fdaa92a4 dev=fb00001.
[168132.458761] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[168132.458764] snumbd_make_request(mms,487949): Session is in unusable state=0, bio=00000000fdaa92a4 dev=fb00001.
[168132.458765] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[168132.458768] snumbd_make_request(mms,487949): Session is in unusable state=0, bio=00000000fdaa92a4 dev=fb00001.
[168132.458770] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[168132.458771]  snumbd1d: unable to read partition table
So for now I have removed the dkms modules and stopped the acronis_mms & aakore services. I guess I'll wait for the official release - hope it's soon! Thanks


So I installed the plugin using the method that George recommended by bypassing the OS detection, but when I was looking at dmesg, I was seeing the same I/O errors even before the plugin was installed. 


Hello David.
Our agent in fact supports that. But the plugin is considered an integration so doesn't work exactly on the same way.
The Cpanel integration just supports the following OS: https://www.acronis.com/en-us/support/documentation/WHMCPanel/
The integration has been tested on the following operating systems supported by cPanel & WHM:
AlmaLinux OS 8
CentOS 7
CloudLinux 6, 7 and 8
Red Hat Enterprise Linux 7
Ubuntu 20.04 LTS
Best regards.
 

      
                
                
                    
                                                    Tue, 05/07/2024 - 15:47
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Melis Freag
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 30
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            In the meantime, a workaround has been suggested which involves installing the Linux agent directly inside each machine, which should work. Additionally, a user has reported success by overriding the OS check during the plugin installation, allowing the plugin to install fine and the agent as well. This method is unsupported by Acronis, but it might be a temporary solution until official support is released.

      
                
                
                    
                                                    Tue, 05/07/2024 - 20:54
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    David Petruzzella
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Ok, but what about the I/O errors that I am seeing even before I installed the cpanel plugin?
 
Jose Pedro Magalhaes wrote:

David Petruzzella wrote:

George_Fusioned wrote:

Looks like the driver is not ready after all. In my dmesg I see thousands of these:
[167232.253770] session_init(mms,487949): OK. kdev=fb:1, len=2048 sect=512 s=00000000ce1747e9 pgrp=(487893).
[167232.256131] snumbd_open_blk(systemd-udevd,673199): Disable access (689,487893,487893)...
[167232.294447] snumbdctl_release(mms,487949): OK s=00000000ce1747e9
[167232.342018] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[167232.342024] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[167232.342026] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[167232.342028] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[167232.342031]  snumbd1d: unable to read partition table
[167280.460700] snumbdctl_open(TrueImageMount,673400): OK s=000000002bd449cc
[167280.461021] snumbdctl_release(TrueImageMount,673400): OK s=000000002bd449cc
[167399.363455] snumbdctl_open(TrueImageMount,673757): OK s=00000000ce1747e9
[167399.364458] snumbdctl_release(TrueImageMount,673757): OK s=00000000ce1747e9
[167580.901794] snumbdctl_open(TrueImageMount,675027): OK s=00000000363ad3ec
[167580.902130] snumbdctl_release(TrueImageMount,675027): OK s=00000000363ad3ec
[167700.127694] snumbdctl_open(TrueImageMount,675415): OK s=00000000a3ac3ca4
[167700.128016] snumbdctl_release(TrueImageMount,675415): OK s=00000000a3ac3ca4
[167881.359122] snumbdctl_open(TrueImageMount,676407): OK s=000000004a97f9d4
[167881.359543] snumbdctl_release(TrueImageMount,676407): OK s=000000004a97f9d4
[168000.853542] snumbdctl_open(TrueImageMount,676707): OK s=0000000091a24d4a
[168000.853964] snumbdctl_release(TrueImageMount,676707): OK s=0000000091a24d4a
[168132.458243] snumbdctl_open(mms,487949): OK s=0000000032c72f00
[168132.458737] snumbd_make_request(mms,487949): Session is in unusable state=0, bio=00000000fdaa92a4 dev=fb00001.
[168132.458742] buffer_io_error: 2 callbacks suppressed
[168132.458744] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[168132.458750] snumbd_make_request(mms,487949): Session is in unusable state=0, bio=00000000fdaa92a4 dev=fb00001.
[168132.458752] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[168132.458755] snumbd_make_request(mms,487949): Session is in unusable state=0, bio=00000000fdaa92a4 dev=fb00001.
[168132.458757] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[168132.458759] snumbd_make_request(mms,487949): Session is in unusable state=0, bio=00000000fdaa92a4 dev=fb00001.
[168132.458761] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[168132.458764] snumbd_make_request(mms,487949): Session is in unusable state=0, bio=00000000fdaa92a4 dev=fb00001.
[168132.458765] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[168132.458768] snumbd_make_request(mms,487949): Session is in unusable state=0, bio=00000000fdaa92a4 dev=fb00001.
[168132.458770] Buffer I/O error on dev snumbd1d, logical block 0, async page read
[168132.458771]  snumbd1d: unable to read partition table
So for now I have removed the dkms modules and stopped the acronis_mms & aakore services. I guess I'll wait for the official release - hope it's soon! Thanks


So I installed the plugin using the method that George recommended by bypassing the OS detection, but when I was looking at dmesg, I was seeing the same I/O errors even before the plugin was installed. 


Hello David.
Our agent in fact supports that. But the plugin is considered an integration so doesn't work exactly on the same way.
The Cpanel integration just supports the following OS: https://www.acronis.com/en-us/support/documentation/WHMCPanel/
The integration has been tested on the following operating systems supported by cPanel & WHM:
AlmaLinux OS 8
CentOS 7
CloudLinux 6, 7 and 8
Red Hat Enterprise Linux 7
Ubuntu 20.04 LTS
Best regards.
 



      
                
                
                    
                                                    Wed, 05/08/2024 - 05:00
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    David Petruzzella
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Melis Freag wrote:

In the meantime, a workaround has been suggested which involves installing the Linux agent directly inside each machine, which should work. Additionally, a user has reported success by overriding the OS check during the plugin installation, allowing the plugin to install fine and the agent as well. This method is unsupported by Acronis, but it might be a temporary solution until official support is released.


The solution did work and backups have been going fine, aside from the I/O errors. 

      
                
                
                    
                                                    Wed, 05/08/2024 - 05:01
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Emanuel Vicente
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 8
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
We realized plugin version 1.8.1 was released with support for Almalinux9/CloudLinux9 as shown on changelog: https://www.acronis.com/en-eu/support/updates/changes.html?p=41411
We tested the installation of the plugin and was just fine. Backups run well, and I can open them on Cyber Protect Cloud.
The problem is when we try to open a backup on Acronis plugin for cPanel, the following error occurs:

 
There are still any known issues with the plugin for EL9 based OS's?
Server info:
OS: Cloudlinux 9.4
Kernel version:  5.14.0-427.13.1.el9_4.x86_6
cPanel version: 120.0.5
Acronis Agent version: 24.4.37802
Acronis Plugin version: 1.8.1.757
 
Thank you

      
                
                
                    
                                                    Fri, 05/10/2024 - 17:51
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Emanuel Vicente wrote:

Hello,
We realized plugin version 1.8.1 was released with support for Almalinux9/CloudLinux9 as shown on changelog: https://www.acronis.com/en-eu/support/updates/changes.html?p=41411
We tested the installation of the plugin and was just fine. Backups run well, and I can open them on Cyber Protect Cloud.
The problem is when we try to open a backup on Acronis plugin for cPanel, the following error occurs:

 
There are still any known issues with the plugin for EL9 based OS's?
Server info:
OS: Cloudlinux 9.4
Kernel version:  5.14.0-427.13.1.el9_4.x86_6
cPanel version: 120.0.5
Acronis Agent version: 24.4.37802
Acronis Plugin version: 1.8.1.757
 
Thank you


Hello Emanuel.
That issue isn't related with this thread. I've checked our internal resources and there aren't any tickets or known issues for that error with this version.
I suggest you to raise a ticket so we can troubleshoot the issue https://kb.acronis.com/content/8153 .
Best regards. 

      
                
                
                    
                                                    Mon, 05/13/2024 - 12:06
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
