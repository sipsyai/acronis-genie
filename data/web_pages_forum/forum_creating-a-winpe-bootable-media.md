# Creating a WinPE bootable media

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/creating-winpe-bootable-media

## Original Post
**Author:** Unknown

Creating a WinPE bootable media

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Phil Whitmore
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 10
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi all,
 
Today I have been attempting to carry out a bare metal restore of a machine that uses a B120i RAID controller to which all logical drives are attached and provisioned from.
 
I've already read the posts regarding the incompatibility of the Linux boot media due to HP's closed source drivers. I've also read the get around is to create a WinPE bootmedia with Acronis boot media injected into it alongside the RAID driver for Windows OS'. My question is, as a Solution Provider for Acronis Backup Cloud, I cannot find where to download the media creation tool for windows. The boot media available from the Management Portal is just the Linux one.
 
I've looked on account.acronis.com under our primary account but there are no products registered to which I can download the tool - neither can I raise a support ticket without a registered licence key.
 
Many thanks,
 
Phil
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 01/22/2019 - 23:02

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Backup Cloud

            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Evgeny Ryuntyu
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 56
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Phil,
 
It's Evgeny from Acronis Service Providers Support.
We have described the steps on how to create the WinPE media for Acronis Data Cloud in the following KB article:
 
https://kb.acronis.com/content/59611
 
Please follow the instruction. 
 
PS: we also have a KB article about the custom media which support B120i controller - https://kb.acronis.com/content/6495 - but the media which can be shared from on demand is outdated.
I have contacted the responsible team to check if we can compile the media with B120i support based on the latest Acronis Data Cloud agent build.
 
-----------------------------------------------------------------
Evgeny Ryuntyu | Senior Support Engineer
Acronis Backup Cloud | #1 Cloud Service Provider Backup

      
                
                
                    
                                                    Wed, 01/23/2019 - 10:29
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Phil Whitmore
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 10
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Evgeny,
 
Once again, many thanks for your reply. I was given our Account Manager's details and got in contact with them earlier today. They pointed me at article: https://kb.acronis.com/content/59611  This got me to what I needed as far as being able to create a bootable media in WinPE.
 
That may help any other Service Solution Providers using Acronis Backup Cloud that solely rely on the endpoint agents and don't have any "products" registered to themselves. The endpoint agent didn't have the "Bootable Media" option in the installer.
 
All the best,
 
Phil

      
                
                
                    
                                                    Wed, 01/23/2019 - 15:18
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Backup Cloud
