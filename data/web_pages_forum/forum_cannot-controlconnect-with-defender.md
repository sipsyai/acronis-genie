# Cannot control/connect with Defender

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/cannot-controlconnect-defender

## Original Post
**Author:** Unknown

Cannot control/connect with Defender

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Jérôme Ray
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello.
 
We have 45 computer with the same plan. On a half we get an error that Acronis cannot control Windows Defender because it is controlled by flobal policy 
It's unfortunately not true . No GPO, no intune, no Defender plan.
We want to ensure that Defender is active and also grab the alerts on computer and see them in Acronis console.
What has to be changed or where is the log to know why it does not work on a half of computers (all are configured the same way) ?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 03/21/2023 - 21:29

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Jerome!
Please check the solution over the following KB: https://kb.acronis.com/content/67340
( Make sure all the devices have that applied ).
Please confirm that all of them use the same build, if not, please update them: https://kb.acronis.com/content/56313
Let me know if that resolved the issue.
Thanks.
 

      
                
                
                    
                                                    Wed, 03/22/2023 - 13:44
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jérôme Ray
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello.
Thanks for the reply.
All agents are 15.0.31771
Tamper protection is OFF in Windows Security
There is no global or local policy related to defender (based on gpresult)

      
                
                
                    
                                                    Thu, 03/23/2023 - 07:59
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jérôme Ray
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Additional question: we (temporarily I hope) failed a security audit because alerts are not centralized (test with "fake" virus).
Does Acronis grab the malware alerts from Windwos Defender (or Windows Event log) or deos it only work when the Acronis malware protection is on ?
We had to turn virus protection of Acronis off, becasue it slows our computer very very much.
What we expected, was that Defender alerts are brought to Acronis console, but seems not to work.
Is there some log where we can find which settings blocks Acronis or where it finds that Defender is controlled by group policy ?

      
                
                
                    
                                                    Thu, 03/23/2023 - 08:08
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Jérôme Ray wrote:

Additional question: we (temporarily I hope) failed a security audit because alerts are not centralized (test with "fake" virus).
Does Acronis grab the malware alerts from Windwos Defender (or Windows Event log) or deos it only work when the Acronis malware protection is on ?
We had to turn virus protection of Acronis off, becasue it slows our computer very very much.
What we expected, was that Defender alerts are brought to Acronis console, but seems not to work.
Is there some log where we can find which settings blocks Acronis or where it finds that Defender is controlled by group policy ?


Hello Jerome.
Our A.virus is totally independent from the Windows Defender. It's not possible to bring Windows defender alerts to our console if you don't have it active in the backup plan. 
You would need to add the Windows defender on the backup plan, please check the screenshot of this KB: https://kb.acronis.com/content/71192
If the plan is configured that way and the threats aren't detected then there is an issue and we should contact support for investigation.
Thanks in advance!
 

      
                
                
                    
                                                    Thu, 03/23/2023 - 13:44
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Bradley Williams
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I have also facing the same issue.

      
                
                
                    
                                                    Mon, 03/27/2023 - 07:14
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Bradley Williams wrote:

I have also facing the same issue. 


Hello Bradley!
Could you please specify what issue are you facing? Because we discussed 2 different issues here.
Thanks in advance. 

      
                
                
                    
                                                    Mon, 03/27/2023 - 11:34
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jérôme Ray
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            hello. Thanks for your feedback.
Sorry, but are you sure ?
I got one a malware alert in the console an the virus and malware protection was off (Defender on).
Best regards

      
                
                
                    
                                                    Mon, 03/27/2023 - 12:39
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Jérôme Ray wrote:

hello. Thanks for your feedback.
Sorry, but are you sure ?
I got one a malware alert in the console an the virus and malware protection was off (Defender on).
Best regards


Thanks for commenting!
I will rephrase so everything gets clear.
It's possible to bring the alerts just if the Windows defender is active in the backup plan. Like in the screenshot of this KB : https://kb.acronis.com/content/71192 ). If it's not enabled you can't bring those alerts.
If that's the case and the notifications don't appear, you should contact our support or your service provider because that requires an internal investigation.
Thanks in advance!

      
                
                
                    
                                                    Mon, 03/27/2023 - 13:10
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
