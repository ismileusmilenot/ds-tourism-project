# Formats a number as currency with symbol
def currency(number, unit="€"):
    return "{:,.2f} {}".format(number, unit)

def remove_outliers(dataframe, column_name, lower=25, upper=75):
    c = dataframe[column_name]
    lower_bound  = c.quantile(lower/100), 
    upper_bound  = c.quantile(upper/100)
    outlier_mask = (c < lower_bound) | (c > upper_bound)
    return dataframe[~outlier_mask]



from sklearn.metrics import (
    classification_report,
    confusion_matrix, 
    accuracy_score,
)

# Function to calculate accuracy 
def cal_accuracy(y_test, y_pred): 
    print("-----"*15)
    print ("Accuracy : \n", accuracy_score(y_test, y_pred) * 100) 
    
    print("-----"*15)
    print("Report : \n", classification_report(y_test, y_pred)) 

    print("-----"*15)
    print("Confusion Matrix: \n", confusion_matrix(y_test, y_pred)) 
    
    cf_test = confusion_matrix(y_test, y_pred_test)
    sns.set(rc={"figure.figsize":(4, 3)})
    sns.heatmap(cf_test, annot=True, fmt="", cmap='Blues');
  