# ScholarWebscapper

## Goal:

The goal of this project was to create a CLI where you can search different academic journals for keywords to find articles of interest.

## Files:

- **CLI_webscapper.py**: in development

- **open_site.py**: This file contains the functions used to actually open a site in a new tab in a browser. The user can search either the nature journal or the ACS Publishing for articles of interest. The user provides the name of the journal as either nature or ACSPub and then the keywords that they want to look for. A new browser tab is then opened.

- **Webscrap_Interface.py**: This file sets up the CLI for the project using argparse module. It only accepts an input argument at the moment. It runs the open_site function from the open_site.py file.

## In Progress:

- Still would like to be able to extract information about the publications
