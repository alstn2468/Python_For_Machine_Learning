# build_matrix.py

import numpy as np
import pandas as pd

def get_rating_matrix(filename, dtype = np.float32) :
    df = pd.read_csv(filename)

    return df.groupby(['source', 'target'])['rating'].sum().unstack().fillna(0)

def get_frequent_matrix(filename, dtype = np.float32) :
    df = pd.read_csv(filename)
    df['rating'] = 1

    return df.groupby(['source', 'target'])['rating'].sum().unstack().fillna(0)


if __name__ == '__main__' :

    # get_rating_matrix test
    print('- get_rating_matrix test -')
    print(get_rating_matrix('./movie_rating.csv'))
    '''
    - get_rating_matrix test -
    target         Just My Luck  Lady in the Water  Snakes on a Plane  \
    source
    Claudia Puig            3.0                0.0                3.5
    Gene Seymour            0.0                3.0                3.5
    Jack Matthews           0.0                3.0                4.0
    Lisa Rose               3.0                2.5                3.5
    Mick LaSalle            2.0                3.0                4.0
    Toby                    0.0                0.0                4.5

    target         Superman Returns  The Night Listener  You Me and Dupree
    source
    Claudia Puig                0.0                 4.5                0.0
    Gene Seymour                0.0                 3.0                3.5
    Jack Matthews               5.0                 3.0                3.5
    Lisa Rose                   3.5                 3.0                2.5
    Mick LaSalle                3.0                 3.0                0.0
    Toby                        4.0                 0.0                0.0
    '''

    # get_frequent_matrix test
    print('- get_frequent_matrix test -')
    print(get_frequent_matrix('./movie_rating.csv'))
    '''
    - get_frequent_matrix test -
    target         Just My Luck  Lady in the Water  Snakes on a Plane  \
    source
    Claudia Puig            1.0                0.0                1.0
    Gene Seymour            0.0                1.0                1.0
    Jack Matthews           0.0                1.0                1.0
    Lisa Rose               1.0                1.0                1.0
    Mick LaSalle            1.0                1.0                1.0
    Toby                    0.0                0.0                1.0

    target         Superman Returns  The Night Listener  You Me and Dupree
    source
    Claudia Puig                0.0                 1.0                0.0
    Gene Seymour                0.0                 1.0                1.0
    Jack Matthews               1.0                 1.0                1.0
    Lisa Rose                   1.0                 1.0                1.0
    Mick LaSalle                1.0                 1.0                0.0
    Toby                        1.0                 0.0                0.0
    '''
