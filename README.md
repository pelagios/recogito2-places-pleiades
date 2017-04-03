# Recogito 2 Gazetteer Package: Pleiades

Gazetteer data from the [Pleiades Gazetteer of the Ancient World](http://pleiades.stoa.org),
packaged for use with [Recogito v.2](http://github.com/pelagios/recogito2). The package is
built from [Pleiades nightly JSON dumps](https://pleiades.stoa.org/downloads), but includes a few
changes specifically for use with Recogito:

- All place URLs are normalized to __http__, rather than __https__
- Barrington Atlas grid rectangles are collapsed to a point for better visualization in Recogito
- Regions are patched with geometries digitized by the [MAGIS project](http://cgma.depauw.edu/MAGIS/), and
  made available by Pedar Foss for free redistribution (Copyright [AWMC](http://awmc.unc.edu), CC-BY).
  ([Read more...](https://github.com/pelagios/gazetteer-data/tree/master/magis-pleiades-regions))

### Releases

| Version | Date       | Notes           |
|---------|------------|-----------------|
|1.0      | 2017-04-03 | Initial release |

### buildJSONL.py

The `buildJSONL.py` script is a small Python utility that reads the GZipped Pleiades data dump
in the `data` folder, adds the MAGIS regions, and outputs a Recogito-compatible [new-line
delimited JSON](http://jsonlines.org) file.
