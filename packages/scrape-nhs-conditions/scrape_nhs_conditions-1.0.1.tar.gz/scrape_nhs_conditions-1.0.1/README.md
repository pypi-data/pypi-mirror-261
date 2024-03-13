# Scrape NHS Conditions 

![Build](https://github.com/nhsengland/scrape_nhs_conditions/actions/workflows/ci.yml/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This package uses the [NHS Website Developer portal](https://developer.api.nhs.uk/nhs-api) and [Scrapy](https://scrapy.org/) to pull down the text content of the [NHS Conditions](https://www.nhs.uk/conditions/) website into text files for downstream use by data science projects.

This is a simplified version of the work found here: https://github.com/nhsx/language-corpus-tools

## Contact
**This repository is maintained by [NHS England Data Science Team](datascience@nhs.net)**.
> _To contact us raise an issue on Github or via email._
> 
> See our (and our colleagues') other work here: 
> - [NHS England Analytical Services](https://github.com/NHSDigital/data-analytics-services)
> - [NHSX](https://github.com/nhsx)

## Description

There is a need for easy access to the text content of NHS Conditions, particularly [given the useful work by CogStack in creating lists of NHS Conditions questions and answers](https://github.com/CogStack/OpenGPT/tree/main).

The NHS Developer API is very useful, but requires some setup and training to use - overkill if all a data science project needs is the NHS Conditions text. Additionally, the outputs of the API need further processing to get just the textual components of each page.

This package aims to make this whole process easier, requiring the user to simply run:

* *run_nhs_conditions_scraper*: to extract the HTML for each page
* *process_nhs_conditions_json*: to extract the text for each page into txt files

An example of how these are used can be see in the [scrape_nhs_conditions.ipynb](./scrape_nhs_conditions.ipynb) notebook

## Prerequisites

> If applicable, list the items a user needs to be able to use your repository, such as a certain version of a programming language. It can be useful to link to documentation on how to install these items.

* Python (> 3.0)

## Getting Started

> Tell the user how to get started (using a numbered list can be helpful). List one action per step with example code if possible.

1. Clone the repository. To learn about what this means, and how to use Git, see the [Git guide](https://nhsdigital.github.io/rap-community-of-practice/training_resources/git/using-git-collaboratively/).

```
git clone <insert URL>
```

2. Set up your environment using [pip](https://pypi.org/project/pip/). For more information on how to use virtual environments and why they are important see the [virtual environments guide](https://nhsdigital.github.io/rap-community-of-practice/training_resources/python/virtual-environments/why-use-virtual-environments/).

### Using pip
```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```
For Visual Studio Code it is necessary that you change your default interpreter to the virtual environment you just created .venv. To do this use the shortcut Ctrl-Shift-P, search for Python: Select interpreter and select .venv from the list.

## Project structure

> Provide the user with an outline of your repository structure. This template is primarily designed for publications teams at NHS England. Projects with different requirements (e.g. more complex documentation and modelling) should look to [DrivenData's cookiecutter project structure](https://drivendata.github.io/cookiecutter-data-science/#directory-structure), as well as our [Community of Practice](https://nhsdigital.github.io/rap-community-of-practice/training_resources/python/project-structure-and-packaging/) for guidance.

```text
|   .gitignore                        <- Files (& file types) automatically removed from version control for security purposes
|   config.toml                       <- Configuration file with parameters we want to be able to change (e.g. date)
|   requirements.txt                  <- Requirements for reproducing the analysis environment 
|   pyproject.toml                    <- Configuration file containing package build information
|   LICENSE                           <- License info for public distribution
|   README.md                         <- Quick start guide / explanation of your project
|
|   scrape_nhs_conditions.ipynb       <- Shows how to use the main functions to scrape NHS Conditions.     
|
+---src                               <- Contains project's codebase.
|   |       __init__.py               <- Makes the functions folder an importable Python module
|   |
|   +---utils                     <- Scripts relating to configuration and handling data connections e.g. importing data, writing to a database etc.
|   |       __init__.py               <- Makes the functions folder an importable Python module
|   | 
|   +---data_ingestion                <- Scripts with modules containing functions to preprocess read data i.e. perform validation/data quality checks, other preprocessing etc.
|   |       __init__.py               <- Makes the functions folder an importable Python module
|   |       simple_nhs_conditions_scrap.py <- Scrapes the HTML down from the NHS Conditions website.
|   |
|   +---processing                    <- Scripts with modules containing functions to process data i.e. clean and derive new fields
|   |       __init__.py               <- Makes the functions folder an importable Python module
|   |       process_html.py           <- processes the HTML files to make text files 
|   |
|   +---data_exports
|   |       __init__.py               <- Makes the functions folder an importable Python module
|   |
|
+---tests
|   |       __init__.py               <- Makes the functions folder an importable Python module
|   |
|   +---backtests                     <- Comparison tests for the old and new pipeline's outputs
|   |       __init__.py               <- Makes the functions folder an importable Python module
|   |
|   +---unittests                     <- Tests for the functional outputs of Python code
|   |       test_simple_nhs_conditions_scrape.py
|   |       __init__.py               <- Makes the functions folder an importable Python module
```

## Licence

> The [LICENCE](/LICENCE) file will need to be updated with the correct year and owner

Unless stated otherwise, the codebase is released under the MIT License. This covers both the codebase and any sample code in the documentation.

Any HTML or Markdown documentation is [© Crown copyright](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/) and available under the terms of the [Open Government 3.0 licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).

## Acknowledgements
- [Connor Quinn](https://github.com/connor1q)
- [Sam Hollings](https://github.com/SamHollings)
- [Maakhe Ndhlela](https://github.com/maakhe)
- [Harriet Sands](https://github.com/harrietrs)
- [Xiyao Zhuang](https://github.com/xiyaozhuang)
- [Helen Richardson](https://github.com/helrich)
- [The RAP team](https://github.com/NHSDigital/rap-community-of-practice)!
