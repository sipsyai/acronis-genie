# Questions about VPN for disaster recovery

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/questions-about-vpn-disaster-recovery

## Original Post
**Author:** Unknown

Questions about VPN for disaster recovery

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Fabio Fantoni
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi, I did some tests for disaster recovery using the vpn appliance for site to site and worked in easy and fast way with minimal manual operations required.
someone specified that not in all situations the one could be used due to lack of virtualization systems on some customers and others with multiple locations with different subnets and also want necessarily a only one solution for all cases
I suppose that appliance as linux vm I already started also in kvm without issue can be used also used on any phisical device with x86 archs (with a dd of the disk image before converted to raw) even if I stil not tried it
I suppose can be used ipsec for the multisite as documented (even if still not tried), but they tell me that they are not feasible in any case and that the setup would be "delirious"
I was forced instead to use zerotier as a solution and attempt an elaborate the better solution to switch all active directory dns to zerotier for the case we have to start some customers into disaster recovery
I had some issue on zerotier itself, largely temporary (I suppose probably mainly caused by use of symmetric nat and double nat) and many additional operations to do in dns servers of domain controllers and issue also relating to this, not counting the devices that do not support zerotier and various scattered local ip link (where on the contrary with acronis vpn appliance I had no problem)
they keep telling me anyway that the best method to configure with zerotier must be found and use zerotier instead acronis vpn and "there are many people that use in production as it would be for us"
---
So i would like to ask a few questions:
Has anyone had problems using acronis vpn for disaster recovery and used zerotier instead with good result?
Has anyone had situations of serious produrection use (and not just for testing) of disaster recovery with acronis vpn and maybe even in particular or large situations and can you tell me how you found good (or not) them?
Thanks for any reply and sorry for my bad english.
---
Small out of topic: today I tried some searchs on acronis forum but always did no result (even if it should give instead), time ago if I remember good was working, is only a temp. issue?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 05/23/2023 - 10:21

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Fabio!
We have raised a ticket in order to provide you appropriate support and answer to the situation you just tested ( 05904983 ).
You can expect an email from our side.
Thanks in advance!

      
                
                
                    
                                                    Tue, 05/23/2023 - 11:17
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fabio Fantoni
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            thanks for the answer and sorry for my bad english, I was looking for more experiences from other users, in the tests I made using the acronis appliance for site-site connection went well and much better than the attempts with zerotier to use everything on that when switching to disaster recovery.
I wanted to understand if it made sense to switch all to zerotier (when start one or more device in disaster recovery) instead of use acronis vpns and my tests weren't representative enough and/or my current evaluations were wrong

      
                
                
                    
                                                    Tue, 05/23/2023 - 15:56
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Fabio Fantoni wrote:

thanks for the answer and sorry for my bad english, I was looking for more experiences from other users, in the tests I made using the acronis appliance for site-site connection went well and much better than the attempts with zerotier to use everything on that when switching to disaster recovery.
I wanted to understand if it made sense to switch all to zerotier (when start one or more device in disaster recovery) instead of use acronis vpns and my tests weren't representative enough and/or my current evaluations were wrong


Hello Fabio.
We sent you an email on the 23th of May ( in Italian ). Please check it and let us know if that clarified your doubts. If you have any questions, please reply to the email since our team is waiting the answer.
Thanks! 

      
                
                
                    
                                                    Thu, 05/25/2023 - 11:41
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
