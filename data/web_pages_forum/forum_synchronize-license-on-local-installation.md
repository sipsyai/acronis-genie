# synchronize license on local installation

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/synchronize-license-local-installation

## Original Post
**Author:** Unknown

synchronize license on local installation

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Christian Wurst
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi, i'm trying to sync my licences to local installation. problem is, that in my case there is a proxy between management server (also license server) and internet. i set up proxy setting on installation, but i can't access from local installation. is there any solution? 
also which ports do the local installation need to communicate with cloud-console?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 07/17/2017 - 15:05

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Christian
Please ensure that the following ports are open (With a description of what the ports are used for):
443 and 8443 These ports are used for accessing the backup console, registering the agents, downloading the certificates, user authorization, and downloading files from the cloud storage 
 7770...7800 The agents use these ports to communicate with the backup management server
44445 The agents use this port for data transfer during backup and recovery 
80 Web-triggered update uses this port to download installation packages 
Then on Backup Advanced the port 55556 is also used for registration
I hope this resolves your issue.
Regards

      
                
                
                    
                                                    Tue, 07/18/2017 - 06:20
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
                    In reply to Hi Christian… by Jays
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Christian Wurst
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Jays, thanks for this, but i need some more informations.
which destination do i have to allow in my firewalls for Cloud? i will not open this ports with an any rule...
 
also, how about proxy? can i configure or modify an config-file with proxy-settings?

      
                
                
                    
                                                    Tue, 07/18/2017 - 06:29
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Christian,
Can you please advise to which product you are using?
Regards

      
                
                
                    
                                                    Tue, 07/18/2017 - 06:35
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
                    In reply to Hi Christian,… by Jays
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Christian Wurst
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Acronis Backup Advanced 12.5 on a dedicated backup server which has to backup some Hyper-V servers, Exchange, Active Directory, SQL and so one

      
                
                
                    
                                                    Tue, 07/18/2017 - 06:36
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Christian,
And what firewall do you use? Some of the more advanced firewalls such as Sophos etc have a different proxy configuration than for example to older SonicWall etc.
Regards

      
                
                
                    
                                                    Tue, 07/18/2017 - 09:29
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
                    In reply to Hi Christian,… by Jays
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Christian Wurst
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi,
 
Firewall is not the problem... i need to configure a proxy in acronis, so the software can access to internet and acronis cloud. at the moment, i've to whitelist the hole server and this is in my case a security issue.
 
anybody there who knows how to configure proxy in acronis?

      
                
                
                    
                                                    Tue, 07/18/2017 - 12:59
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Christian
To configure a proxy server you will need to perform the following:
1. Create a new text document and open it in a text editor, such as Notepad.
2. Copy and paste the following lines into the file:
Windows Registry Editor Version 5.00
[HKEY_LOCAL_MACHINE\SOFTWARE\Acronis\Global\HttpProxy]
"Enabled"=dword:00000001
"Host"="proxy.company.com"
"Port"=dword:000001bb
3. Replace proxy.company.com with your proxy server host name/IP address, and 000001bb
with the hexadecimal value of the port number. For example, 000001bb is port 443.
4. Save the document as proxy.reg.
5. Run the file as an administrator.
6. Confirm that you want to edit the Windows registry.
7. If the backup agent is not installed yet, you can now install it. Otherwise, do the following to
restart the agent:
a. In the Start menu, click Run, and then type: cmd
b. Click OK.
c. Run the following commands:
net stop mms
net start mms
And then to add the proxy within the management console you use the option "Cloud backup proxy" which will ask you for the usual "Address,Port,Username and Password"
I hope this resolves your issue.
Regards

      
                
                
                    
                                                    Wed, 07/19/2017 - 11:06
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
                    In reply to Hi Christian… by Jays
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Christian Wurst
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Jays, it's not working. Acronis does not send any paket to proxy... 

      
                
                
                    
                                                    Thu, 07/20/2017 - 11:07
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            HI Christian,
I would then recommend that you log a call with the Acronis support team to assist you with this case.
Regards

      
                
                
                    
                                                    Fri, 07/21/2017 - 06:08
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products
