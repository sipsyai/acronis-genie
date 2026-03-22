# VMware backup - VPS environment

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/vmware-backup-vps-environment

## Original Post
**Author:** Unknown

VMware backup - VPS environment

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Julien Rick
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
I'm evaluating Acronis Cloud Backup and the product looks great but I can't find how to proceed with our VPS infrastructure.
We have a VMware infrastructure with many customers VPS and want to backup these VMs with Acronis Cloud Backup. All these VPS runs in the same vCenter Server, idealy customer should be able to restore his files/VMs and application items by himself (in-place for the VM)
What I did :
- Create a new Customer
- Create a new unit per Customer
- Add the vCenter Server at the Customer level
 
Is it possible to assign VMs to units ?
How to proceed for a case like our ?
 
Thanks for your help,
Julien

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 02/20/2019 - 15:11

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Julien, hello!
 
Thanks for posting!
As I understood, you are providing your customers with virtual machines that you host yourself and seek options to protect those machine by Acronis Backup Cloud.
 
I gather that you use the Agent for VMware or a VMware appliance to populate the Backup Console with the VMs.
Using that approach you can't split the VMs between the untis (Unit-level tenant in the Management Console).
 
What I can suggest is to install the agents for Windows directly inside the VMs and register them to the respective user-level tenants in the Units.
 
Depending on how things are set up you can use different methods to push the agents down inside each VM, for example via Policy rules -> https://www.acronis.com/en-us/support/documentation/BackupService/index…
Also another method described here -> https://kb.acronis.com/content/57107
 
We do have some ideas to allow splitting the VMs hosted by a single vCenter nto different units, but this is still beyond the horizon for now.
 
Let me know if you have any further questions!

      
                
                
                    
                                                    Thu, 02/21/2019 - 18:53
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Joe Tucker
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 31
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            If you are providing your customers with virtual machines that you host yourself and seek options to protect those machine by Acronis Backup Cloud I would recommend you to install windows vps server.

      
                
                
                    
                                                    Mon, 08/02/2021 - 15:17
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Charley Strighan
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hey! Thanks for posting

      
                
                
                    
                                                    Mon, 08/02/2021 - 15:18
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jessica Cheng
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I believe that the main responsibilities of the company that sells hosting to you should include helping customers with hot communication, and fast service.

      
                
                
                    
                                                    Sat, 10/23/2021 - 06:02
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Jessica Cheng wrote:

I believe that the main responsibilities of the company that sells hosting to you should include helping customers with hot communication, and fast service.


Hi Jessica,
do you experience any issues with Acronis products? Please share more details. We'd be happy to help! 

      
                
                
                    
                                                    Sun, 10/24/2021 - 20:45
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
