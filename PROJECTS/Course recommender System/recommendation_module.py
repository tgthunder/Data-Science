# Importing Data preprocessing Libraries
import numpy as np
import pandas as pd

# Importing text preprocessing libraries
import neattext.functions as nfx
import nltk
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity,linear_kernel

# Load dataset
df = pd.read_csv("udemy_courses.csv")

# Removing null and duplicate values
df.drop_duplicates(inplace=True,ignore_index=True)

# Clean Text: By removing stopwords,special characters,punctuations
df["clean_course_title"] = df["course_title"].apply(nfx.remove_stopwords)
df["clean_course_title"] = df["clean_course_title"].apply(nfx.remove_special_characters)
df["clean_course_title"] = df["clean_course_title"].apply(nfx.remove_punctuations)
df["clean_course_title"] = df["clean_course_title"].apply(lambda x: x.lower())

# Counting "course" word which is common in many course 
# It will impact which calculating similarity so we will remove "course" word
df['clean_course_title'] = df['clean_course_title'].apply(lambda x: x.replace("course","@"))
df["clean_course_title"] = df["clean_course_title"].apply(nfx.remove_special_characters)

# Converting all the text into numbers
vectorizer = CountVectorizer()
vec_mat = vectorizer.fit_transform(df["clean_course_title"])

# Cosine Similarity
cos_mat = cosine_similarity(vec_mat)

def recommand(user_input,num_of_rec=10):
    user_input_cv = vectorizer.transform([user_input])
    sim_user_input = cosine_similarity(vec_mat, user_input_cv).flatten()
    
    course_indices = sim_user_input.argsort()[::-1][:10] # Get indices of top 5 similar courses
    

    # Sort courses based on number of subscribers
    recommended_course_indices = sorted(course_indices, key=lambda idx: df.iloc[idx].num_subscribers, reverse=True)
    
    result_df = df.iloc[recommended_course_indices]
    
    final_recommended_courses = result_df[['course_title','url','price','num_subscribers']]
    return final_recommended_courses.head(num_of_rec)




    

