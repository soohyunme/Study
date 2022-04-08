import pandas as pd
import numpy as np

pit_df = pd.DataFrame({'Team': ['PIT', 'PIT', 'PIT', 'PIT', 'PIT'],
                       'League': ['NL', 'NL', 'NL', 'NL', 'NL'],
                       'Year': [2012, 2011, 2010, 2009, 2008],
                       'RS': [651, 610, 587, 636, 735],
                       'RA': [674, 712, 866, 768, 884],
                       'W': [79, 72, 57, 62, 67],
                       'G': [162, 162, 162, 161, 162],
                       'Playoffs': [0, 0, 0, 0, 0]})

# Iterate over pit_df and print each index variable and then each row
for i, row in pit_df.iterrows():
    print(type(row))
    print(row)
    print(type(row))

# Print the row and type of each row
for row_tuple in pit_df.iterrows():
    print(row_tuple)
    print(type(row_tuple))

# Run differentials with .iterrows()


def calc_run_diff(runs_scored, runs_allowed):

    run_diff = runs_scored - runs_allowed

    return run_diff


giants_df = pd.DataFrame({'Team': ['SFG', 'SFG', 'SFG', 'SFG', 'SFG'],
                          'League': ['NL', 'NL', 'NL', 'NL', 'NL'],
                          'Year': [2012, 2011, 2010, 2009, 2008],
                          'RS': [718, 570, 697, 657, 640],
                          'RA': [649, 578, 583, 611, 759],
                          'W': [94, 86, 92, 88, 72],
                          'G': [162, 162, 162, 162, 162],
                          'Playoffs': [1, 0, 1, 0, 0]})

# Create an empty list to store run differentials
run_diffs = []

# Write a for loop and collect runs allowed and runs scored for each row
for i, row in giants_df.iterrows():
    runs_scored = row['RS']
    runs_allowed = row['RA']

    # Use the provided function to calculate run_diff for each row
    run_diff = calc_run_diff(runs_scored, runs_allowed)

    # Append each run differential to the output list
    run_diffs.append(run_diff)

giants_df['RD'] = run_diffs
print(giants_df)

'''
Iterating with .itertuples()
'''

rangers_df = pd.DataFrame({'Team': ['TEX', 'TEX', 'TEX', 'TEX', 'TEX', 'TEX', 'TEX', 'TEX', 'TEX', 'TEX', 'TEX', 'TEX', 'TEX', 'TEX', 'TEX', 'TEX', 'TEX', 'TEX', 'TEX', 'TEX', 'TEX', 'TEX', 'TEX', 'TEX', 'TEX', 'TEX', 'TEX', 'TEX', 'TEX', 'TEX', 'TEX', 'TEX', 'TEX', 'TEX', 'TEX', 'TEX', 'TEX'],
                           'League': ['AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL'],
                           'Year': [2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001, 2000, 1999, 1998, 1997, 1996, 1993, 1992, 1991, 1990, 1989, 1988, 1987, 1986, 1985, 1984, 1983, 1982, 1980, 1979, 1978, 1977, 1976, 1975, 1974, 1973],
                           'W': [93, 96, 90, 87, 79, 75, 80, 79, 89, 71, 72, 73, 71, 95, 88, 77, 90, 86, 77, 85, 83, 83, 70, 75, 87, 62, 69, 77, 64, 76, 83, 87, 94, 76, 79, 83, 57],
                           'Playoffs': [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]})

# Loop over the DataFrame and print each row's Index, Year and Wins (W)
for row in rangers_df.itertuples():
    i = row.Index
    year = row.Year
    wins = row.W

    # Check if rangers made Playoffs (1 means yes; 0 means no)
    if row.Playoffs == 1:
        print(i, year, wins)

'''
Run differentials with .itertuples()
'''


def calc_run_diff(runs_scored, runs_allowed):

    run_diff = runs_scored - runs_allowed

    return run_diff


run_diffs = []

# Loop over the DataFrame and calculate each row's run differential
for row in yankees_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA

    run_diff = calc_run_diff(runs_scored, runs_allowed)

    run_diffs.append(run_diff)

# Append new column
yankees_df['RD'] = run_diffs
print(yankees_df)

'''
apply()
'''


def text_playoffs(num_playoffs):
    if num_playoffs == 1:
        return 'Yes'
    else:
        return 'No'


# Gather sum of all columns
stat_totals = rays_df.apply(sum, axis=0)
print(stat_totals)

# Gather total runs scored in all games per year
total_runs_scored = rays_df[['RS', 'RA']].apply(sum, axis=1)
print(total_runs_scored)

# Convert numeric playoffs to text by applying text_playoffs()
textual_playoffs = rays_df.apply(lambda row: text_playoffs(row['Playoffs']), axis=1)
print(textual_playoffs)

'''
Settle a debate with .apply()
'''


def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc,2)


'''
Replacing .iloc with underlying arrays
'''


def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc, 2)

# win_percs_list = []
#
# for i in range(len(baseball_df)):
#     row = baseball_df.iloc[i]
#
#     wins = row['W']
#     games_played = row['G']
#
#     win_perc = calc_win_perc(wins, games_played)
#
#     win_percs_list.append(win_perc)
#
# baseball_df['WP'] = win_percs_list

# Use the W array and G array to calculate win percentages
win_percs_np = calc_win_perc(baseball_df['W'].values, baseball_df['G'].values)

# Append a new column to baseball_df that stores all win percentages
baseball_df['WP'] = win_percs_np

print(baseball_df.head())

'''
Bringing it all together: Predict win percentage
'''


def predict_win_perc(RS, RA):
    prediction = RS ** 2 / (RS ** 2 + RA ** 2)
    return np.round(prediction, 2)


win_perc_preds_loop = []

# Use a loop and .itertuples() to collect each row's predicted win percentage
for row in baseball_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA
    win_perc_pred = predict_win_perc(runs_scored, runs_allowed)
    win_perc_preds_loop.append(win_perc_pred)

# Apply predict_win_perc to each row of the DataFrame
win_perc_preds_apply = baseball_df.apply(lambda row: predict_win_perc(row['RS'], row['RA']), axis=1)

# Calculate the win percentage predictions using NumPy arrays
win_perc_preds_np = predict_win_perc(baseball_df['RS'].values, baseball_df['RA'].values)
baseball_df['WP_preds'] = win_perc_preds_np
print(baseball_df.head())