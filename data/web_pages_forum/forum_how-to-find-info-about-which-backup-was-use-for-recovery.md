# How to find info about which backup was use for recovery

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/how-find-info-about-which-backup-was-use-recovery

## Original Post
**Author:** Unknown

How to find info about which backup was use for recovery

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Konica Minolta
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
I am wondering if there is any possibility to check info about the recovery point which was used. I am looking for a specific unique id, for a reverse check.
E.g.: there are 3 recovery points -  from 31/5/2021, 1/6/2021, and 2/6/2021. 1/6/2021 has been chosen. Once the recovery procedure is done, how I can check that 1/6/2021 was used/restored.

Thank you.
 
Jan.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 06/02/2021 - 08:19

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Jan,
if recovery is performed from the product's UI, you can download the related activity log from the Overview, which should contain the ID of the recovery point.
The command acrocmd list backups --loc=online:// --credentials= ,<password> --arc= --output=raw  shall list all recovery points in the archive with the respective IDs and timestamps, you can compare it against the output from activities.

      
                
                
                    
                                                    Thu, 06/03/2021 - 10:48
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Konica Minolta
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Ekaterina,
thanks for your answer. 
Seems to be reasonable.
But I have to ask, what do you exactly mean by activity log from the Overview?
What is the path, or where I should look for it?
Is this related to 'Collect system information'?
Thank you.

 

 
 

      
                
                
                    
                                                    Thu, 06/03/2021 - 12:14
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Good day,
So no collecting system information will collect information from the machine itself that is useful in the event that you need to troubleshoot a failure or error etc.
If you go to Dashboard > Activities > Search for the specific recovery that was done > Click on it > Then you will be able to view the properties of the recovery task
This includes the archive that was used, the ID, which used initiated the request etc
As Ekaterina has advised you will be able to also download the log from dashboard > overview
I hope this helps,
Regards

      
                
                
                    
                                                    Wed, 06/09/2021 - 09:10
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Konica Minolta
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
             Hello Jason,
thanks for the explanation. 
I just go through all of the information there and I was not able to find any related info.
I am able to find "ProtectionPlanID" involve in "context" but it is common information for all recovery points connected to a particular backup plan.
Below please find info options listed from dashboard activities and please navigate me, where exactly we should looking for.
Description: Protection plan 'AB' > Protection plan 'AB' > All properties

cancellable


cancelRequested


completedAt


context


enqueuedAt


executor


id


idString


issuer


policy


priority


progress


queue


resource


result


startedAt


startedByUser


state


tenant


type


updatedAt


uuid

Because I created 2 backups, and then I recovered the machine, I compared each info from all properties, but I was not able to find the unique ID of the recovery point.
Thank you
 
Jan.
 

      
                
                
                    
                                                    Wed, 06/09/2021 - 11:44
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Good day,
Will it be possible to share the activity via a screenshot or even via notepad? (Please just remember to remove any sensitive data such as machine names, usernames etc)
Then also please attempt to download a report from dashboard > Activities (Change range to the date that falls into the date of the recovery) and share the same info (Please also just remember to remove any sensitive information)
Regards

      
                
                
                    
                                                    Mon, 06/14/2021 - 08:20
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Konica Minolta
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Jason,
please check the print screen from Activities. I also uploaded details from the Protection plan and Recovering virtual machine (red frames). In case that you will need more details, please let me know what exactly needs to be collected.

About "download a report from dashboard > Activities (Change range to the date that falls into the date of the recovery)."
There is no such option for downloading any. I can just open particular case and check all properties (done and results are shared with you)
Once I choose info from the Protection plan and Recovering virtual machine details, there is no information about specific recovery points.
I am able to find info about backup ID, but that is common for all recovery points.
Please let me know where to look for it.
Thanks.
Jan.

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      580856-278145.txt

                      4.43 KB
                  
              
                      580856-278148.txt

                      1.46 KB
                  
              
                      580856-278151.txt

                      1.47 KB
                  
              
                      580856-278154.txt

                      1.51 KB
                  
              
                      580856-278157.txt

                      1.45 KB
                  
              
                      580856-278160.txt

                      1.48 KB
                  
              
                      580856-278163.txt

                      1.87 KB
                  
              
                      580856-278166.txt

                      1.47 KB
                  
              
                      580856-278169.txt

                      1.41 KB
                  
              
                      580856-278172.txt

                      1.41 KB
                  
              
                      580856-278175.txt

                      1.42 KB
                  
              
                      580856-278178.txt

                      1.55 KB
                  
              
                      580856-278181.txt

                      1.41 KB
                  
              
                      580856-278184.txt

                      1.58 KB
                  
          
    

                    
    
                
                
                    
                                                    Mon, 06/28/2021 - 11:10
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Georgi Dimitrov
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 10
                
            
            
                
                    Comments: 49
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Konica, 
Please open a case with the service provider support team in order to receive prompt assistance with this.

      
                
                
                    
                                                    Tue, 07/06/2021 - 09:10
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Georgi Dimitrov | Support Engineer

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Konica Minolta
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Georgi,
Thank you for the suggestion.
Unfortunately, I already did with the recommendation of asking here on the forum - Case ID: 04934620.
J.

      
                
                
                    
                                                    Mon, 07/12/2021 - 06:46
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Konica Minolta
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
Is there anyone who can help me solve this topic?
Thank you.
j.

      
                
                
                    
                                                    Tue, 08/24/2021 - 13:39
