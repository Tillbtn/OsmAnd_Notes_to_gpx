# OsmAnd_Notes_to_gpx

A simple script to convert local notes from OsmAnd to GPX format for use in JOSM.

## Usage

### Step 1: Export Local Notes from OsmAnd

1. Open **Settings** in OsmAnd.
2. Choose **Export to file**.
3. Go to **My Places**.
4. Select **OSM notes**.

### Step 2: Run the Script

1. Save the exported `.osf` file in the same directory as this script.
2. Run the script with the following command:

   ```bash
   python .\osf_to_gpx.py

### Step 3: Open `.gpx` file as a new layer in JOSM
- your previous exports can be found in folder 'Export'
