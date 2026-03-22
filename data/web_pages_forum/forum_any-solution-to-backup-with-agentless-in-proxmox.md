# Any solution to backup with agentless in Proxmox?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/any-solution-backup-agentless-proxmox

## Original Post
**Author:** Unknown

Any solution to backup with agentless in Proxmox?

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Pakpoom Chatsuwan
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Now many of my customer asking if Acronis can backup with agentless mode in Proxmox. Due to licensing issue with VMWARE drive our customer to migrate for opensource solution.
Please suggest for this scenario please.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 04/26/2024 - 08:21

                                                              
                                  
                                    Tags:   RM-260

                                  
                                
                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Thank you for your inquiry.
At present, we do not have an agent for Proxmox, as we do not support that environment.
As a workaround, you can try to install a Windows/Linux agent inside each VM.
I have forwarded your request to the team for more details. I will update the thread as soon as I have more information.
Best regards.
 

      
                
                
                    
                                                    Fri, 04/26/2024 - 09:43
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Melis Freag
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 30
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            For customers migrating from VMware to an open-source solution due to licensing issues, there are several alternatives to consider. Open-source virtualization platforms like Proxmox, KVM, and Xen are popular choices. These platforms can provide similar functionalities as VMware but without the associated licensing costs

      
                
                
                    
                                                    Tue, 05/07/2024 - 20:53
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Xavier Di Tullio
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            This is something we are also interested in.

      
                
                
                    
                                                    Wed, 10/09/2024 - 18:25
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
There is a feature request for this topic, but at the moment, there is no ETA.
The reference is RM-260.
I've forwarded your message to the team and added a vote on your behalf.
Best regards.

      
                
                
                    
                                                    Thu, 10/10/2024 - 11:45
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Xavier Di Tullio
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you.

      
                
                
                    
                                                    Thu, 10/10/2024 - 12:32
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Xavier Di Tullio wrote:

Thank you.


You are welcome. 

      
                
                
                    
                                                    Thu, 10/10/2024 - 13:59
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    support@zebra.cz
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Jose,
 
Could you, please, add our vote? 
 
Thank you.
 
Best Regards,
Petr

      
                
                
                    
                                                    Fri, 10/11/2024 - 08:44
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            support@zebra.cz wrote:

Hello Jose,
 
Could you, please, add our vote? 
 
Thank you.
 
Best Regards,
Petr


Hello!
Sure, added it now.
Best regards. 

      
                
                
                    
                                                    Fri, 10/11/2024 - 09:30
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    James Burns
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            This needs to happen or Acronis will lose paying customers to Veeam. Just like everyone dropping VMware due to the ridiculous change to licensing that took place.  If this isn't done soon, I will not renew my maintenance with Acronis and use the money to buy Veeam. Too bad, so sad.

      
                
                
                    
                                                    Thu, 10/24/2024 - 13:53
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    tmservo
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I'm in this same boat. We've basically been forced to abandon VMware and I've always loved Acronis. But the transition for multiple clients has been to ProxMox. 
I'm hoping to see something come about that integrates or understands, I know Veam already has it, or Proxmox Backup Server, but there are features of Acronis I've always loved.
I'm hopeful this is something that comes about or in the next year I'm probably going to have to leap to something else also

      
                
                
                    
                                                    Thu, 10/24/2024 - 16:04
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Joni Lee
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Another voice for agentless backup on Proxmox, please do us a favor Acronis.
 
Thank you

      
                
                
                    
                                                    Fri, 10/25/2024 - 06:44
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Thank you for the feedback.
This topic is intended for Service Providers using Acronis Cyber Protect Cloud.
On-premises deployments are discussed in other threads. Acronis Cyber Protect 16 supports Proxmox (supported only for fully virtualized, also known as HVM, guests).
For more details, visit: https://www.acronis.com/en-us/support/documentation/AcronisCyberProtect_16/#supported-virtualization-platforms.html
Please note that a hypervisor agent specifically for Proxmox is not available, and as far as I know, there are no plans for integration in the near future.
If you have any queries please contact our support at https://support.acronis.com/
Best regards.

      
                
                
                    
                                                    Fri, 10/25/2024 - 14:49
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    İlker Şekkeli
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Acronis Team,
I have had positive experiences with Acronis' powerful backup and disaster recovery solutions for a long time. Recently, however, I started using Proxmox, and I am in need of integrating Acronis solutions with this platform. Proxmox is widely used in virtualization environments, and ensuring compatibility between Acronis and Proxmox would bring significant value to users like myself.

      
                
                
                    
                                                    Tue, 01/21/2025 - 18:26
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            İlker Şekkeli wrote:

