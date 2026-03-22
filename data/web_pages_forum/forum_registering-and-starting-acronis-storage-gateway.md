# Registering and starting Acronis Storage Gateway

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/registering-and-starting-acronis-storage-gateway

## Original Post
**Author:** Unknown

Registering and starting Acronis Storage Gateway

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Steven Donohoe
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            This is the error when trying to Register and start 'Acronis Storage Gateway'
Any help or ideas would be great

Failed:
Traceback (most recent call last):
  File "/bin/acronis-storage-registration", line 198, in <module>
    main(parser.parse_args()[0])
  File "/bin/acronis-storage-registration", line 170, in main
    register_storage(args.host, args.owner, args.username, args.password, args.address, args.uid, args.outdir, args.config)
  File "/bin/acronis-storage-registration", line 95, in register_storage
    redirect = json.loads(opener.open(request, data=data).read())
  File "/usr/lib64/python2.7/urllib2.py", line 431, in open
    response = self._open(req, data)
  File "/usr/lib64/python2.7/urllib2.py", line 449, in _open
    '_open', req)
  File "/usr/lib64/python2.7/urllib2.py", line 409, in _call_chain
    result = func(*args)
  File "/usr/lib64/python2.7/urllib2.py", line 1258, in https_open
    context=self._context, check_hostname=self._check_hostname)
  File "/usr/lib64/python2.7/urllib2.py", line 1214, in do_open
    raise URLError(err)
URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:618)>
 
 
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 09/03/2020 - 11:17

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Since Acronis Storage Gateway is EOL, I'm not sure you'll get any support. It's probably better to move to Acronis Cyber Infrastructure 3.5 instead.
I also experienced some issues in the past, and wasn't feeling confident storing my backups on an abandoned solution.
That said, can you try running:
export PYTHONHTTPSVERIFY=0

Before running the acronis-storage-registration command?
You might also want to try setting the correct ownership to the folder with certificates:
chown -R acronis:acronis /etc/pki/tls/certs/Acronis/storage/

      
                
                
                    
                                                    Fri, 09/04/2020 - 13:54
