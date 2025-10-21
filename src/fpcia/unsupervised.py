import numpy as np
import pandas as pd
from geopy.distance import great_circle
from shapely.geometry import MultiPoint
from sklearn.cluster import DBSCAN

# Most of this code is from Geoff Boeing article.
# If you get lost, read through it and it will explain way better than I could ever do!
# https://geoffboeing.com/2014/08/clustering-to-reduce-spatial-data-set-size/


def get_hot_spots(max_distance, min_cars, ride_data):
    ## get coordinates from ride data
    coords = ride_data[["Lat", "Lon"]].to_numpy()

    ## calculate epsilon parameter using
    ## the user defined distance
    kms_per_radian = 6371.0088
    ##The epsilon parameter is the max distance that points can be from each other to be considered a cluster.
    epsilon = max_distance / kms_per_radian

    ## perform clustering
    db = DBSCAN(
        eps=epsilon, min_samples=min_cars, algorithm="ball_tree", metric="haversine"
    ).fit(np.radians(coords))

    ## group the clusters
    cluster_labels = db.labels_
    num_clusters = len(set(cluster_labels))
    clusters = pd.Series([coords[cluster_labels == n] for n in range(num_clusters)])

    ## report
    print("Number of clusters: {}".format(num_clusters))

    ## initialize lists for hot spots
    lat = []
    lon = []
    num_members = []

    ## loop through clusters and get centroids, number of members
    for ii in range(len(clusters)):
        ## filter empty clusters
        if clusters[ii].any():
            ## get centroid and magnitude of cluster
            lat.append(MultiPoint(clusters[ii]).centroid.x)
            lon.append(MultiPoint(clusters[ii]).centroid.y)
            num_members.append(len(clusters[ii]))

    hot_spots = [lon, lat, num_members]

    return hot_spots
