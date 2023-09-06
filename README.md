# Folium Warehouse Locations Visualizer

Visualize warehouse locations across the USA with filtering options based on state and tier.

## Prerequisites

- Python (3.x recommended)
- pip (Python package installer)

## Installation

1. Clone the repository or download the project to your local machine.
2. Navigate to the project directory in your terminal.
3. Install the required Python libraries:

```bash
pip install -r requirements.txt
```

## Running the App

1. Ensure the path to the CSV file is correctly set in `app.py`. Replace `'/path/to/abc - Sheet1.csv'` with the correct path to your dataset.
2. Run the Flask app:

```bash
python app.py
```

3. Open your browser and navigate to:

```bash
http://localhost:5000/
```

You should see the Folium map with warehouse data points and filtering options.

## Features

- Visualize warehouse locations with markers on a map.
- Filter warehouse data based on state and tier.
- Modern, responsive design with intuitive user interface.
