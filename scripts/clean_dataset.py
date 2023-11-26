import numpy as np

def clean_dataset(df):
    df.drop('ID', axis=1, inplace=True)

    df.replace({" Wildlife": "Wildlife"}, inplace=True)

    df.replace({'Yes': 1, 'No': 0}, inplace=True)

    country_replacements = {
        "SWIZERLAND": "SWITZERLAND",
        "BURGARIA":   "BULGARIA",
        "MALT":       "MALTA",
        "DRC":        "DEMOCRATIC REPUBLIC OF THE CONGO",
        "SCOTLAND":   "UNITED KINGDOM",
        "UAE":        "UNITED ARAB EMIRATES",
        "PHILIPINES": "PHILIPPINES",
        "DJIBOUT":    "DJIBOUTI",
        "MORROCO":    "MOROCCO"
    }
    df.country = df.country.replace(country_replacements)
    
    df['most_impressing'].fillna('No comments', inplace=True)
    
    df['night_total'] = df['night_zanzibar'] + df['night_mainland']
    
    df['age_group'] = df['age_group'].replace('24-Jan', '1-24')

    
    
    no_women  = df['total_female'] == 0
    one_woman = df['total_female'] == 1
    no_men    = df['total_male']   == 0
    one_man   = df['total_male']   == 1
    singles   = (one_woman & no_men) | (no_women & one_man)

    # set single travelers to 'Alone'
    df.loc[singles, 'travel_with'] = 'Alone'

    # create new columns for single travelers (OHE)
    df['single_female']   = one_woman & no_men
    df['single_male']     = no_women & one_man

    # update total_travelers
    df["total_travelers"] = df["total_female"] + df["total_male"]
    
    # where traveling alone choose either male or female
    random_field = np.random.choice(['total_female', 'total_male'])
    df.loc[no_women & no_men & (df['travel_with'] == 'Alone'),  [random_field]] = 1

    # when traveling with spouse
    df.loc[no_women & no_men & (df['travel_with'] == 'Spouse'), ['total_male', 'total_female']] = 1

    # the rest is spouse + children or friends and relatives. lets assume this:
    df.loc[df.total_travelers == 0, ['total_male', 'total_female']] = 2

    # update total_travelers
    df['total_travelers'] = df['total_female'] + df['total_male']
    
    df.dropna(inplace=True)
    
    # Remove duplicates if any
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        df.drop_duplicates(inplace=True)
    
    return df
