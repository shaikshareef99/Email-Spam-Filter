
import nltk,codecs
from nltk.corpus import stopwords  #import stopwords from NLTK corpus


"""This funciton used to extract the features from the email"""

def extract_features(content, min_len=2, max_len=20):   
 
    words = []       
    pattern = r'''(?x)([A-Z]\.)+|\w+(-\w+)*|\$?\d+(\.\d+)?%?| \.\.\.| [][.,;"'?():-_`]'''  	#regular expression to tokenize    
    tokens = nltk.regexp_tokenize(content,pattern)   
    words = [unicode(w.lower(),encoding='latin-1') for w in tokens]                 #convert all letters to lowercase   
    imp_words = [w for w in words if w.lower() not in stopwords.words('english')] 		#Remove stopwords    
    poster = nltk.PorterStemmer()    
    words = [poster.stem(w) for w in imp_words if min_len<=len(w)<=max_len]   			#stem the features   
      
return words
