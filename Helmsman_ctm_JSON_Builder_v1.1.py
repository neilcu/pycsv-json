import json
from collections import OrderedDict
import os
import csv

###This program will by default read from 3 columns in a csv file###
###The values will be parsed one by one and looped through the build function###
###A JSON file will be the resultant output requiring a control-m automation api
###template to wrap it with the default job attributes###


def invals():
    csvFile = csv.reader(open('helmscsv_build.csv', 'r')) ###Read csv file
    for row in csvFile:
        #print(row[0])                          ##Print for debugging

        def build():                            ##Loop through these using input values
            jobdef = {'%s' % row[1]: {
                    "DD##Type": "Job:Command",
                    "EE##Command": "%s"% row[3],
                    "FF##Description": "%s+'ORDERID'+%s+CAT+%s"% (row[5],row[0],row[2]),	# OrderID and InConditions 
					"FF##RunAs": "%s"% row[4],								# OutConditions
					#"GG##CreatedBy": "%s"% row[0]
                }}
            #print(jobdef)                      ##Print for debugging
            with open("helms_inout_conds1_createdby_cat.json", "a") as json_file:
                json.dump(jobdef, json_file, sort_keys=True)
        build()
invals()

