"""subset_discretize.py:  splits the Cleaned_AG_News_Dataset_Unlabeled 1.xlsx 
dataset into 1000 random samples (exclusive) and discretizes into
20/40/60/80/100 percent of full message"""

# __ Libraries _________________________________________________________________
import pandas as pd


# __ Helper Functions __________________________________________________________
def five_split_df(df):
    '''Splits the cleaned news data set into 5 equal parts and returns a new dataframe.

    Arguments: df (the pandas dataframe read in from the xlsx file) using pandas.read_excel
    
    Returns: A new dataframe containing the 5 splits is returned.
    '''
    
    # initialize new empty dataframe to hold splits
    # TODO: different headers missing review response and user id
    split_df = pd.DataFrame(columns=['Article Index', 'Class Label', 'Description', 'Percent of Full'])
    
    i = 1
    # iterate through the reviews dataframe
    for index in df.index:

        # output index for status check
        print(f"{i} of {len(df)}")
        i += 1

        # get the current rows description
        description = df.loc[index]['Description']
        # split into list to separate based off of word count
        description_list = description.split()

        # get number of words in review for calculating split
        num_words = len(description_list)
        # split into 20, 40, 60, 80, 100
        twenty = description_list[:int(num_words *0.2)]
        fourty = description_list[:int(num_words *0.4)]
        sixty = description_list[:int(num_words *0.6)]
        eighty = description_list[:int(num_words *0.8)]

        # convert split lists back into strings
        twenty = ' '.join(twenty)
        fourty = ' '.join(fourty)
        sixty = ' '.join(sixty)
        eighty = ' '.join(eighty)
        hundred = description
    
        # append to split dataframe
        split_df.loc[len(split_df), split_df.columns] = df.loc[index]['Article Index'], df.loc[index]['Class Index'], twenty, 20
        split_df.loc[len(split_df), split_df.columns] = df.loc[index]['Article Index'], df.loc[index]['Class Index'], fourty, 40
        split_df.loc[len(split_df), split_df.columns] = df.loc[index]['Article Index'], df.loc[index]['Class Index'], sixty, 60
        split_df.loc[len(split_df), split_df.columns] = df.loc[index]['Article Index'], df.loc[index]['Class Index'], eighty, 80
        split_df.loc[len(split_df), split_df.columns] = df.loc[index]['Article Index'], df.loc[index]['Class Index'], hundred, 100
    
    # return the new dataframe containing the 5 splits of the review message
    return split_df



if __name__ == "__main__":
    # read in dataset
    df = pd.read_excel("Cleaned_AG_News_Dataset_Unlabeled 1.xlsx")

    # get 1000 samples from dataset
    df = df.sample(1000)

    # split and discretize
    df = five_split_df(df)

    # save to new excel file
    df.to_excel('news_dataset_random_1000_five_split.xlsx')
