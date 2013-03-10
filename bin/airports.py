#!/usr/bin/env python

import sys
import os.path
import optparse
import csv

def show_row(row):

    for k, v in row.items():
        print "[%s] %s" % (k, v)

    print ""

if __name__ == '__main__':

    parser = optparse.OptionParser(usage='')

    parser.add_option('--source', dest='source',
                        help='',
                        action='store')

    parser.add_option('--id', dest='id',
                        help='',
                        action='store')

    opts, args = parser.parse_args()

    whoami = os.path.abspath(sys.argv[0])
    bindir = os.path.dirname(whoami)
    rootdir = os.path.dirname(bindir)

    refdir = os.path.join(rootdir, 'reference')
    airports = os.path.join(refdir, 'airports.csv')

    fh = open(airports, 'r')
    reader = csv.DictReader(fh)

    for row in reader:

        if opts.source == 'iata' and opts.id == row['airport_iata_code']:
            show_row(row)
            break

        elif opts.source == 'icao' and opts.id == row['airport_icao_code']:
            show_row(row)
            break

        elif opts.source == 'woe' and opts.id == row['airport_woe_id']:
            show_row(row)
            break

        elif opts.source == 'ne' and opts.id == row['airport_ne_gid']:
            show_row(row)
            break

        elif opts.source == 'urbanarea' and opts.id == row['urbanarea_ne_gid']:
            show_row(row)

        elif opts.source == 'aerotropolis' and opts.id == row['aerotropolis_woe_id']:
            show_row(row)

        # TO DO: names

        else:
            pass

    sys.exit()
