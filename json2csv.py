#!/usr/bin/python

# pylint: disable-all

import sys
import getopt
import json
import csv


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    if len(inputfile) > 0:
        with open(inputfile) as inputdata:
            items = json.load(inputdata)
        if len(outputfile) > 0:
            f = csv.writer(open(outputfile, 'wb+'))
            f.writerow(['No', 'Product Name', 'Price', 'Description', 'Printer Type', 'Material', 'Build Volume', 'Minimum Layer Height',
                        'Number of Extruder Head', 'Speed', 'Open Source', '3rd Party Material', 'Filament Diameter', 'Connectivity', 'Source'])
            for idx, item in enumerate(items):
                for key in item:
                    if item[key] != None:
                        item[key] = unicode(item[key]).encode('utf-8').strip()
                price = item['price'] or item['alternative_price']
                f.writerow([idx + 1, item['name'], price, item['description'], item['printer_type'], item['material'], item['buildvolume'], item['min_layer_height'],
                            item['extruder_head'], item['speed'], item['open_source'], item['third_party_material'], item['filament_diameter'], item['connectivity'], item['url']])


if __name__ == "__main__":
    main(sys.argv[1:])
