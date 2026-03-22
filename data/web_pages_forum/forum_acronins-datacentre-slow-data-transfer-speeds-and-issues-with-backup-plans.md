# Acronins datacentre slow data transfer speeds and issues with backup plans?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/acronins-datacentre-slow-data-transfer-speeds-and-issues-backup-plans

## Original Post
**Author:** Unknown

Acronins datacentre slow data transfer speeds and issues with backup plans?

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                
                    
                        
            The other day I noticed that there were a duplicate set of backups for a server and it turned it was caused from when I temporarily disabled the backup plugin. For some reason now, when you turn-off/disable the cPanel Acronis plugin within cPanel/WHM, it disconnects the backup plan. So when you turn-on/reenable the plugin, it looks to create a new backup plan and starts a fresh backup of the server. Can someone confirm if it is doing the same for them?
So last night I tried this guide to reconfigure the backup so it would resume the backup process (forum won't let me link to it).
 
And I see it is taking a very long time, i.e. increase 1% every 15-20 minutes. Never have I seen Acronis perform so slow.
 
03:11 PM • 52% completed • More than one hour left
Protection plan 'webcp'
Status:In progress
Device:snipped
Plan:webcp
Started by:snipped
Start time:Oct 30, 2020, 03:11:59 PM
Duration:3 hrs, 14 min
Bytes processed:264 GB
Bytes saved:42.7 GB
 
Also, this morning a backup didn't complete due to a network error
 
"Network connection failed due to timeout." but I doubt that was from OVH network end.
When Acronis works, it is speedy, but it doesn't work is very annoying, especially for the high price compared to other services.
 
I'm just glad I have backups from JetBackup in case...
 
Anyone else finding odd/strange issues from time to time with Acronis, especially when they release new agent updates, or is it just me?
 
I seem to spend a lot of time fighting with the software to get it to work nice for some Shared/Reseller hosting services, yet it works perfectly for some small VPS customers.
 
The usage seems off sometimes too.
 
Of course, when I try to correct the issue, and it starts a fresh backup it's just extra in storage all the time, and I've done it many times since I started using Acronis.
 
I hope Acronis improves at least with the cPanel/WHM plugin. Using Acronis on a stand-alone server seems to work fine, just not the cPanel/WHM plugin.
 
I feel like I'm paying for the software to test it and provide feedback and help fix bugs all the time.
 
That said, Acronis support is excellent! But I wouldn't need to pester them if the cPanel Acronis plugin worked properly in the first place!

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 11/03/2020 - 17:26

                                                          
                                                            
                                                                                        
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Are you backing up to Acronis Cloud or your own backup server?

      
                
                
                    
                                                    Tue, 11/03/2020 - 09:34
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            George_Fusioned wrote:

Are you backing up to Acronis Cloud or your own backup server?


This was to Acronis Backup Cloud. I think it was slow because it was trying to resume the backup but wasn't doing it right.
 
I started the backup from scratch and the speed was fine again. 

      
                
                
                    
                                                    Tue, 11/03/2020 - 09:39
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security
