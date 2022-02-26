# Eureka


[![Coverage Status](https://coveralls.io/repos/github/julianVelandia/Eureka/badge.svg?branch=master)](https://coveralls.io/github/julianVelandia/Eureka?branch=master)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


Eureka is a Rest-API project for Web Scraping, data cleaning and organization, based on FastAPI and following a
hexagonal architecture. Designed for the Eureka by Turing project of the National University of Colombia


Disclaimer: this is a work in progress project, stay tuned for updates (*).

## Installation and Usage

### Setup environment

You should create a virtual environment and activate it:

```bash
python -m venv venv/
```

```bash
source venv/bin/activate
```

Clone repository

```bash
git clone https://github.com/julianVelandia/Eureka.git
```

And then install the development dependencies:

```bash
pip install -r requirements.dev.txt
```

### Run unit tests

You can run all the tests with:

```bash
make tests
```

Alternatively, you can run `pytest` yourself.

```bash
pytest
```

### Run 

The project runs like any FastApi application and by default the configuration endpoint works.

```bash
uvicorn main:app --reload
```

## Features
- [ ] RenderEngine: Render a web page from its url to select the texts to scrape and save them in a Json file
- [ ] Templates to visualize the scraped information
- [ ] export data in json and csv files
- [x] Make automated requests from a Json configuration file
- [x] Unpack Json configuration files

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
This project is licensed under the terms of the [MIT](https://choosealicense.com/licenses/mit/) license.