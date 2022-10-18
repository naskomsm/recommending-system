# 🥃 Recommending system

- The main idea of this app is to try and recommend different whiskies based on some properties and put the whiskies into groups. Of course they are for the sake of demo. You can add/remove whatever you want.

* smokiness - from (0-3)
* heaviness - from (0-3)
* coastalness - from (0-3)

Creating clusters using the 'k-means clustering' algorithm. Briefly how k-means clustering works:

- The process begins with k centroids initialised at random.
- These centroids are used to assign points to its nearest cluster.
- The mean of all points within the cluster is then used to update the position of the centroids
- The above steps are repeated until the values of the centroids stabilise.

The main problem here is the question - how to determine the optimal number of clusters for k-means clustering? The 'elbow method' is the thing that will help us determine the number of clusters in a data set.

- The method consists of plotting the explained variation as a function of the number of clusters and picking the elbow of the curve as the number of clusters to use.

After creating the clusters we can try and run the project to see what it recommends. Additionally we can apply some filters afterwards.

## 🕵️‍♂️ Try it out

- In root folder create python environment and activate it.

```
python3 -m venv env
source env/bin/activate
```

- Afterwards install the requirements.

```
pip install -r requirements.txt
```

- Get the optimal number for clusters

```
Go inside /services -> python3 elbow_method.py
This will give you an image showing 'elbow'. The curve of the elbow is the number you want. In our case it will be between 3 and 4. So i will choose 3.
```

- Create the clusters

```
Go inside /services -> python3 create_clusters.py
This will create the clusters and we are ready to go.
```

- Run the flask application

```
python3 api.py
```
