# Critical Support Request – Backup Index File Lost and TIBX Recovery Inquiry

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/critical-support-request-backup-index-file-lost-and-tibx-recovery-inquiry

## Original Post
**Author:** Unknown

Critical Support Request – Backup Index File Lost and TIBX Recovery Inquiry

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Alex Cardoso
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Dear Acronis Support Team,
I am reaching out to request escalation of a critical issue in our backup environment. Previous support interactions have not resolved the problem, and I believe the case requires analysis by a senior technical specialist at Acronis.
Environment Overview:
Platform: Microsoft Hyper-V
Operating System: Windows Server 2019
File Server with Windows native deduplication enabled
Backup routines: Local, Cloud, Daily, and Monthly
Current backup size: ~11 TB
Issue Summary: In September 2025, we attempted to restore a file and encountered persistent errors preventing access to restore points. After extensive investigation, I was able to access the backup using a Windows Server 2012 R2 machine with agent version v25.1.39482, indicating a compatibility or agent-related issue.
We performed the following actions on the affected server:
Agent update – unsuccessful
OS update + agent reinstallation – unsuccessful
After the update on 21/09/2025, the server began performing full backups instead of the previous incremental ones. The backup process lasted until 16/10/2025. Subsequent local backup jobs failed to complete, although backup slices were being generated. These slices did not appear in the job list.
On 20/10/2025, we interrupted a backup job that had been running since 16/10/2025. Due to the large number of files not visible in the management console, and having direct access to the backup storage disk, I manually deleted data by date. Unfortunately, this action also removed the metadata/index file.
Current Situation:
We have approximately one year of backup data stored.
The index file is missing, making it impossible to access the backup contents.
I acknowledge the deletion was an operational error due to lack of knowledge.
Request:
Is it possible to rebuild the index file or recover access to the TIBX files without it?
Has Acronis encountered similar incidents where index corruption or deletion was resolved?
I kindly request this case be escalated to Acronis core support, not local partners, as previous responses were limited to forum references and did not involve deeper technical analysis.
Additional Notes:
We have successfully configured and executed new backup routines on a separate unit.
I am available to provide logs, technical details, and perform any necessary tests to assist in the investigation.
Thank you for your attention. I look forward to your guidance and support.
Best regards,Alex Cardoso

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 10/28/2025 - 09:38

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Olá Alex, bom dia.
Infelizmente, depois de eliminar cópias manualmente, a cadeia de backups é quebrada e a sequência torna-se inutilizável.
A única coisa que pode ser tentada é abrir os backups manualmente, um por um, através do Windows Explorer, por exemplo, e verificar se algum deles ainda é acessível — embora não haja garantia de que isso funcione.
É importante manter cópias em dois ou, preferencialmente, três locais diferentes para evitar situações como esta. Armazenar todas as cópias num único local pode levar a este tipo de problema.
Pelo que é visível, o senhor possui contrato com a Stock, portanto, as comunicações e o suporte devem ser feitos através deles.
Se o senhor tiver o número do ticket, podemos rever o caso internamente; sem essa informação, não é possível proceder com a verificação.
Obrigado.

      
                
                
                    
                                                    Tue, 10/28/2025 - 14:07
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
