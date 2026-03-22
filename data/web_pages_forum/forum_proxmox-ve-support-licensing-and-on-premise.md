# Proxmox VE support - licensing and on-premise?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-17-forum/proxmox-ve-support-licensing-and-premise

## Original Post
**Author:** Unknown

Proxmox VE support - licensing and on-premise?

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    SvenT
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 68
                
            
            
                
                    Comments: 232
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hey there,
in the announcement of version 17, the agentless support of Proxmox VE seems to show up.
Currently we use Veeam tp backup the Proxmox host and the guests ;-(
So 2 questions
- Will the PVE support also be available in the on-premise (!) Cyber Protect Advanced Backup edition?
- Which license is needed to backup a physical PVE host and the hosted  VMs (1 Windows Server for filehshare, 1 Windows Server with Active Directory, 3 LXC containers...)? Is this the Virtual host license?
Thanks in advance.
 
S.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 10/30/2025 - 08:27

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Cyber Protect Backup Advanced 15/16 in professional usecases


            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Sven,
Yes, to back up both the host and the VMs, you need a Virtual Host license.
Regarding licensing, the on-premises version supports this. You can find more details in the following document:https://www.acronis.com/en/resource-center/resource/acronis-cyber-protect-editions-comparison-including-cloud-deployment/
Best regards.

      
                
                
                    
                                                    Thu, 10/30/2025 - 08:51
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    SvenT
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 68
                
            
            
                
                    Comments: 232
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Jose,
thanks for the answers.
The linked document does not show anything regarding Proxmox as the document is datead 04/2025 and the support for Proxmox is fairly new.
So can you confirm, that the on-premise Acronis Caber Protect Backup Advanced can handle agentless Procmox VE backups and also Active directory in a hosted Windows server on a PVE host?
Due to the costs involved, we need to evaluate whether we stick with the competitor's solution or whether standardization is worth the expense.
 
S.

      
                
                
                    
                                                    Thu, 10/30/2025 - 09:52
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Backup Advanced 15/16 in professional usecases


            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            SvenT wrote:

Hello Jose,
thanks for the answers.
The linked document does not show anything regarding Proxmox as the document is datead 04/2025 and the support for Proxmox is fairly new.
So can you confirm, that the on-premise Acronis Caber Protect Backup Advanced can handle agentless Procmox VE backups and also Active directory in a hosted Windows server on a PVE host?
Due to the costs involved, we need to evaluate whether we stick with the competitor's solution or whether standardization is worth the expense.
 
S.


1. Yes, Acronis Cyber Protect Backup Advanced supports agentless backups of Proxmox. (To clarify, it’s very similar to Acronis Cyber Protect Advanced, but without many of the additional security and cyber protection features.)
2. Yes, for application-aware backups (To perform application-aware backup on virtual machines that are running Windows Server 2022 or Windows Server 2025, you must use agent-based backup ).
You can try it for free, take a trial and test whether it meets your requirements:https://www.acronis.com/en/products/cyber-protect/trial/
Best regards.
 
 

      
                
                
                    
                                                    Thu, 10/30/2025 - 11:29
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
