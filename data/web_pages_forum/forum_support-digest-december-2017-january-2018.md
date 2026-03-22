# Support Digest: December 2017 - January 2018

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/digests-and-support-best-practices/support-digest-december-2017-january-2018

## Original Post
**Author:** Unknown

Support Digest: December 2017 - January 2018

        
  



    
  


  
          





    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Vyacheslav Bykov
                            

                            
                    
                        Cloud SP Trainer
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 10
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello Colleagues!
Let me introduce to you the digest for the past two months. In December we have implemented multiple fixes targeted to make Acronis Backup Cloud server platform more scalable and improve its performance. Also, a fresh version of backup client software that contains several important patches has been released for all supported OS versions. You may perform a centralized update of all client machines using the live update feature. Here's what we have in the list to review:
Hot topics
New KB articles
New training materials
Datacenter and agent updates
Release notes and documentation
Hot topics
One of the most common questions asked by Partners is "what are the recovery options in case production server goes down". Let's go through possible restore scenarios in case you have an image backup of original machine:
  #1 ► Recovery through Backup Console
This method allows you to perform recovery through Acronis Backup Cloud user interface. In order to restore the source machine this way you'll need to meet certain prerequisites first:
    - Install backup client on the target machine
    - Make sure target machine is present under Backup Console
Overall recovery process of a physical machine to another physical machine is explained here. In case you need to recover it a physical machine's image to a new VM, refer to these instructions. Overall recovery cheat sheet for all data types is available here.
Note: in order to be able to recover an image to VM you'll need to have a Hypervisor (VMware ESXi or MS Hyper-V) set up and Agent for VMware or Agent for Hyper-V respectively installed and registered under Acronis Backup Cloud. Recovery through the console does not allow to choose particular disks/volumes to recover as disk mapping is performed automatically by the product. If you'd like to map the disks/volumes manually proceed to next item below.
  #2 ► Recovery through Acronis Bootable Media
This option is applicable in case recovery through Backup Console is impossible for some reason: BMR recovery, machine running MacOS, specific disk configuration, no backup agent installed on target machine.
Exact steps are described under the respective user guide article. This method is applicable for recovering backup image both to a new physical or virtual machine. Check this page for the steps describing Bootable media's creation. Once recovery process is finished, make sure to apply Acronis Universal Restore (AUR) in case performing restore to dissimilar hardware/P2V or V2P migration/BMR recovery. Also, keep in mind, that the Media not only allows you to recover entire machine's image or volumes, but also particular files from backup.

  #3 ► Run a VM from backup (Instant Restore)
This option is the fastest way to bring back the machine in case of disaster. Alternatively, it can be used for the purpose of checking existing backup's consistency: in case some backup is successfully ran as VM and newly created machine is booted into OS, then the backup is 100% consistent. The following article describes prerequisites of "Run as VM" procedure.
Step-by-step process of setting up this method of recovery is described here. The best performance of Instant Restore is achieved in case backup is stored either locally or on some network share. Running a VM from Cloud backup may be slightly slower since
Keep in mind, though, that a machine which is being ran from backup is just a temporary solution, it does not substitute original machine due to specific algorithm Instant Restore works. It's strongly not recommended to leave it running more than 1-3 days and set up a permanent machine in order to substitute the crashed one following any of the options described in the sections above. Optionally, you may finalize your VM running from backup(currently applicable only for VMware VMs) to make this machine permanent.
 
 Did you know that Acronis Disaster Recovery Cloud provides a possibility to instantly spin up a replica of our customer's machine in Acronis data center in case of original machine's failure? See more at https://www.acronis.com/en-us/cloud/service-provider/disaster-recovery/
 
New KB articles
Acronis Backup Cloud
KB60864: Acronis Backup Cloud: "Logging on with the specified credentials is impossible, probably because the account does not exist or the password is invalid" error    
KB60855: Acronis Backup Cloud: recovering a phisycal server to a Hyper-V host fails with "The processor topology specified for the virtual machine cannot be supported by this host"    
KB60842: Acronis Backup Cloud: "JWT is issued by unregistered issuer" error when browsing website and/or mobile backup    
KB60836: Acronis Backup Cloud: "Failed to open the backup archive by the ID" error when attempting to browse recovery points of website of mobile backup    
KB60809: Acronis Backup Cloud Integration with ConnectWise Automate: how to disable ticket creation for a specific type of alerts
Acronis Storage
KB60632: Acronis Storage: Chunk Server node is in 'Failed' state
KB60794: Acronis Storage: 'The Storage is not register with the user' error
See all new KB articles here: https://kb.acronis.com/new
Did you know that our quick troubleshooting kit is the easiest way to find all troubleshooting articles related to Acronis backup Cloud? See more here: https://kb.acronis.com/backup-cloud-known-solutions

 
New training materials
Acronis Data Cloud support training (Presentation + Recording)
Acronis Backup Cloud v.7.5 Troubleshooting Training 
Acronis Storage v.2.3 Product and Troubleshooting Training (Presentation + Recording)
See all training materials here: https://kb.acronis.com/MSPtraining
Did you know that certification only requires a basic 2-hour training and a 1.5-hour quiz? Those who have experience with the software successfully pass the exam with the first attempt and receive a verification certificate right away.
 

Datacenter and agent updates
Current agent versions:
Backup Agent for Windows (v.12.0.4500)
Backup Agent for Mac (v.12.0.4500)
Backup Agent for Linux (v.12.0.4500)
 

Datacenter


Platform version


Available services


Strasbourg (BETA)


7.5HF1


Backup
File Sync&Share


St. Luis (BETA2)


7.5HF1


Backup
Disaster Recovery
File Sync&Share


Strasbourg (EU1)


7.5HF1


Backup


Frankfurt (EU2)


7.5HF1


Backup
Disaster Recovery
File Sync&Share


London (EU3)


7.5HF1


Backup
Disaster Recovery
File Sync&Share


Frankfurt (EU4)


7.5HF1


Backup


Zurich (EU5)


7.5HF1


Backup


Ashburn (US2)


7.5HF1


Backup
Disaster Recovery
File Sync&Share


Ashburn (US5)


7.5HF1


Backup
Disaster Recovery
File Sync&Share


Nagano (JP1)


7.5HF1


Backup


Singapore (SG1)


7.5HF1


Backup


Sidney (AU1)


7.5HF1


Backup


Moscow (RU2)


7.5HF1


Backup

 
Release notes and documentation

Acronis Data Cloud backup agent v.12.0.4500

Acronis Backup Cloud extension for Plesk
Share your experience!
Did you ever face an urgent recovery situation? How did you manage to solve it?
Let us know what topics you'd like to see covered next month.
Share below your experience and your questions.

      
                                            
                
            
                            
                    
                        
                            
                              Wed, 01/17/2018 - 12:15

                                                          
                                                            
                                                                                        
    
                    
                Vyacheslav Bykov
Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                    
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful
