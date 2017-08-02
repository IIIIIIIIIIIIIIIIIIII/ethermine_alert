#!/usr/bin/env python
#
# Written by /u/ExploitZero. Constructive feedback is always welcome. Feel free to modify this script for your own needs.
#
# Purpose:
#
#    Monitor Ethermine to determine whether your rigs are active and performing as expected.
#
# Usage:
#
#    Run this script from a Linux system that is NOT one of your rigs.
#
#    1) Create a new Gmail account with a username and password you do not use for other websites.
#    2) Copy this script into your preferred directory. Ensure that it is executable by issuing the 'chmod a+x ethermine_alert.py' command.
#    3) Use a text editor (e.g., nano) to replace all items in USER DEFINED VARIABLES section with your rig's wallet address, your new gmail credentials, and the email to SMS addresses you'd like to receive the alerts.
#    4) Issue the 'crontab -e' command and append '*/5 * * * * python /full/path/to/ethermine_alert.py' to the file (for a check every 5 minutes).
#
#    If you would like to run a test to make sure the script is working, modify the 'my_total_hashrate_threshold' variable to a number absurdly high for your workers, then issue the './ethermine_alert.py' command
#
# Feeling generous?
#
#     ETH:0x09439AD892a676a814aEA49aF2e0e8ee3106F11B
#     BTC:14y78wmeJJhgZR9w1q468zvbmqFaWGKsku
#

##########################
# USER DEFINED VARIABLES #
##########################

my_wallet_address = '0xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
my_gmail_account = 'myrigmonitoremail@gmail.com'
my_gmail_password = 'myrigmonitoremailgmailpassword'
my_recipients = ['1234567890@txt.att.net','myalertrecipientemail@site.com']
my_total_hashrate_threshold = 500
my_worker_hashrate_threshold = 70

########
# Main #
########

import urllib2
import json
import smtplib

issue = False
message = 'There may be an issue with one of your rigs.\n\n'

json_output = json.load(urllib2.urlopen(urllib2.Request('https://ethermine.org/api/miner_new/'+ my_wallet_address, headers={'User-Agent' : 'Magic Browser'})))
for majorkey, subdict in json_output.iteritems():
    if majorkey == 'workers':
        worker_names = subdict
    if majorkey == 'hashRate':
        total_hashrate = subdict

if float(total_hashrate.split(" ")[0]) < my_total_hashrate_threshold:
    issue = True
    message += 'Total hashrate is %s, which is below the threshold set at %s MH/s.\n\n' % (total_hashrate, my_total_hashrate_threshold)

for key, subdict in worker_names.iteritems():
    worker_name = subdict
    for key, value in worker_name.iteritems():
        if key == 'worker':
            message += "%s:%s\n" % (key,value)
        if key == 'hashrate':
            message += "    %s:%s\n" % (key,value)
            if float(value.split(" ")[0]) < my_worker_hashrate_threshold:
                issue = True
                message += 'Hashrate is below the threshold set at %s MH/s.\n\n' % (my_worker_hashrate_threshold)

def send_emails():
    subject = 'Rig Issue'
    smtpserver = smtplib.SMTP('smtp.gmail.com',587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(my_gmail_account, my_gmail_password)
    msg = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (my_gmail_account, my_recipients, subject, message)
    smtpserver.sendmail(my_gmail_account, my_recipients, msg)
    smtpserver.close()

if issue == True:
    send_emails()
else:
    print "No issues found."
