=========================
Interactive Project Euler
=========================

Use the Interactive Project Euler command line tool in a browser.

Installation
------------

should have liamcryan/ieuler image update automatically & restart - same with liamcryan/ieuler-server

these instructions: https://certbot.eff.org/lets-encrypt/debianbuster-nginx

First download & install necessary things on linux machine.  Check here for docker-compose download command: https://docs.docker.com/compose/install/ and replace below if necessary::

    $ sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get install git curl docker.io -y
    $ sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    $ sudo chmod +x /usr/local/bin/docker-compose

Then download & install interactive project euler::

    $ git clone https://github.com/liamcryan/interactive-project-euler.git

Add the environment (change localhost to your host)::

    $ echo "MYSQL_USER=<someuser>\nMYSQL_PASSWORD=<somepass>\nMYSQL_DATABASE=ieuler" > .mysql-env
    $ echo "NGINX_HOST=localhost" > .nginx-env

Start docker-compose (http only)::

    $ docker-compose up -d

Now play on http://localhost:80.

See https://github.com/liamcryan/ieuler for more details on using the command line tool.

See https://github.com/liamcryan/ieuler-server for more details on the server saving your data.

For https, follow certbot installation instructions, then eventually run::

    $ sudo certbot certonly --webroot -w ~/interactive-project-euler/tmp/ -d www.localhost -d localhost
    $ sudo chmod 755 /etc/letsencrypt/archive/

Now you need to verify that the NGINX_HOST is correct in this volumes to the .pem files.

Finally, uncomment ssl related lines in nginx.conf.template.

Then::

    $ sudo docker-compose up -d

Note: using localhost in this way will not get you https.
