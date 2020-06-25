# ScholarWebscapper

## Goal:

The goal of this project was to create a CLI where you can search different academic journals for keywords to find articles of interest. It currently can search Nature, Cell, and ACS Publishing

Currently works for four journals. They are listed below along with the ideal way to enter them in the command line in parentheses:

- Nature: (nature)
- Cell: (cell)
- ACS Publishing: (acspub)
- The Journal of Medical Genetics: (med_genetics)

## Files:

- **CLI_webscapper.py**: This file uses beautifulsoup and requests modules to fetch the desired webpage and then to collect it as a soup. It can then pull the article title, the date published, and the journal published in from that soup and write it to a text file to be used to find the most interesting articles.

- **open_site.py**: This file contains the functions used to actually open a site in a new tab in a browser. The user can search either the nature journal for for articles of interest. The user provides the name of the journal as either nature or ACSPub and then the keywords that they want to look for. A new browser tab is then opened.

- **Webscrap_Interface.py**: This file sets up the CLI for the project using argparse module. It only accepts an input argument at the moment. It runs the open_site function from the open_site.py file.

* **Cell_webscrapper.py**: This file does the same as the open_site.py file. It takes the address of the site and finds the article title, the authors, the journal published in, and the date published and prints it to a text file. There is a weird that that happens where it prints more than the title such as the saying "cited in scropus" and then it adds volume numbers to the journal for some entry.

* **ACS_webscrapper.py**: This file does the same as the Cell_webscrapper.py except it works for the ACS publishing site instead of cell.

* **Med_Genetics_webscrapper.py**: This file does the same thing as the other \*\_webscrapper.py for the journal of Medical Genetics.

## In Progress:

- also need to write it so that you can either visit the page or you could get the list generated, not both.