Hello Acronis Team,
I have had positive experiences with Acronis' powerful backup and disaster recovery solutions for a long time. Recently, however, I started using Proxmox, and I am in need of integrating Acronis solutions with this platform. Proxmox is widely used in virtualization environments, and ensuring compatibility between Acronis and Proxmox would bring significant value to users like myself.


Hello!
At this moment, there are no plans to integrate it in the near future, based on my review.
I’ve added a vote on your behalf and shared your comments with the team.
Best regards,

      
                
                
                    
                                                    Wed, 01/22/2025 - 17:18
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Marek Klimaszewski
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi All,
Please count my vote, as well as the votes from my colleagues at our company. Acronis is our primary backup platform and is integrated with our customers' environments based on VMware (in addition to M365, workstations, XDR in some cases, etc.).
However, the significant changes in VMware licensing represent a major shift in the entire customers infrastructure, which could make switching to another backup platform relatively straightforward. Please keep this in mind, Acronis.
Looking for constructive response.

      
                
                
                    
                                                    Fri, 01/24/2025 - 14:30
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Marek Klimaszewski wrote:

Hi All,
Please count my vote, as well as the votes from my colleagues at our company. Acronis is our primary backup platform and is integrated with our customers' environments based on VMware (in addition to M365, workstations, XDR in some cases, etc.).
However, the significant changes in VMware licensing represent a major shift in the entire customers infrastructure, which could make switching to another backup platform relatively straightforward. Please keep this in mind, Acronis.
Looking for constructive response.


Hello Marek,
Thank you for your feedback.
After reviewing the account, I couldn’t find your email in our database.
I suggest reaching out to your service provider or reseller (if they are responsible for your support) so they can raise a ticket and leave the message on record.
Best regards.
 

      
                
                
                    
                                                    Sat, 01/25/2025 - 00:32
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    İlker Şekkeli
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Jose Pedro Magalhaes wrote:


İlker Şekkeli wrote:

Hello Acronis Team,
I have had positive experiences with Acronis' powerful backup and disaster recovery solutions for a long time. Recently, however, I started using Proxmox, and I am in need of integrating Acronis solutions with this platform. Proxmox is widely used in virtualization environments, and ensuring compatibility between Acronis and Proxmox would bring significant value to users like myself.


Hello!
At this moment, there are no plans to integrate it in the near future, based on my review.
I’ve added a vote on your behalf and shared your comments with the team.
Best regards,

Hello,
Thank you for your interest.
The lack of a roadmap on this matter in the near term is both surprising and concerning, as VMware's licensing policy doesn't seem likely to be corrected anytime soon, and it’s receiving significant backlash from the industry. Meanwhile, the majority of customers—those whose VMware support is expiring or those planning to migrate to a new virtualization platform—are turning to more cost-effective solutions.
One of the most critical factors in this shift is backup scenarios. Companies offering quick support for solutions like Proxmox are gaining a competitive advantage. This situation, however, ties our hands as an MSP, creating a playing field where we cannot effectively compete.
I strongly hope Acronis can present a roadmap on this issue without further delay.
 


      
                
                
                    
                                                    Sat, 01/25/2025 - 03:36
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Joni Lee
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Well speak. I really hope Acronis takes this seriously. This is a very good advantage for all parties, especially Acronis.

      
                
                
                    
                                                    Sat, 01/25/2025 - 09:46
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I believe it won’t take much longer.
From what I can see, agentless backups for Nutanix are arriving very soon ( next month ) so it’s highly likely that Proxmox will be next on the list.
Best regards,

      
                
                
                    
                                                    Mon, 01/27/2025 - 15:03
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    rlopez
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Any updates on this??
It´s imperative to have a Proxmox agent at hypervisor level as soon as possible.
Thank you so much.

      
                
                
                    
                                                    Tue, 03/18/2025 - 18:48
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            rlopez@nesic.es wrote:

