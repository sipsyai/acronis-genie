# Acronis WHMCS  module fury

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/acronis-whmcs-module-fury

## Original Post
**Author:** Unknown

Acronis WHMCS  module fury

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Andrews Salisbury
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I am trying to install Acronis WHMCS module, I currently do not have the Previous installation. But while activating getting this weired error:
Cannot upgrade products and services. Error: Direct upgrade from the current version 0.0.0-0 to the new version 2.6.0-375 is not supported. Please upgrade the module to the version 1.0.0-177 first.
It says Direct Upgrade from current version 0-0-0-0 .
Any help on resolving the issue?
 
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sat, 07/02/2022 - 16:03

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Andrews Salisbury
Did you ever have the Acronis WHMCS module installed in the past? If so, there way be some leftover tables in your database that are causing this.

      
                
                
                    
                                                    Mon, 07/04/2022 - 15:09
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Andrews Salisbury
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Yes, I  do had, but I sanitized all the tables of whmcs with Acronis existence. But still struckup. any developers could point out this check causing prevention of installltion.

      
                
                
                    
                                                    Thu, 07/07/2022 - 05:44
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ivaylo Tsvetkov
                            

                            
                    
                        Acronis engineer
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 85
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Andrews,
It looks like WHMCS still detects old portions of the Acronis module.
Old module version pointed in the error as valid for upgrade scenario can be downloaded from here: https://dl.acronis.com/u/ci/whmcs/AcronisModulesForWHMCS-build-177.zip
But if you intended and went for a clean installation in first place, you should check again what can be cleaned up before directly installing and configuring the latest module version which won't require the upgrade step by going through that legacy version 1 build. Please, check all the uninstalling instructions at: https://www.acronis.com/en-us/support/documentation/WHMCS/#uninstalling…
With focus on: https://www.acronis.com/en-us/support/documentation/WHMCS/#removing-tab…
This is the final step for cleaning up any leftovers of the module from folder structure and WHMCS database.
Then go for a fresh install of v2.6.0-375 again. If still failing please raise a Support ticket, to be further assisted.
Thank you.

      
                
                
                    
                                                    Tue, 07/12/2022 - 09:20
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ivaylo Tsvetkov | API Platform Senior Support Engineer 

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                            
                Products: 
                Acronis Cyber Protect Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daria Sorokina
                            

                            
                    
                        Acronis Support
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 487
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dear Andrews Salisbury,
Please let us know was your problem that you presented here resolved if yes, what helped you?

      
                
                
                    
                                                    Tue, 09/27/2022 - 21:48
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards, Daria Sorokina | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Andrews Salisbury
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Yes, I need to search deeply the entire whmcs databse and after thorough sanitisation it worked.

      
                
                
                    
                                                    Tue, 12/27/2022 - 10:30
