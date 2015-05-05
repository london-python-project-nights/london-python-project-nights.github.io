# london-python-project-nights.github.io

This is the home page of London Python Project Nights. 

In the aims of simplicity this is all static html with minimal theming.

## To edit a page

While it is possible to simply edit the html file that maps to each page, these are generated from Jinja2 templates, and so direct changes will be lost when further changes are made. The preferred method is therefore to edit the template that is used to generate said page. It shuld be reasonably easy to find this by looking in [build.py](build.py). Once you have edited said tempate, run `python build.py` to generate the full html output files. Constructing pages in this way makes it much easier to keep consistency in the nav bar and any other chrome around the page content.

## To create a new page

Simply create a new template that extends [base.html](templates/html/base.html), add an extra entry to [build.py](build.py) and add a link within [nav.html](templates/html/nav.html) to the generated page name. Once you have run `python build.py` you should find that the page has been generated and is linked on the nav bar.

## Testing changes

To test your changes run `python test.py` and connect to [localhost:8080](http://localhost:8080/)