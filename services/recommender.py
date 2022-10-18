import numpy as np
import pandas as pd
import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

def get_distillery(searched_distillery: str, distillery_names: list):
    valid_name = False
    searched_distillery_index = -1

    if searched_distillery in distillery_names:
        valid_name = True

    if valid_name:
        searched_distillery_index = distillery_names.index(searched_distillery)

    return searched_distillery_index, searched_distillery


def get_whisky(searched_whisky: str, whisky_names: list):
    valid_name = False
    searched_whisky_index = -1

    if searched_whisky in whisky_names:
        valid_name = True

    if valid_name:
        searched_whisky_index = whisky_names.index(searched_whisky)

    return searched_whisky_index, searched_whisky


def run_recommender(name: str):
    whisky_data = pd.read_csv(f"{os.getcwd()}/static/whiskys_with_cluster.csv")
    whisky_features = ['smokiness', 'heaviness', 'coastalness']
    whisky_names = whisky_data['whisky_name'].tolist()

    whisky_2_group = dict(
        zip(whisky_data.whisky_name.values, whisky_data.Cluster.values))
    searched_whisky_index, searched_whisky = get_whisky(name, whisky_names)
    cluster = whisky_2_group[searched_whisky]
    searched_whisky_loc = whisky_data.loc[whisky_data.index[searched_whisky_index], whisky_features]

    searched_whisky_loc = searched_whisky_loc.values
    recommendation = whisky_data[whisky_data['Cluster'] == cluster]
    recommendation['distance'] = recommendation[whisky_features].sub(
        np.array(searched_whisky_loc)).pow(2).sum(1).pow(0.5)

    recommendation = recommendation.sort_values(by=['distance'])

    recommendation = recommendation['whisky_name'].tolist()

    return recommendation
