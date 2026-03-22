# WHM Disaster recovery

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/whm-disaster-recovery

## Original Post
**Author:** Unknown

WHM Disaster recovery

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    James Fouracre
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 15
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi I have a few questions regarding a WHM cPanel restore regarding a major failure. 
 
1. The current server fails, we will call it Cloud01. We have another server, Cloud02 which is fine in another datacentre. How could we restore the accounts only from Cloud01 to Cloud02 within WHM using Acronis??
2. The server fails and a new one needs to be rebuilt. We will keep the same hostname, but new IP'S would be provided. Do we need to reinstall cpanel / WHM and then install acronis to restore the accounts only? also how can we select the correct backups to restore??
or as an alternative, can we just install the same cenos version and perform a full restore?
 
Thanks 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 01/17/2019 - 14:21

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Michael Brunner
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 21
                
            
            
                
                    Comments: 33
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            As a cpanel hoster I can tell you, that we have done option 2 a few times. You don't need to install anything on the new server, just configure the hardware raid, if needed and then boot with the acronis boot media. Afterwards you can configure the network settings in the gui and connect to the acronis cloud. There you can choose the server you want to restore and the date. 
The restore worked very well for us, we always had a bootable server at the end.
Regarding option 1, I don't think this is possible.
Regards
Michael
 

      
                
                
                    
                                                    Thu, 01/17/2019 - 15:08
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    James Fouracre
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 15
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Michael, 
 
Thanks for your help. We use VPS's is there a way to use the boot media with a VPS?
 
Many Thanks
James

      
                
                
                    
                                                    Thu, 01/17/2019 - 15:14
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Michael Brunner
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 21
                
            
            
                
                    Comments: 33
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Which VPS hypervisor are you using? If you use vmware or kvm, you can boot with an iso.  
Regards
Michael

      
                
                
                    
                                                    Thu, 01/17/2019 - 15:18
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    James Fouracre
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 15
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            yes we are using kvm. 
do you have a link to the iso please?
also if we just setup the vps as normal, can we re install acronis and restore the accounts only?
 
Many Thanks
James

      
                
                
                    
                                                    Thu, 01/17/2019 - 15:20
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Michael Brunner
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 21
                
            
            
                
                    Comments: 33
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi James
Just login to cloud.acronis.com and select the server you want to recover, click on the right side on "Recovery" and then on "More ways to recover". There you can download a ISO Image.
I'm not aware of any option to restore only cpanel accounts without the OS. 
Michael

      
                
                
                    
                                                    Thu, 01/17/2019 - 15:36
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    James Fouracre
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 15
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Michael, 
I was thinking reinstalling cpanel and the system as we need it. Then if there was a way to reinstall acronis and then log back in to acronis, select our server and then restore accounts. 
Many Thanks
James

      
                
                
                    
                                                    Thu, 01/17/2019 - 15:38
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Michael Brunner
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 21
                
            
            
                
                    Comments: 33
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi James
As far as I know this is not possible. 
Michael

      
                
                
                    
                                                    Thu, 01/17/2019 - 15:42
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    James Fouracre
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 15
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Oh :( :(
Do you think this is a feature we could request please? as that would be really good. 
 
I think It is sort of implimented already with normal windows desktop when restoring folders and files. 

      
                
                
                    
                                                    Thu, 01/17/2019 - 15:44
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Michael Brunner
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 21
                
            
            
                
                    Comments: 33
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi James
I'm only a customer and not working for acronis. Maybe someone from acronis team will answer this.
Michael

      
                
                
                    
                                                    Thu, 01/17/2019 - 15:48
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            James and Michael, hello to you two.
Michael, thanks for pitching in and sharing your expertise.
James, may I ask you to elaborate on the desired scenario - the feature that you'd like to implement?
Please describe what you have at the start, what you wish to achieve and how you think it's best to achieve it and why you think it's the best way?

      
                
                
                    
                                                    Fri, 01/18/2019 - 22:08
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    James Fouracre
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 15
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi, 
We currently use JetBackup and are looking for a long time replacement. We already use your Acronis service for our clients on their windows desktops so it makes sense to use Acronis.
Going back to cPanel / WHM. What we would like to do is to do:
Ideally we would like the ability to restore the 'cPanel accounts only' after the server has been put back online after a disaster. 
For example; If we backup a server with Acronis and its running fine for a long time, lets call it Cloud01. 
Cloud01 suffers a major failure and our data centre can't repair the server. A new one is deployed, but it is different specification etc, it may need to be with a new provider.
What I would like is to load WHM / cPanel back on to the server using the normal WHM / cPanel install.
Then once cPanel is installed, allow us to install the Acronis module.
Once the Acronis module is installed allow the module to select a previous server from our cloud data store and allow us to restore our cPanel accounts back on to the server. You could maybe give the option from loading the module, if you need to perform a disaster restore or a new backup set.
After the restore, you could also allow the server to remember the backup set, so it doesn't need to perform a full backup and can continue where the old ones left off.
On another note:
In an ideal world it would be great it you could select different server backups from the cloud if one server failed, you could quickly restore the cpanel accounts to another server.
I think these are pretty standard operations with the way cPanel tends to work and performing restores. I realise that full server restores are going to be quicker using the Acronis media, but data centres have different options on what you can do. Also a lot of people like to do a fresh install of cPanel and restore the accounts afterwards. I wanted to try and make it easier for many people and give multiple options for restores. 
I would really love this feature and I think others would as well. 
 
 

      
                
                
                    
                                                    Fri, 01/18/2019 - 22:18
