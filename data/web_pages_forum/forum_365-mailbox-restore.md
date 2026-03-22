# 365 Mailbox restore

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/365-mailbox-restore

## Original Post
**Author:** Unknown

365 Mailbox restore

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Michael Rayfield
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                
                    
                        
            A couple questions; 1. How to bulk restore a list of 365 mailboxes? It seems that I can only restore one at a time. 2. When a mailbox restore is processing, can I exit out of the tab or will that cancel the restore process? Thanks!

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 05/14/2025 - 19:32

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Welcome to the forum.
That depends on your deployment type (C2C agent or local agent) and how you intend to perform the recovery.
Please refer to the following user guides for available options:

Recovering a Team Mailbox


Recovering Mailboxes

Once the recovery has started, you can safely disconnect from the console—the operation will continue unless you manually cancel it.
If you have any questions during the process, feel free to contact our support team or your service provider for further guidance.
Best regards.
 

      
                
                
                    
                                                    Thu, 05/15/2025 - 12:01
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Michael Rayfield
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I believe we're using the C2C agent.  I used the "add" function and selected "Microsoft 365 Business - Backup". 
Also, I started the restore process on one mailbox and watched it complete successfully; however I haven't received an email with the download link.

      
                
                
                    
                                                    Thu, 05/15/2025 - 15:02
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Michael Rayfield wrote:

I believe we're using the C2C agent.  I used the "add" function and selected "Microsoft 365 Business - Backup". 
Also, I started the restore process on one mailbox and watched it complete successfully; however I haven't received an email with the download link.


Hello!
What do you mean by "download link"?
If the recovery is performed according to the user guides mentioned above, the data will be restored directly to the mailbox—nothing will be downloaded.
The only way to download the data is by exporting it to a PST file:Recovering Mailboxes to PST
You can also do this through the console:Backup Storage > PST files
Best regards.

      
                
                
                    
                                                    Thu, 05/15/2025 - 15:51
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Michael Rayfield
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Sorry, I meant to mention I'm restoring to PST file. I put a ticket in with support.
 
Resolved: It was pointed out to me that that recovered PST files are listed under "Backup Storage > PST Files", within the client company's management portal, from where they can be downloaded. Download links weren't sent out.

      
                
                
                    
                                                    Thu, 05/15/2025 - 16:11
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Michael Rayfield wrote:

Sorry, I meant to mention I'm restoring to PST file. I put a ticket in with support.
 
Resolved: It was pointed out to me that that recovered PST files are listed under "Backup Storage > PST Files", within the client company's management portal, from where they can be downloaded. Download links weren't sent out.


Hello!
I'm glad to hear the issue was resolved.
Feel free to participate anytime you need help.
Best regards.

      
                
                
                    
                                                    Fri, 05/16/2025 - 12:07
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
