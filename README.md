# API connector creation test task

Here is test assignment for Data Engineer position. This project implements a simple connector to open api, but it also implements the ability to transfer the api key to the header. This connector follows simple elt logic where we store data in database raw layer (postgres in my case) same as it present in the source. 

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation

* Clone this repository via `git clone https://github.com/runrudyrun/simple_api_connector.git`
* Move to project folder
* Change .env variables to Yours
* Run `docker build -t open_api_etl_process_name . `

## Usage
* Change variables in .env file to your ones
* Run `docker run -d --name container_name -v /path/to/local/logs:/app/logs your_app_image`

## TO DO

* Various tests:
- to test connection to api
- to test connection to database and presence of schema specified
- to test result of elt process


## License

Information is distributed under MIT License