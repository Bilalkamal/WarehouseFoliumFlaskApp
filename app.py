# Imports
from flask import Flask, render_template, jsonify, request
import pandas as pd
import folium
from folium.plugins import MarkerCluster

# Constants
DATASET_PATH = "abc - Sheet1.csv"

# Load and preprocess the dataset
data = pd.read_csv(DATASET_PATH)
data['warehouse_tier_sf'].fillna('no-tier', inplace=True)

# Initialize the Flask app
app = Flask(__name__)

def create_map(filtered_data):
    """Generates a folium map based on the given dataset."""
    m = folium.Map(location=[37.0902, -95.7129], zoom_start=4)  # Centered at USA
    marker_cluster = MarkerCluster().add_to(m)
    
    # Add markers to the map for each warehouse
    for _, row in filtered_data.iterrows():
        folium.Marker(
            location=[row['latitude_sf'], row['longitude_sf']],
            popup=(
                f"<b>Warehouse ID:</b> {row['warehouse_id']}<br>"
                f"<b>State:</b> {row['state']}<br>"
                f"<b>City:</b> {row['city']}<br>"
                f"<b>Tier:</b> {row['operator_tier']}<br>"
                f"<b>Address:</b> {row['facility_full_address']}<br>"
            ),
        ).add_to(marker_cluster)
    
    return m._repr_html_()

@app.route("/")
def index():
    """Main route that renders the HTML template with the map."""
    map_html = create_map(data)
    return render_template("index.html", 
                           map=map_html, 
                           states=data['state'].unique(), 
                           tiers=data['operator_tier'].unique())

@app.route("/get_data/<state>/<tier>")
def get_data(state, tier):
    """API route that returns a map based on the selected state and tier."""
    filtered_data = data.copy()
    if state != "All":
        filtered_data = filtered_data[filtered_data['state'] == state]
    if tier != "All":
        filtered_data = filtered_data[filtered_data['operator_tier'] == tier]
    map_html = create_map(filtered_data)
    return jsonify({"map": map_html})

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
