# Files/Folders exclusions

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/filesfolders-exclusions

## Original Post
**Author:** Unknown

Files/Folders exclusions

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Ioannis Tsimpidis
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I read the documentation: 
File filters (Inclusions/Exclusions)
/u/baas/help/23.10/user/en-US/index.html#cshid=46970
I still have questions.
Let's say I want to exclude all folders (and their contents obviously), wherever they might be located, that could have names like below:
x-done
xx-done
xxx-done
X-done
X-Done
x-doneagain
xx-doneagain
XXX-DONE
 
First - could we use anything like this: **/*[Xx][XxXx]-done/** 
Secondly - to exclude all folders with name x-done (from anywhere)...
What is the most appropriate:
x-done
/x-done/
*/x-done
*x-done
*x-done*
**x-done
**/x-done
or something else?
 
-------------------
Also, all files wherever those could be with file extension:
.done
Does this need to look like: "**.done", or "*.done" would be enough?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 11/16/2023 - 09:10

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello! 
Welcome to the forum.
Please refer to the following user-guide where the rules about the files filters are detailed with examples of certain scenarios: https://www.acronis.com/en-us/support/documentation/CyberProtectionServ…
If after applying them they don't are executed in the plan properly I suggest you to recreate the plan or to contact support at https://kb.acronis.com/content/8153
Best regards.

      
                
                
                    
                                                    Thu, 11/16/2023 - 16:24
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
