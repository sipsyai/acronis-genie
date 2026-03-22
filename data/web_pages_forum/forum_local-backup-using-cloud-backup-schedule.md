# Local backup using Cloud  - backup schedule

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/local-backup-using-cloud-backup-schedule

## Original Post
**Author:** Unknown

Local backup using Cloud  - backup schedule

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Paul Burrows
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi everyone,
We are just starting in the realm of backup solutions and we need to provide a solution that will keep dormant documents for 6 years, the idea is:
Local -daily incremental , weekly differential and monthly full
Cloud - daily
My concern is local storage retention now the plan would be to keep the monthly full backups for 36 months, weekly for 3 months and daily for 1 month. it would be like this for ease of use locally to look back rather than login to cloud.
Does anyone have a preference on creating a local retention policy to make use of the available storage space?
We are in South Africa and work in the medical industry, this is why the 6 year retention is a must but do we really need to keep the local storage for that long?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 07/11/2017 - 14:24

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Paul
Based on HPCSA guidance on the retention of medical records, all records should be kept for at least six (6) years after which they become dormant as well as multiple other scenarios such as:
The records of minors should be kept until their 21st birthday
The records of patients who are mentally impaired should be kept until their death.
Records pertaining to illness or accident arising from a person’s occupation should be kept for 20 years after treatment has ended
As far as I am aware to be compliant with HPCSA  the six (6) year retention period must be met. It is recommended by HPCSA to keep electronic records "off-site".
Based on all of the above your deployment of an Acronis Backup Cloud hybrid deployment will most definitely suite the industry needs and requirements. 
To answer your question if you are doing an hybrid deployment where you are replicating the same backup to the cloud as well as to local storage then no you will not need to have the retention that long for local storage, what I mean by this is your cloud based backups will have the proper six (6) year retention etc but your local storage (Which will act like a secondary backup) can have a default retention or even lower.
This scenario will allow for a type of BLOB situation (Loosely described) where your data in the cloud is archived (Where your retention is as required etc "cold data") and the data on the local storage acts as your hot data where if in the case of a disaster you can quickly access the records using local network. And then in case of a critical failure where local storage etc is completely down you will be able to recover all data using maximum retention from the cloud.
I hope this answers your question.
Best regards
 
 

      
                
                
                    
                                                    Thu, 07/13/2017 - 12:23
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products
