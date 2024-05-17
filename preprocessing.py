#this file deals with the preprocessing of the data and generate the final merged dataset for further analysis, feature selection and classification


def filter_low_counts(df, min_counts=10, min_samples=3):
    #this function filters out genes with low counts
    return df[(df >= min_counts).sum(axis=1) >= min_samples]

def normalize_rnaseq_data(df, case_samples, control_samples):
    #this function uses CPM to normalize the data
    case_df = df[case_samples]
    control_df = df[control_samples]

    # Function to compute CPM
    def compute_cpm(df):
        return df.div(df.sum()) * 1e6

    # Compute CPM for case and control
    case_df_cpm = compute_cpm(case_df)
    control_df_cpm = compute_cpm(control_df)
    normalize_df=compute_cpm(df)
    return normalize_df, case_df_cpm, control_df_cpm 

def transpose(df):
    #this function transposes the dataframe
    df_transposed = df.transpose()
    return df_transposed
    
if __name__ == '__main__':
    import pandas as pd
    df = pd.read_csv('Countdata.csv', sep=',')  
    print("DataFrame")
    print(df)

    # Filter low counts function is called
    df.set_index(df.columns[0], inplace=True)
    df_filtered = filter_low_counts(df)
    df_filtered.reset_index(inplace=True)
    df_filtered.to_csv('filtered.csv', index=False)
    print("Filtered DataFrame")
    print(df_filtered)
    
    with open('case_label.txt') as fin:
        lines = fin.readlines() 
        case_samples = [line.strip() for line in lines]
    with open('control_label.txt') as fin:
        lines = fin.readlines() 
        control_samples = [line.strip() for line in lines]
    #print(case_samples, control_samples)

    # Normalize RNASeq data function is called
    df_filtered.set_index(df_filtered.columns[0], inplace=True)
    df_normalized, case_df_cpm, control_df_cpm = normalize_rnaseq_data(df_filtered, case_samples, control_samples)
    df_normalized.reset_index(inplace=True)
    df_normalized.to_csv('normalized_data.csv', index=False)
    print("normalised dataframe")
    print(df_normalized)#case_df_cpm, control_df_cpm 

    # The normalised DF is transposed 
    transformed_df=transpose(df_normalized)
    print("transformed dataframe")
    print(transformed_df)
    transformed_df.to_csv('transformed.csv',header=False)

    #the lines below are to merge the data with metadata and convert the last column to binary
    #the final dataset is saved as merged_final.csv and is used for further analysis
    data=pd.read_csv('transformed.csv')
    print(data)
    metadata=pd.read_csv('Meta_File.csv')
    print(metadata)
    merged = pd.merge(data, metadata, on='Gene_id')
    print(merged)

    last_column_index = merged.columns[-1]
    last_column_values = merged.iloc[:, -1]

    for idx, value in last_column_values.items():
            if value == 'Normal':
                    merged.at[idx, last_column_index] = 1
            else:
                    merged.at[idx, last_column_index] = 0
    print(merged)                
    merged.to_csv('merged_final.csv',index=False)