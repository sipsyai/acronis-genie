# How to continue backing up server to old backup after reinstall of agent

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/how-continue-backing-server-old-backup-after-reinstall-agent

## Original Post
**Author:** Unknown

How to continue backing up server to old backup after reinstall of agent

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                
                    
                        
            Hi,
How to continue backing up server to old backup after reinstalling of the agent? There was trouble with Acronis not working and I uninstalled the agent by also "Clearing all product traces". When I reinstalled the agent it creates a new set of backups, but I want it to use the existing backup.
I read some articles and tried many different things but couldn't find how to correct it.
I know the old entries of the backup are
Last backup:
Nov 20, 2019, 07:23
server-name-snipped-FDC7298C-9720-4F92-A43C-56F00104EFE9-E18086CF-4284-47DB-B96C-32A2D9DA6093A
How do I get the agent to connect using that backup set above so I can restore data from it using the WHM plugin?
Regards,
Chris

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 12/11/2019 - 11:37

                                                          
                                                            
                                                                                        
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Have you tried this? https://kb.acronis.com/content/56493

      
                
                
                    
                                                    Wed, 12/11/2019 - 14:23
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I tried it for a different server I had the issue on. Obviously I must be doing it wrong. But the instructions are not easy to follow.
 
I have custom URL acronis.hostxnow.com not like
https://kb.acronis.com/system/files/content/2016/02/57601/57601-01a.png
 
I guess I need the correct MMSCurrentMachineID and InstanceID to the original ones and then update the config file
 
In Linux: open /etc/Acronis/BackupAndRecovery.config and modify these values:
     <value name="InstanceID" type="TString">
                                "<insert_value_noted_in_step1>"
                        </value>
                        <value name="MMSCurrentMachineID" type="TString">
                                "<insert_value_noted_in_step1>"
                        </value>
 
and then go to WHM plugin and connect the account back to the Web Console account? I'll try to find original MMSCurrentMachineID and InstanceID from the console but not having much luck with the above guide and the method it says to use.
 
I did have an email from Acronis support but it is very lengthy and numbers all over the place, so don't think I'm entering the correct numbers for a start.
 
Easier if they just add the option in GUI to select which backup set you to want to use.
 
Also, I have the same issue on a different server regarding that ticket from yesterday in the thread you created. Not sure why it now says "There are no backups yet. The next backup is scheduled at 12 Dec 2019 04:18" because I'm sure I didn't reinstall the agent.
Might have to switch back to the much slower JetBackup at this rate.

      
                
                
                    
                                                    Wed, 12/11/2019 - 14:50
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            HostXNow wrote:

Also, I have the same issue on a different server regarding that ticket from yesterday in the thread you created. Not sure why it now says "There are no backups yet. The next backup is scheduled at 12 Dec 2019 04:18" because I'm sure I didn't reinstall the agent.
Might have to switch back to the much slower JetBackup at this rate.


That seems to be working after trying it the second time but guess it should not be doing that and maybe timeout needs to be increased as mentioned at https://forum.acronis.com/comment/523741#comment-523741
 
Still checking that issue.
Back to the original question/issue for a different server in the first post of this ticket... So I now got the correct MMSCurrentMachineID and InstanceID of the backup from the date I want to use but not sure what else I am supposed to do to get the Acronis backup to use the older set of backups?
Do I do the following:
1. make sure the agent is first uninstalled from the server
yum -y remove acronis-backup-cpanel
2. /usr/lib/Acronis/BackupAndRecovery/uninstall/uninstall
3. #2 plus select the box for "Clear all traces of the product" or just #2 only?
4. wget -N https://download.acronis.com/ci/cpanel/stable/install_acronis_cpanel.sh
sh install_acronis_cpanel.sh
5. replace instanceid and mmscurrentmachineid with the ones I got from the backup console in /etc/Acronis/BackupAndRecovery.config and save the file.
6. Go to the WHM plugin and enter username and password of the account I want it to connect to
 
Then it should show the old backup set that I want? Sure I've tried that a few times already with no success. 
Hope Acronis can see how confusing that part is and should be an option in GUI for it to speed things up/make it more clear.

      
                
                
                    
                                                    Wed, 12/11/2019 - 17:53
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Couldn't get it to work. Luckily, it only affected the one server and as no backups were needed I reconfigured Acronis and now it is fine.
 
It would be good to know in advance how to do it in case it happens again. Reply from Acronis and Resellers are not always fast depending on timezone which could cause a lot of problems for someone who really needed to link old backup set back to the existing server to restore some data and to continue backing up to it.
 
Please add an option in Acronis to simply allow the administrator to assign a set of backups to a machine with a few clicks here and there. Much easier than trying to get it to work from these guides
https://kb.acronis.com/content/56493
https://kb.acronis.com/content/55244
 
Either they are not written very good or the info there just doesn't work.
 
Hope my feedback helps improve Acronis.

      
                
                
                    
                                                    Thu, 12/12/2019 - 14:48
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Reply from Acronis Reseller:
The KB you linked to should walk you right through the process. https://kb.acronis.com/content/56493
What step of this are you having trouble with?
Acronis will be adding the ability to link protected devices to archives in the future but we do not have a ETA on this
######
I tried that but couldn't get it to work.
Could someone do a video of how it should be done?

      
                
                
                    
                                                    Fri, 12/13/2019 - 03:15
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello HostXNow
I've also found the following article 60276: Acronis Backup Cloud: how to continue backing up to an existing archive with a new backup plan, which might be helpful (sorry if it was already referenced)

      
                
                
                    
                                                    Mon, 12/23/2019 - 09:31
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
