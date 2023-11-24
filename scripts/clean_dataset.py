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
    
    df["number_travelers"] = df["total_female"] + df["total_male"]

    df['night_total'] = df['night_zanzibar'] + df['night_mainland']
    
    df.dropna(inplace=True)
    
    return df