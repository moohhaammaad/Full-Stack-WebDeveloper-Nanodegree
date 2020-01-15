Linux-Server-Configuration project Overview 
-------------------------------------------
-This project involves taking a baseline installation of Linux on a virtual machine and
 preparing it to host web applications. This includes installing updates,securing the
 server from attacks, and installing / configuring web and database servers.

Accessing 
---------
- IP address : `18.194.44.232`
- SSH port : `2200`
- Webpage URL : (http://18.194.44.232) 

Get my server steps
-------------------
- Sign in to (https://lightsail.aws.amazon.com/ls/webapp) using an Amazon Web Services account.

- Follow the 'Create an instance' link.

- Choose the 'OS Only' and 'Ubuntu 16.04 LTS' options.

- Choose a payment plan.

- Give the instance a unique name and click 'Create'.

- Wait for the instance to start up.

- Download the instance's private key by navigating to the Amazon Lightsail 'Account page'.

- Click on 'Download default key'.

- A file called LightsailDefaultPrivateKey.pem (I change it to key.pem) will be downloaded; open this in a text editor.


Secure the server
-----------------
3- update all currency installed packages:
     `sudo apt-get update
      sudo apt-get upgrade`

4- change the ssh from 22 to 2200
    >> `sudo nano /etc/ssh/sshd_config` (change the ssh port from 22 to 2200)

5- configure the uncomplicated
    >> `sudo ufw default deny incoming`

    >> `sudo ufw default allow outgoing`
	 
    >> `sudo ufw allow ssh`

    >> `sudo ufw allow 2200/tcp`

    >> `sudo ufw allow www`

    >> `sudo ufw allow ntp`

    >> `sudo ufw enable`

    >> `sudo ufw status`

Give grader access
------------------
6- create a new user (grader)
    >> `sudo adduser grader`
	
7- give the grader sudo permission
     >> `sudo nano /etc/sudoers.d/grader`

	 - add this text to the created file	>> `grader ALL=(ALL:ALL) ALL`
	 
8- create an ssh key pair for grader	
     - On the local system, Go to the directory where you want to save the Key,
	   and run the following command  >> `ssh-keygen`

     - Log into the remote VM as root user through ssh and open the following file >> `cat /.ssh/authorized_keys` ,
       then copy the content of the file at >> `sudo nano /home/grader/.ssh/authorized_keys`  
	 
         - Change the SSH port from 22 to 2200, Enforce key-based authentication &  Disable login for root user.
       	 
         - Run >> `sudo nano /etc/ssh/sshd_config` 

		- go to Port line and edit it from 22 to 2200.

		- go to PasswordAuthentication line and edit it to no.

		- go to PermitRootLogin line and edit it to no. 

		- save the file then restart the service by run >> `sudo service ssh restart` .

>> `ssh grader@18.194.44.232 -p 2200  -i m` (login into grader user now where i saved the private key file as m)    
		
Deploy the project 
------------------
9- Configure the local timezone to UTC:
    >>  `sudo timedatectl set-timezone UTC`
	
10- Install and configure Git, Apache2 to serve a Python mod_wsgi application :

    >> `sudo apt-get install apache2 libapache2-mod-wsgi git`. (this cmd will install apache2 and mod-wsgi and git)
	
    >> `sudo a2enmod wsgi`  (check if wsgi enabled or not)

11- Update all currently installed packages:

    >> `sudo apt-get update`

    >> `sudo apt-get upgrade`
 
12- Install and configure PostgreSQL :

     >> `sudo apt-get install libpq-dev python-dev`  (Installing PostgreSQL Python dependencies)
	 
 	 >> `sudo apt-get install postgresql postgresql-contrib`  (Installing PostgreSQL)

     >> `sudo cat /etc/postgresql/9.5/main/pg_hba.conf`  (Check if no remote connections are allowed)

     >> `sudo su - postgres`  (Login as postgres User )

         >> `psql` (get into PostgreSQL shell then follow this steps)

	     `# CREATE USER catalog WITH PASSWORD 'password';`  (Create a new User named catalog)

		 `# CREATE DATABASE catalog WITH OWNER catalog;`    (Create a new DB named catalog)

		 `# \c catalog`   (Connect to the database catalog)

		 `# REVOKE ALL ON SCHEMA public FROM public;`   (Revoke all rights)

		 `# GRANT ALL ON SCHEMA public TO catalog;`    (Lock down the permissions only to user catalog)

		 `# \q`    (Log out from PostgreSQL)

		 `$ exit` (return to the grader user)
		 
	 -Install Flask & other dependencies in global :

	    >> `sudo apt-get install python-pip`

            >> `sudo pip install Flask`

            >> `sudo pip install httplib2 oauth2client sqlalchemy psycopg2 sqlalchemy_utils`	 
		
	 - Inside the Flask application change DB connection in all .py files to be :
	 
	    >> `engine = create_engine('postgresql://catalog:password@localhost/catalog')`
	 
13 - follow this steps to clone the item catalog from github in current machine :

     >> `sudo mkdir /var/www/catalog` (make directory called catalog in /var/www/)

     >> `sudo chown -R grader:grader /var/www/catalog` (Change the owner of the directory catalog)

     >> `git clone https://github.com/moohhaammaad/Item-catalog.git catalog` (Clone the Item-catalog to the catalog directory)	 
     
     >> `cd /var/www/catalog`

     >> `nano catalog.wsgi` (make this file inside the catalog directory and put the following content inside it):
         
         - the content :
                          `#!/usr/bin/python
                           import sys
                           import logging
                           logging.basicConfig(stream=sys.stderr)
                           sys.path.insert(0, "/var/www/catalog/")
                           from final import app as application` 
   
14 - enable a virtual host :

     >>	`sudo nano /etc/apache2/sites-available/000-default.conf` (open this file and edit it with the follwing content)
         
        - the content :
                         `<VirtualHost *:80>
                            ServerName 18.194.44.232
                            ServerAdmin midomedo33@gmail.com
                            WSGIScriptAlias / /var/www/catalog/catalog.wsgi
                            <Directory /var/www/catalog/>
                                Order allow,deny
                                Allow from all
                            </Directory>
                            Alias /static /var/www/catalog/catalog/static
                            <Directory /var/www/catalog/static/>
                                Order allow,deny
                                Allow from all
                            </Directory>
                            ErrorLog ${APACHE_LOG_DIR}/error.log
                            LogLevel warn
                            CustomLog ${APACHE_LOG_DIR}/access.log combined
                         </VirtualHost>`

15 - Restart the Apache to launch the app on the server:

     >> `sudo service apache2 restart`

16 - if the app not launch check this cmd to see what the error:

     >> `sudo cat /var/log/apache2/error.log` 
         (the previous cmd check what the error with the apache & i fixed all major errors that was prevent my app to be launched)                               

References used
---------------
- flask documentation >> (http://flask.pocoo.org/docs/0.12/installation/).

- Digital ocean site To Install the Apache Web Server on Ubuntu 16.04 
   >>(https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-16-04).
	 