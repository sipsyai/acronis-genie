# Features Request from MSP's Client

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/features-request-msps-client

## Original Post
**Author:** Unknown

Features Request from MSP's Client

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Reng Kwan Lee
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Dear Acronis, 
I have a few features that i would love to see implemented within the Acronis Backup Cloud. Yet i do not know what's the best way to reach Acronis to express the features. i hope by posting here is one of the best channel.
 
1) Having a remark fields in Tenant's management portal for administrator's to enter notes e.g. installation time or configuration. This for example, under the same backup account having multiple workstation/pc that is exactly the same computer name!
2) Able to replicate cloud storage off-site for MSP backend, yet configurable by Tenant's portal. This scenario is due to customer runs production data in MSP's cloud, having BaaS within the same cloud is only same site backup. If MSP BaaS can replicate off-site then the picture is more complete. 
3) RBAC on tenant's portal. Certain users only require Read Access. there's no way to customize that.
 
Thanks and hope can get response from Acronis. 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 11/25/2015 - 04:16

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Vladimir Miroshkin
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 174
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Reng Kwan Lee,
Thank you for all your ideas. 
#1 - Could you clarify where do you want to have this field? Is this a property of machine or something else?
#2 - Don't get use case. Are you talking about geo replicated storage or something else? 
#3 - RBAC is planned and we are moving in this direction. As you may see in version 4 we merged administrator and backup acccounts. For now crete other accounts is just privilege. So, we are going to have role based feature management in one of the next releases.
Regards,
Vladimir
 

      
                
                
                    
                                                    Thu, 11/26/2015 - 13:55
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Reng Kwan Lee
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dear VM, 
Thanks for your reply. Let me further clarify. 
#1 - We can have the field anywhere in the GUI Management portal. We uses single Backup Account to deploy agent into multiple server. Say we deploy Agent into Production Server and Development Server, obviously the VM on both machine having the same name and this is where it is very confusing from the GUI Management Portal where each same have 2 Virtual Machines yet there's no indication of this VM is from which server. 
This scenario goes to the same where we deploy agents into multiple SILO branch under same backup account to manage centrally. All branches uses the same computer name and we are unable to determine which computer is from which branch. 
Hence, having a field to uniquely identify the computers will be great.
 
#2 - yes, talking about geo-replicated storage whereby to cater for customer who willing to pay premium and have a site-resilient backup data set. As backup data set is important for them to pass Audit on safe keeping of archived files. hence, geo-replicating backup data allow service provider gives higher SLA.
 
#3 - noted on RBAC.
 
more requirement as we further leverage on the product:
#4 - having to allow us to further customize number of copies to be able to keep locally on Network Shares and Cloud. Users want fast recovery locally but only latest data set, which rest of the files goes into Cloud. 
#5 - DRaaS was told to launch soon, but there's no sign of it.
#6 - Future roadmap accessible by service provider so we can pitch to potential customer who might be looking at features.
#7 - Allow to backup Hyper-V VM over SMB3. 
 


VM wrote:

Hello Reng Kwan Lee,
Thank you for all your ideas. 
#1 - Could you clarify where do you want to have this field? Is this a property of machine or something else?
#2 - Don't get use case. Are you talking about geo replicated storage or something else? 
#3 - RBAC is planned and we are moving in this direction. As you may see in version 4 we merged administrator and backup acccounts. For now crete other accounts is just privilege. So, we are going to have role based feature management in one of the next releases.
Regards,
Vladimir
 



      
                
                
                    
                                                    Mon, 12/07/2015 - 04:45
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Vladimir Miroshkin
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 174
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dear Reng Kwan Lee,
#1 - Currently, we support distinguishing registered machines by IP address, and by "Computer description" properties (for Windows OS only).
To set this description field, please, open properties of computer, press "Change settings" field and set "Computer description". This field will be shown in "Overview" tab of the selected machine.
I will add your future to the feature request list. 
#2 - We support replication of customer's data from customer promises to service provider datacenter. Replication between two datacenters is in product backlog. No concrete ETA so far.
#4 - Different retention schedules for primary and second location is planned for one of the next releases. Using this functionality you can implement such scheme. 
#5 - Next release includes DR on customer premises.
#6 - We will communicate plans for next release in advance, and maybe for next two releases.
It won't be accessible publicly. This information can be shared with partners who signed NDA. 
The list of features is communicated publicly only when we start beta program. All partners who has direct contract can have access to beta environment and play with feature before they becomes available on production.
If you find out that some features are missed in product and it prevent you from selling it, please, contact support and describe them a problem. They either provide you the solution, workaround, or contact product management team to add this feature to one of the next releases.
#7 - Acronis Backup Cloud supports Hyper-V machines located on SMB3. Please, contact support if you have any problem with this functionality.
Regards,
Vladimir

      
                
                
                    
                                                    Mon, 12/07/2015 - 11:30
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Chris Porosky
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            We're looking forward to all of these same features as well.  
#2  Multiple replication sites would also be useful for replicating some or all of the cloud data back to the local managed service provider (who is in the same city as the customer).  So in affect, the most important data is in three places; if on premise backup is lost, the local msp can then quickly restore recent data to the customer's location without needing to download or wait for drive to be shipped from remote cloud.
#7 Open file VSS support for SMB3 is great to hear.  
new #8  We have been unable to find any kind of detailed backup job progress stats - like estimated time remaining, number of files transferred / remaining, actual average transfer speed, data size selected / transferred, etc. - hoping this might be a training issue though?
 
 
 

      
                
                
                    
                                                    Thu, 03/10/2016 - 21:58
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Vladimir Miroshkin
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 174
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Chris,
In the latest version 5 there is the following info:
- Start time
- Progress itslef (for example, 11% completed)
- Time remaining (for example, 5 min left)
- Duration
- Bytes processed
- Bytes saved
To see it, please, open activities tab, select the required activity and open Activity details section.
Regarding "number of files transferred / remaining", it is applicable for file level backup only. Why do you need this info? It does not help to predict remaining time, or do something else. Please, clarify.
Regards,
Vladimir

      
                
                
                    
                                                    Fri, 03/11/2016 - 06:27
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Global-e | CS   
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 17
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            As a service provider we would also like to see some new features:
 
