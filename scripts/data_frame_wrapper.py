class DataFrameWrapper():
    def __init__(self, df):
        self.df = df
        
    def has_duplicates():
        return self.df.duplicated().sum() > 0
        
    def remove_duplicates(self)
        if self.has_duplicates():
            self.df.drop_duplicates(inplace=True)
        return self
    
    def unique(column_name):
        return self.df[column_name].unique()
    
    def replace_boolean()
        return self.df.replace({'Yes': True, 'No': False}, inplace=True)
    
    def missing_fields():
        return self.df.isna().sum()
    