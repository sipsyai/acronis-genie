# Backup Corruption Issue with Acronis on RHEL 9.4 Based OS (Kernel 5.14.0-427)

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/backup-corruption-issue-acronis-rhel-94-based-os-kernel-5140-427

## Original Post
**Author:** Unknown

Backup Corruption Issue with Acronis on RHEL 9.4 Based OS (Kernel 5.14.0-427)

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Emanuel Vicente
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 8
                
            
                                                        
    
    
        
    


                
                
                    
                        
            For several months, we have been in communication with our Acronis partner regarding persistent filesystem errors in backup images created with kernel version 5.14.0-427 on AlmaLinux 9.4 and CloudLinux 9.4 operating systems.
Backups made with Acronis on this kernel are being silently corrupted. This becomes critical during a bare metal restore, where filesystem errors occur upon booting the restored machines.
When using the Acronis cPanel plugin, these issues manifest when attempting to open a recovery point within the plugin. For example, partitions may fail to mount due to filesystem corruption in the backup.
The only current workaround is to downgrade the kernel to the version used in the 9.3 OS release (5.14.0-362).
This situation is critical because we cannot rely on backup software that claims to support RHEL 9.4-based operating systems since May, yet fails to deliver.
Four months have passed since the release of AlmaLinux 9.4, and this problem remains unresolved.
We understand that this is a known issue, one that you've been aware of for a significant amount of time, with multiple support tickets filed. Therefore, we urge you to prioritize and focus on providing a solution as soon as possible.
Issues like this cause clients to lose trust in the software, which may lead them to seek alternative backup solutions.
Could you please provide an estimated timeline for when this issue will be resolved, or any additional information on the progress being made? Clear communication on this matter would help us better plan our backup strategy moving forward.
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 08/30/2024 - 12:27

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
Thank you for sharing the information.
Please review the following documentation: Supported Operating Systems and Environments.
The kernel version is currently supported as follows: Starting from version 8.4, only kernels from 4.18 to 5.19 are supported, at least since the latest update (regarding the Acronis Backup agent).
Regarding the cPanel plugin, these are the currently supported environments: System Requirements and Supported OS.
Could you also share the ticket numbers you have raised so we can review them?
Thanks.

      
                
                
                    
                                                    Mon, 09/09/2024 - 18:40
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Emanuel Vicente
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 8
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
At this moment I can't give you ticket numbers, since they were sent by our Acronis Partner.
All the information that I have is that this issue is assigned with the ID's ABR-381717 and ABR-388306 that affect kernel versions 5.14.0-427 shipped with RHEL 9.4 based OS's.
Can you check internally?
 
Thanks

      
                
                
                    
                                                    Tue, 09/17/2024 - 15:28
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Emanuel Vicente wrote:

Hello,
At this moment I can't give you ticket numbers, since they were sent by our Acronis Partner.
All the information that I have is that this issue is assigned with the ID's ABR-381717 and ABR-388306 that affect kernel versions 5.14.0-427 shipped with RHEL 9.4 based OS's.
Can you check internally?
 
Thanks


Hello!
These IDs are related to internal tasks assigned to implement those improvements in future builds of the product.
There is no exact ETA at this time, but you can most likely expect it to be applied by the end of this year.
Best regards.

      
                
                
                    
                                                    Tue, 09/17/2024 - 16:44
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Emanuel Vicente
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 8
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
The real question here is that in the documentation link you provided, it’s stated that "Red Hat Enterprise Linux 9.4", "CloudLinux 9.4", "Almalinux 9.4" and "Rocky Linux 9.4" are supported.
You also reference: "Starting from version 8.4, supported only with kernels from 4.18 to 5.19".
However, this is misleading. There are critical issues with backup images created using the 5.14.0-427 kernel, which falls within that range. Given this, why is this information still listed in your "Supported operating systems and environments" on this page: https://www.acronis.com/en-us/support/documentation/CyberProtectionService/#supported-operating-systems-and-environments.html ?
This comes across as false information. There are likely many users running Acronis on RHEL 9.4-based OSs who may face corrupted systems during disaster recovery. This is a serious concern! 
Acronis has been viewed as a top-tier company, but issues like this raise concerns about transparency. If there are problems with RHEL 9.4-based OSs, it should not be listed as supported, and a public warning or statement on the known issues should be made.
Simply asking for internal tickets, as you often do, keeps critical information hidden from the wider community. 
The lack of publicly available details on known issues is frustrating. Being transparent, even when problems arise, builds trust. This is something Acronis needs to work on.
 
