# Python with MongoDB

This repository demonstrates how to load JSON data into MongoDB with Python, query and aggregate the data with MongoDB Query Language (MQL), and visualize the results with pandas and Matplotlib.

## Repository Structure

```text
.
├── car_data.json
├── python_mongodb_cars.ipynb
├── python_mongodb_restaurants.ipynb
├── requirements.txt
├── restaurant_data.json
└── README.md
```

## Data

### Cars: `car_data.json`

The car data is a JSON array of vehicle offers. Records include information such as:

- offer identifier, vehicle type, brand, and initial registration date
- fuel type and transmission
- price in CHF and engine power in PS
- dealer location fields

Some dealer details are intentionally anonymized as `***confidential***`.

The cars notebook imports these records into the `car_database` database and `car_collection` collection. It queries petrol cars with prices between CHF 10,000 and CHF 120,000 and more than 125 PS, then aggregates prices by brand and creates charts.

### Restaurants: `restaurant_data.json`

The restaurant data follows a GeoJSON-like structure. Each record contains a `Feature` with:

- `properties`: restaurant metadata such as name, amenity, cuisine, and address
- `geometry`: geographic coordinates and shape information

The restaurants notebook imports these records into the `restaurant_database` database and `restaurant_collection` collection. It queries burger and pizza restaurants in Zürich and Winterthur, aggregates them by city and cuisine, and creates a bar chart.

## Prerequisites

- Python 3.11 or newer
- A running MongoDB server reachable at `mongodb://mongo:27017/`
- Jupyter Notebook or JupyterLab

The notebooks currently use `/workspace/car_data.json` and `/workspace/restaurant_data.json`. Run them from this workspace, or change those paths in the data-loading cells when using the repository elsewhere.

## Installation

Create and activate a virtual environment, then install the Python dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Make sure MongoDB is running before executing cells that connect to it. The notebooks use the hostname `mongo`, which is commonly provided by a Docker Compose service or development-container setup. If MongoDB runs locally under another hostname or port, update the `MongoClient` connection string in both notebooks.

## Run the Jupyter Notebooks

Start Jupyter from the repository root:

```bash
jupyter notebook
```

Alternatively, start JupyterLab:

```bash
jupyter lab
```

Open and run either notebook:

1. `python_mongodb_cars.ipynb` loads and analyzes the vehicle data.
2. `python_mongodb_restaurants.ipynb` loads and analyzes the restaurant data.

Run the cells from top to bottom. Each notebook connects to MongoDB, inserts its JSON records, runs queries and aggregation pipelines, displays the resulting DataFrames and plots, and finally removes the database and collection it created. Re-running a notebook therefore starts with a clean dataset.

## Dependencies

The required packages are listed in `requirements.txt`:

- `jupyter` for running the notebooks
- `pymongo` for MongoDB access
- `pandas` for tabular data processing
- `matplotlib` for visualizations
- `openpyxl` for spreadsheet-related pandas support