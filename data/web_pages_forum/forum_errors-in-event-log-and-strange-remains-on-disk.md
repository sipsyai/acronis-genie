# Errors in Event log and strange remains on disk

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/errors-event-log-and-strange-remains-disk

## Original Post
**Author:** Unknown

Errors in Event log and strange remains on disk

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    SvenT
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 68
                
            
            
                
                    Comments: 232
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hey,
I have a Hyper-V Server running Windows Server 2022.
On this Server are 4 virtual Servers. 
a) Domaincontroller running Windows Server 2019
b) File/Printserver running Windows Server 2022
c) Remote Desktop Session Host with one collection, running Server 2022
d) Server running Windows Server 2022 on which the Acronis ManagementServer and WSUS is installed.
I use Acronis Cyber Backup Version 16, most recent version.
Each night some backup plans run:
- 2 filebackups (uses Agent in VM)
- Domaincontrolles is backed up agentless
- File/Printserver  is backed up agentless
- plan to backup Server with the AMS uses agent in the VM
- plan to backup Remote Desktop Session Host uses agent in the VM
- Hyper-V Host
If the Hyper V host starts the backup I see eventlog entries:
- in the VMs 12293/VSS
- in the VM of the Remote Desktop Session host I see additional entries (I opened another thrad for that: Backup of Hyper- V Host creates EventIDs in Guest - How can I Install SQL Agent ? )
- on the Hyper-V Host I see Event IDs  3280 (Hyper-V-Worker), 18012 and 10150 (Source Hyper-V.VMMS) for a) b) and c) and shortly after these events I see 3 event IDs 16010
What I also see:
On the disks I see for a) b) and c) in the snapshot folder a *.vmgs file and a folder with the same name.
Folder is empty.
Time of the folder and the file is 2 minutes earlier than the upper mentioned entries in the event log.
But in the Hyper-V manager there are no snaphots/checkpoints shown.
For a) and b) I have a *.mrt and *.rct for each VHDX of that machine in the folder where the VHDX is located.
Time of these files is 1 minutes earlier than the upper mentioned entries in the event log
 
VSS Doctor states one VSS shadow storage to be misconfigured:
ForVolume: \\?\Volume{ed3f0378-0e74-4dc4-bb9b-13ab0cb01775}\
OnVolume: \\?\Volume{ed3f0378-0e74-4dc4-bb9b-13ab0cb01775}\
Used: 0 B
Allocated: 0 B
Maximum: 52 MB
Minimum: 320 MB
VolumeSize: 522 MB
Available: 83 MB
TargetMaximum: 320 MB
MaximumGreaterThenMinimum: False
MaximumIsEnough: False
MaximumIsNotReached: True
AvailableIsEnoughForMaximum: True
IsOk: False
Description: Maximum storage size is less than required minimum

But this is the recovery volume on c:\ so I am somewhat cautious about correcting that.
on the same volume it is also stated "free space is below required minimum"
The upper mentioned folders and *.vmgs remains I had also on the previous system (Cyber Backup Advanced 15).
All VMs are configured to use production checkpoints and the tick is set to use stabdard checkpoints if the guest does not support production checkpoints.
Allplans are configured to select the VSS provider on their own.
Any hints to solve these issues?
Thanks in advance
Sven
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sun, 01/11/2026 - 17:37

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Cyber Protect Backup Advanced 15/16 in professional usecases


            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    SvenT
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 68
                
            
            
                
                    Comments: 232
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hey there, 
After I created this post I digged in a bit deeper and I found the following:
Acronis Cyber Protect: Recommendations for backing up a Hyper-V host when Virtual Machines are stored locally
 
Hmm okay. this is exactly what I do:
I have serveral volumes in the physical server:
- One Volume with the Hypervisor OS
- One Volume with all the files of the VMs (also the "Virtual Machines" Folders with the *.vmcx and *-vmrs files of the Hyper-V Manager) 
- Several other volumes that with no need for a backup
- my backup of the Hyper-V host backs up these 2 volumes 
It seems as if this is not recommended ?
My poblem in understanding:
If a backup a volume on which the Hyper-V Data is stored is not recommended, how can I backup the Hyper-V configuration?
Or asked in another way:
How can I backup the Hyper-V in a correct and recommended way that after a restore the VM ID, SID withiin the VM and all Microdoft activations are the same as before?
Thanks in advance
Sven  
 

      
                
                
                    
                                                    Mon, 01/12/2026 - 08:32
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Backup Advanced 15/16 in professional usecases


            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Sven.
