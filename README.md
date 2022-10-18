# 🥃 Recommending system

- The main idea of this app is to try and recommend different whiskies based on some properties and put the whiskies into groups. Of course they are for the sake of demo. You can add/remove whatever you want.

* smokiness - from (0-3)
* heaviness - from (0-3)
* coastalness - from (0-3)
* price_range - price range of the whisky (0-3)
* availability - (1-4), 1-rearest, 4-most common
* strength_range - the strenth of the whisky (1-2)
* bottle_range -

Creating clusters using the 'k-means clustering' algorithm. Briefly how k-means clustering works:

- The process begins with k centroids initialised at random.
- These centroids are used to assign points to its nearest cluster.
- The mean of all points within the cluster is then used to update the position of the centroids
- The above steps are repeated until the values of the centroids stabilise.

The main problem here is the question - how to determine the optimal number of clusters for k-means clustering? The 'elbow method' is the thing that will help us determine the number of clusters in a data set.

- The method consists of plotting the explained variation as a function of the number of clusters and picking the elbow of the curve as the number of clusters to use.
