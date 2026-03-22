# Open ports Acronis Linux Agent

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/open-ports-acronis-linux-agent

## Original Post
**Author:** Unknown

Open ports Acronis Linux Agent 

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    DominikD
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Dear Acronis Team,
i thought the Acronis Agents only does outgoing connections and does not open any incoming public ports. 
But after updating to the newest agent (12.5.10170) there are now 3 open ports on our machines in listen state and bound to every ip on the system:
tcp 0 0 0.0.0.0:9850 0.0.0.0:* LISTEN 24115/mms
tcp 0 0 0.0.0.0:43234 0.0.0.0:* LISTEN 24115/mms
tcp6 0 0 :::9876 :::* LISTEN 24189/acronisagent
Can you please check why these ports are now permanently open on public system ips?
Greetings,
Dominik

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 06/22/2018 - 10:16

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Backup Cloud

            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Dominik,
Sorry for the delayed response! The ports 9876, 9850 and 43234 should not be open. It's a known issue that is planned to be permanently fixed in Acronis Data Cloud 7.8. Meanwhile, the ports can be safely blocked.
Thank you, 

      
                
                
                    
                                                    Wed, 07/18/2018 - 09:19
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    DominikD
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I just tried blocking these 3 ports by a iptables rule. But now the backup is failing with a socket error. Can you please help what is wrong here?
I use the following iptables rule:
iptables -I INPUT -p tcp -m tcp -s 0.0.0.0/0 -m multiport --dports 9876,9850,43234 -j REJECT --reject-with tcp-reset
 

      
                
                
                    
                                                    Sun, 08/12/2018 - 18:29
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Backup Cloud

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello, Dominik!
 
These ports were merged as part of the code from the on-premise branch of Acronis Backup family of products.
Current agent require these ports to be open.
 
We will fix this in upcoming 7.8 and add that info to the documentation.
 
Hope that covers it!

      
                
                
                    
                                                    Thu, 08/16/2018 - 08:13
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    DominikD
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Is there a documentation for which IP addresses those ports need to be open? We can not fully open them up.
In our ticket your support said that we can completely close them, but as you wrote, that does not work. :(

      
                
                
                    
                                                    Mon, 08/20/2018 - 13:08
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Backup Cloud

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello DominikD,
Could you please share the ID of the related support ticket? 

      
                
                
                    
                                                    Mon, 08/27/2018 - 10:10
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    DominikD
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dear Ekaterina,
we have access to a 7.8 beta and the problem is solved there. The ports are bound to localhost and not open towards internet anymore.
But we have another problem. During every backup the "service_process" opens a totally random port towards internet. Here the netstat output from two different backup runs:
tcp        0      0 0.0.0.0:37019           0.0.0.0:*               LISTEN      6563/service_proces
tcp        0      0 0.0.0.0:40159           0.0.0.0:*               LISTEN      6883/service_proces
 
With our open port monitoring we get a notification during every single backup because a port is opened to public internet. Would it be possible for your development to also bind this random port (which is only open during backup) to localhost?

      
                
                
                    
                                                    Wed, 08/29/2018 - 09:53
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Backup Cloud