On the last informations that we have from our Acronis Parnter, this issue is now an "ERT" ("Emergency response task"?) and that the task is under "IMT-40".
 
Could you please provide more public information regarding this case, including details about the problem itself and any recommendations for affected users?
 
Thank you.

      
                
                
                    
                                                    Wed, 09/18/2024 - 09:15
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Emanuel Vicente wrote:

Hello,
The real question here is that in the documentation link you provided, it’s stated that "Red Hat Enterprise Linux 9.4", "CloudLinux 9.4", "Almalinux 9.4" and "Rocky Linux 9.4" are supported.
You also reference: "Starting from version 8.4, supported only with kernels from 4.18 to 5.19".
However, this is misleading. There are critical issues with backup images created using the 5.14.0-427 kernel, which falls within that range. Given this, why is this information still listed in your "Supported operating systems and environments" on this page: https://www.acronis.com/en-us/support/documentation/CyberProtectionService/#supported-operating-systems-and-environments.html ?
This comes across as false information. There are likely many users running Acronis on RHEL 9.4-based OSs who may face corrupted systems during disaster recovery. This is a serious concern! 
Acronis has been viewed as a top-tier company, but issues like this raise concerns about transparency. If there are problems with RHEL 9.4-based OSs, it should not be listed as supported, and a public warning or statement on the known issues should be made.
Simply asking for internal tickets, as you often do, keeps critical information hidden from the wider community. 
The lack of publicly available details on known issues is frustrating. Being transparent, even when problems arise, builds trust. This is something Acronis needs to work on.
 
On the last informations that we have from our Acronis Parnter, this issue is now an "ERT" ("Emergency response task"?) and that the task is under "IMT-40".
 
Could you please provide more public information regarding this case, including details about the problem itself and any recommendations for affected users?
 
Thank you.


Hello Emanuel,
I would recommend reviewing the information.
Our backup agent does support that environment. If I’m not mistaken, you mentioned using the cPanel plugin. The cPanel integration is tied to cPanel, and they haven’t yet released a build that supports those versions.
However, if you install an Acronis agent (rather than the plugin) on the Linux machine, and the machine’s kernel is supported, you should be able to perform backups. As you’d expect, we don’t manage third-party integrations; we simply enable our customers to use them within our product. The respective companies manage their own builds.
Best regards.

      
                
                
                    
                                                    Wed, 09/18/2024 - 14:08
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Emanuel Vicente
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 8
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
Jose Pedro Magalhaes wrote:
Our backup agent does support that environment. If I’m not mistaken, you mentioned using the cPanel plugin. The cPanel integration is tied to cPanel, and they haven’t yet released a build that supports those versions.

I'm not understanding this statement.
Do you mind checking your "Acronis cPanel Plugin" changelog page for version 1.8.1 (Build 757 April 29, 2024) on the following URL?: https://www.acronis.com/en-gb/support/updates/changes.html?p=41411
It says: "This update introduces support for AlmaLinux 9, CloudLinux 9, and Rocky Linux 9 operating systems in the plugin."
 
