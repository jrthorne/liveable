#!/usr/bin/python2.6
import pyproj as pyp
import shapefile
import numpy as np
from dbfpy import dbf


def main():
	# open the database file.....
	db 		= dbf.Dbf("UNSW_2013/PD0217_st_furniture.dbf", readOnly=1)
	print "No of records = ", len(db)
	
	# whose records line up with the shape file
	sf = shapefile.Reader("UNSW_2013/PD0217_st_furniture")
	shapeRecs	= sf.shapeRecords()
	
	# for conversion to latitude and longitude
	UTMstring		= "+proj=tmerc +lat_0=0.0 +lon_0=153.0 +k=0.9996 +x_0=500000.0 "
	UTMstring		+= "+y_0=10000000.0"
	UTM2latlong 	= pyp.Proj(UTMstring)
	
	furnTypes		= []
	
	#for i in range(min(10,len(db))):
	for i in range(len(db)):
		rec = db[i]
		servName	= ""
		servProps	= ""
		for fldName in db.fieldNames:
			print '%s:\t %s' %(fldName, rec[fldName])

			if fldName[:10] == "DESCRIPTIO":
				if rec[fldName] not in furnTypes:
					furnTypes.append(rec[fldName])
				# end if
				
				servName 		+= rec[fldName] + ", "
			# end if
			
			# if this field is the name of the record, then store it
			if fldName[:9] == "SECT_FROM":
				servName 		+= rec[fldName]
			# end if
			
			servProps			+= str(rec[fldName]) + "\n"
			
		# next fldName
		
		# now get the latitude and longitude for this asset
		UTMcoord	= shapeRecs[i].shape.points[0]
		North		= UTMcoord[1]
		East		= UTMcoord[0]
		longLat		= UTM2latlong(East, North, inverse=True)
		# reverse for cut and paste to google maps
		latLong		= (longLat[1], longLat[0])
		
		print servProps
		print "Latitude, Longitude for %s" %servName
		print latLong
		print
		print "*********************************************************************"
		
		
	# next i
	
	db.close()
	
	print furnTypes
	
	
# end main


if __name__=="__main__":
    main()




