# Acronis Cyber Protect Cloud Nutanix VM Image Slowly Problem

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/acronis-cyber-protect-cloud-nutanix-vm-image-slowly-problem

## Original Post
**Author:** Unknown

Acronis Cyber Protect Cloud Nutanix VM Image Slowly Problem

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    İlhan Korkut
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello Everyone
 I have a problem on my Nutanix environment with ACP. I am working for backup VMs from a nutanix cluster via Virtual Appliance for nutanix. But my backup speed is very slowly. I am using SMB location for proxy and both are in the same subnet,  also the nutanix cluster too.
All of the point are using 10G network connections but my backup speed is just between 50 mb/s and 150 mb/s. 
What can i do for upgrade my backup speed? I have 750 VMs in my cluster and that speed is not enough for me. 
NOTE: Normally i am working another backup solution for backup operations. At the moment i am migrating all of the backup from old backup solution to ACP step by step. 
Best regards. 
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 06/26/2025 - 16:31

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Cyber Protect Cloud
Acronis Cyber Infracture
Acronis With Nutanix
Acronis With Vmware

            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Welcome to the forum.
First, verify that your backup storage and network can actually sustain higher throughput. Acronis performance tests on 10 Gb networks show hundreds of MB/s are achievable, so 50–150 MB/s suggests a bottleneck. Use a high-performance backup repository – ideally a dedicated server or appliance with fast disks, not a shared VM or slow NAS. In fact, Acronis advises using a physical server (with SSDs) for backup storage to maximize I/O performance. For example, consider writing backups to a local SSD on the backup proxy (or a Nutanix volume) instead of a remote SMB share. If you must use a network share, ensure it runs on fast hardware (lots of spindles or SSDs) and that the SMB server’s disks are not the limiting factor.

Use NFS if possible: Since Acronis supports backing up Nutanix Files via both SMB and NFS, try using an NFS share instead of SMB. Some users find NFS performance to be higher or more stable than SMB in highly parallel workloads. Switching protocols may eliminate SMB-specific overhead.


Check network settings: Ensure all 10 Gb links are negotiated at 10 Gb (not 1 Gb) and that switches/hosts are configured for full-speed. Verify that jumbo frames and flow control (if used) are configured consistently on both sides. If you have multiple physical NICs or an RDMA-capable setup, you might enable SMB Multichannel/SMB Direct to aggregate bandwidth. (Note: in some cases Acronis has warned that SMB multichannel can hurt backup speed, so you may need to test with it disabled on the client or server if you see strange performance issues.)

Tune Acronis Backup Settings
In the backup plan options, increase parallelism so that more VMs stream simultaneously. By default an Acronis agent can back up multiple VMs in parallel (up to 10 by design)dl.acronis.com. In your plan, set the “Limit number of simultaneous backups” to a higher value (up to 10) so the Virtual Appliance will process multiple VMs at once. Running VMs in parallel on a 10 Gb network and fast storage can multiply aggregate throughput. (Be careful that overlapping plans don’t exceed this limit – Acronis will cap the total concurrent VMs per agent to 10dl.acronis.com.)
Also check resource usage on the backup appliance: ensure it has plenty of CPU cores and memory. If the appliance VM is CPU-starved (due to encryption, compression or snapshot workload), it may top out well below network speed. For example, turning off encryption or using normal instead of maximum compression can improve throughput, since encryption is CPU-intensive and “can have an impact on your backup times even at lower settings”. If you enabled heavy compression/deduplication on the plan, try a test run with these disabled to see if raw speed improves.
Monitor and Iterate
Finally, monitor where the bottleneck is occurring. Check disk I/O and CPU on the SMB server and on the Acronis appliance during a backup. If the I/O on the target is maxed out, the storage is the limit; if the appliance’s CPU or NIC is maxed, adjust its resources. Also ensure you’re using the latest Acronis version (updates often include performance fixes). By combining a faster storage target, proper network tuning, and increased backup concurrency, you should see backup rates well above 150 MB/s on a 10 Gb network.
Due to the complexity of this topic I advise you to contact our support or our sales department so you can get further guidance: https://support.acronis.com/ , https://www.acronis.com/en-eu/contact-sales/
Best regards.

      
                
                
                    
                                                    Fri, 06/27/2025 - 11:00
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
