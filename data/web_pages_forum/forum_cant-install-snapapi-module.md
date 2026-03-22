# Can't install SnapAPI Module

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/cant-install-snapapi-module

## Original Post
**Author:** Unknown

Can't install SnapAPI Module

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Alexandre Chaillet
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
I am trying to install a Cyber Protect Agent on a debian 11 server but i am blocked at the installation step. The Installation software is telling me that he can't install the snapapi26 file module. I tried to follow your steps on the documentation and tried with 2 other kernels version, reinstalled the kernel headers and image packages without any success.
Here is the tutoriel i followed on my computer : https://kb.acronis.com/content/67148
I'm receiving this message when i'm trying to install the agent : 
Failed to build the SnapAPI kernel module. Operations with disk-level backups will not be available.
Is it possible to confirm if Debian 11 is compatible with Acronis CyberProtect ?
Alexandre Chaillet

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 05/05/2022 - 12:46

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Georgi Dimitrov
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 10
                
            
            
                
                    Comments: 49
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Alexandre
This appears to be unexpected behavior of the product. 
Please open a case with our support team so that an investigation can be performed and we will be able to provide a resolution.

      
                
                
                    
                                                    Mon, 05/23/2022 - 09:26
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Georgi Dimitrov | Support Engineer

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hey Alexandre Chaillet
Did you ever got this resolved?

      
                
                
                    
                                                    Mon, 07/04/2022 - 14:28
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            What do you get if you run:
dkms {build,install} -m snapapi26 -v 0.8.12
?
 

      
                
                
                    
                                                    Fri, 07/15/2022 - 15:42
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daria Sorokina
                            

                            
                    
                        Acronis Support
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 487
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dear Alexandre Chaillet,
Please let us know was your problem that you presented here resolved if yes, what helped you?

      
                
                
                    
                                                    Tue, 09/27/2022 - 22:13
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards, Daria Sorokina | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Alexandre Chaillet
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
Sorry i didn't take the time to answer, the problem happenened a few months ago but i wasn't able to fix it so i just reinstalled everything on a new server with a different kernel configuration.
Have a nice day,
Alexandre Chaillet

      
                
                
                    
                                                    Fri, 09/30/2022 - 14:58
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daria Sorokina
                            

                            
                    
                        Acronis Support
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 487
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dear Alexandre Chaillet,
Thank you very much for the answer!

      
                
                
                    
                                                    Wed, 10/05/2022 - 12:54
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards, Daria Sorokina | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
