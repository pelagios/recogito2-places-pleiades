# Recogito 2 Gazetteer Package: Pleiades

Gazetteer data from the [Pleiades Gazetteer of the Ancient World](http://pleiades.stoa.org),
packaged for use with [Recogito v.2](http://github.com/pelagios/recogito2). The package is
built from [Pleiades nightly JSON dumps](https://pleiades.stoa.org/downloads), but includes a few
changes specifically for use with Recogito:

- All place URLs are normalized to __http__, rather than __https__
- Barrington Atlas grid rectangles are collapsed to a point for better visualization in Recogito
- Regions are patched with geometries digitized by the [MAGIS project](http://cgma.depauw.edu/MAGIS/)

### Releases

| Version                                                                     | Date       | # of Records | Notes           |                                                                                  |
|-----------------------------------------------------------------------------|------------|--------------|----------------|----------------------------------------------------------------------------------|
|[0.2](https://github.com/pelagios/recogito2-places-pleiades/releases/tag/0.2)| 2018-02-19 | 35,704 | Updated dump    |[pleiades-20180219.jsonl.gz](https://github.com/pelagios/recogito2-places-pleiades/releases/download/0.2/pleiades-20180219.jsonl.gz)|
|[0.1](https://github.com/pelagios/recogito2-places-pleiades/releases/tag/0.1)| 2017-04-03 | 35,222 | Initial release |[pleiades-20170403.jsonl.gz](https://github.com/pelagios/recogito2-places-pleiades/releases/download/0.1/pleiades-20170403.jsonl.gz)|

### Attribution & License

[Pleiades](http://pleiades.stoa.org) data is distributed under the terms of a Creative Commons
Attribution license (CC-BY). Content is governed by the copyrights of the [individual Pleiades
contributors](http://pleiades.stoa.org/credits/).

Digitized regions from the [MAGIS project](http://cgma.depauw.edu/MAGIS/) are made available by
Pedar Foss for free redistribution (Copyright [AWMC](http://awmc.unc.edu), CC-BY). With support
from the [Pelagios project](http://commmons.pelagios.org), [Stuart Eve](http://www.dead-mens-eyes.org/)
has added Pleiades identifiers in 2015 and converted the geometries to Pelagios RDF Format.
[Jean-Marc Montanier](https://github.com/montanier) has kindly provided [a converter to
GeoJSON](https://github.com/pelagios/magis-pleiades-regions).
