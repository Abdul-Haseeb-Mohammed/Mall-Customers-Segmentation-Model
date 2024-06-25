from sklearn.cluster import KMeans
import pandas as pd
from sklearn.metrics import silhouette_score

# Function to train the model
def train_k_means(train_data):
    k = range(3,9)
    K = []
    WCSS = []
    SS = []
    for i in k:
        kmodel = KMeans(n_clusters=i).fit(train_data)
        wcss_score = kmodel.inertia_
        ypred = kmodel.labels_
        sil_score = silhouette_score(train_data[['Annual_Income','Spending_Score']], ypred)
        SS.append(sil_score)
        WCSS.append(wcss_score)
        K.append(i)
        if i == 5:
            best_model = kmodel
    wss = pd.DataFrame({'cluster': K, 'WSS_Score':WCSS,'Silhouette_Score':SS})

    return best_model, wss