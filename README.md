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
them. For example given the following airports:

	urbanarea_id,iata_code,gps_code,airport_name
	2541,SFO,KSFO,San Francisco Int'l
	2541,SJC,KSJC,San Jose Int'l
	2541,OAK,KOAK,Oakland Int'l
	...
	4818,LGA,KLGA,LaGuardia
	4818,JFK,KJFK,John F Kennedy Int'l

Urban area #4818 would be named `JFK-LGA` and urban area #2541 would be `OAK-SFO-SJC`, assuming that 3-letter airport codes are used 
instead of 4-letter codes. It's sort of academic as one can serve as an exonym
for the other; likewise with nearby cities for each airport. Either way, all the
airport codes contained by an urban area are sorted alphabetically and then
hyphenated.

Natural Earth data contains 891 airports.  The
[whereonearth-airports](https://github.com/straup/whereonearth-airport) dataset
contains 16079 airports in total and 1128 airports with matching IATA
codes (many of which overlap with NE). It's not that the other 15, 000 airports don't have IATA codes (although
some don't) but rather that I haven't completed the mapping.

Natural Earth airports take precedence when naming urban areas. For example, the
name of urban area #2541 is `OAK-SFO-SJC` rather than
`HWD-JCE-NUQ-OAK-PAO-SFO-SJC-SQL` (which is the set of airports defined in WOE
and contained by that urban area).

As of this writing there are 974 aerotropolii.

Each new "aerotropolis" has been assigned a (64-bit) WOE ID using an [artisanal
integer provider](http://www.brooklynintegers.com/) and will eventually be
assigned a WOE hierarchy (region, country, etc.).

As of this writing there are draft quality (ESRI) shapefiles in the `data`
directory. There are also (sometimes incomplete) reference CSV files for
aerotropolii and airports in the `reference` directory.
 
Sample images can be seen at: http://www.flickr.com/photos/straup/tags/aerotropolis/

Caveats
--

This is totally a work in progress. Objects will shift in transit.

