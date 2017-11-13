from collections import defaultdict

#Classifier object declaration
class classifier(object):

	"""Classifier feature initialization"""
	
    def __init__(self):        
        self.label_word_count = defaultdict(int)
        self.feature_count = defaultdict(lambda: defaultdict(int))
        self.total_word_count = 0
        self.total_email_count = 0
        self.label_email_count = defaultdict(int)  
        
          
     """Train function used to train the classifier based on the given features"""  
      
    def train(self,features,label):         
        for feature in features:
            self.feature_count[label][feature] = self.feature_count[label][feature]+1                  
            self.label_word_count[label] = self.label_word_count[label]+1
            self.total_word_count = self.total_word_count+1
            
        self.label_email_count[label] = self.label_email_count[label]+1
        self.total_email_count = self.total_email_count+1
