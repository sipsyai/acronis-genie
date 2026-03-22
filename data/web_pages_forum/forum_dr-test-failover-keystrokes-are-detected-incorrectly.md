# DR :: test-failover keystrokes are detected incorrectly

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/dr-test-failover-keystrokes-are-detected-incorrectly

## Original Post
**Author:** Unknown

DR :: test-failover keystrokes are detected incorrectly

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Nils Reuter
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi all.
It is impossible for me to send the #-key to the server via the Acronis console during a test failover. It always returns a 3 to the server. If I use the ASCII code for the # character it also returns a 3. The whole keyboard layout is somehow wrong. Server are in german, keyboard layout too. I also tried to set the layout to english. Same error.
Is it the console of Acronis or is the backup corrupted in some way?
Has anyone ever had this problem and know how to fix it? 
 
Regards
Nils

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 08/11/2021 - 08:13

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Alexey Dorofeev
                            

                            
                    
                        Senior Support Engineer 
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Nils!
Please provide general information:
1- What is the recovery server's operating system? Version + build.
2- Please try to reproduce the issue using other browsers (IE 11, Edge, Firefox, Chrome) and provide what browser version you're using on each test.
Here are possible workarounds:
1- Try to use CTRL+ALT and intended # keystroke
2- Install VMware tools > new backup > use this recovery point as a test.
Otherwise you can install vmware tools just after Recovery server activation from inside Operating System:

Download link: https://my.vmware.com/en/web/vmware/downloads/details?downloadGroup=VMTOOLS1130&productId=1073&rPId=68195 

3- Switch keyboard layout on production server to U.S. International Keyboard > new backup > use this recovery point for testing
4- Submit a case to support@acronis.com for further investigation

      
                
                
                    
                                                    Tue, 08/17/2021 - 15:16
                                                                            
                                
                            
                                            
                                            
    
                    
                Alexey Dorofeev | Senior Support Engineer

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                            
                Products: 
                Acronis Cyber Infrastructure
