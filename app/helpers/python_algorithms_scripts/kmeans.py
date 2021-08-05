import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns;

sns.set()

df1 = pd.read_csv('../../data/datatest.csv').drop(['sn', 'date'], axis=1)
df2 = pd.read_csv('../../data/datatest2.csv').drop(['sn', 'date'], axis=1)
df_train = pd.read_csv('../../data/datatraining.csv').drop(['sn', 'date'], axis=1)

df_total = df_train.append(df1).append(df2)
x = np.array(df_total[['Light', 'Temperature']])
y = np.array(df_total['Occupancy'])

# K-means clustering with hardcoded centroids, calculated from previous executions to achieve optimal result
kmeans = KMeans(n_clusters=2, n_init=1, init=np.array([[10.33503514, 20.50117836], [466.37994764, 22.03506988]]))
kmeans.fit(x)
# Predicted values
y_kmeans = kmeans.predict(x)

correct = 0
for i in range(len(y)):
    if y[i] == y_kmeans[i]:
        correct = correct + 1

print('Total elements: ' + str(len(y)))
print('Correct predictions: ' + str(correct))
print('Wrong predictions: ' + str((len(y_kmeans) - correct)))
print('Accuracy ' + '{0:.2%}'.format(correct/len(y)))

# ####PLOTS
# Create plot with predicted values
# Create custom colormap with 2 colors
base = plt.cm.get_cmap('coolwarm')
color_list = base(np.linspace(0, 1, 2))
custom_cmap = plt.cm.colors.ListedColormap(color_list, color_list, 2)

plt.scatter(x[:, 0], x[:, 1], c=y_kmeans, s=15, cmap=custom_cmap)
plt.xlabel('Light')
plt.ylabel('Temperature')
cbar = plt.colorbar(label='Occupancy',ticks=np.linspace(0.25, 0.75, 2))
cbar.set_ticklabels([0,1])
plt.title('k-means occupancy predicted values');
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5);
plt.savefig('../../img/kmeans_predicted_clusters.png')

# Create plot with actual values
plt.scatter(x[:, 0], x[:, 1], c=y, s=15, cmap=custom_cmap)
plt.title('k-means occupancy actual values');
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5);
plt.savefig('../../img/kmeans_actual_clusters.png')
