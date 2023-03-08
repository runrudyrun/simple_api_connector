# API connector creation test task

Here is test assignment for Data Engineer position. This project implements a simple connector to open api, but it also implements the ability to transfer the api key to the header. This connector follows simple elt logic where we store data in database raw layer (postgres in my case) same as it present in the source. 

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation

* Clone this repository via  `git clone https://github.com/runrudyrun/simple_api_connector.git`
* Move to project folder
* Change .env variables to needed ones
* Run  `docker build -t place_your_name . `

## Usage
### Docker
* Change variables in .env file to needed ones
* Run  `docker run -d --network host --name container_name`
### Locally
* Change variables in .env file to needed ones
* Install requirements  `pip install -r requirements.txt`
* Run  `python run_elt.py`

## TO DO

* Various tests:
    - to test connection to api
    - to test connection to database and presence of schema specified
    - to test result of elt process


## License

Information is distributed under MIT License