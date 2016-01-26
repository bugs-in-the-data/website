# subsample
- id [pkey]
- sample_id [fkey -> sample pkey]
- order [varchar]
- family [varchar]
- genus [varchar]
- sub_genus [varchar]
- species [varchar]
- taxa [varchar]
- count [int]
- percent_subsample [decimal]
- total_count [int]
- comment [text]

# sample
- id [pkey]
- site_id [fkey -> site pkey]
- date [date]
- subsite [int]
- microhabitat [varchar]
- sample_hydro [varchar]
- habitat_size [varchar]
- pool_area [decimal]
- riff_area [decimal]
- canopy_upstream [decimal]
- canopy_left [decimal]
- canopy_downstream [decimal]
- average_canopy_cover [decimal]
- total_canopy_cover [decimal]
- bedrock [decimal]
- cobble [decimal]
- gravel [decimal]
- silt [decimal]
- travertine [decimal]
- sand [decimal]
- algae [decimal]
- macrophite [decimal]
- moss [decimal]
- detritus [decimal]
- temperature [decimal]
- disolved_oxygen [decimal]
- ph [decimal]
- conductivity [decimal]
- grazing_impact [decimal]
- collection_comments [text]
- habitat_comments [text]
- collector [varchar]
- zone [varchar]
- UTM Easting [varchar]
- UTM Northing [varchar]

# site
- id [pkey]
- state [varchar]
- installation [varchar]
- drainage [varchar]
- mountain_range [varchar]