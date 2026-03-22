# Receiving error registering our Acronis storage gateway

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/receiving-error-registering-our-acronis-storage-gateway

## Original Post
**Author:** Unknown

Receiving error registering our Acronis storage gateway

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Adam Coon
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            These are the following errors and points of reference as I attempted to follow KB articles to fix:

[root@archivesg1 misc]# acronis-storage-registration -u <admin account email> -p <xxxxx> -s cloud.acronis.com -a 66.57.55.146:44445 -i "ARChive Offsite Storage" -o "/etc/pki/tls/certs/Acronis/storage/"
('POST', 'https://cloud.acronis.com/api/1/groups/self/storages')
Failed:
Traceback (most recent call last):
File "/usr/bin/acronis-storage-registration", line 198, in <module>
main(parser.parse_args()[0])
File "/usr/bin/acronis-storage-registration", line 170, in main
register_storage(args.host, args.owner, args.username, args.password, args.address, args.uid, args.outdir, args.config)
File "/usr/bin/acronis-storage-registration", line 95, in register_storage
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
HTTPError: HTTP Error 401: Unauthorized
***NOTE: Double checked the logon by actually logging into the portal and seeing all of our backup groups.  Is this the correct account information or do we need to use a different one for this registration?


[root@archivesg1 misc]# service acronis-storage-mds status
● acronis-storage-mds.service - SYSV: Acronis Storage Metadata Server
Loaded: loaded (/etc/rc.d/init.d/acronis-storage-mds; bad; vendor preset: disabled)
Active: active (running) since Thu 2017-09-07 11:56:41 EDT; 5h 11min ago
Docs: man:systemd-sysv-generator(8)
CGroup: /system.slice/acronis-storage-mds.service
├─978 /bin/sh /sbin/acronis-storage-run_with_pid_file /run/Acronis/acronis-storage-mds.pid acronis-storage-mds --config-file=/etc/Acronis/acronis-storage-mds.xml
└─993 acronis-storage-mds --config-file=/etc/Acronis/acronis-storage-mds.xml
 
Sep 07 11:56:41 archivesg1.arccgi.com systemd[1]: Starting SYSV: Acronis Storage Metadata Server...
Sep 07 11:56:41 archivesg1.arccgi.com acronis-storage-mds[955]: acronis-storage-mds is stopped
Sep 07 11:56:41 archivesg1.arccgi.com runuser[965]: pam_unix(runuser:session): session opened for user acronis by (uid=0)
Sep 07 11:56:41 archivesg1.arccgi.com runuser[965]: pam_unix(runuser:session): session closed for user acronis
Sep 07 11:56:41 archivesg1.arccgi.com acronis-storage-mds[955]: Starting acronis-storage-mds: [ OK ]
Sep 07 11:56:41 archivesg1.arccgi.com systemd[1]: Started SYSV: Acronis Storage Metadata Server.
 


[root@archivesg1 misc]# service acronis-storage-gateway status
● acronis-storage-gateway.service - SYSV: Acronis Storage Gateway
Loaded: loaded (/etc/rc.d/init.d/acronis-storage-gateway; bad; vendor preset: disabled)
Active: active (exited) since Thu 2017-09-07 17:01:56 EDT; 6min ago
Docs: man:systemd-sysv-generator(8)
Process: 3034 ExecStop=/etc/rc.d/init.d/acronis-storage-gateway stop (code=exited, status=0/SUCCESS)
Process: 3140 ExecStart=/etc/rc.d/init.d/acronis-storage-gateway start (code=exited, status=0/SUCCESS)
 
Sep 07 17:01:56 archivesg1.arccgi.com systemd[1]: Starting SYSV: Acronis Storage Gateway...
Sep 07 17:01:56 archivesg1.arccgi.com acronis-storage-gateway[3140]: acronis-storage-gateway is stopped
Sep 07 17:01:56 archivesg1.arccgi.com runuser[3143]: pam_unix(runuser:session): session opened for user acronis by (uid=0)
Sep 07 17:01:56 archivesg1.arccgi.com acronis-storage-gateway[3140]: Starting acronis-storage-gateway: [ OK ]
Sep 07 17:01:56 archivesg1.arccgi.com systemd[1]: Started SYSV: Acronis Storage Gateway.
 
**** Not sure how to correct this issue.
 


[root@archivesg1 misc]# /usr/sbin/acronis-storage-gateway --config-file=/etc/Acronis/acronis-storage-gateway.xml &
[1] 3252
[root@archivesg1 misc]# Error in application main function: E:980323: K:/23/products/as/ssl/certificates_manager.cpp:181 (LoadFiles) Bad own x509 file '/etc/pki/tls/certs/Acronis/storage/fes.pem'.
 


[root@archivesg1 misc]# openssl crl -in /etc/pki/tls/certs/Acronis/storage/reg.crl -noout -text
/etc/pki/tls/certs/Acronis/storage/reg.crl: No such file or directory
 


[root@archivesg1 misc]# openssl x509 -in /etc/pki/tls/certs/Acronis/storage/reg.crt -text
Error opening Certificate /etc/pki/tls/certs/Acronis/storage/reg.crt
139809670780832:error:02001002:system library:fopen:No such file or directory:bss_file.c:398:fopen('/etc/pki/tls/certs/Acronis/storage/reg.crt','r')
139809670780832:error:20074002:BIO routines:FILE_CTRL:system lib:bss_file.c:400:
unable to load certificate
 


      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 09/08/2017 - 21:34

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Adam Coon
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Reviewed very similar post: https://forum.acronis.com/forum/acronis-backup-cloud-forum/error-attemp…
The solutions offered there were already attempted, I think it may possibly be with the SSL cert, I don't see any in the folder (/etc/pki/tls/certs/Acronis/storage/) can I download this to manually install or am I off target?
Thanks in advance.
Adam

      
                
                
                    
                                                    Fri, 09/08/2017 - 21:41
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Adam,
Based on your question:
"Is this the correct account information or do we need to use a different one for this registration?"
The account that you need to use should be the credentials of a distributor administrator account or a sub-distributor administrator account.
Please do note that Acronis Storage cannot be registered with an EUC administrator account.
Can you please advise to the backend storage you are using for example: Local storage, S3 etc
Can you then also ensure that the correct backend library is installed using the command:
ls -l /usr/lib/Acronis
Depending on your backend you should see something similar to:
acronis-storage-backend-local.so
Regards
 

      
                
                
                    
                                                    Tue, 09/19/2017 - 08:06
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products
