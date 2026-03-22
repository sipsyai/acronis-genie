# Still no official support for Microsoft Exchange SE

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/still-no-official-support-microsoft-exchange-se

## Original Post
**Author:** Unknown

Still no official support for Microsoft Exchange SE

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Tappsy
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I would like to ask for clarification regarding the current support status of Exchange Server SE. As far as I understand, there is still no official Microsoft support for this version. Could you please confirm whether this is indeed the case?
If so, this would mean that Acronis by October 14, 2025 does not have any officially Microsoft-supported Exchange Server version in its portfolio. Could you let me know if and when this situation might change?
Thank you in advance for your clarification.
Best regards

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 09/23/2025 - 10:16

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Javier
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 52
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I have the same problem.
I setup a new VM with Server 2025 and Exchange SE to migrate our current Server 2022 with Exchange 2019CU15 but when I installed the agents I found it didn't recongnize SE so it cannot be backed up. and had to stop the process This leaves us having to decide in a few weeks between a potentially vulnerable system due to end of security patching and unprotected databases/mailboxes due to lack of application support in backups. One may argue that there is still protection by restoring at the file or even VM level but depending on setup this can be quite slow and unconvenient.
A few days ago I raised a ticket for this reason and I was told support would communicate the issue to the developpment team and keep me informed of any progress but so far I have not received any updates.
There is less than a month left Oct. 14th being the deadline. Since was released last month of July and SE being code identical to 2019CU15 with only version number changes, I don't understand why this is taking so long to release an update with new agents for SE.
Can we please get a least an ETA?
TIA
 
 

      
                
                
                    
                                                    Tue, 09/23/2025 - 10:59
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Tappsy
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I heard from another competitor that they have problems with single item restore, maybe it is the same with Acronis.
But another big player has already full support for SE, so it should be possible ;)

      
                
                
                    
                                                    Tue, 09/23/2025 - 11:23
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Javier
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 52
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I have no problems with restoring either invidual databases or messages in V.16.4.39929 (we only update when new stuff or fixes apply to our system/needs) and thus I can't se how that could be an issue in SE using the same 2019CU15 code but maybe MS changed more than it admits.

      
                
                
                    
                                                    Tue, 09/23/2025 - 11:39
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Our support team has taken note of your comments and created feature request RM-10627 (I believe they have already informed you).
I encourage everyone to contact our support and reference this task so that the feature can be prioritized and implemented as soon as possible. It’s important to keep it documented in the records.
Best regards,

      
                
                
                    
                                                    Tue, 09/23/2025 - 12:46
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Javier
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 52
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            
 


 
Helo Pedro,
No, they haven't informed me of anything beyond what I've said or if they did I'm nbot aware of it. I didn't know there was a change request number created until you posted it here nor whether its progress can be tracked. 
Anyway, the important thing here is the urgency of an updated release of ACB with the required Exchange agents. 
 
KR,
J

      
                
                
                    
                                                    Tue, 09/23/2025 - 13:12
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Javier wrote:


 


 
Helo Pedro,
No, they haven't informed me of anything beyond what I've said or if they did I'm nbot aware of it. I didn't know there was a change request number created until you posted it here nor whether its progress can be tracked. 
Anyway, the important thing here is the urgency of an updated release of ACB with the required Exchange agents. 
 
KR,
J


Hi Javier,
I’ve attached this thread to the feature request so the team can review it and understand the importance of this matter.

      
                
                
                    
                                                    Tue, 09/23/2025 - 14:22
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Javier
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 52
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            José P. Magalhães wrote:
 
Hi Javier,

I’ve attached this thread to the feature request so the team can review it and understand the importance of this matter.


 Thanks José, appreciated, hope they can release this ASAP

      
                
                
                    
                                                    Tue, 09/23/2025 - 14:36
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Javier wrote:

José P. Magalhães wrote:
 
Hi Javier,

I’ve attached this thread to the feature request so the team can review it and understand the importance of this matter.


 Thanks José, appreciated, hope they can release this ASAP