Any updates on this??
It´s imperative to have a Proxmox agent at hypervisor level as soon as possible.
Thank you so much.


Hello!
Thank you for reaching out.
There is no ETA for this feature at the moment. However, I’ve forwarded your request to the team and added a vote on your behalf.
Best regards.

      
                
                
                    
                                                    Wed, 03/19/2025 - 07:35
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    rlopez
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Are you conscient that all other backup solutions in the market that are direct competitors to Acronis are Proxmox compatible or are in a final phase to become compatible? Do you know that a lot of people like me are looking for alternatives to Acronis due this?
 

      
                
                
                    
                                                    Thu, 03/20/2025 - 21:10
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Norm Rasmussen
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I agree that this is a needed feature/option.  The VMWare integration is good, but we will be moving away from VMWare as quickly as we need to re-license.
 
Can we be placed on some sort of update time frame?
 
Thanks

      
                
                
                    
                                                    Fri, 04/18/2025 - 18:37
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Roland Lee
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Also waiting on Proxmox hypervisor level support for my customers.

      
                
                
                    
                                                    Fri, 04/18/2025 - 23:21
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Norm Rasmussen wrote:

I agree that this is a needed feature/option.  The VMWare integration is good, but we will be moving away from VMWare as quickly as we need to re-license.
 
Can we be placed on some sort of update time frame?
 
Thanks!


Hello!
Thank you for reaching out.
There is no ETA for this feature at the moment. 
 If there are any news I will update this thread.
Best regards.

      
                
                
                    
                                                    Tue, 04/22/2025 - 08:15
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    İlker Şekkeli
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Jose P. Magalhaes wrote:

Norm Rasmussen wrote:

I agree that this is a needed feature/option.  The VMWare integration is good, but we will be moving away from VMWare as quickly as we need to re-license.
 
Can we be placed on some sort of update time frame?
 
Thanks!


Hello!
Thank you for reaching out.
There is no ETA for this feature at the moment. 
 If there are any news I will update this thread.
Best regards.


Hello,
Is there another platform where we can effectively raise this issue? Because since the topic was opened, only our messages have been shared, and there has been no progress. Meanwhile, updates are coming on the virtualization side, and I need to make a decision. It would be appropriate for Acronis to provide a statement regarding this matter.

      
                
                
                    
                                                    Tue, 04/22/2025 - 09:39
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            İlker Şekkeli wrote:

Jose P. Magalhaes wrote:

Norm Rasmussen wrote:

I agree that this is a needed feature/option.  The VMWare integration is good, but we will be moving away from VMWare as quickly as we need to re-license.
 
Can we be placed on some sort of update time frame?
 
Thanks!


Hello!
Thank you for reaching out.
There is no ETA for this feature at the moment. 
 If there are any news I will update this thread.
Best regards.


Hello,
Is there another platform where we can effectively raise this issue? Because since the topic was opened, only our messages have been shared, and there has been no progress. Meanwhile, updates are coming on the virtualization side, and I need to make a decision. It would be appropriate for Acronis to provide a statement regarding this matter.


As mentioned above, I’ve voted for your feature request and shared your comments with the team. However, please note that this is not a support platform. I recommend raising a support ticket or asking your service provider to do so on your behalf.
Best regards,

      
                
                
                    
                                                    Tue, 04/22/2025 - 11:31
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Roberto Novasconi
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Support for agentless backup of Proxmox VMs was implemented with Cyber Protect Cloud 25.07, supporting Proxmox VE 8.2+.
With 25.08, support for Proxmox VE 9.0+ was added.

      
                
                
                    
                                                    Thu, 09/04/2025 - 08:26
                                                                            
                                
                            
                                            
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Roberto Novasconi wrote:

Support for agentless backup of Proxmox VMs was implemented with Cyber Protect Cloud 25.07, supporting Proxmox VE 8.2+.
With 25.08, support for Proxmox VE 9.0+ was added.


Hello Roberto,
Indeed, it was.
Thank you for being attentive and for updating this thread.
Best regards,

      
                
                
                    
                                                    Thu, 09/04/2025 - 10:24
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
