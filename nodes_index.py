def nodes_index():
    return [
            ("Gathering", [
                ("gathering.read_gis","SvMegapolisReadGis"),
                ("gathering.read_csv","SvMegapolisReadCsv"),
                ("gathering.read_json","SvMegapolisReadJson"),
                ("gathering.read_dem","SvMegapolisReadDem"),
                ("gathering.read_las","SvMegapolisReadLas"),
                ("gathering.download_st_imagery","SvMegapolisDownloadStImagery"),
                ("gathering.load_street_network","SvMegapolisLoadStreetNetwork"),
                ("gathering.osm_downloader","SvMegapolisOSMDownloader"),
                ("gathering.pandas_series","SvMegapolisPandasSeries"),
                ("gathering.pandas_dataframe","SvMegapolisPandasDataframe"),
                ("gathering.split_string","SvMegapolisSplitString"),
                ("gathering.download_data_url","SvMegapolisDownloadDataUrl"),
                ("gathering.request_data_api","SvMegapolisRequestDataApi"),
                ("gathering.get_pandas_feature","SvMegapolisGetPandasFeature")





                ]),
            ("Analysis", [

                ("analysis.whitebox_gis_tools","SvMegapolisWhiteboxGisTools"),
                ("analysis.dem_terrain_attributes","SvMegapolisDemTerrainAttributes"),
                ("analysis.network_analyses","SvMegapolisNetworkAnalyses"),
                ("analysis.isovists","SvMegapolisIsovists"),
                ("analysis.shortest_path","SvMegapolisShortestPath"),
                ("analysis.correlation_index","SvMegapolisCorrelationIndex"),
                ("analysis.correlation_matrix","SvMegapolisCorrelationMatrix"),
                ("analysis.correlation_with","SvMegapolisCorrelationWith"),
                ("analysis.linear_model_selection","SvMegapolisLinearModelSelection"),
                ("analysis.model_fit","SvMegapolisModelFit"),
                ("analysis.model_predict","SvMegapolisModelPredict"),
                ("analysis.model_evaluate","SvMegapolisModelEvaluate"),
                ("analysis.dataframe_utils","SvMegapolisDataframeUtils"),
                ("analysis.object_detection","SvMegapolisObjectDetection"),
                ("analysis.detectron","SvMegapolisDetectron")



                ]),


            ("Generation", [

                ("generation.lat_lon_to_points","SvMegapolisLatLonToPoints"),
                ("generation.faces_from_vertices","SvMegapolisFacesFromVertices"),
                ("generation.pandas_filter","SvMegapolisPandasFilter"),
                ("generation.transpose_dataframe","SvMegapolisTransposeDataframe"),
                ("generation.pandas_map_feature","SvMegapolisPandasMapFeature"),
                ("generation.file_to_gdf","SvMegapolisFileToGdf"),
                ("generation.file_to_geojson","SvMegapolisFileToGeoJson"),
                ("generation.csv_to_dataframe","SvMegapolisCsvToDataframe"),
                ("generation.sequential_colormap","SvMegapolisSequentialColormap"),
                ("generation.get_file_path","SvMegapolisGetFilePath")



                ]),
            ("Visualisation", [
                ]),
                      ]