This is expected Hyper-V behavior with Production Checkpoints.
The *.vmgs, RCT/MRT files and event IDs are normal during VSS-based backups.
VM storage volumes should not be backed up at host level—use agentless VM backups and back up only the Hyper-V host OS.
The VSS warning on the recovery partition can be ignored.
Best regards.

      
                
                
                    
                                                    Mon, 01/12/2026 - 12:02
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    SvenT
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 68
                
            
            
                
                    Comments: 232
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hey Jose,
Well, 
 
The *.vmgs, RCT/MRT files and event IDs are normal during VSS-based backups.

Yes I understand that, but AFTER the backup is done, my expectation was, that at least the *.vmgs files and the folders in the snapshot folder of the Virtual Machines are gone. 
But after each backup an additional golder and file shows up and that is strange.
Or is that also expected? 
How can I get rid of them as it grows and grows? 
 
 

The VSS warning on the recovery partition can be ignored.

Ok thanks for that information


VM storage volumes should not be backed up at host level—use agentless VM backups and back up only the Hyper-V host OS.
 

Okay understood, that is what also the linked KB article states.
But as mentioned, the VM config (the Hyper-V vmcx files) are on the same volume as the virtual disk storage.
So how can I backup this?
Is the recommendation to split the locations so that the Hyper-V Host OS and the configuration of the Hyper-V VMs (so the "Virtual Machines" folder) ar on one volume and on another volume are the virtual disks and the snaphots folder?
And then only backup the volume with the Hypervisor OS and the Hyper-V config?
 
Best regards.
Sven

      
                
                
                    
                                                    Mon, 01/12/2026 - 12:42
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Backup Advanced 15/16 in professional usecases


            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    SvenT
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 68
                
            
            
                
                    Comments: 232
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hmm Jose?
Any recommendations for the lovation of the config files? 

      
                
                
                    
                                                    Tue, 01/13/2026 - 13:21
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Backup Advanced 15/16 in professional usecases


            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Sven,
Thank you for the detailed follow-up. I understand your concerns regarding the *.vmgs, RCT/MRT files, and the Hyper-V configuration. Here’s some clarification:

*Persistent .vmgs / snapshot folders
	These files and folders are expected artifacts when using Production Checkpoints with VSS-based backups. They are not automatically deleted by Hyper-V or Acronis. Their presence is normal, but if you want to prevent accumulation, the recommended approach is to schedule a post-backup cleanup via a script or automation that removes old snapshot-related files once the backup completes successfully.


Backing up VM configuration vs. VM storage
	Best practice is:

Do not back up the Hyper-V VM storage volumes at the host level. Agentless VM backups take care of the virtual disks while preserving VM IDs, SIDs, and activations.


Backup the Hyper-V host OS and configuration files. Ideally, place the Hyper-V “Virtual Machines” folder (with *.vmcx files) on the same volume as the Hyper-V OS. The virtual disks themselves can remain on separate volumes. This ensures host-level backup captures configuration without backing up the VM storage directly.



Splitting volumes
	Yes, separating the Hyper-V host OS + configuration from the VM virtual disks is the recommended setup. It simplifies host-level backups and avoids the artifacts you’re seeing from VM storage backups.


VSS warning on the recovery partition
	This can be ignored if the volume is small and not part of your main backup plans.

Summary Recommendation:

Keep VM storage backups agentless (inside the VM or agentless via Hyper-V).


Host-level backups should include only OS + configuration volumes.


Implement cleanup for snapshot artifacts to prevent file accumulation.

This approach aligns with Microsoft Hyper-V and Acronis best practices while keeping your backup workflow clean and reliable.
Best regards,

      
                
                
                    
                                                    Tue, 01/13/2026 - 18:28
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    SvenT
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 68
                
            
            
                
                    Comments: 232
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hey Jose,
thanks for clarification.
 the recommended approach is to schedule a post-backup cleanup via a script or automation that removes old snapshot-related files once the backup completes successfully.

