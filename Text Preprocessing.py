def clean(text):
    #performing lowercase 
    text=re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))','',text, flags=re.MULTILINE)
    text=re.sub(r'#','',text) #removal of Hastags
    text=re.sub(r'RT[\s]+','', text) #Removal of retweets
    text=re.sub(r'@[A-Za-z0-9]+','',text) #Removal of '@'\
    text=re.sub(r'[^\x00-\x7f]',r' ',text)#Removing ascii characters
    text=str(text).lower()
    text = text.translate(str.maketrans('', '', string.punctuation))#removing punctuations
    text=re.sub('\n', '',text)
    text=re.sub("\d+","",text)
    return(text) 

#conversion of emoji's 
def emojis(text):
    for fig in emoji.UNICODE_EMOJI:
        text=re.sub(r'('+emot+')',"_".join(emoji.UNICODE_EMOJI[emot].replace(","," ").replace(":"," ").split()),text)
        return(text)

#tokenization, Lemmitization and stemming 
le=WordNetLemmatizer()
ps=PorterStemmer()

def norm(text):
    words=word_tokenize(text)
    words_stem=[le.lemmatize(w) for w in words]
    words_lem=[sb.stem(w) for w in words_stem]
    return words_lem

#Tokenization
def tokenize(text):
    words= word_tokenize(text)
    return(words)

#Removal of stop words
from collections import Counter
def stop(text):
    stop_words = stopwords.words('english')
    stopwords_dict = Counter(stop_words)
    text=' '.join([word for word in text.split() if word not in stopwords_dict])
    return(text)

#Removal of frequent words 
from collections import Counter
cnt = Counter()
for text in df["Tweets"].values:
    for word in text:
        cnt[word] += 1
     
cnt.most_common(10)
FREQWORDS = set([w for (w, wc) in cnt.most_common(10)])
def remove(text):
    return " ".join([word for word in str(text).split() if word not in FREQWORDS])
