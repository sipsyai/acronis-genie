# WHMCS Module - billing for overusage

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/whmcs-module-billing-overusage

## Original Post
**Author:** Unknown

WHMCS Module - billing for overusage

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Chris Danks
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 20
                
            
                                                        
    
    
        
    


                
                
                    
                        
            HI
I need some help with the latest WHMCS module.
We've followed the PDF guide and successfully installed & configured the Acronis module in WHMCS.
 
I placed a test order and gave my test user 1 Agent & 30GB cloud Space.
 
I then logged in to acronis and added an agent and used 200GB cloud space.
 
How do I get WHMCS to generate invoices for the additional used diskspace? from what I can see this is not possible?
 
What I want to do is allow a customer to signup and not be restricted to agents/cloud space
then when their monthly invoice is generated it bills them the per agent/per gb rate so they only pay for what they have used.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 08/24/2020 - 15:39

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ivaylo Tsvetkov
                            

                            
                    
                        Acronis engineer
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 85
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Chris,
Thank you for sharing your question.
As you have noticed the Acronis addon module for WHMCS does not offer a Pay-as-you-go billing mechanism, or the possibility of charging a customer for the actual resource usage on a defined rate.
You can enable one of the available billing models: One Time/Monthly, Quarterly, Semi-Annually, Annually, Biennially, Triennially, and then specify Setup fee and Price. If a customer's usage has exceeded the purchased amount of agents or Cloud usage space the Backup Service will stop for this user once the latest currently running backup has completed.
The solutions that our module offers are:
1. You have the option to add a configurable option group which will allow your customers to purchase additional resources when these limits are exceeded (see point 6.3 from the User Guide).
2. Or you can specify the Unlimited value for the Quantity item type in your products which will not limit your customers.
You can also setup and enable resource overage (point 6.4.3 from the User Guide) which will allow additional usage limit before the Backup Service is terminated. Your customer will receive a warning message that he is exceeding the purchased amount of resource but the Backup Service will still continue to operate. However once this Overage Limit is reached it will terminate the Backup Service immediately even preventing the currently running backup from completing.
Thank you.

      
                
                
                    
                                                    Tue, 08/25/2020 - 14:49
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ivaylo Tsvetkov | API Platform Senior Support Engineer 

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                            
                Products: 
                Acronis Cyber Protect Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Chris Danks
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 20
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            HI
I setup the module however if someone chooses the config option and adds 500GB space, it creates it with unlimited space in Acronis?

      
                
                
                    
                                                    Fri, 08/28/2020 - 16:00
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ivaylo Tsvetkov
                            

                            
                    
                        Acronis engineer
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 85
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Chris,
Please accept my apologies for the delayed response.
I would suggest opening a Support case. Please, provide your Acronis Cloud account login name, DC of your account, the name of the affected customer tenant for which the purchase from the configurable option set the space to Unlimited instead adding the space to the previous value. You can use my name as point of contact so the case be assigned to me. We can have a remote session and try to set up this together.
Please, also share some description of the issue and steps to reproduce. I would appreciate if you set debug logging on the module based on this article and share it to the case after you've reproduced the described scenario: https://kb.acronis.com/content/61074
Thank you in advance.

      
                
                
                    
                                                    Wed, 09/02/2020 - 22:17
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ivaylo Tsvetkov | API Platform Senior Support Engineer 

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                            
                Products: 
                Acronis Cyber Protect Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Chris Danks
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 20
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            HI
i found the cause.  
 
Addons > acronis cyber cloud
 
the product must be set to 0 for servers/virtual/diskspace for it to use the configurable fields in whmcs.  Once i changed this from unlimited to 0 then new order didn't set it as unlimited space.

      
                
                
                    
                                                    Fri, 09/04/2020 - 08:54
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ivaylo Tsvetkov
                            

                            
                    
                        Acronis engineer
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 85
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Chris,
I see, of course you have set the template under Addons -> Acronis Cyber Cloud to Unlimited before, I didn't know that. If the template is set with Unlimited quota, it will always stay Unlimited, no matter what the Configurable Options will try to apply.
This goes to each of the offering items you have selected in your edition in the template.
Great, I am happy to know that you have find the solution and you are getting confident with the product.
However feel free to ask us for additional options, we will gladly assist you.
Thank you.

      
                
                
                    
                                                    Fri, 09/04/2020 - 09:15
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ivaylo Tsvetkov | API Platform Senior Support Engineer 

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                            
                Products: 
                Acronis Cyber Protect Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Chris Danks
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 20
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi
 
I recommend updating your documentation so the installation guide says if you are using configurable options set the package to 0 for servers/vms/cloud storage.

      
                
                
                    
                                                    Fri, 09/04/2020 - 09:31
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ivaylo Tsvetkov
                            

                            
                    
                        Acronis engineer
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 85
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Chris,
I agree with you.
We are actually already preparing a release to fit the newest changes on Acronis Cyber Protect Cloud. One of the main Epics is fixing the documentation, we are already working on making it better.
However I will check that particular point with PM team and submit an improvement if not planned already.
All best Chris.

      
                
                
                    
                                                    Fri, 09/04/2020 - 09:55
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ivaylo Tsvetkov | API Platform Senior Support Engineer 

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                            
                Products: 
                Acronis Cyber Protect Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Nice find Chris Danks! Thanks for sharing.

      
                
                
                    
                                                    Fri, 09/04/2020 - 13:38
