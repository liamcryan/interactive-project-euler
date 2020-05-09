=============
ieuler online?
=============

I don't think I can use docker to build the environment because I will be calling docker within the application.

So this is a docker-in-docker situation, which I am reading may need special privileges, which seems bad for security.
But see this: https://stackoverflow.com/questions/27879713/is-it-ok-to-run-docker-from-inside-docker

Requires:
- docker
- ttyd
- python
- some web server
- some hosting

https://interactiveprojecteuler.liamcryan.com

It will be hosted on Digital Ocean because I like it.


Step 1. Make this into a github repository.
Step 2. Deploy to Digital Ocean.
Step 3. Figure out domain stuff.
Step 4. ieuler-server.