Simply delete them?
Well....if it is that easy....why isn´t the backup task doing this?
Acronis knows best, whether the backup completed successfully.
 
Agentless VM backups take care of the virtual disks while preserving VM IDs, SIDs, and activations.

Hmmm...,are you sure? ;-)
That might be the case for agentless...maybe...but as you know: there is a bug in the tool that prevents successful agentless backups od Server 2022 if an application aware backup is needed.
So only 1 of my 4 servers can be backed up agentless....
Is there any estimation until when this works ?Acronis Cyber Protect: Application-aware backup of Hyper-V VM fails with "Internal error: Unsuccessful response code '7' of action request"
 
This approach aligns with Microsoft Hyper-V and Acronis best practices while keeping your backup workflow clean and reliable.

Okay....MS states slightly different recommendations.
The say, that the Hyper-V config volumes shall be on a different volume than the Hyper-V OS and on the same as the virtual drives.
Hmmm So I will check and see whether I create a third volume only for the VM config files (it needs only a tiny one.....)
S.

      
                
                
                    
                                                    Wed, 01/14/2026 - 07:59
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Backup Advanced 15/16 in professional usecases


            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            SvenT wrote:

Hey Jose,
thanks for clarification.
 the recommended approach is to schedule a post-backup cleanup via a script or automation that removes old snapshot-related files once the backup completes successfully.

Simply delete them?
Well....if it is that easy....why isn´t the backup task doing this?
Acronis knows best, whether the backup completed successfully.
 
Agentless VM backups take care of the virtual disks while preserving VM IDs, SIDs, and activations.

Hmmm...,are you sure? ;-)
That might be the case for agentless...maybe...but as you know: there is a bug in the tool that prevents successful agentless backups od Server 2022 if an application aware backup is needed.
So only 1 of my 4 servers can be backed up agentless....
Is there any estimation until when this works ?Acronis Cyber Protect: Application-aware backup of Hyper-V VM fails with "Internal error: Unsuccessful response code '7' of action request"
 
This approach aligns with Microsoft Hyper-V and Acronis best practices while keeping your backup workflow clean and reliable.

Okay....MS states slightly different recommendations.
The say, that the Hyper-V config volumes shall be on a different volume than the Hyper-V OS and on the same as the virtual drives.
Hmmm So I will check and see whether I create a third volume only for the VM config files (it needs only a tiny one.....)
S.


Hello Sven,
Quick summary:

*.vmgs / snapshot folders are normal with Production Checkpoints. To prevent accumulation, consider a post-backup cleanup script.


Keep Hyper-V OS + VM config (*.vmcx) on one volume, VM storage (VHDX) on another. Agentless backups handle disks; use agent-based for VMs requiring application-aware backup.


For bugs or issues like Server 2022 application-aware backups, please  contact Acronis Support for official guidance.

This approach preserves VM IDs/SIDs/activations and avoids unnecessary files.
Best regards,
 

      
                
                
                    
                                                    Wed, 01/14/2026 - 10:36
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    SvenT
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 68
                
            
            
                
                    Comments: 232
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hey Jose,
please excuse me for being so persistent here. 
vmgs/snapshot folders:
You state that these remainings are normal.
Well....if I create manually a production checkpoint and delete/merge it vy the Hyper-V manager or Powershell these files are gone.
After the backup, there are no snapshots/checkpoints in Hyper-V Manager visible and so there is no merge (neither via Hyper-V Manager not Powershell) possible, as there are no checkpoints available.
You suggest a post-backup celanup script.
So far so good.
But: what shall this script do?
As mentioned, powershell cannot manage any cleanup as it sees no checkpoints....
I will try to contact support for the Server 2022 issue.
But my support case I opened yesterday is still no available in my supportcase list....is this normal that it needs so long to show up there?
S.

      
                
                
                    
                                                    Wed, 01/14/2026 - 11:44
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Backup Advanced 15/16 in professional usecases


            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            SvenT wrote:

