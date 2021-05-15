This project relies on a range of pip packages, that will need installing

- beautifulsoup4
- stanza
- OSGridConverter
- nuts_finder
- pandas
- plotly
- geojson_rewind

This also relies on the shapefile super-generalised.geojson, which provides a map for the visualization.

Two CSV files have been provided for testing, the main file is NHLEExport.csv, this contains all the castles from the search I have done.

mini.csv is provided to prove that the code works as expected, without having the time consumption of all the castles. This is simply the first 10 results from NHLEExport.csv.

The code can be ran by running main.py, and the resulting images will be placed in the root directory.

During the course of creating this project, one of the libraries(nuts_finder) stopped working as the url of the files it depended on changed. This was rectified by selecting a different year for it to choose from, however these links may change again, and if so the code sadly will not work.

