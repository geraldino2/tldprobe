#!/usr/bin/env python3

import sys, subprocess, datetime

base = sys.argv[1]

with open('output/combinations-{}.txt'.format(base), 'a') as output_file:
	cctlds = gtlds = []
	with open('cctlds.txt', 'r') as cctlds_file:
		cctlds = cctlds_file.read().splitlines()
	with open('short_gtlds.txt', 'r') as gtlds_file:
		gtlds = gtlds_file.read().splitlines()
	for cctld in cctlds:
		for gtld in gtlds:
			output_file.write("{}.{}.{}\n".format(base, gtld, cctld))
	with open('tlds.txt', 'r') as tlds_file:
		for tld in tlds_file:
			output_file.write("{}.{}".format(base, tld))
subprocess.call(['httpx', '-l', 'output/combinations-{}.txt'.format(base), '-location', '-content-length', '-status-code', '-title', '-silent', '-ports', '80,443,8008,8080,8443', '-o', 'output/http-{}.txt'.format(base)])
