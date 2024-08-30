import argparse
import re
import os

def _validate_mail(string: str):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    return re.fullmatch(regex, string)

def _validate_file(filepath: str):
    return os.path.isfile(filepath)

def read_args():
    parser = argparse.ArgumentParser(description= "Cli based email sender.")
    parser.add_argument("-f", "--file", help="Attach email/txt file")
    parser.add_argument("-s", "--sender", help="Specify sender's email")
    parser.add_argument("-r", "--receiver", help="Specify recipient's email")
    args = parser.parse_args()
    args = vars(args)
    if not _validate_mail(args["sender"]) :
        print("Error: No sender email")
    elif not _validate_mail(args["receiver"]): 
        print("Error: No receiver email")
    else:
        return args
    return None
