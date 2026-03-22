# Issue with Module Compilation on Oracle Linux 8 After Updating SnapAPI to 26.0.8.42

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/issue-module-compilation-oracle-linux-8-after-updating-snapapi-260842

## Original Post
**Author:** Unknown

Issue with Module Compilation on Oracle Linux 8 After Updating SnapAPI to 26.0.8.42

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Daniel Pereira
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Good morning,
After updating the snapapi module to version 26.0.8.42, our Oracle Linux servers, which have GCC 8.5 installed, are no longer able to compile the required modules. Is there any way to work around this issue? None of the machines running Oracle Linux 8 can compile the modules anymore.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 12/09/2024 - 19:05

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daniel Pereira
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I noticed that the DKMS used in Acronis cannot compile because it uses GCC version 11 (for compilation), but our servers are using version 8.5. How can I make DKMS compile the system modules without having to change the GCC version on our servers?

      
                
                
                    
                                                    Mon, 12/09/2024 - 22:36
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Please review the following:
Cyber Protect supports x86 and x86_64 Linux distributions that use the following components:

Kernel version: From 2.6.9 to 6.9
	Supported kernel versions are listed according to the releases on www.kernel.org. Some distributions, such as Red Hat Enterprise Linux, backport new features to older kernel versions. These distribution-specific kernels might not be supported even if their version falls within the supported range.


GNU C Library (glibc): Version 2.3.4 or later

The following distributions have been specifically tested. However, even if your Linux distribution or kernel version is not listed, it might still function correctly in all required scenarios due to the flexibility of Linux operating systems. If you encounter issues while using Cyber Protect with your distribution and kernel version combination, please contact the Support team for further investigation.
Installing the protection agent on Oracle Linux 8.6 and later, on which Secure Boot is enabled, requires manual signing of kernel modules. For more information on how to sign a kernel module, refer to this knowledge base article ( Also https://care.acronis.com/s/article/62490-Acronis-Cyber-Protect-Acronis-… ).
Rebooting the machine may resolve certain issues with the Snap API, so you may consider this as a troubleshooting step.
If your environment is supported, I recommend raising a ticket with our team: https://support.acronis.com/.
Best regards.

      
                
                
                    
                                                    Tue, 12/10/2024 - 08:54
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daniel Pereira
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I did everything in the manual, but the error persists

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      643391-453227.png

                      37.44 KB
                  
          
    

                    
    
                
                
                    
                                                    Tue, 12/10/2024 - 15:26
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Daniel Pereira wrote:

I did everything in the manual, but the error persists


Hello!
First, install the kernel sources that exactly match your kernel version: see product documentation for instructions.
After installing the necessary sources, repeat Agent for Linux installation on the machine.
If this does not resolve the issue, collect system information from Acronis management server and the affected agent and contact Acronis Support ( or your service provider ) with reference to this article.
Best regards.
 

      
                
                
                    
                                                    Wed, 12/11/2024 - 08:45
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daniel Pereira
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            managed to complete the installation, but the module is not reloaded due to the unsigned key. Is it possible to sign it without the need to restart the server or enter the BIOS?

      
                
                
                    
                                                    Thu, 12/12/2024 - 16:07
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Daniel Pereira wrote:

managed to complete the installation, but the module is not reloaded due to the unsigned key. Is it possible to sign it without the need to restart the server or enter the BIOS?


In Oracle Linux 8, you can sign and reload a kernel module without restarting the server or entering the BIOS by following these steps:

Locate Signing Tools: Ensure the kernel-devel and openssl packages are installed:
sudo dnf install kernel-devel openssl 


Sign the Module: Use the sign-file script from the kernel source:
/usr/src/kernels/$(uname -r)/scripts/sign-file sha256 private_key.pem public_key.der /path/to/module.ko 


Load the Signed Module: Remove the unsigned module and load the signed one:
sudo rmmod module_name sudo insmod /path/to/module.ko 

Ensure your keys match the ones configured for module verification in your kernel.
Best regards.
 

      
                
                
                    
                                                    Thu, 12/12/2024 - 17:53
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daniel Pereira
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I have an AlmaLinux 8 that is also experiencing the issue. Does this solution work for it as well?

      
                
                
                    
                                                    Thu, 12/12/2024 - 19:00
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Daniel Pereira wrote:

I have an AlmaLinux 8 that is also experiencing the issue. Does this solution work for it as well?


Did it work for the original machine?
If not, I recommend submitting a ticket with our team so we can thoroughly review the situation.
If it worked for the original system, you can give it a try.
Best regards.

      
                
                
                    
                                                    Fri, 12/13/2024 - 16:57
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daniel Pereira
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
             
I have identified an issue related to the version of the snapapi26 module being downloaded by the Acronis agent for kernel 4.18. Upon analyzing DKMS, I noticed that the agent is always downloading version 0.8.34, while in a new VM identical to the server setup, version 0.8.42 was downloaded and installed without requesting a signature.
Since Acronis is not automatically downloading the correct version of the module on the servers, I would like to request version snapapi26-0.8.42 so I can manually compile and install it on the servers. This will allow me to resolve the issue without relying on the older version.
Thank you for your assistance, and I look forward to receiving the correct version to continue with the installation.
Best regards,

      
                
                
                    
                                                    Fri, 12/13/2024 - 17:35
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Daniel Pereira wrote:

 
I have identified an issue related to the version of the snapapi26 module being downloaded by the Acronis agent for kernel 4.18. Upon analyzing DKMS, I noticed that the agent is always downloading version 0.8.34, while in a new VM identical to the server setup, version 0.8.42 was downloaded and installed without requesting a signature.
Since Acronis is not automatically downloading the correct version of the module on the servers, I would like to request version snapapi26-0.8.42 so I can manually compile and install it on the servers. This will allow me to resolve the issue without relying on the older version.
Thank you for your assistance, and I look forward to receiving the correct version to continue with the installation.
Best regards,


Hello Daniel,
As mentioned above, this must be requested through our support team.
You can contact our support or your service provider (if you aren’t eligible for direct support) so we can review the issue and provide you with a solution.
Best regards.

      
                
                
                    
                                                    Mon, 12/16/2024 - 11:12
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
