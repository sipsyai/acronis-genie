# Acronis Solution for OT Network with No Internet Access

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/acronis-solution-ot-network-no-internet-access

## Original Post
**Author:** Unknown

Acronis Solution for OT Network with No Internet Access

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Germain Allotey-Pappoe
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi everyone,
We’re working with a customer who has a specific requirement for an in-house backup solution within an OT (Operational Technology) network that is completely air-gapped (no internet-facing devices).
We're considering Acronis Cyber Protect Cloud, but given the offline nature of the environment, we're unsure if it’s the right fit.
Our questions:

Would Cyber Protect Cloud work in such a setup, or is internet access required?


If not, is there a similar Acronis product designed for fully offline/on-prem environments?


If it is compatible, what are the necessary steps for deployment in this kind of setup?

Appreciate any insights or recommendations from those with experience in similar environments.
Thanks in advance!
— Germain Allotey

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 06/13/2025 - 11:05

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Welcome to the forum.
Acronis Cyber Protect Cloud requires an internet connection to run and connect to its services.
It cannot operate offline.
Best regards.

      
                
                
                    
                                                    Fri, 06/13/2025 - 11:39
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Germain Allotey-Pappoe
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi,
Is there any other tool within the Acronis range that would fit the usecase? Or i would have to look at alternatives.
 
Thanks so much!
 

      
                
                
                    
                                                    Fri, 06/13/2025 - 13:15
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Germain Allotey-Pappoe wrote:

Hi,
Is there any other tool within the Acronis range that would fit the usecase? Or i would have to look at alternatives.
 
Thanks so much!
 


Hello!
There is an option, but for this operation, you must use both the cloud and local consoles.
To access the cloud console, you’ll need a second machine connected to the Internet — so it's not 100% offline.
You can review the details here:
? Types of Management Servers – Acronis Cyber Protect 16
It’s also possible to execute backups using bootable media, but again, that setup isn’t fully offline either:
? How to back up with bootable media
You can request a trial and test it for yourself:
? Acronis Cyber Protect – Free Trial
If you have any questions, feel free to contact our sales department:
? Contact Acronis Sales
Best regards.

      
                
                
                    
                                                    Fri, 06/13/2025 - 14:05
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Roberto Novasconi
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            On June 13th 2025 Josè told that "Acronis Cyber Protect 16 ...cannot operate offline."
Maybe he meant that Acronis Cyber Protect Cloud cannot operate offline.
In the User Guide for Acronis Cyber Protect 16 here
https://www.acronis.com/en-us/support/documentation/AcronisCyberProtect…
the chapter "Offline on-premises management server" tells
"You can activate an offline management server and sync its licensing information to your Acronis account manually, through a file."
So it seems that we are able to manage an air-gapped environment, deployng both Managment Server and agent in the air gapped network, and activating the Management Server throught a file.
 
Am I right ?

      
                
                
                    
                                                    Thu, 09/04/2025 - 08:20
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Roberto Novasconi
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            On June 13th 2025 Josè told that "Acronis Cyber Protect 16 ...cannot operate offline."
Maybe he meant that Acronis Cyber Protect Cloud cannot operate offline.
In the User Guide for Acronis Cyber Protect 16 here
https://www.acronis.com/en-us/support/documentation/AcronisCyberProtect…
the chapter "Offline on-premises management server" tells
"You can activate an offline management server and sync its licensing information to your Acronis account manually, through a file."
So it seems that we are able to manage an air-gapped environment, deployng both Managment Server and agent in the air gapped network, and activating the Management Server throught a file.
Am I right ?

      
                
                
                    
                                                    Thu, 09/04/2025 - 08:27
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Roberto Novasconi wrote:

On June 13th 2025 Josè told that "Acronis Cyber Protect 16 ...cannot operate offline."
Maybe he meant that Acronis Cyber Protect Cloud cannot operate offline.
In the User Guide for Acronis Cyber Protect 16 here
https://www.acronis.com/en-us/support/documentation/AcronisCyberProtect…
the chapter "Offline on-premises management server" tells
"You can activate an offline management server and sync its licensing information to your Acronis account manually, through a file."
So it seems that we are able to manage an air-gapped environment, deployng both Managment Server and agent in the air gapped network, and activating the Management Server throught a file.
Am I right ?


Hello!
Actually, I was referring to Acronis Cyber Protect Cloud, as this thread is intended for that product. It always requires a network connection because the management service is hosted in the cloud.
Regarding Acronis Cyber Protect 16, it supports offline license activation through a file-based process. This involves generating a registration file on a machine with internet access and transferring it to the air-gapped machine for activation.
However, you still need a network connection for the backups to run and for the services to function. This solution was not designed for fully air-gapped environments. The closest option is performing a backup with bootable media, where a connection is only established when booting from the media.
Best regards,

      
                
                
                    
                                                    Thu, 09/04/2025 - 10:44
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
