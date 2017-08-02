# ethermine_alert.py

Written by /u/ExploitZero. Constructive feedback is always welcome. Feel free to modify this script for your own needs.

Purpose:
  Monitor Ethermine to determine whether your rigs are active and performing as expected.

Usage:

    Run this script from a Linux system that is NOT one of your rigs.

    1) Create a new Gmail account with a username and password you do not use for other websites.
    2) Copy this script into your preferred directory. Ensure that it is executable by issuing the 'chmod a+x ethermine_alert.py' command.
    3) Use a text editor (e.g., nano) to replace all items in USER DEFINED VARIABLES section with your rig's wallet address, your new gmail credentials, and the email to SMS addresses you'd like to receive the alerts.
    4) Issue the 'crontab -e' command and append '*/5 * * * * python /full/path/to/ethermine_alert.py' to the file (for a check every 5 minutes).

    If you would like to run a test to make sure the script is working, modify the 'my_total_hashrate_threshold' variable to a number absurdly high for your workers, then issue the './ethermine_alert.py' command

Feeling generous?

     ETH:0x09439AD892a676a814aEA49aF2e0e8ee3106F11B
     BTC:14y78wmeJJhgZR9w1q468zvbmqFaWGKsku
