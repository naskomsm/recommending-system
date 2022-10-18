import pandas as pd
from sklearn.cluster import KMeans

def run_create_clusters():
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
        return whisky_groups, pred

    # Read File
    whisky = pd.read_csv('../static/whiskys.csv')

    # Select the features needed
    whisky_features = ['smokiness', 'heaviness', 'coastalness']

    # Get the features and distillery names from the data set
    X = whisky[whisky_features]
    labels = whisky[['whisky_name']]
    OPTIMAL_K = 4 # Change this depenging on the value generated from elbow_method.py

    whisky_recommendation, pred = classify_whisky(OPTIMAL_K, X, labels, 0)

    # Save the results to text files for displaying purpose
    filename = '../static/whiskys_clusters.txt'
    result_file = open(filename, 'w')
    for i in whisky_recommendation:
        result_file.write('Group ')
        result_file.write(str(i+1))
        result_file.write(': ')

        for j in range(len(whisky_recommendation[i])):
            if j != len(whisky_recommendation[i])-1:
                result_file.write(str(whisky_recommendation[i][j]))
                result_file.write(', ')
            else:
                result_file.write(str(whisky_recommendation[i][j]))

        result_file.write('\n')
        result_file.write('\n')

    result_file.close()

    # Add a column to whisky.csv for grouping
    pred += 1  # Increment 1 to turn 0-base to 1-base cluster
    pred = pd.DataFrame(pred, columns=['Cluster'])
    whisky = pd.concat([whisky, pred], axis=1)
    whisky.to_csv('../static/whiskys_with_cluster.csv', index=False)

    print(whisky)


run_create_clusters()
