# CloudLinux - Full support? Ubuntu 22.04?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/cloudlinux-full-support-ubuntu-2204

## Original Post
**Author:** Unknown

CloudLinux - Full support? Ubuntu 22.04?

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Karl Austin
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 7
                
            
            
                
                    Comments: 15
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
 
Are there any plans to properly and fully support CloudLinux?  A great number of service providers who run cPanel and Plesk, use CloudLinux for increased security and isolated between users.
Whilst backups work fine, Disaster Recovery does not support CloudLinux despite supporting CentOS and RHEL which is what CloudLinux is derived from.
The same applies with Ubuntu 22.04, no support for DR right now.
The documentation says:
The software may work with other Windows operating systems and Linux distributions, but this is not guaranteed.

But this does not appear to be true, because unless you're on a supported OS the Disaster Recovery option doesn't even show as available on a Protection Plan.
Thanks,
Karl

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 04/26/2023 - 09:29

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Karl.
There is a feature request to support those OS ( the code is CI-7056 ).
We have informed the team regarding your request.
You can monitor our page with updates ( https://www.acronis.com/en-us/support/updates/ ) or contact our support if you need to know what's the status of the requests https://kb.acronis.com/content/8153 .
Thanks in advance!

      
                
                
                    
                                                    Wed, 04/26/2023 - 09:47
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Karl Austin
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 7
                
            
            
                
                    Comments: 15
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Jose,
Is that definitely for the Advanced Disaster Recovery? I can see recently the OS list for the backup side was updated for them both.
Thanks for the quick reply :)
Karl

      
                
                
                    
                                                    Wed, 04/26/2023 - 10:18
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Karl Austin wrote:

Hi Jose,
Is that definitely for the Advanced Disaster Recovery? I can see recently the OS list for the backup side was updated for them both.
Thanks for the quick reply :)
Karl


Hello Karl, thank you for your response and observation.
I have received new information that the feature request was only for backups (not for DR) and that it is currently inactive.
I am submitting a request to obtain more information and to determine if a new feature request can be created.
I will update this thread as soon as I receive more information.
Thank you!

      
                
                
                    
                                                    Wed, 04/26/2023 - 11:36
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Karl Austin wrote:

Hi Jose,
Is that definitely for the Advanced Disaster Recovery? I can see recently the OS list for the backup side was updated for them both.
Thanks for the quick reply :)
Karl


Hello Karl.
I have the new feature requests for DR.
 
Disaster recovery support for workloads with Ubuntu Linux versions 22.04 - RM-7254
Disaster recovery support for workloads with Cloud Linux CloudLinux - RM-7255
So far there is no ETA for the implementation but I voted for you so hopefully we can implement it in the near future.
Let me know if you have any questions.
Thanks in advance!

      
                
                
                    
                                                    Wed, 04/26/2023 - 14:56
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
