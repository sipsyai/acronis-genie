# Copy a Backup (Protection) Plan

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/copy-backup-protection-plan

## Original Post
**Author:** Unknown

Copy a Backup (Protection) Plan

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    David Cocke
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I cannot figure out how to make a copy of an existing backup plan (now called a Protection Plan).  We have an existing backup plan, and now I'd like to create a new plan based upon the original plan, as I have 1 machine that needs to deviate slightly from the plan applied to other machines.  These instructions no longer appear to be correct with the latest version of the Cyber Protect Console: kb . acronis . com /content/56331  In fact, the screenshots in that article are not matching the current product.  The forum will not let me paste a hyperlink to the Acronis Knoweledgebase, but hopefully you can figure out which KB article I'm referring to.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sat, 07/18/2020 - 14:08

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ivaylo Tsvetkov
                            

                            
                    
                        Acronis engineer
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 85
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello David,
Please note, that you can apply and import protection plans created only in Cyber Protection 9.0. Backup plans created in the previous product versions are incompatible with the version 9.0 and they will show only for the device they were initially applied to under Acronis Cyber Cloud 8.0.
To apply an existing protection plan in Cyber Protection 9.0:
Select the machines that you want to protect.
Click Protect. If a protection plan is already applied to the selected machines, click Add plan.
The software displays previously created protection plans.
Select a protection plan to apply and click Apply.
https://www.acronis.com/en-us/support/documentation/CyberProtectionServ…
Also note that only plans that do not conflict with the selected device will be displayed. For example if a plan is created for a machine with installed OS agent, the same plan will not appear for VMs that are displayed in the console from a Hyper-V or VMWare hypervisors.
If you are trying to apply a backup plan created in 8.0 please recreate the plan under 9.0 and it should be then available to be applied on the devices of same type.
Thank you.

      
                
                
                    
                                                    Tue, 07/21/2020 - 12:23
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ivaylo Tsvetkov | API Platform Senior Support Engineer 

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                            
                Products: 
                Acronis Cyber Protect Cloud
