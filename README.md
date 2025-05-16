# golden-raspberry-api

A RESTful API to query the producers with the longest and shortest gaps between consecutive Razzie wins (Worst Picture).
## Requisitos

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
   uvicorn main:app --reload
   ```
