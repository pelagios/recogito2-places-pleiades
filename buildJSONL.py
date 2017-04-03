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

    def collapseRectangle(uri, features):
        if len(features) > 0 and 'geometry' in features[0]:
            geom = features[0]['geometry']
            if geom and geom['type'] == 'Polygon':
                coords = geom['coordinates'][0]
                if len(coords) == 5:
                    # A geometry with 5 coordinates? Might be a Barrington Atlas page
                    if coords[0][0] == coords[1][0] and coords[0][1] == coords[3][1]:
                        lon = (coords[0][0] + coords[2][0]) / 2
                        lat = (coords[0][1] + coords[1][1]) / 2

                        # Replace with point geometry
                        features[0]['geometry'] = {
                            'type': 'Point',
                            'coordinates': [ lon, lat ]
                        }

                        return True
        return False

    # Counts all places
    ctrPlaces    = 0

    # Counts how many rectangles were collapsed
    ctrCollapsed = 0

    # Counts how many places were patched with MAGIS geometry
    ctrMAGIS     = 0

    print('Building JSONL file')
    with gzip.open('data/pleiades-places-20170402.json.gz', 'rb') as f,  open('pleiades.jsonl', 'w') as out:
        pleiades = json.loads(f.read().decode('utf8'))

        for place in pleiades['@graph']:
            ctrPlaces += 1

            # Normalize to http URIs
            uri = place['uri'].replace('https', 'http')
            place['uri'] = uri

            if uri in regions:
                ctrMAGIS += 1
                print('Updating geometry for ' + uri)
                place['features'] = [{
                    'geometry': regions[uri],
                    'type': 'Features'
                }]
            else:
                collapsed = collapseRectangle(uri, place['features'])
                if collapsed:
                    ctrCollapsed += 1

            out.write(json.dumps(place, ensure_ascii=False) + '\n')

        f.close()
        out.close()

    print('Done.')
    print(str(ctrPlaces) + ' places converted')
    print(str(ctrMAGIS) + ' regions patched')
    print(str(ctrCollapsed) + ' rectangles collapsed')

# Load MAGIS regions and build the JSONL file
convertPlaces(loadRegions())
