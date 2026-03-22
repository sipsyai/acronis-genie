# Recovery to New VMWare Virtual Machine not possible, OK button is grayed out

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/recovery-new-vmware-virtual-machine-not-possible-ok-button-grayed-out

## Original Post
**Author:** Unknown

Recovery to New VMWare Virtual Machine not possible, OK button is grayed out

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Antonios Throuvalas
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
I tried to recover a backup to a new VMWare Machine, but the recovery cannot be started because the OK button is grayed out, see attached screenshot. I followed the steps below:
* Selected the device to recover,
* Clicked Recovery and selected Recover Entire Machine
* Clicked on the Target machine
* Selected VMWare ESXi
* New Machine
* Entered the machine name
* The OK button remained grayed out, I can only cancel the process.
A WMWare Agent is installed and registered.
Any ideas what is going wrong?
Thank you very much in advance.
Regards,
Antonios
 

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      2016-10-27_08-26-32.jpg

                      99.29 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Thu, 10/27/2016 - 06:36

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Antonios,
Thanks for posting your question here.
Recover to new VM feature requires you to have an agent that is managing a hypervisor, so it can create a new VM on that server. If you cannot see a host, it means you don't have any online Agent for VMware installed by this user.
Please see attached an example of how it should look like when an Agent for VMware is available and is connected to an ESXi server.
Please let me know if this answers your question or provide more details on whether you Agent for VMware can otherwise correctly perform VM backup/recovery operations, but still no ESXi host appears in this recovery screen.
Best regards,

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      396603-134623.png

                      14.3 KB
                  
          
    

                    
    
                
                
                    
                                                    Thu, 10/27/2016 - 06:53
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Wim Vermunt
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi,
Do you install this agent on the hyperisor itself or on the backed up server?
Where can I download the client?
Thx!
Best regards

      
                
                
                    
                                                    Mon, 03/20/2017 - 21:08
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Wim,
The Agent installation depends on the type of the agent. Agent for VMware should be installed on any Windows machine which has network connection to the ESXi server and datastore to which recovery will be performed. Read more about installation options in the user guide.
Download links for the Agents in Acronis Backup Cloud are availabe in the Backup Management Console with the Add button, or via the User icon > Downloads in the top right hand corner of the bowrser screen.
Let me know if you have additional questions.
Best regards,

      
                
                
                    
                                                    Wed, 03/22/2017 - 08:41
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.
