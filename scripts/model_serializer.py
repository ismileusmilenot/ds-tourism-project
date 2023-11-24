import pickle

class ModelSerializer:
    """
    Save and Load Models into a file specified in the constructor.
    
    ModelSerializer('models/best_model.sav').dump(model)
    ModelSerializer('models/best_model.sav').load()
    """

    def __init__(self, filename='models/model.sav'):
        self.filename = filename
        
    def dump(self, model):
        return pickle.dump(model, open(self.filename, 'wb'))
    
    def load(self):
        return pickle.load(open(self.filename, 'rb'))


    

#def save_model(filename='final_model.sav'):
#    return pickle.dump(model, open(filename, 'wb'))

#def load_model(filename='final_model.sav'):
#    return pickle.load(open(filename, 'rb'))

