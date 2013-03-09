#!/usr/bin/env python

import sys
import os
import os.path

import fiona
import shapely.geometry

import utils

if __name__ == '__main__':

    whoami = os.path.abspath(sys.argv[0])
    bindir = os.path.dirname(whoami)
    rootdir = os.path.dirname(bindir)

    datadir = os.path.join(rootdir, 'data')
    jsondir = os.path.join(datadir, 'geojson')

    if not os.path.exists(jsondir):
        os.makedirs(jsondir)

    shp = os.path.join(datadir, '10m_aerotropolis', '10m_aerotropolis.shp')
    col = fiona.open(shp, 'r')

    for f in col:

        props = {}

        for k,v in f['properties'].items():
            k = k.lower()

            if k == 'woeid':
                v = int(v)
            elif k == 'airports':
                v = v.replace('{', '')
                v = v.replace('}', '')
            else:
                pass

            props[k] = v

        p = f['geometry']
        p = shapely.geometry.asShape(p)
        bbox = p.bounds

        f['properties'] = props
        f['bbox'] = bbox
        f['id'] = props['woeid']

        tree = utils.woeid2path(f['id'])
        fname = "%s.json" % f['id']

        root = os.path.join(jsondir, tree)
        path = os.path.join(root, fname)

        if not os.path.exists(root):
            os.makedirs(root)
            
        fh = open(path, 'w')
        indent = None

        utils.write_json(f, fh, indent)
        print path
