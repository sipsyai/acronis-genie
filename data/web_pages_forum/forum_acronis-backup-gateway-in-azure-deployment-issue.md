# Acronis Backup Gateway in azure Deployment issue

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/acronis-backup-gateway-azure-deployment-issue

## Original Post
**Author:** Unknown

Acronis Backup Gateway in azure Deployment issue

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Oliver Heymanns
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Dear all,
currently we have the backup gateway on one of our NAS systems.
We want to use azure in the future and i tried to install the Acronis Backup Gateway in Azure (https://azuremarketplace.microsoft.com/en-us/marketplace/apps/acronis.storage-gateway?tab=Overview) 
but I get a deployment error
{ "id": "/subscriptions/34c51f21-c7ea-4df6-9160-2eb15ba2d266/resourceGroups/GatewayAcronis/providers/Microsoft.Resources/deployments/acronis.storage-gateway-20190802131724/operations/F6C01B7B189B38E8", "operationId": "F6C01B7B189B38E8", "properties": { "provisioningOperation": "Create", "provisioningState": "Failed", "timestamp": "2019-08-02T11:27:53.3854653Z", "duration": "PT8M21.5075719S", "trackingId": "e8046cbf-99c2-438e-b8e8-4dd264400458", "statusCode": "Conflict", "statusMessage": { "status": "Failed", "error": { "code": "ResourceDeploymentFailure", "message": "The resource operation completed with terminal provisioning state 'Failed'.", "details": [ { "code": "VMExtensionProvisioningError", "message": "VM has reported a failure when processing extension 'InitializeStorage'. Error message: \"Enable failed: failed to execute command: command terminated with exit status=1\n[stdout]\n\n[stderr]\n\"." } ] } }, "targetResource": { "id": "/subscriptions/34c51f21-c7ea-4df6-9160-2eb15ba2d266/resourceGroups/GatewayAcronis/providers/Microsoft.Compute/virtualMachines/acronisstoragegateway/extensions/InitializeStorage", "resourceType": "Microsoft.Compute/virtualMachines/extensions", "resourceName": "acronisstoragegateway/InitializeStorage" } }}
 

 Does someone has similar issues or knows how to solve this?
Thanks in advance

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 08/02/2019 - 11:39

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Oliver,
thank you for your posting! 
Such issue should be investigated with the help of Acronis support team. But prior opening a support ticket, I'd ask you to verify the performed steps with the following documentation article 
https://dl.acronis.com/u/vstorage/docs/pdf/AcronisSoftwareDefinedInfrastructure_2_abgw_quick_start_guide_for_azure_en-US.pdf
and also with Microsoft TechNet article:
https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-manager-common-deployment-errors 
If you only have Storage (general purpose v1), you need to upgrade your Azure account
Should the issue persist, please raise a support ticket and share the following information with the engineers:
- full error message and/or screenshots illustrating the issue
- step-by-step description of the deployment process done

      
                
                
                    
                                                    Mon, 08/26/2019 - 07:46
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Bob Aubry
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Ekaterina : We are getting exactly the same error deploying the template VM. We have reviewed both documents in your reply again and still have the error. When we run the template, we do NOT have an option for Storage (general purpose v2) to select.  We can upgrade it after the template completes. If we try to redeploy the template we get this message:
The resource group is in a location that is not supported by one or more of the resources in the template. 
Please choose a different resource group.
I entered a support ticket Monday and heard nothing.  
Thanks!
Bob Aubry 
Main Street Software 
boba@mssinc.com 

      
                
                
                    
                                                    Thu, 10/31/2019 - 18:25
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dear Bob,
sorry to know you've faced the same issue! Checked the status of the support ticket - our engineers are going to collect the diagnostic information required for the investigation and then escalate the ticket to the higher level for analysis I'd strongly recommend working on the issue with our support engineers, since the investigation would require the involvement of the dedicated specialists from the expert team. 

      
                
                
                    
                                                    Mon, 11/11/2019 - 09:17
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