- Directory's wich are included to be shown in the logfiles/mail notifications. There is a lot of information already in the logfiles but in our opinion its essential to have the items wich are backup up shown in the mail notifications. Right now our customers do not know wich folders are present in the backup, and also for us its a lot of work to figure out wich folders should be backup up everytime a new schedule needs to be created because of issues/bugs/problems in the excisting schedule.
 
- An option to exclude folders. Right now you can select folders you want to backup but when you select lets say C:\Shares, everything under C:\shares is backed up. What about when i want to exclude a folder under C:\Shares? Yes i can disable it in the initial selection, but when i do this and new folders wich are created under C:\Shares wont automatically be added to the schedulde, so the root inheritance to be backed up is lost. An exclusion option would help greatly so you can simply select C:\ and then afterwards set exclusions as to wich folders should not be included.

      
                
                
                    
                                                    Wed, 04/13/2016 - 08:37
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Vladimir Miroshkin
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 174
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Global-e | CS,
We have an item in product backlog on showing content of backup in notifications. Could you clarify why you cannot select the specific folder for backup and trust that it was backed up? What is the reason to check content that was included into backup manually?
Regarding #2, it is supported in current version. You need to create a backup plan, select c:\shares for backup, and then in Backup options in File Filters section you can specify masks for files and folder to exclude from backup.
Regards,
Vladimir

      
                
                
                    
                                                    Wed, 04/13/2016 - 12:26
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Global-e | CS   
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 17
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            #2 is resolved, thank you for the information.
 
Regarding number #1; We as a service provider configure the backups for our customers. But the mail notifications about wether a backup job has completed successfully or not do not contain the contents of the backup. So these mail notifications which are received by our customers are lacking this information. It would be a great improvement for our customers to get this info.

      
                
                
                    
                                                    Wed, 04/13/2016 - 12:59
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Vladimir Miroshkin
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 174
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you for clarification.
In case if you manage backups for them, do you think customers will look inside those emails to see what was backed up? Why do they need this info? Just for curiosity or something else?
Regards,
Vladimir

      
                
                
                    
                                                    Wed, 04/13/2016 - 13:41
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Global-e | CS   
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 17
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            In our experience our customers do look at the mail notifications.
The addition to see whats actually backed up would help greatly.
 
Example: We have a couple of directories configured to be backed up for a customer.
They have told us about these directories when we first configured their backup.
But now a couple of months later, they have created some new directories and have not told us about this, so we did not include them in the backup.
With the addition for the customer to see the contents of the Backup jobs, they can alert us about this and say "Hey Global-e, I would like to have This and That new directory added to my backup, because this also contains company data!" and we can quickly solve this for them.
 
Another way this would be helpfull is for us a service provider when we need to create a new job, because of lets say a bug in the current job that deletes the file paths of the folders wich are currently backed up. (this is an actual bug at this moment). If we had the information of whats actually backed up in the notification mails, we could very quickly create a new job with this information instead of going trough the whole disk of the customer to verify where the data is stored.

      
                
                
                    
                                                    Wed, 04/13/2016 - 14:22
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Vladimir Miroshkin
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 174
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Got it. Thank you for such detailed explanation. I will add your comment to this feature request.
Regards,
Vladimir

      
                
                
                    
                                                    Wed, 04/13/2016 - 14:51
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Global-e | CS   
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 17
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Another idea for future updates;
The error messages that are now received when a backup fails are very technical.
As an IT administrator i can make some sense of it, but still a lot of it is completely unclear to me.
So instead of knowing what to do after looking at the error, i have to go check out the KB (knowlegde base) every time, check the forums and create a support ticket. 
Wich in the end gives me a work-around most of the times instead of a definitive fix because there seem to be a lot of bugs in the product.
 
So to begin with, the error messages could be made a lot easier to understand.
Example of a current error message: Backup Failed - Device is not ready:"!currentBunchChunks.IsNull()","$module":"ArsAgentPro
Example of an improved error message: Backup Failed - The VSS writers reported a problem. Please check the VSS writer state and Knowlegde base artical KB....
 
With this new way of receiving errors we immediately know it has something to do with VSS (writers) and also have the corresponding KB article to check for solutions.

      
                
                
                    
                                                    Tue, 05/10/2016 - 10:42
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Vladimir Miroshkin
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 174
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            We are working on it and with each release we analyse the most frequently happened errors and create a human readable error message for them.
To my regret we cannot fix all error messages at once.
Thank you for feedback!
Regards,
Vladimir 

      
                
                
                    
                                                    Tue, 05/10/2016 - 11:01
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Global-e | CS   
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 17
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Vladimir,
 
The fact that it has got your attention and you are working to create more human readable error messages is great.
Thanks for you answer

      
                
                
                    
                                                    Tue, 05/10/2016 - 11:31