Hey Jose,
please excuse me for being so persistent here. 
vmgs/snapshot folders:
You state that these remainings are normal.
Well....if I create manually a production checkpoint and delete/merge it vy the Hyper-V manager or Powershell these files are gone.
After the backup, there are no snapshots/checkpoints in Hyper-V Manager visible and so there is no merge (neither via Hyper-V Manager not Powershell) possible, as there are no checkpoints available.
You suggest a post-backup celanup script.
So far so good.
But: what shall this script do?
As mentioned, powershell cannot manage any cleanup as it sees no checkpoints....
I will try to contact support for the Server 2022 issue.
But my support case I opened yesterday is still no available in my supportcase list....is this normal that it needs so long to show up there?
S.


Hello Sven,
The *.vmgs and snapshot folders are expected artifacts from VSS-based production checkpoints. They can remain even when no checkpoints are visible in Hyper-V Manager.
About a post-backup cleanup script: it would simply remove the old snapshot-related files (*.vmgs, RCT/MRT) after the backup completes successfully. I’m mentioning this as a best practice — I won’t be providing or maintaining such a script.
I also checked and don’t see your support case in the system yet. Please submit it directly as a ticket so it’s properly tracked by Acronis Support. There can sometimes be a short delay before it appears in the portal, but submitting it ensures it’s logged.
Best regards,
 

      
                
                
                    
                                                    Wed, 01/14/2026 - 11:59
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    SvenT
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 68
                
            
            
                
                    Comments: 232
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Jose,
could you please give ma a hint, where I can find the info
"The *.vmgs and snapshot folders are expected artifacts from VSS-based production checkpoints. They can remain even when no checkpoints are visible in Hyper-V Manager."
And simply removing vmgs rct/mrt files.....really a good idea?
Well for what reason ever, I am not able to put hyperlinks here any more....
So please search iin google for "Safe to delete contents of Machines\Snapshots folder" and use the Spiceworks link.....
They tell something different...
So honestly spoken I am a bit cautious in simply deleting these files/folders..
The ticket in queston is case number 07110999.
Or is the expectation of the support, that I write an answer on the mail that gave me that ticketnumber with a repetition of the ticket content?
S.

      
                
                
                    
                                                    Wed, 01/14/2026 - 15:34
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Backup Advanced 15/16 in professional usecases


            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            SvenT wrote:

Hello Jose,
could you please give ma a hint, where I can find the info
"The *.vmgs and snapshot folders are expected artifacts from VSS-based production checkpoints. They can remain even when no checkpoints are visible in Hyper-V Manager."
And simply removing vmgs rct/mrt files.....really a good idea?
Well for what reason ever, I am not able to put hyperlinks here any more....
So please search iin google for "Safe to delete contents of Machines\Snapshots folder" and use the Spiceworks link.....
They tell something different...
So honestly spoken I am a bit cautious in simply deleting these files/folders..
The ticket in queston is case number 07110999.
Or is the expectation of the support, that I write an answer on the mail that gave me that ticketnumber with a repetition of the ticket content?
S.


Hello Sven,
I’ve linked your forum post to your support ticket (07110999). The support team will review it and get back to you as soon as possible.
This ensures your issue is officially tracked and handled by the proper channel.
Best regards,
 

      
                
                
                    
                                                    Thu, 01/15/2026 - 15:01
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    SvenT
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 68
                
            
            
                
                    Comments: 232
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thanks a lot,
Well it´s a bit disappointing, that even after 2 days the mentioned ticket i neither visible in my user account nor that I received any answer.
I have 12 licenses under maintenance and this reaction time is.....well....not fast enough or what is trhe expected reaction time normally ? 

      
                
                
                    
                                                    Thu, 01/15/2026 - 18:20
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Backup Advanced 15/16 in professional usecases


            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    SvenT
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 68
                
            
            
                
                    Comments: 232
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hey,
I opened the ticket on tuesday.....now its sunday.
Up to now, the ticket is still not visible....
Is it understandable, that I am really disappointed?
I pay for support but support shows no reaction within 4 1/2 DAYS !!!!!
The backup tool is a crucial and important component in network operation and I have severe issues and nobody is willing to answer the questions?
Really?

      
                
                
                    
                                                    Sun, 01/18/2026 - 10:34
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Backup Advanced 15/16 in professional usecases


            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            SvenT wrote:

