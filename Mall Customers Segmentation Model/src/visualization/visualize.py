from sklearn import tree
import matplotlib.pyplot as plt
import os
import seaborn as sns

def pairplot(dataset,save_path=None):
    plt.figure(figsize=(20, 10))
    sns.pairplot(dataset[['Age','Annual_Income','Spending_Score']])
    
    # Save the plot if save_path is provided
    if save_path:
        plt.savefig(save_path, dpi=300)
        plt.close()
        print(f"Pair plot saved to {os.path.abspath(save_path)}")
    else:
        plt.show()
        
def elbow_plot(wss,save_path=None):
    plt.figure(figsize=(20, 10))
    wss.plot(x='cluster', y = 'WSS_Score')
    plt.xlabel('No. of clusters')
    plt.ylabel('WSS Score')
    plt.title('Elbow Plot')
        
    # Save the plot if save_path is provided
    if save_path:
        plt.savefig(save_path, dpi=300)
        plt.close()
        print(f"Elbow Plot plot saved to {os.path.abspath(save_path)}")
    else:
        plt.show()

def silhouette_plot(wss,save_path=None):
    # Now, plot the silhouette plot
    wss.plot(x='cluster', y='Silhouette_Score')
    plt.xlabel('No. of clusters')
    plt.ylabel('Silhouette Score')
    plt.title('Silhouette Plot')

    # Save the plot if save_path is provided
    if save_path:
        plt.savefig(save_path, dpi=300)
        plt.close()
        print(f"Silhouette Plot plot saved to {os.path.abspath(save_path)}")
    else:
        plt.show()

def show_clusters(dataset,hue_by,save_path=None):
    # Let' visualize these clusters
    plt.figure(figsize=(20, 10))
    sns.scatterplot(x='Annual_Income', y = 'Spending_Score', data=dataset, hue=hue_by, palette='colorblind')
    
    # Save the plot if save_path is provideWW@d
    if save_path:
        plt.savefig(save_path, dpi=300)
        plt.close()
        print(f"Clusters visualization plot saved to {os.path.abspath(save_path)}")
    else:
        plt.show()