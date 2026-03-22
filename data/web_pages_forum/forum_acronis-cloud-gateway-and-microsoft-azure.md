# Acronis Cloud Gateway and Microsoft Azure

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/acronis-cloud-gateway-and-microsoft-azure

## Original Post
**Author:** Unknown

Acronis Cloud Gateway and Microsoft Azure

        
  



    
  


  
          






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    marcelovvm
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Dear friends,, we are looking at the cloud backup solution, Acronis Cloud Gateway, to backup our (~ 8.5TB) data from our company. We will use the Acronis Cloud Gateway with Microsoft's Azure Storage service, however we are in doubt about the type of service being hired, File, Disk or Blob?
Live long and prosper,
Marcelo Magalhães 

      
                                            
                
            
                            
                    
                        
                            
                              Sat, 08/12/2017 - 03:34

                                                          
                                                            
                                                                                        
    
                    
                Live lona and prosper

            
                    
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Marcelo,
Welcome to Acronis community! You'll need to set Blob as the Access type. Open a picture in a new tab to see full resolution.


      
                
                
                    
                                                    Wed, 08/16/2017 - 12:39
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                            
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    marcelovvm
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Ekaterina,
     Ok. But inside de blob I create a VHD file to "represent the disk"... that is right? I was able to mount and format this drive on the Acronis Storage Gateway VM. And I've already changed the /etc/Acronis/acronis-storage-backend-azure.xml file to reflect these changes.
<AzureSettings>
  <UserSettings>
    <HomePath>/mnt/backup</ HomePath>
  </ UserSettings>
  <Endpoint>
    <Account> acronisstoragebackup </ Account> <AccessKey> eQyCZn + soid / 9nKisT7ABLiOutf6XxytK1UIbV + 9D5o0G + OOIcuHdKUh / APUjJ4 + weNHISBy0AF6g5GjCYrlRA == </ AccessKey>
  </ Endpoint>
</ AzureSettings>

 

      
                
                
                    
                                                    Wed, 08/16/2017 - 23:11
                                                                            
                                
                            
                                            
                                            
    
                    
                Live lona and prosper

            
                    
                                                                            
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you for your reply! You don't need to make further adjustments. Once you have a container at Azure, specify it in the configuration file  /etc/Acronis/acronis-storage-gateway.xml and Acronis Storage Gateway will adjust the target location to store Acronis archives. 

      
                
                
                    
                                                    Fri, 08/18/2017 - 13:21
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                            
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    marcelovvm
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Ekaterina,
     Now I was confused! If I do not create the disk inside the blob container, I will not be able to mount this disk inside de VM... because the disk does not exist (only the blob container). So how will I configure /etc/Acronis/acronis-storage-backend-azure.xml to put the blob container path?
Live long and prosper,
Marcelo Magalhães

      
                
                
                    
                                                    Fri, 08/18/2017 - 16:36
                                                                            
                                
                            
                                            
                                            
    
                    
                Live lona and prosper
