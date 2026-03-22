# Error in attempting to register Acronis Storage Gateway

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/error-attempting-register-acronis-storage-gateway

## Original Post
**Author:** Unknown

Error in attempting to register Acronis Storage Gateway

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    marcelovvm
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I am trying to register my Acronis Storage Gateway (VM Azure machine) in the Acronis Backup Cloud, but the error below occurs when I try to register. What can it be?
CMD:
sudo acronis-storage-registration -u marcelo.magalhaes@marteengenharia.com -p 'XXXX' -s cloud.acronis.com -a storage-gateway.brazilsouth.cloudapp.azure.com:44445 -i AzureAcronisBackup -o /etc/pki/tls/certs/Acronis/storage/
[sudo] password for administrador:
('POST', 'https://cloud.acronis.com/api/1/groups/self/storages')
Failed:
Traceback (most recent call last):
  File "/bin/acronis-storage-registration", line 198, in <module>
    main(parser.parse_args()[0])
  File "/bin/acronis-storage-registration", line 170, in main
    register_storage(args.host, args.owner, args.username, args.password, args.address, args.uid, args.outdir, args.config)
  File "/bin/acronis-storage-registration", line 95, in register_storage
    redirect = json.loads(opener.open(request, data=data).read())
  File "/usr/lib64/python2.7/urllib2.py", line 437, in open
    response = meth(req, response)
  File "/usr/lib64/python2.7/urllib2.py", line 550, in http_response
    'http', request, response, code, msg, hdrs)
  File "/usr/lib64/python2.7/urllib2.py", line 475, in error
    return self._call_chain(*args)
  File "/usr/lib64/python2.7/urllib2.py", line 409, in _call_chain
    result = func(*args)
  File "/usr/lib64/python2.7/urllib2.py", line 558, in http_error_default
    raise HTTPError(req.get_full_url(), code, msg, hdrs, fp)
HTTPError: HTTP Error 400: Bad request
 
Live long and prosper,
Marcelo Magalhães

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sun, 08/13/2017 - 07:27

                                                          
                                                            
                                                                                        
    
                    
                Live lona and prosper

            
                    
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Marcelo
I would suggest that you run it as follows:
To register the gateway in Acronis Backup Cloud
As the root user, execute the following command in any directory:
acronis-storage-registration -u USERNAME -p PASSWORD -s HOST -a GATEWAYADDRESS -i "UID" -o "/etc/pki/tls/certs/Acronis/storage/"
USERNAME is the login for your administrator account in Acronis Backup Cloud
PASSWORD is the password for the above account
If the password contains Linux Bash special characters (for example, ^, $, or &), the password
must be enclosed in single quotes.
If the password contains single quote characters ('), they must be properly escaped according
to the Linux Bash syntax.
HOST is the web address of the Acronis Backup Cloud management console (for example,cloud.acronis.com)
GATEWAYADDRESS is the public DNS name and port of this gateway, as specified in the
	gateway configuration (for example, storage.example.com:44445)
UID is a name of the storage that will be displayed on the Storage tab of the Acronis Backup
	Cloud management console. Create a unique name (for example, "My Storage 123") and
	type it in this parameter.
Once this is completed you will need to start the gateway:
As the root user, execute the following commands in any directory:
service acronis-storage-mds start
service acronis-storage-gateway start
Best regards

      
                
                
                    
                                                    Wed, 08/16/2017 - 07:29
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    marcelovvm
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Jays,
     Thanks for the tip... but, as root... same problem :(
Live long and prosper,
Marcelo Magalhães
 

      
                
                
                    
                                                    Wed, 08/16/2017 - 23:02
                                                                            
                                
                            
                                            
                                            
    
                    
                Live lona and prosper

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Marcelo
Can you please advise if you are receiving any error message or failure, so that I can just have a bit more of an insight into your issue.
Would it be possible for you to copy the output of the command?
Regards

      
                
                
                    
                                                    Mon, 08/21/2017 - 14:55
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    marcelovvm
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Jays,
     The message and error it gave when I tried to add the gateway as root was the same as before (already posted above). So, same problem, same error.
('POST', 'https://cloud.acronis.com/api/1/groups/self/storages')
Failed:
Traceback (most recent call last):
  File "/bin/acronis-storage-registration", line 198, in <module>
    main(parser.parse_args()[0])
  File "/bin/acronis-storage-registration", line 170, in main
    register_storage(args.host, args.owner, args.username, args.password, args.address, args.uid, args.outdir, args.config)
  File "/bin/acronis-storage-registration", line 95, in register_storage
    redirect = json.loads(opener.open(request, data=data).read())
  File "/usr/lib64/python2.7/urllib2.py", line 437, in open
    response = meth(req, response)
  File "/usr/lib64/python2.7/urllib2.py", line 550, in http_response
    'http', request, response, code, msg, hdrs)
  File "/usr/lib64/python2.7/urllib2.py", line 475, in error
    return self._call_chain(*args)
  File "/usr/lib64/python2.7/urllib2.py", line 409, in _call_chain
    result = func(*args)
  File "/usr/lib64/python2.7/urllib2.py", line 558, in http_error_default
    raise HTTPError(req.get_full_url(), code, msg, hdrs, fp)
HTTPError: HTTP Error 400: Bad request
Live long and prosper,
Marcelo Magalhães

      
                
                
                    
                                                    Mon, 08/21/2017 - 16:35
                                                                            
                                
                            
                                            
                                            
    
                    
                Live lona and prosper

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Marcelo
The error " HTTPError: HTTP Error 400: Bad Request refers to: a credential issue. I would recommend that you check your credentials of which you are using to register the Aronis Storage Gateway. These credentials should be the credentials of a distributor administrator account or a sub-distributor administrator account.
Please do note that Acronis Storage cannot be registered with an EUC administrator account.
I do hope that the provided information resolves your issue
Best regards
 

      
                
                
                    
                                                    Wed, 08/23/2017 - 08:41
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products
