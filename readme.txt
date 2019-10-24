# password-manager
#DISCLAIMER: THIS PASSWORD MANAGER IS NOT SECURE. I'M NOT RESPONSIBLE FOR LOSS OR THEFT OF SENSITIVE DATA.
python script to allow user to save and access passwords quickly from terminal using simple commands

>SALIENT FEATURES
 1) stores passwords for different services locally on the hard drive.
 2) suggests strong passwords when asked for.
 3) copies passwords when needed to clipboard for use in other places.
 
>HOW TO USE THIS PASSWORD MANAGER?
 just save the python file to any location on your machine that seems convenient to you. Open terminal or command prompt on the machine  
 and run the python script using the command (keep in mind that this script won't work in IDLE or VS Code or other IDEs and has to be    
 executed form the terminal or command prompt):
     
     python3 pwm.py -arguement  [FOR MAC USERS]
     
 you can use similar syntax for other operating systems.
 The real magic of the program lies in the arguements which you will supply in the command. The arguements which you can pass are:
 
 1) new/edit
  
  syntax : python3 pwm.py new OR python3 pwm.py edit
  
  use: allows you to add passwords for new services or modify existing passwords.
 
 2) <service_name>
  
  syntax : python3 pwm.py <service_name>
  
  use: copies the requested password of <service_name> to keyboard.

 3) delete
  
  syntax : python3 pwm.py delete
  
  use: allows you to delete the stored password for a service.
 
 4) all
  
  syntax : python3 pwm.py all
  
  use: prints the names of services whose passwords are being currently stored in memory
 
