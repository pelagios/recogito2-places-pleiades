import json
import gzip

def loadRegions():
    print('Loading MAGIS regions')
    regions = {}
    with open('data/pleiades-regions-magis-pelagios.geojson') as f:
        for feature in json.load(f)['features']:
            uri = feature['properties']['uri']
            geometry = feature['geometry']
            regions[uri] = geometry
        f.close()

    return regions

def convertPlaces(regions):

    ctrPlaces = 0
    ctrMAGISUpdates = 0

    print('Building JSONL file')
    with gzip.open('data/pleiades-places-20170402.json.gz', 'rb') as f,  open('pleiades.jsonl', 'w') as out:
        pleiades = json.loads(f.read().decode('utf8'))

        for place in pleiades['@graph']:
            ctrPlaces += 1

            uri = place['uri'].replace('https', 'http')
            if uri in regions:
                ctrMAGISUpdates += 1
                print('Updating geometry for ' + uri)
                place['features'] = [{
                    'geometry': regions[uri],
                    'type': 'Features'
                }]

            out.write(json.dumps(place, ensure_ascii=False) + '\n')

        f.close()
        out.close()

    print('Done. Converted ' + str(ctrPlaces) + ' places, patched ' + str(ctrMAGISUpdates) + ' regions.')

# Load MAGIS regions and build the JSONL file
convertPlaces(loadRegions())
