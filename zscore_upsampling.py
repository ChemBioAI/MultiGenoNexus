#this file deals with the zscore normalization and upsampling of the data to balance the classes

# this function perrforms zscore normalization on the merged data
def z_score_normalisation(df):
    cols_to_scale = df.columns[1:-1]
    scaler=StandardScaler()
    df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])
    return df
    #scaled_data=scaler.fit_transform(df)
    #scaled_df= pd.DataFrame(scaled_data, columns=df.columns)
    #print(df)
    #df.to_csv('z_final.csv',index=False)

# this function performs upsampling of the data using SMOTE
def smote_upsampling(df):
    from imblearn.over_sampling import SMOTE
    import pandas as pd
    
    df_features = df.drop(columns=['Condition','Gene_id'])
    target = df['Condition']

    smote = SMOTE()
    # Upsample the data
    X_resampled, y_resampled = smote.fit_resample(df_features, target)
    # Reconstruct the DataFrame with upsampled data
    df_upsampled = pd.DataFrame(X_resampled, columns=df_features.columns)
    df_upsampled['target'] = y_resampled
    return df_upsampled
    #df_upsampled.to_csv('upsampled.csv',index=False)

if __name__ == '__main__':
    from sklearn.preprocessing import StandardScaler
    import pandas as pd
    df=pd.read_csv('merged_final.csv')
    print(df)

    #calling zscore function to pertform zscore normalization
    z_score= z_score_normalisation(df)
    print(z_score)

    #calling smote_upsampling function to perform upsampling
    upsampled= smote_upsampling(df)
    print(upsampled)
    upsampled.to_csv('upsampled.csv',index=False)