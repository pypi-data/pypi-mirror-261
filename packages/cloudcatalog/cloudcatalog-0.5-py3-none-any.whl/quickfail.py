import cloudcatalog

cr = cloudcatalog.CatalogRegistry()
endpoint = cr.get_endpoint('GSFC HelioCloud Public Temp')
fr = cloudcatalog.CloudCatalog(endpoint, cache=False)
bad="mms1_fpi_fast_des-dist"
s='2020-01-01T00:00'
e='2020-01-02T00:00'
keyset = fr.request_cloud_catalog(bad,start_date=s,stop_date=e)
