#!/usr/bin/env python

import requests
import sys
import time

hostname = '192.168.0.149'
addr = 'http://' + hostname + '/api/core/status'
addr_start = 'http://' + hostname + '/api/core/start'
addr_reboot = 'http://' + hostname + '/api/core/reboot'

def soft_reboot (addr_reqv, step):
	r = requests.get(addr) 
	st = r.json()['running']
	if st == 'running':
		requests.put(addr_reqv, auth=('admin', 'admin')) 
		time.sleep(80)
	elif st == 'not_running':
		requests.put(addr_reqv, auth=('admin', 'admin')) 
		time.sleep(80)

sys.stdout = open('reboot_test.log', 'a')
for i in range (1, 50):
	try:
		soft_reboot(addr_start, i)
		soft_reboot(addr_reboot, i)
#		print 'Step {} successful'.format(i)
	except Exception:
		print 'Step {} error load'.format(i)
sys.stdout.close ()

