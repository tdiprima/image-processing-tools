# Translate point coordinates to image
import pymongo


def mongodb_conn(connectstr):
    try:
        conn = pymongo.MongoClient(connectstr)
        print("Connected successfully!!!")
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to server: %s" % e)
    return conn


def get_mark(connectstr):
    conn = mongodb_conn(connectstr)
    if conn is None:
        # no connection, exit early
        return
    try:
        mydb = conn["camic"]
        # mydb = conn.dbname.collection
        mycol = mydb["mark_test"]
        # myquery = {"provenance.image.slide": "TCGA-C4-A0F6-01Z-00-DX1", "provenance.analysis.execution_id": "CNN_synthetic_n_real"}
        # myquery = {"provenance.image.slide": "TCGA-06-0148-01Z-00-DX1", "provenance.analysis.execution_id": "20170207"}
        myquery = {"provenance.image.slide": "TCGA-21-5783-01Z-00-DX1.svs", "provenance.analysis.execution_id": "_5ezdk52mv"}
        # myquery = {"provenance.image.slide": "TCGA-21-5783-01Z-00-DX1.svs", "provenance.analysis.execution_id": "_5i6hy2zsx"}
        print(myquery)
        mydoc = mycol.find_one(myquery)
        feature = mydoc['geometries']['features']
        geo = feature[0]['geometry']
        coords = geo['coordinates'][0]
        print(coords)
    except:
        print("No marks found")


# get_hosts("mongodb://129.49.170.48:27017/")
get_mark("mongodb://localhost:27017/")
