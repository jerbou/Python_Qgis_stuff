# on save toutes les layers
path_to_csv = "G:/00_data_ref/sdis/"
for vLayer in iface.mapCanvas().layers():
    QgsVectorFileWriter.writeAsVectorFormat( vLayer, 
        path_to_csv + vLayer.name().upper() + ".shp", "utf-8", 
        vLayer.crs(), "ESRI Shapefile" )
