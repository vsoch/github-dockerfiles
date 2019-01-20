# Design

A review of some oft used geometry libraries and how they'll influence the design of this one

## Existing Libraries

* Boost Geometry: https://github.com/boostorg/geometry
* Java Topology Suite: https://github.com/locationtech/jts
  * Feels very java centric (go figure)
  * Things like geometry factories are heavy and a pain to create
* Turf.js: https://github.com/Turfjs/turf
  * Not really a full featured geometry library
* Apache SIS: http://sis.apache.org/
  * ISO Focused
  * Feels complex, unintuitive

## Design considerations and Desires

* "Easy things should be easy, hard things should be possible"
* Support for 3D
* Support for multiple projections
* Easy and native IO
* Easy and native spatial comparators
* Easy and native spatial operations
* New school focus:
  * GeoJSON, GeoPackage over GML/Shapefile
  * Thoughts about streaming data?
  * GeoProtobuf formats?
  * Support for GPU powered computation?

## Status

### Algorithm

### Densify

### Dissolve

### Edge Graph

### Geom

* [x] Coordinate
* [ ] CoordinateArray
* [ ] CoordinateFilter
* [ ] CoordinateList
* [ ] Dimension
* [ ] Envelope
* [ ] Geometry
* [ ] GeometryCollection
* [ ] IntersectionMatrix
* [ ] LineSegment
* [ ] LineString
* [ ] Lineal
* [x] LinearRing
* [ ] Location
* [x] MultiLineString
* [x] MultiPoint
* [x] MultiPolygon
* [ ] OctagonalEnvelope
* [x] Point
* [x] Polygon
* [ ] Polygonal
* [ ] PrecisionModel
* [ ] Puntal
* [ ] TopologyException
* [ ] Triangle

### Geom Graph

### Index

### IO

* [x] GeoJSON
* [ ] Geopackage
* [ ] WKT
* [ ] WKB

### Linear Ref

### Math

### Noding

### Operation

### Planar Graph

### Precision

### Shape

### Simplify

## Triangulate

### Util