Hey,
I opened the ticket on tuesday.....now its sunday.
Up to now, the ticket is still not visible....
Is it understandable, that I am really disappointed?
I pay for support but support shows no reaction within 4 1/2 DAYS !!!!!
The backup tool is a crucial and important component in network operation and I have severe issues and nobody is willing to answer the questions?
Really?


Hello Sven,
Thank you for your patience. I see that the support team has responded to your ticket today. Please continue working with them directly for any additional technical questions or remote session needs, as they are best equipped to resolve the issue.
Best regards,
 

      
                
                
                    
                                                    Mon, 01/19/2026 - 12:52
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    SvenT
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 68
                
            
            
                
                    Comments: 232
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Well they demanded the system reports and so on for a question regarding a proper procedure....well I sent it now but no idea why this is needed.
Ticket is still not visible in my account....
S. 

      
                
                
                    
                                                    Mon, 01/19/2026 - 19:27
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Backup Advanced 15/16 in professional usecases


            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Sven,
The sysreport is the standard procedure for a case, as it ensures the support team has all necessary logs in case the situation requires escalation.
Regarding ticket 07110999, please confirm with the team whether there is any ongoing issue with Acronis Account. I believe the platform experienced some issues last week, which may explain why it isn’t visible in your account, but this requires confirmation from the team.
Best regards,

      
                
                
                    
                                                    Tue, 01/20/2026 - 14:20
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    SvenT
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 68
                
            
            
                
                    Comments: 232
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Yes I am contact with a person from Acronis Support regarding ticket 07110999.
Additionally with the account linked to the mail I use here in the forum there exists also a ticket with ID07116157 that I never created. 
And yes, the account I use for the forum is a different one with a different mail cpompared to the account I use for supportcases and the business licences. 
S.

      
                
                
                    
                                                    Tue, 01/20/2026 - 17:04
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Backup Advanced 15/16 in professional usecases


            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    SvenT
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 68
                
            
            
                
                    Comments: 232
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            One additional information:
 
The sysreport is the standard procedure for a case, as it ensures the support team has all necessary logs in case the situation requires escalation.


Yes, I understand that, if you have to dig into the logs.
 
But.....to clarify
- why the ticket is not visible in my account
- what is the recommended storage location of the different parts of Hyper-V
- the ETA of a bugfix
nothing, really nothing, from MY system and machine can help to answer these questions in any way....
S.
 
 
 
 

 

      
                
                
                    
                                                    Tue, 01/20/2026 - 17:13
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Backup Advanced 15/16 in professional usecases


            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            SvenT wrote:

One additional information:
 
The sysreport is the standard procedure for a case, as it ensures the support team has all necessary logs in case the situation requires escalation.


Yes, I understand that, if you have to dig into the logs.
 
But.....to clarify
- why the ticket is not visible in my account
- what is the recommended storage location of the different parts of Hyper-V
- the ETA of a bugfix
nothing, really nothing, from MY system and machine can help to answer these questions in any way....
S.
 
 
 
 

 


Hi Sven,
Thank you for all the details you’ve provided. I understand your concerns regarding ticket visibility, Hyper-V configuration, and backup artifacts. At this point, the support team is the only channel that can provide official answers on bugfix timelines, account issues, or detailed procedures.
Please continue working directly with your support ticket(s) for updates and guidance. The forum cannot provide case-specific resolutions or ETAs.
Thanks for your understanding,
 

      
                
                
                    
                                                    Wed, 01/21/2026 - 15:46
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    SvenT
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 68
                
            
            
                
                    Comments: 232
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Full ack, that support are the people in charge.
But where my questions are case-specific I cannot see.
Because I asked for specific recommendations regarding the hints in a KB article.
And why it is needed to create system logs to clarify this....well.
Ans also my system logs can give no hint on ETA or ticket visibility issues either.
So...I will wait and see if the questions can be clarified withiin reasonable time...

      
                
                
                    
                                                    Thu, 01/22/2026 - 07:43
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Backup Advanced 15/16 in professional usecases
