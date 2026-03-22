# Replica gone bad. VM displayed with a wrong status

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/replica-gone-bad-vm-displayed-wrong-status

## Original Post
**Author:** Unknown

Replica gone bad. VM displayed with a wrong status 

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    nicolas diard
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi all,
First post here, as i'm a new customer coming from Veeam.
We used replica to move VM between 2 vcenters. We faced an error. A replication plan was used to create a replica. Let's call the replica VM : "VM1r"
Just before migration, we stopped original VM, executed replication plan. Something gone wrong, replication wouldn't launch. We had no time to troubleshoot. So we started VMr thru vcenter, and we just deleted replication plan.
My VMr is working fine, but acronis portal is still showing VMr as a replica vm, i mean there is the icon with le letter R. I'd like Acronis to show the correct status, and forget this is not a replica.
How can i do ?
 
TY
N.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 10/14/2021 - 10:14

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello nicolas,
sorry for the delayed response! To switch the workload from the original virtual machine to its replica, one would need to perform the Failover operation as described in  https://www.acronis.com/support/documentation/CyberProtectionService/#f… To finalize the restored VM, use the Failback option - the replica will be recovered as the original or a new virtual machine.

      
                
                
                    
                                                    Sun, 10/17/2021 - 11:51
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    nicolas diard
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            So, finally, here is the way i solved this :
Shutdown the VM wrongly seen as replica.
From venter, browse the datastore where the vm resides. download the vm configuration file  (.vmx) to your desktop.
Then edit the configuration file, and remode all acronisTags, except acronisTag.Meta.
Then upload the .vmx file back to the vm folder with datatore browser.
Start Vm, you should notice Acronis now displays correctly the vm a a normal vm.
 
This is a bit weird i got a case open since last august for that issue, and support has not yet found a solution. I asked them to validate the way i solved it. Still no answer yet. My previous Backup support surely would have answered it in less that a week. (veeam).

      
                
                
                    
                                                    Mon, 01/24/2022 - 12:09
