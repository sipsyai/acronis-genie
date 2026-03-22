# Finalization error in Disaster Recovery Cloud...

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/finalization-error-disaster-recovery-cloud

## Original Post
**Author:** Unknown

Finalization error in Disaster Recovery Cloud...

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Jorge Carvajal Astorga
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
I have an error starting the failover in Disaster Recovery:
"The failover will be canceled due to finalization failure. The changes that occurred to the recovery server during the failover will be discarded. After that, you can start the failover again."
and he can't get it out of that state... "Finalization error"...
It's a demo... and previously it had worked...

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      20210913 Fail Disaster Recovery.docx

                      236.21 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Mon, 09/13/2021 - 21:14

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Good day Jorge
Unfortunately the "Internal Error" is a very generic and unclear error message,
Can you please provide us with the following activity log to better understand the issue:
Navigate to Disaster Recovery > Servers > Select the affected machine > Click activities > Click on the corresponding activity > Hold control and left click the activity > After this you should see the ellipsis of which you can then select "Task activity info"
Please provide us with the tasks activity info
Kind regards

      
                
                
                    
                                                    Wed, 09/15/2021 - 13:56
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jorge Carvajal Astorga
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi,
Thanxz...
Finally, it was fixed by Acronis Support:
"The issue however has been fixed. We have found a ghost VM on the hypervisor which was in offline state - those was preventing 'cancel fail over' operation via the cloud recovery console..."

      
                
                
                    
                                                    Wed, 09/15/2021 - 14:08
                                                                            
                                
                            
                                            
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi,
I am glad your issue has been resolved,
Kind regards

      
                
                
                    
                                                    Wed, 09/15/2021 - 19:01
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products
