#!/usr/bin/env python3

from os import environ
from sys import exit

from multilanguage import *
from hash_and_cipher import hash_value

ENV_lang = environ.get("TAL_lang")
ENV_white_string = environ.get("TAL_white_string")
ENV_hash_type = environ.get("TAL_hash_type")
ENV_colored_feedback = (environ.get("TAL_ISATTY") == "1")
    
set_colors(ENV_colored_feedback)
messages_book = select_book_and_lang("compute_hash_server", ENV_lang)

def print_lang(msg_code, *msg_rendering, **kwargs):
    msg_text=eval(f"f'{messages_book[msg_code]}'")
    TAcprint(msg_text, *msg_rendering, **kwargs)

        

if ENV_white_string not in {None, "None"}:
    print_lang("give-only-hash", "yellow")
    #All-languages: print(f"{hash_value(ENV_white_string,ENV_hash_type)}")
else:
    print_lang("open-channel", "green")        
    #English: print(f"# I will serve: problem=morra, service=compute_hash, white_string={ENV_white_string}, hash_type={ENV_hash_type}, colored_feedback={ENV_colored_feedback}, lang={ENV_lang}.")

    print_lang("ask-for-white-string", "yellow", ["bold"])
    #English: print("Since the parameter white_string was not specified in this call, we now ask you to insert the string in white, of which to compute the hash:");
    white_str=input()
    print_lang("give-hash-verbose", "yellow")
    #All-languages: print(f"h({white_str}) = {hash_value(white_str,ENV_hash_type)}")
    
exit(0)
