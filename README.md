# MAILCLI

![Demo Video](static/video.webm)

A mail client that is used to email text files. The package has beeen properly tested in order to prevent from security issues and has been developed in a user friendly manner

## Prerequisite

- python3
  - smtplib
  - argparse

## Run Program 

`python ./main.py -s <sender-email> -r <recipient-email> -f <email-file>.txt` 

The above command will initiate a mail job with an initial procedure of validating auth password or sender-email 

## Usage 

- Automated email 
- Extensive sender email clients available (outlook, hotmail, yahoo)

## Issues 

- GMail as sender email is not supported
