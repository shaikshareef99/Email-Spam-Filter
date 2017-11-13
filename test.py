
import os,codecs
from train import trained_classifier  	#import trained classifier
from extract_feature import *			#import extrat_features funtion



"""Calculate each feature probability in given label using naive bayes algorithm"""
def feature_probability(classifier, feature, label,ap=1.0):        
    feature_count = classifier.feature_count[label][feature]    
    label_count = classifier.label_word_count[label]    
    x=(float(feature_count)+ap)/(label_count+(ap*(len(classifier.feature_count['ham'].keys()+classifier.feature_count['spam'].keys()))))    
    return x*1000.0
    
"""calculate the email probability of given label"""    
def email_probability(classifier, features, label):   
        p = 1.0        
        for feature in features:            
            p = p*feature_probability(classifier,feature, label)        
        return p
        
        
"""Calculate the over all probability of give label with all the emails"""
def probability(classifier, features, label):            
        label_prob = (float(classifier.label_email_count[label]) / classifier.total_email_count)*10.0    
        doc_prob = email_probability(classifier,features, label)        
        return doc_prob*label_prob
    
"""Classify the given new email is spam or ham based on the probability"""    
def classify(classifier, features,lab):       
        spam_prob=probability(classifier,features, 'spam')
        ham_prob=probability(classifier,features, 'ham')        
        if(spam_prob>ham_prob):
            return 'spam'
        else:
            return 'ham'        


"""test the trained classifier with test emails"""
def test(classifier, corpus='C:\\Users\\Kishore\\spamfilter\\test'):      
    spam_dir = os.path.join(corpus, 'spam')
    ham_dir = os.path.join(corpus, 'ham')
    correct = total = 0
    for (path, label) in ((spam_dir, 'spam'), (ham_dir, 'ham')):
        for filename in os.listdir(path):             
            contents=codecs.open(os.path.join(path, filename)).read()                           
            features = extract_features(contents)            
            result = classify(classifier,features,label)            
            if result==label:                
                correct=correct+1                    
            total=total+1            
    print "correct:", correct, "total::",total
    print 'Accurary of test data is', (float(correct)/total)*100
        



test(trained_classifier,)
