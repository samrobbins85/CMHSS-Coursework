# Computational Modelling in the Humanities and Social Sciences Coursework

Starting with using stanza for text analysis.

Stanza doesn't come with as many features as corenlp, meaning I can't analyze things such as "no keep" as the relationship between no and keep is `det` in stanza, whereas in corenlp it's `neg`

The geojson file is found [here](https://data.gov.uk/dataset/2aa6727d-c5f0-462a-a367-904c750bbb34/nuts-level-1-january-2018-full-clipped-boundaries-in-the-united-kingdom), the download is very iffy though so you might struggle.

The size has been reducing using [mapshaper](https://www.npmjs.com/package/mapshaper) according to [this blog](https://blog.exploratory.io/how-to-reduce-your-geojson-file-size-smaller-for-better-performance-8fb77759870c)
