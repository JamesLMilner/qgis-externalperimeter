# QGIS - External Facing Perimeter

## Introduction
Inside is a QGIS script that will determine the external facing perimeter of buildings. Buildings must be in Lines to function correctly. You can use the Polygon to Line tool to achieve this if you have buildings as Polygons.

## Using the script
Unfortunately there seems be something causing the script to fail the validation check to allow you to add the script to the QGIS toolbox. Whilst I work this out, you can run it in the following manner:

    1. Open QGIS
    2. go to the 'Processing' tab and click 'Toolbox'
    3. A panel will appear in the left hand side; click 'create new script'
    4. Open the script
    5. Hit the run button (the cogs button)
    6. Select your building dataset

You can optionally export this to a new Shapefile (or format of your choice).
