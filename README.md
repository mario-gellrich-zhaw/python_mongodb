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

- The MongoDB server from the Codespaces/devcontainer setup running and
	reachable at `mongodb://mongo:27017/`
- Jupyter Notebook

This repository is configured for GitHub Codespaces and the development
container. Python and the dependencies listed in `requirements.txt` are
provided by the existing `devcontainer.json` setup.
The MongoDB server is also part of this setup and must be running before the
notebooks are executed.

The notebooks currently use `/workspace/car_data.json` and `/workspace/restaurant_data.json`. Run them from this workspace, or change those paths in the data-loading cells when using the repository elsewhere.

The notebooks use the hostname `mongo`. If MongoDB runs under another
hostname or port, update the `MongoClient` connection string in both
notebooks.

## Development Container Architecture

The `.devcontainer/docker-compose.yml` file defines two separate containers, not one:

```text
Codespace VM (Docker host)
 ├── "python" container  -> VS Code, the terminal, and the notebooks run here
 └── "mongo" container   -> MongoDB runs here, completely separate
```

This is not Docker-in-Docker, and MongoDB is not installed inside the `python`
container. Both containers are started by the same Docker daemon on the
Codespace host and joined to a shared network, where the hostname `mongo`
resolves to the MongoDB container. That is how the notebooks can connect to
`mongodb://mongo:27017/` without MongoDB being installed alongside them.

Because the terminal runs inside the `python` container, commands like
`docker ps` are not available there — no Docker CLI or socket is installed in
it. Only the Codespace host itself can inspect and manage containers.

### Checking whether MongoDB is running

From the integrated terminal, check MongoDB over the network instead of with
`docker ps`:

```bash
# 1) Is the port open?
timeout 3 bash -c "echo > /dev/tcp/mongo/27017" && echo OPEN || echo CLOSED

# 2) Does it actually respond as MongoDB?
python3 -c "
from pymongo import MongoClient
client = MongoClient('mongodb://mongo:27017/', serverSelectionTimeoutMS=3000)
print(client.admin.command('ping'))
"
```

A reply of `{'ok': 1.0}` confirms MongoDB is up and reachable.

## Run the Jupyter Notebooks

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