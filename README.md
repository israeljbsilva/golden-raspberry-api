# golden-raspberry-api

A RESTful API to query the producers with the longest and shortest gaps between consecutive Razzie wins (Worst Picture).
## Requirements

- Python 3.11+
- Poetry (install with `pip install poetry`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/israeljbsilva/golden-raspberry-api
   cd golden-raspberry-api
   ```
   
2. Install dependencies with Poetry:
   ```bash
   poetry install
   ```

3. Activate the virtual environment:
   ```bash
   poetry env activate
   ```

## Running the application

1. Run the server in the virtual environment:
   ```bash
   uvicorn app.main:app --reload
   ```
2. Go to url to access the endpoints:
   ```
   http://127.0.0.1:8000/docs
   ```


## Running tests

1. Run the test:
   ```bash
   poetry run pytest
   ```


## Observation

If you need to test with different data content, simply change the data in the file: 
- app/data/movielist.csv