Also, on your cPanel plugin PDF guide ( https://dl.acronis.com/u/pdf/Acronis_Backup_plugin_for_cPanel_en-US.pdf ), on Page 4, you can check the section "Supported operating systems":
The integration has been tested on the following operating systems supported by WHM and cPanel:
l AlmaLinux OS 8 and 9
l CentOS 7
l CloudLinux 6, 7, 8, and 9
l Red Hat Enterprise Linux 7
l Rocky Linux 8 and 9
l Ubuntu 20.04 LTS

 
Can you clarify the information that I need to review based on your documentation?
 
Jose Pedro Magalhaes wrote:
However, if you install an Acronis agent (rather than the plugin) on the Linux machine, and the machine’s kernel is supported, you should be able to perform backups. As you’d expect, we don’t manage third-party integrations; we simply enable our customers to use them within our product. The respective companies manage their own builds.

In our experience, this statement isn't accurate. We've tested both scenarios, the agent and plugin with our cPanel partner, and unfortunately, backups still experience silent corruption when using the agent alone, without the plugin.
I’m aware that this information is available internally, but it seems we’re still receiving unclear or incomplete responses...
 
Key Issue:
The problem appears to be related to Kernel 5.14.0-427 shipped with version 9.4. After downgrading the kernel to version 5.14.0-362 (from the previous 9.3 release), the issue no longer occurs.
 
However, it seems my previous question hasn't been addressed yet:
Emanuel Vicente wrote:
On the last informations that we have from our Acronis Parnter, this issue is now an "ERT" ("Emergency response task"?) and that the task is under "IMT-40".
 
Could you please provide more public information regarding this case, including details about the problem itself and any recommendations for affected users?

 
Best Regards

      
                
                
                    
                                                    Wed, 09/18/2024 - 17:17
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Emanuel Vicente wrote:

Hello,
Jose Pedro Magalhaes wrote:
Our backup agent does support that environment. If I’m not mistaken, you mentioned using the cPanel plugin. The cPanel integration is tied to cPanel, and they haven’t yet released a build that supports those versions.

I'm not understanding this statement.
Do you mind checking your "Acronis cPanel Plugin" changelog page for version 1.8.1 (Build 757 April 29, 2024) on the following URL?: https://www.acronis.com/en-gb/support/updates/changes.html?p=41411
It says: "This update introduces support for AlmaLinux 9, CloudLinux 9, and Rocky Linux 9 operating systems in the plugin."
 
Also, on your cPanel plugin PDF guide ( https://dl.acronis.com/u/pdf/Acronis_Backup_plugin_for_cPanel_en-US.pdf ), on Page 4, you can check the section "Supported operating systems":
The integration has been tested on the following operating systems supported by WHM and cPanel:
l AlmaLinux OS 8 and 9
l CentOS 7
l CloudLinux 6, 7, 8, and 9
l Red Hat Enterprise Linux 7
l Rocky Linux 8 and 9
l Ubuntu 20.04 LTS

 
Can you clarify the information that I need to review based on your documentation?
 
Jose Pedro Magalhaes wrote:
However, if you install an Acronis agent (rather than the plugin) on the Linux machine, and the machine’s kernel is supported, you should be able to perform backups. As you’d expect, we don’t manage third-party integrations; we simply enable our customers to use them within our product. The respective companies manage their own builds.

In our experience, this statement isn't accurate. We've tested both scenarios, the agent and plugin with our cPanel partner, and unfortunately, backups still experience silent corruption when using the agent alone, without the plugin.
I’m aware that this information is available internally, but it seems we’re still receiving unclear or incomplete responses...
 
Key Issue:
The problem appears to be related to Kernel 5.14.0-427 shipped with version 9.4. After downgrading the kernel to version 5.14.0-362 (from the previous 9.3 release), the issue no longer occurs.
 
However, it seems my previous question hasn't been addressed yet:
Emanuel Vicente wrote:
On the last informations that we have from our Acronis Parnter, this issue is now an "ERT" ("Emergency response task"?) and that the task is under "IMT-40".
 
Could you please provide more public information regarding this case, including details about the problem itself and any recommendations for affected users?

 
Best Regards


Hello!
If the issue lies with the Acronis agent and not the plugin, it should be reported to the team, as the installation of agents on that OS and kernel should be supported. The corruption of the backups likely doesn't originate from this issue, but further investigation will be required.
Regarding the IMT-40 code I mentioned earlier, the task is specifically related to the cPanel issue.
I can confirm that the upcoming builds are expected to address this, with a release scheduled for the coming weeks (around October).
The cPanel metadata file issue, which causes backup corruption, isn't related to the product itself, but rather due to the lack of support for Linux distributions beyond 9.3 and kernel 362.
While we can assist with feature requests and backup errors here on the forum, for deeper insights or more detailed information, it's best to raise a support ticket (or request your MSP to do so). Our support teams can handle the investigation, provide updates, and share insight that isn't available here.
Best regards.
 

      
                
                
                    
                                                    Thu, 09/19/2024 - 06:38
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
