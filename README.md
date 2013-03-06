whereonearth-aerotropolis
==

_"An aerotropolis is an urban plan in which the layout, infrastructure, and
economy is centered around an airport, existing as an airport city. It is
similar in form and function to a traditional metropolis, which contains a
central city core and its commuter-linked suburbs. The term was first
proposed by New York commercial artist Nicholas DeSantis, whose drawing of a
skyscraper rooftop airport in the city was presented in the November 1939 issue
of Popular Science. The term was revived and substantially extended by
academic and air commerce expert Dr. John D. Kasarda in 2000, based on his prior
research on airport-driven economic development."_ –– [Wikipedia](https://en.wikipedia.org/wiki/Aerotropolis)

`whereonearth-aerotropolis` is a subset of the [Natural Earth urban
areas](http://www.naturalearthdata.com/downloads/10m-cultural-vectors/)
dataset. It is the list of urban areas that contain one or more
airports. Those airports are then used to _name_ the urban areas that contain
them. For example urban area #4818 contains the following airports:

	4818,LGA,KLGA,LaGuardia
	4818,JFK,KJFK,John F Kennedy Int'l

This means that urban area #4818 would be named LGA-JFK, assuming that 3-letter airport codes are used 
instead of 4-letter codes. It's sort of academic as one can serve as an exonym
for the other; likewise with nearby cities for each airport. Either way, all the
airport codes contained by an urban area are sorted alphabetically and then
hyphenated.

Currently the list is compiled using the Natural Earth airports data (891
airports) but will eventually use the [whereonearth-airports](https://github.com/straup/whereonearth-airport) list (16079
airports).

Each new "aerotropolis" will be assigned a (64-bit) WOE ID using an [artisanal
integer provider](http://www.brooklynintegers.com/) and assigned a WOE hierarchy
(region, country, etc.).

As of this writing there are no ESRI shape or GeoJSON files but there is a CSV
file containing the parent-child relationships.

Caveats
--

This is totally a work in progress. Objects will shift in transit.