You are welcome. 

      
                
                
                    
                                                    Tue, 09/23/2025 - 15:09
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Javier
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 52
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Less than 2 weeks left before Exchange 2016CUxx/2019CUxx go into EOL.... It'll be nice if we got at least an ETA so we could plan migrations

      
                
                
                    
                                                    Wed, 10/01/2025 - 11:29
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Javier wrote:

Less than 2 weeks left before Exchange 2016CUxx/2019CUxx go into EOL.... It'll be nice if we got at least an ETA so we could plan migrations


Hello Javier,
I’ve requested the information from the team. As far as I know, there is no ETA yet.
As soon as I receive more details, I’ll update this thread.
Best regards,

      
                
                
                    
                                                    Wed, 10/01/2025 - 14:39
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Javier wrote:

Less than 2 weeks left before Exchange 2016CUxx/2019CUxx go into EOL.... It'll be nice if we got at least an ETA so we could plan migrations


Hello Javier,
Just to give you an update.
The team has tested the SE version, and official support will be added to the documentation over the next hours/days.
The product is fully compatible with the SE version.
Best regards,
 

      
                
                
                    
                                                    Thu, 10/02/2025 - 09:43
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Javier
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 52
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thanks for the info José P. those are good news. I'll be checking the release notes page frequently beacause I have everything ready for migrating our users to the new SE server once we verify the update has no problems/issues. 
Cheers
J

      
                
                
                    
                                                    Thu, 10/02/2025 - 10:04
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Javier wrote:

Thanks for the info José P. those are good news. I'll be checking the release notes page frequently beacause I have everything ready for migrating our users to the new SE server once we verify the update has no problems/issues. 
Cheers
J


You are welcome. 

      
                
                
                    
                                                    Thu, 10/02/2025 - 10:36
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Tappsy
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dear José,
are there any official news yet? Because i still can't find it on the webpage or in the documentation.
Kind regards

      
                
                
                    
                                                    Thu, 10/09/2025 - 08:14
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Tappsy wrote:

Dear José,
are there any official news yet? Because i still can't find it on the webpage or in the documentation.
Kind regards


It will be added.
From this channel, we honestly can’t provide detailed information, as these matters are managed by different teams.
I have been informed that the version is fully supported and that the feature will be added—let’s see when.
Best regards,

      
                
                
                    
                                                    Thu, 10/09/2025 - 15:55
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Javier
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 52
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Starting today all Acronis supported versions of MS Exchange are EOL by Microsoft and the only MS supported version is not supported by Acronis.
If we remain on an Exchange EOL version in order to be able to backup it up and a vulnerabilty is discovered we will find ourselves at a huge risk, on the other hand, if we migrate/upgrade to Exchange SE to be protected against any potential vulnerabilities we won't be able to perform any database/mailbox backups.  
This is an urgent matter and failure to see it as such a respond accordingly will not be good. We were told 12 days ago it was a matter of "hours/days" and it didn't occcur to me that it could actually turn into "weeks/months".
 
 

      
                
                
                    
                                                    Tue, 10/14/2025 - 09:48
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Javier wrote:

Starting today all Acronis supported versions of MS Exchange are EOL by Microsoft and the only MS supported version is not supported by Acronis.
If we remain on an Exchange EOL version in order to be able to backup it up and a vulnerabilty is discovered we will find ourselves at a huge risk, on the other hand, if we migrate/upgrade to Exchange SE to be protected against any potential vulnerabilities we won't be able to perform any database/mailbox backups.  
This is an urgent matter and failure to see it as such a respond accordingly will not be good. We were told 12 days ago it was a matter of "hours/days" and it didn't occcur to me that it could actually turn into "weeks/months".
 
 


Hello Javier,
I just shared the information I had at the time of writing: the product is supported, but the user guides didn’t include it.
I’ve requested the team for any updates regarding when those documents will be revised.
Best regards,

      
                
                
                    
                                                    Tue, 10/14/2025 - 10:12
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            José P. Magalhães wrote:

Javier wrote:

Starting today all Acronis supported versions of MS Exchange are EOL by Microsoft and the only MS supported version is not supported by Acronis.
If we remain on an Exchange EOL version in order to be able to backup it up and a vulnerabilty is discovered we will find ourselves at a huge risk, on the other hand, if we migrate/upgrade to Exchange SE to be protected against any potential vulnerabilities we won't be able to perform any database/mailbox backups.  
This is an urgent matter and failure to see it as such a respond accordingly will not be good. We were told 12 days ago it was a matter of "hours/days" and it didn't occcur to me that it could actually turn into "weeks/months".
 
 


Hello Javier,
I just shared the information I had at the time of writing: the product is supported, but the user guides didn’t include it.
I’ve requested the team for any updates regarding when those documents will be revised.
Best regards,


Hello,
The team informed me that the user guides and other documents are scheduled to be updated around next week.
I can’t personally guarantee it, but that’s the time frame they provided.
Best regards,

      
                
                
                    
                                                    Wed, 10/15/2025 - 15:09
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Javier
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 52
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            After "quite a few" agent install/uninstall/reinstall" attempts it finally seems to work, at least I can see the SE server databases and also mailboxes. I haven't tested backing it up yet but I will probably be able to do it over the weekend.
I will confirm as soon as I find out.
 
Thanks.

      
                
                
                    
                                                    Wed, 10/15/2025 - 15:49
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Javier wrote:

After "quite a few" agent install/uninstall/reinstall" attempts it finally seems to work, at least I can see the SE server databases and also mailboxes. I haven't tested backing it up yet but I will probably be able to do it over the weekend.
I will confirm as soon as I find out.
 
Thanks.


Once you’ve done some additional testing, feel free to update this thread with your findings.
Best regards,

      
                
                
                    
                                                    Wed, 10/15/2025 - 16:02
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Javier
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 52
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I confirm it is possible to backup Exchangre SE databases but I'm having issues with mailboxes backups. I'm getting licensing errors and only a few mailboxes get backed up. Can't confirm yet if it is an Exchange problem or an Acronis one. It started when I added the new server CAS entry in the Mailbox section and looks like since both server share the same external URI Acronis is getting "confused". Al Mailboxes appear to be hosted on SE tough they are stil on the old 2019 one.

      
                
                
                    
                                                    Tue, 10/21/2025 - 06:52
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Javier wrote:

I confirm it is possible to backup Exchangre SE databases but I'm having issues with mailboxes backups. I'm getting licensing errors and only a few mailboxes get backed up. Can't confirm yet if it is an Exchange problem or an Acronis one. It started when I added the new server CAS entry in the Mailbox section and looks like since both server share the same external URI Acronis is getting "confused". Al Mailboxes appear to be hosted on SE tough they are stil on the old 2019 one.


Hello Javier.
Thank you for the feedback and the availability. 
This week a new version/build of Acronis Cyber Protect should be released. 
That version should include the full support of the SE ( and the user-guides updates ).
 

      
                
                
                    
                                                    Tue, 10/21/2025 - 07:05
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Javier
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 52
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi José Pedro,
As this week is almost gone without news, do you have a ETA for the release of the new build?
With current version I'm able to do database level backups but mailbox level backup is not working . I have already migrated users to the new SE server and decommissioned the old 2019 one and we need this working ASAP.
TIA
 

      
                
                
                    
                                                    Fri, 10/24/2025 - 06:49
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Javier wrote:

Hi José Pedro,
As this week is almost gone without news, do you have a ETA for the release of the new build?
With current version I'm able to do database level backups but mailbox level backup is not working . I have already migrated users to the new SE server and decommissioned the old 2019 one and we need this working ASAP.
TIA
 


Hello Javier,
I was expecting it to be released yesterday, based on the information I had.
As mentioned, we can’t guarantee an exact ETA. Let’s see if it happens today or on Monday.
If I receive any updates or learn that it has been postponed, I’ll make sure to update this thread.
Best regards,

      
                
                
                    
                                                    Fri, 10/24/2025 - 06:52
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Just to update: https://www.acronis.com/en-us/support/documentation/AcronisCyberProtect…

      
                
                
                    
                                                    Thu, 10/30/2025 - 09:03
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
