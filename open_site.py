import webbrowser
import sys

# import pyperclip


def opening_browser(address):
    webbrowser.open(address, new=2)


def choose_site(arg_list):
    # Need to search a dictionary for the site title
    site_dict = {
        "nature": "https://www.nature.com/search?q=",
        "ACSPub": "https://pubs.acs.org/action/doSearch?AllField=",
    }

    if arg_list[0].lower() in site_dict:
        search_term = " ".join(arg_list[1:])
        address = site_dict["nature"] + search_term
        opening_browser(address)


def open_site(arg_list):

    choose_site(arg_list)

