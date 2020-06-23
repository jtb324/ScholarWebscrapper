import webbrowser
import sys
from CLI_webscrapper import getSoup

# import pyperclip


def opening_browser(dict_row, arg_list):
    search_term = " ".join(arg_list[1:])
    address = dict_row + search_term
    webbrowser.open(address, new=2)

    getSoup(address)


def choose_site(arg_list):
    # Need to search a dictionary for the site title
    site_dict = {
        "nature": "https://www.nature.com/search?q=",
        "acspub": "https://pubs.acs.org/action/doSearch?AllField=",
    }

    if arg_list[0].lower() == "nature":
        opening_browser(site_dict["nature"], arg_list)

    if arg_list[0].lower() == "acspub":
        opening_browser(site_dict["acspub"], arg_list)


def open_site(arg_list):

    choose_site(arg_list)

