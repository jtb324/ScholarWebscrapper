import webbrowser
import sys
from CLI_webscrapper import getSoup
from Cell_webscrapper import getSoupCell

# import pyperclip


def opening_browser(dict_row, arg_list):
    search_term = " ".join(arg_list[1:])
    address = dict_row + search_term
    webbrowser.open(address, new=2)
    return address


def opening_browser_mod(dict_row, arg_list):
    """This function is used to add extra info to the search term so that it will seaarch the cell site"""
    search_term = " ".join(arg_list[1:])
    address = dict_row[0] + search_term + dict_row[1]
    webbrowser.open(address, new=2)
    return address


def choose_site(arg_list):
    # Need to search a dictionary for the site title
    site_dict = {
        "nature": "https://www.nature.com/search?q=",
        "acspub": "https://pubs.acs.org/action/doSearch?AllField=",
        "cell-ajhg": [
            "https://www.cell.com/action/doSearch?searchType=quick&searchText=",
            "&searchScope=fullSite&journalCode=ajhg&seriesISSNFltraddfilter=0002-9297&occurrences=all&code=cell-site&journalCode=ajhg",
        ],
    }

    if arg_list[0].lower() == "nature":
        address = opening_browser(site_dict["nature"], arg_list)
        getSoup(address)

    if arg_list[0].lower() == "acspub":
        address = opening_browser(site_dict["acspub"], arg_list)
        # TODO: need to make a function to get the soup for the acspub site

    if arg_list[0].lower() == "cell-ajhg":
        address = opening_browser_mod(site_dict["cell-ajhg"], arg_list)
        getSoupCell(address)


def open_site(arg_list):

    choose_site(arg_list)

