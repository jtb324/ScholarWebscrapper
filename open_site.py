import webbrowser
import sys
from CLI_webscrapper import getSoup
from Cell_webscrapper import getSoupCell
from ACS_webscrapper import getSoupACS
from Med_Genetics_webscrapper import getSoupMedGenetics

# import pyperclip
def open_browser(address):
    """This function opens the browser if a specifc argument is selected"""
    webbrowser.open(address, new=2)


def make_address(dict_row, arg_list):
    search_term = " ".join(arg_list[1:])
    address = dict_row + search_term
    return address


def make_address_mod(dict_row, arg_list):
    """This function is used to add extra info to the search term so that it will seaarch the Cell site"""
    search_term = " ".join(arg_list[1:])
    address = dict_row[0] + search_term + dict_row[1]
    return address


def choose_site(arg_list, openBrowser):
    # Need to search a dictionary for the site title
    site_dict = {
        "nature": "https://www.nature.com/search?q=",
        "acspub": "https://pubs.acs.org/action/doSearch?AllField=",
        "cell-ajhg": [
            "https://www.cell.com/action/doSearch?searchType=quick&searchText=",
            "&searchScope=fullSite&journalCode=ajhg&seriesISSNFltraddfilter=0002-9297&occurrences=all&code=cell-site&journalCode=ajhg",
        ],
        "medical_genetics": "https://jmg.bmj.com/search/",
    }

    if arg_list[0].lower() == "nature":
        address = make_address(site_dict["nature"], arg_list)
        getSoup(address)
        if openBrowser == True:
            open_browser(address)

    if arg_list[0].lower() == "acspub":
        address = make_address(site_dict["acspub"], arg_list)
        getSoupACS(address)
        if openBrowser == True:
            open_browser(address)

    if arg_list[0].lower() == "cell-ajhg":
        address = make_address_mod(site_dict["cell-ajhg"], arg_list)
        getSoupCell(address)
        if openBrowser == True:
            open_browser(address)

    if arg_list[0].lower() == "medical_genetics":
        address = make_address(site_dict["medical_genetics"], arg_list)
        getSoupMedGenetics(address)
        if openBrowser == True:
            open_browser(address)


def open_site(arg_list, openBrowser):

    choose_site(arg_list, openBrowser)

