import numpy as np
import pandas as pd

# read in both csvs
sub1 = pd.read_csv("Hotel_Sub_1.csv")
reviews = pd.read_csv("Hotel_Review_1000_selected_unlabeled.csv")



# list to hold percentages parallel to sub1 iteration
percent_list = []
# loop through sub1 cav rows
for i in range(len(sub1)):
    # get current rows index sub1
    current_index= sub1['index'].iloc[i]
    # get character count of part in sub1
    char_count = len(sub1['part'].iloc[i])
    # find row in reviews by index match
    reviews_row = reviews[reviews['Index'] == current_index]
    # get character count of reviews text (full review)
    rev_char_count = len(reviews_row['reviews.text'].iloc[0])
    
    # divide sub1 part by reviews full text to get percentage
    percentage = char_count / rev_char_count
    # add to list of percentages parallel to sub1 rows
    # convert percent list to 100,80,60,40,20 %
    percent_list.append(int(np.ceil(percentage * 100)))

# insert percentage column into sub1
sub1.insert(3, "percent", percent_list, True)
# save sub1 with percent added
sub1.to_csv("sub1_with_percentage.csv")

print('saved')

