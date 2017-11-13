
import os,codecs
from clasifier import *
from extract_feature import *



""""This funciton used to call the classifier object train funciton with 
	the extracted features from each email with given label"""    

def train_classifier(classifier, path, label):	
    for filename in os.listdir(path):
        contents = codecs.open(os.path.join(path, filename)).read()                 
        features = extract_features(contents)        
        classifier.train(features, label)
            

""""Get train data spam and ham emails from the corpus and pass to trai_classifier function"""

def train_data(classifier,corpus='C:\Users\spamfilter'):        
    spam_dir = os.path.join(corpus, 'spam')
    ham_dir = os.path.join(corpus, 'ham')   
    train_classifier(classifier, spam_dir, 'spam')  #train the classifier on spam emails
    train_classifier(classifier, ham_dir, 'ham') 	#train the classifier on ham emails
    


clss=classifier() 			#create classifier object               
train_data(clss,) 			#pass the classifier to train_data funtion
trained_classifier=clss #assign trained classifier to trained_classifier
