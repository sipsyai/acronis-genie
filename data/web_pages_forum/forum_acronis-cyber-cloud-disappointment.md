# Acronis Cyber Cloud disappointment

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/acronis-cyber-cloud-disappointment

## Original Post
**Author:** Unknown

Acronis Cyber Cloud disappointment

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Carl Allen
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi Folks,
Apologies if I am posting in the wrong place, I'm new to the forum.
I manage a small MSP looking after around 700 endpoints.. We backup about 30 servers mostly physical and a few VM's.
For many years we used BackupAssist backing up to Azure. However, the product is poorly supported by Zen Software and is missing important DR functions so we decided to move to a new product. Unfortunately after much searching around we chose Acronis Cyber backup as in theory it seems to offer everything we needed under one portal. We moved several customers across to Acronis but within days all the backups were failing for a variation of different reasons. None of the error messages provided enough information to fully investigate the issue. We had VSS writers that would hang within seconds of the backup starting even thought the same writers could be used successfully with several other backup applications. After hours of wasted time searching on line for solutions we admitted defeat and are now looking elsewhere. I should mention that support was utterly useless. One ticket still wasn't resolved after eight days. They continuously asked for logs and eventually we just gave up. So to sum up its a really good idea and is probably ok if the systems run without error. However, support is AWOL so be ready use google to fix problems. 
I am genuinely disappointed as we have already managed to get some customers to pay the extra cost and had sold them on Acronis being a top tier product. We are now going to have to either stick to BackupAssist or look at MSP360. Veeam doesn't have a proper hosted MSP offering and Altaro are focussed on VM only with a basic backup facility for physical systems.
I would be interested to hear your experience with the Cyber backup product and more specifically the support.
 
Kindest Regards
Carl

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 11/11/2020 - 17:25

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Mikhail Rozhkov
                            

                            
                    
                        Support Engineer 
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 21
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Carl.
Could you please tell me the number of the created case so that I can assist you with the solution?

      
                
                
                    
                                                    Mon, 11/16/2020 - 14:26
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Phil Whitmore
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 10
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Carl,
 
We are an ITSM who provide Acronis to our customers and have migrated many legacy backup systems (From Veeam to the good old WBAdmin.exe)
 
Whilst I can have my gripes about the user interface sometimes (see one of my posts down the forum wherein I was expecting backup data refreshes to happen automatically).... Overall we have been very happy with the solution.
Where we have had to make support requests they have generally been dealt with pretty quickly (via our account manager - non urgent stuff goes on here).
 
We too have had issues with VSS writers but being an ITSM we are also responsible for and qualified to diagnose and fix issues within our customers IT environments. In all cases so far we have found the issues with VSS to be related to 3rd party influences (for example AV that blocks access to certain core services Acronis relies on like Cryptographics or WMI). 
 
The basic tenant we follow is sandboxing to ensure compatibility with the myriad of 3rd party apps and then deploy - and always DR test after the initial seed! But I can't imagine treating any other solution differently.
 
Not to sound overly simple but have you tried the VSSDoctor Acronis provide? On a couple of occasions its pointed us at the glaringly obvious and in others pointed us in the right direction.
 
I hope you get a satisfactory outcome here - I think like most products, its not perfect but the pros outweigh the cons and its still evolving.
 
That's my 2 pence worth anyway! :)

      
                
                
                    
                                                    Mon, 11/16/2020 - 17:23
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Backup Cloud
