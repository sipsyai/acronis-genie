# cPanel Plugin Broken since new cPanel v110

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/cpanel-plugin-broken-new-cpanel-v110

## Original Post
**Author:** Unknown

cPanel Plugin Broken since new cPanel v110

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Chris Danks
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 20
                
            
                                                        
    
    
        
    


                
                
                    
                        
            cPanel are now pushing out version 110 and the latest Acronis cpanel plugin version 1.7.542 does not work!
Screenshot attached.  We also tried rebooting the server after a yum update to see if it helped but it did not.


      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      2023-04-04_12-10-09.jpg

                      299.82 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Tue, 04/04/2023 - 11:24

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Chris.
The issue may require a investigation. I've browsed internally and at the moment there aren't any known issues with the Cpanel.
Please collect the HAR logs while logging in the Cpanel account and the Cpanel logs too and contact our support: 
- Har logs: https://kb.acronis.com/content/58514
- Cpanel logs: https://kb.acronis.com/content/61940
Please check the KB about how to contact support: https://kb.acronis.com/content/8153
If you have any questions please me know.

      
                
                
                    
                                                    Tue, 04/04/2023 - 12:52
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Chris Danks
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 20
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            HI
no need for my logs just login to any WHM and update to version 110 from 108 then try to load acronis and you'll too see the problem.

      
                
                
                    
                                                    Tue, 04/04/2023 - 15:52
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Chris Danks wrote:

HI
no need for my logs just login to any WHM and update to version 110 from 108 then try to load acronis and you'll too see the problem.


Yes, I understand, but that issue should be investigated because at the moment we don't have any known issue being reproduced or similar tickets. So it's advisable to collect the HAR logs and raise a ticket so we can communicate the issue to R&D. If you have any issues while raising the ticket, please let me know so I can raise it myself.

      
                
                
                    
                                                    Tue, 04/04/2023 - 16:01
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Chris Danks
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 20
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            We buy our licenses direct through cloudevo.com and after talking with them yesterday acronis are aware of the issue and a high priority fix is underway?
 
Yet you’re saying no one’s reported it???

      
                
                
                    
                                                    Wed, 04/05/2023 - 08:20
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Chris Danks wrote:

We buy our licenses direct through cloudevo.com and after talking with them yesterday acronis are aware of the issue and a high priority fix is underway?
 
Yet you’re saying no one’s reported it???


 Hello Chris!
I searched again and actually there is 1 ticket for this issue, opened last day from your service provider. The issue is being investigated and they will be notified as soon as we have a solution.
Thanks in advance!
 

      
                
                
                    
                                                    Wed, 04/05/2023 - 10:06
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            We're experiencing the same issue on multiple servers that have been upgraded to cPanel v110, and have opened a ticket with mspsupport, Case #05842527.

      
                
                
                    
                                                    Mon, 04/10/2023 - 08:12
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            George_Fusioned wrote:

We're experiencing the same issue on multiple servers that have been upgraded to cPanel v110, and have opened a ticket with mspsupport, Case #05842527.


Hi George.
I've updated the ticket.
You will receive an email from our support as soon as possible with the workaround for the issue.  Please confirm to me after if everything was resolved.
Thanks in advance!

      
                
                
                    
                                                    Mon, 04/10/2023 - 08:40
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Chris Danks
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 20
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            The workaround worked for us 

      
                
                
                    
                                                    Mon, 04/10/2023 - 10:50
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Chris Danks wrote:

The workaround worked for us 


Hello Chris, thanks for keeping me updated.
I am glad it worked for you.
Feel free to participate here anytime you need.
Thanks.

      
                
                
                    
                                                    Mon, 04/10/2023 - 11:25
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            It looks like with v110, cPanel completely deletes the /usr/local/cpanel/base/frontend/paper_lantern folder, and because the Acronis plugin uses a symlink in the jupiter folder to the above path, the files are gone now.
As a workaround solution you can copy acronisbackup folder (https://access.acronis.com/t/LTNTp98wAGOu) from paper_lantern theme folder to jupiter.
Extract the contents of the src folder from the file above, into /usr/local/cpanel/base/frontend/jupiter/acronisbackup/. It should like like this:
# ls -la /usr/local/cpanel/base/frontend/jupiter/acronisbackup/
total 16
drwxr-xr-x  3 root root 4096 Apr 10 11:08 .
drwxr-xr-x 90 root root 4096 Apr 10 11:07 ..
drwxr-xr-x  4 root root 4096 Apr 10 11:08 assets
-rwxr-xr-x  1 root root  306 Apr 10 11:08 index.live.php
and then also create a proper symlink for the WHM plugin:
# cd /usr/local/cpanel/whostmgr/docroot/cgi/acronisbackup
# rm assets
# ln -s /usr/local/cpanel/base/frontend/jupiter/acronisbackup/assets assets
This should resolve the issue for now, until v1.8 is out which will fix this.

      
                
                
                    
                                                    Mon, 04/10/2023 - 11:31
                                                                            
                                
                            
                                            
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            George_Fusioned wrote:

It looks like with v110, cPanel completely deletes the /usr/local/cpanel/base/frontend/paper_lantern folder, and because the Acronis plugin uses a symlink in the jupiter folder to the above path, the files are gone now.
As a workaround solution you can copy acronisbackup folder (https://access.acronis.com/t/LTNTp98wAGOu) from paper_lantern theme folder to jupiter.
Extract the contents of the src folder from the file above, into /usr/local/cpanel/base/frontend/jupiter/acronisbackup/. It should like like this:
# ls -la /usr/local/cpanel/base/frontend/jupiter/acronisbackup/
total 16
drwxr-xr-x  3 root root 4096 Apr 10 11:08 .
drwxr-xr-x 90 root root 4096 Apr 10 11:07 ..
drwxr-xr-x  4 root root 4096 Apr 10 11:08 assets
-rwxr-xr-x  1 root root  306 Apr 10 11:08 index.live.php
and then also create a proper symlink for the WHM plugin:
# cd /usr/local/cpanel/whostmgr/docroot/cgi/acronisbackup
# rm assets
# ln -s /usr/local/cpanel/base/frontend/jupiter/acronisbackup/assets assets
This should resolve the issue for now, until v1.8 is out which will fix this.


Hello George.
Thanks for sharing the workaround and the respective link. This will be valuable for the other partners.
I wish you a nice day! 

      
                
                
                    
                                                    Mon, 04/10/2023 - 13:32
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    William Rawling
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Can anyone share a working link?  
Trying..  https://access.acronis.com/t/LTNTp98wAGOu
We currently get "This download link does not exist."
Thanks

      
                
                
                    
                                                    Thu, 05/04/2023 - 15:06
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            William Rawling wrote:

Can anyone share a working link?  
Trying..  https://access.acronis.com/t/LTNTp98wAGOu
We currently get "This download link does not exist."
Thanks


Hello William. 
Welcome to the forum.
Please check this KB. It has the solution: https://kb.acronis.com/content/72127
Thanks. 

      
                
                
                    
                                                    Thu, 05/04/2023 - 15:56
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
