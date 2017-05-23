from django.http import HttpResponse
from django.shortcuts import render
import re
import random
import os
import socket
import sys
import netmiko
import subprocess
import time
from getpass import getpass
from ciscoconfparse import CiscoConfParse
from html_crap import *

def get_date_and_time():
	date_and_time = ''
	parts = ["%y","%m","%d","%H","%M","%S"]
	for part in parts:
		print
		date_and_time = date_and_time + "_"
		date_and_time = date_and_time + time.strftime(part)
	date_and_time = date_and_time[1:] 
	return date_and_time

def open(program_to_call,args):
	command = ['python', program_to_call]+args
	#for each in args:
	#	command = command + each+ " "
	print (command)
	proc = subprocess.Popen(command)
	proc.wait()



def home(request):
	return render(request, 'tracert.html')
	
def tracert_tshoot(request):
	trace_route = request.POST["trace_route"]
	username = request.POST["username"]
	password = request.POST["password"]
	html_file_name = get_date_and_time() + '.html'
	arguments_to_pass = [username,password,trace_route,html_file_name]
	print (arguments_to_pass)
	open("Tracert V2.py",arguments_to_pass)
	#time.sleep(160)
	return render(request, html_file_name)
	
	
def get_ip (input):
	return(re.findall(r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)', input))
