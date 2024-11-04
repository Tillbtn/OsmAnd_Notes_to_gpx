import json
import os
from datetime import datetime
import zipfile
import xml.etree.ElementTree as ET
from xml.dom import minidom

# create file name with current date
def get_name():
    current_date = datetime.now().strftime('%Y-%m-%d')
    current_date = 'Export_' + current_date + '.osf'
    return current_date

# rename file form .osf to .zip
def rename_to_zip(filename):
    # new_name = filename[:-4] + '.zip'
    new_name = 'archive.zip'
    os.rename(filename, new_name)

def unzip_file(filename):
    target_dir = os.getcwd()
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall(target_dir)

def cleanup():
    os.remove('items.json')
    os.remove('osm_notes.json')
    os.remove('archive.zip')


def json_to_gpx(json_file, gpx_file):
    # read json
    with open(json_file, 'r') as f:
        data = json.load(f)

    # create gpx structure
    gpx = ET.Element('gpx', version="1.1", creator="JSON to GPX Converter")

    for item in data['items']:
        wpt = ET.SubElement(gpx, 'wpt', lat=str(
            item['lat']), lon=str(item['lon']))
        name = ET.SubElement(wpt, 'name')
        name.text = item['text']

    # write to gpx file
    xmlstr = minidom.parseString(ET.tostring(gpx)).toprettyxml(indent="  ")
    with open(gpx_file, "w") as f:
        f.write(xmlstr)

# usage
rename_to_zip(get_name())
unzip_file('archive.zip')
json_to_gpx('osm_notes.json', 'osm_notes.gpx')
cleanup()