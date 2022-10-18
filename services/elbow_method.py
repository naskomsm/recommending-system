import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def run_elbow():
    # Function to train model and produce results
    def classify_whisky(n_class, X, labels, rs):
        # Fit model and predict results
        cluster_machine = KMeans(n_clusters=n_class, random_state=rs).fit(X)
        pred = cluster_machine.predict(X)

        # Declare a dictionary and empty lists for each group
        whisky_groups = {}
        for i in range(n_class):
            whisky_groups[i] = []

        # Append the distillery names into the their assigned group
        for distillery, group in zip(labels['whisky_name'].tolist(), pred):
            whisky_groups[group].append(distillery)

        # Return whisky group and sse of the model
        return whisky_groups, cluster_machine.inertia_

    # Read File
    whisky = pd.read_csv('../static/whiskys.csv')

    # Select the features needed
    whisky_features = ['smokiness', 'heaviness', 'coastalness']

    # Get the features and distillery names from the data set
    X = whisky[whisky_features]
    labels = whisky[['whisky_name']]
    sse_list = []
    distortions = []

    for i in range(1, 12):
        whisky_recommendation, sse = classify_whisky(i, X, labels, 0)
        distortions.append(sse)
        sse_list.append((i, sse))

    # Save the sse in csv file
    filename_sse = '../static/model_sse.csv'
    sse_file = open(filename_sse, 'w')
    sse_file.write('k,sse\n')

    for k, sse in sse_list:
        sse_file.write(str(k))
        sse_file.write(',')
        sse_file.write(str(sse))
        sse_file.write('\n')

    sse_file.close()
    print('Elbow done.')
    # Display
    plt.figure()
    plt.plot(range(1, 12), distortions)
    plt.xlabel('k')
    plt.ylabel('Distortion')
    plt.title('The Elbow Method showing the optimal k')
    plt.show()


run_elbow()
