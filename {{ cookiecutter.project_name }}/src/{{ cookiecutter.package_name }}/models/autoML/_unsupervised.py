
import pandas as pd
from {{ cookiecutter.package_name }}.utils.logger import logger

from sklearn.metrics import silhouette_score
import hdbscan
import numpy as np
import gower
import scipy.cluster.hierarchy as sch
from kmodes.kprototypes import KPrototypes
from sklearn.cluster import DBSCAN


def unsupervised_automl(df:pd.DataFrame, n_clusters:int=4):
    scores = {}
    dist_matrix = gower.gower_matrix(df).astype(np.float64)
    # Apply HDBSCAN
    logger.info("Applying HDBSCAN")
    hdb = hdbscan.HDBSCAN(metric='precomputed')
    cluster1 = hdb.fit_predict(dist_matrix)
    scores['hdbscan'] = silhouette_score(dist_matrix, cluster1)
    # Apply KPrototypes
    logger.info("Applying KPrototypes")
    kproto = KPrototypes(n_clusters=n_clusters, init='Cao', verbose=2)
    cat = df.select_dtypes(include=['object']).columns
    indexes = np.argwhere(df.columns.isin(cat)).flatten().tolist()
    cluster2 = kproto.fit_predict(dist_matrix, categorical=indexes)
    scores['kproto'] = silhouette_score(dist_matrix, cluster2)
    # Apply KMeans
    logger.info("Applying KMeans")
    kmeans = sch.linkage(dist_matrix, method='ward')
    cluster3 = sch.fcluster(kmeans, n_clusters, criterion='maxclust')
    scores['kmeans'] = silhouette_score(dist_matrix, cluster3)
    # Apply DBSCAN
    logger.info("Applying DBSCAN")
    db = DBSCAN()
    cluster4 = db.fit_predict(dist_matrix)
    scores['dbscan'] = silhouette_score(dist_matrix, cluster4)
    # Get the best model
    best_model = max(scores, key=scores.get)
    logger.info(f"Scores: {scores}")
    logger.info(f"Best model found: {best_model}")
    return best_model

