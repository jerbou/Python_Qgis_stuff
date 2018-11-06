import glob, os

# https://gis.stackexchange.com/questions/227271/where-are-the-temporary-output-layers-from-qgis-processing-algorithms-stored
# https://gis.stackexchange.com/questions/169090/how-to-open-and-save-qgis-datasource-with-to-lower-case-fields

# Define path to  directory of your csv files
# path_to_csv = "T:/ideo_bfc/DONNEES/PLATEFORME/ENTRANTE/SRIT/"  
path_to_csv = "G:\00_data_ref\sdis\Telechargement_1521757164_6810\6c7f678e-aecb-46bf-a1b0-7785867cec2b_1521757164_7975"

# Set current directory to path of csv files
os.chdir(path_to_csv)  
# Find each .csv file and load them as vector layers
for fname in glob.glob("*.csv"):  
    uri = "file:///" + path_to_csv + fname + "?delimiter=%s&crs=epsg:4326&xField=%s&yField=%s" % (",", "Longitude", "Latitude")
    name = fname.replace('.csv', '')
    lyr = QgsVectorLayer(uri, name, 'delimitedtext')
    QgsMapLayerRegistry.instance().addMapLayer(lyr)

# https://gis.stackexchange.com/questions/131104/exporting-several-files-at-same-time-in-qgis
# on save toutes les layers

for vLayer in iface.mapCanvas().layers():
    QgsVectorFileWriter.writeAsVectorFormat( vLayer, 
        path_to_csv + vLayer.name() + ".shp", "utf-8", 
        vLayer.crs(), "ESRI Shapefile" )
