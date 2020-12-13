#function to create various N-gram combinations 
def tfidf(i,j):
    tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5,stop_words='english',ngram_range=(i,j))
    return(tfidf.fit_transform(df['Tweets']).toarray
    
  
#features and labels 
x=features
y=df['Label']

#Train test split
x_train, x_test, y_train, y_test = train_test_split(features, y, test_size=0.3, random_state=42)

#Classification using Multinomial Naive Bayes 
classifier = MultinomialNB(fit_prior=True,alpha=0.1)
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)

#Printing the metrics 
print("Classification Report: \n", classification_report(y_test,y_pred)) 
print("Accuracy: ", (accuracy_score(y_test, y_pred))*100)
print("F1 score: ",f1_score(y_test, y_pred, average='macro')) 

#Support Vector machine classifier
clf=SVC(C=1,gamma=1,kernel='linear',probability=True)
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)

#printing metrics 
print("Classification Report: \n", classification_report(y_test,y_pred))
print("Accuracy: ", (accuracy_score(y_test, y_pred))*100)
print("F1 score: ",f1_score(y_test, y_pred, average='macro')) 

#function to plot ROC for classifiers 
def ROC(model):
    ypred=model.predict_proba(x_test)
    return(skpl.metrics.plot_roc(y_test,ypred))

#Plotting the classifer's ROC 
ROC(classifier)
ROC(clf)
