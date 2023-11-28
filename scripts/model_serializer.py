import pickle

class ModelSerializer:
    """
    Save and Load Models into a file specified in the constructor.
    
    ModelSerializer('models/best_model.sav').save(model)
    ModelSerializer('models/best_model.sav').load()
    """

    def __init__(self, filename='models/model.sav'):
        self.filename = filename
        
    def save(self, model):
        return pickle.dump(model, self.file('wb'))
    
    def load(self):
        return pickle.load(self.file())
    
    def file(self, mode='rb'):
        return open(self.filename, mode)



#def save_model(filename='final_model.sav', model):
#    return pickle.dump(model, open(filename, 'wb'))

#def load_model(filename='final_model.sav'):
#    return pickle.load(open(filename, 'rb'))

