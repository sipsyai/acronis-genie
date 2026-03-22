# Create cpmove files

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/create-cpmove-files

## Original Post
**Author:** Unknown

Create cpmove files 

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    James Fouracre
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 15
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi There,
i read on another forum that when using the Acronis plugin on WHM / cPanel that it may be possible to create cpmove files directly within the Acronis cloud, is this correct? 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 02/15/2019 - 23:46

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
Check out section 9.12 here: http://dl.acronis.com/u/pdf/Acronis_Backup_plugin_for_cPanel_en-US.pdf
It's probably what you're looking for.
-G.

      
                
                
                    
                                                    Sat, 02/16/2019 - 23:44
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Michael Brunner
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 21
                
            
            
                
                    Comments: 33
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi
If I understand this concept correct, the cpmove file is generated on the WHM server and not in the cloud. So I don't think you can use this feature the restore a full server with cpmove files.
Regards
Michael

      
                
                
                    
                                                    Mon, 02/18/2019 - 15:09
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Michael Brunner
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 21
                
            
            
                
                    Comments: 33
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I just tried to restore such a cpmove file, it did not work that well. The DNS zone was missing, the apache configuration was not done, the wrong ip was assigned and the mysql users where missing.
Did someone else test this? 
Michael

      
                
                
                    
                                                    Wed, 02/20/2019 - 08:15
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Michael Brunner wrote:

I just tried to restore such a cpmove file, it did not work that well. The DNS zone was missing, the apache configuration was not done, the wrong ip was assigned and the mysql users where missing.
Did someone else test this? 
Michael


When I tested it some time ago it worked.
What I think Acronis should add is a way for the customer to generate cpmove backups directly on the backup server which would be useful if one had an issue with the live server running the websites. Then if the backup server is large enough could just generate all the cPanel backups on the storage server and rsync them to a new server and restore the cPanel accounts that way.

      
                
                
                    
                                                    Thu, 12/12/2019 - 15:07
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I'm using this script from the old R1Soft days to generate cpmove files of all accounts on a server every week. It uses the -skiphomedir flag, so the cpmove file only includes the actual account, emails, passwords and databases. Everything in public_html can then be restored via simple File Restore from within Acronis.
http://wiki.r1soft.com/pages/viewpage.action?pageId=16318627

      
                
                
                    
                                                    Thu, 12/12/2019 - 15:44
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            George_Fusioned wrote:

I'm using this script from the old R1Soft days to generate cpmove files of all accounts on a server every week. It uses the -skiphomedir flag, so the cpmove file only includes the actual account, emails, passwords and databases. Everything in public_html can then be restored via simple File Restore from within Acronis.
http://wiki.r1soft.com/pages/viewpage.action?pageId=163186278


What I mean is when use Acronis and backup the data to own backup storage server, the data is in a single file. It would be good if we could extract/create cPanel accounts directly from the file/server.
I don't mean create accounts directly on the cPanel server itself. Could use default cPanel backup system for that.

      
                
                
                    
                                                    Thu, 12/12/2019 - 18:59
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security
