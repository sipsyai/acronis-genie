# No activation mail

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/no-activation-mail

## Original Post
**Author:** Unknown

No activation mail

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Kevin Loos
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 8
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
Since yesterday when I try to create a new backup or administrator account, I don't receive the activation mail.
I tried with different email address and the probelm is the same. 
Can you help ?
Thanks,
Kevin

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 10/22/2015 - 07:47

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Kevin,
There can be different reasons for activation email not being received, so let's localize it first.
1. Account is not created
In this case e-mail is not sent at all. You can check whether it is so if you login to Account Management Console and don't find a newly created not yet activated account. It will look greyed out.
If this is true, probably you are creating the account with external provisioning system and it's requests are not executed by the Account Management Server. Make sure you can create an account manually (with the same login name) in the Account Management Console, and then troubleshoot the problem in the integration of provisioning system.
2. SMTP server problem
If you are using branding options and modified default email server settings (in any of the parent groups), go to the settings of the respective group and send a test e-mail to make sure it works correctly. The same smtp server is used for all notifications, so if you didn't get any backup notifications for the same period of time, it should be a good point to check.
3. Email filtering
Just to make sure that used mailboxes don't filter out the activation email, try to use the same email address you already used successfully with Acronis Backup Cloud before, but with different login to create a new account.

Please check the above and let me know if the problem persists, I'll be happy to assist further.
Thank you,

      
                
                
                    
                                                    Thu, 10/22/2015 - 08:34
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Kevin Loos
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 8
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Dmitry,

It's not the first account I create and never got any issue.

I didn't modified the smtp setting and I try with 3 different e-mail address.

I have more than 20 backup account and only got the issue since yesterday.

I ask one of my coworker to try it with his account and same issue.

Thanks for your reply,

Kevin

      
                
                
                    
                                                    Thu, 10/22/2015 - 09:13
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Kevin,
Thank you for these details.
So it's clear now that both creating the account and the smtp server worked well just before the issue appeared, and the filtering is not likely a problem. Now we have to make sure what exactly is not working to set further action steps, so please answer following questions:
Do you see the new account created and pending activation (greyed out) in Account Management Console? If not, do you use an external provisioning system?
Please go to STMP settings and send the test e-mail. If you receive it, then nothing happened here in between and nothing to check. Otherwise it explains well why your colleague also cannot receive the activation email, and you'd have to check the SMTP server, not the settings here.
Looking forward to your response,

      
                
                
                    
                                                    Thu, 10/22/2015 - 10:09
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Kevin Loos
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 8
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi,

I can see the new account greyed out.

The branding isn't activated so the smtp configuration is yours by default.

Do I have to try with another smtp server of my own ?

Thanks for your answer,

Kevin

      
                
                
                    
                                                    Thu, 10/22/2015 - 11:51
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Kevin,
Great, so this is indeed purely an email notification issue, accounts do get created.
The fact that branding is not activated in your group means that it inherits these settings from higher hierarchy group, so you should check the branding settings in the group higher than yours in the hierarchy, and then even higher, until you find where the branding was set. Most probably it is set on top of your hierarchy which is Distributor / Provider group type.
If you can't check that immediately, go ahead and activate branding settings in your group and perform 3 checks to find out what actually works and what not:
Set default (Acronis) SMTP settings and send a test email or resend activation link for the account.
Set expected SMTP settings as in top hierarchy and check it.
If none of the above works, use 3rd party SMTP server (e.g. smtp.gmail.com, port: 587, encryption: TLS, credentials: your gmail account).
If the outcome is that only your SMTP server encounters the problem, check that it works successfully with other software from other servers (you can use telnet to do it too). And if it does, make sure that the Account Management Server of your DC is allowed on your SMTP server.
Let me know what the outcome is and if you have further questions.

      
                
                
                    
                                                    Thu, 10/22/2015 - 12:27
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.
