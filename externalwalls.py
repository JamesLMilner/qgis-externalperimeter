##building_input=vector

from qgis.core import *
from PyQt4.QtCore import *

# The tollerance we want to allow for our floating point numbers
EPSILON = 0.0000000001
FIELD_NAME = 'ext_peri'

# We need a way of checking if floating numbers are equivalent
def floatClose(f1, f2, allowed_error):
    return abs(f1 - f2) <= allowed_error

# Add a new attribute called 'external_perimeter' to the layer
building_layer = processing.getObject(building_input)
provider = building_layer.dataProvider()
provider.addAttributes([QgsField(FIELD_NAME, QVariant.Double)])
building_layer.updateFields()

# Open up the external_perimeter for editing
building_layer.startEditing()
building_layer_index = building_layer.fieldNameIndex(FIELD_NAME)

## Iterate through each of the buildings
for main in building_layer.getFeatures():
    try:
        main_geom = main.geometry()
        main_peri = main_geom.length()
        diff_peri = 0

        for compare in building_layer.getFeatures():
            if compare is not main: # If a geometry is not itself
                comp_geom = compare.geometry()
                disjoint = main_geom.disjoint(comp_geom)
                if disjoint == False: # If the geometries are connected we get the difference of the two
                    difference = main_peri - main_geom.difference(comp_geom).length()
                    if floatClose(difference, main_peri, EPSILON ) == False:
                        diff_peri += difference # We aggregate a difference in length between geometry and its connecting geometries

        external_peri = main_peri - diff_peri
        ##print main["fid"], " --- Full Perimeter: ", main_peri, " --- External Perimeter: ", external_peri
        building_layer.changeAttributeValue(main.id(), building_layer_index, external_peri)

    except Exception, e:
        print "Error: ", str(e)
        break

print "Finished!"

building_layer.updateFields()
building_layer.commitChanges()
