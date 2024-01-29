from dotenv import load_dotenv
import os
import sqlite3
import streamlit as st

import google.generativeai as genai 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##function to load google gimini model

def get_gimini_response(question, prompt):
    model = genai.GenerativeModel('gimini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

#Function to retrieve data from db
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

#define prompt 
prompt=[
      """
      You are an expert in converting English questions to SQL query!
      The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
      SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
      the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
      \nExample 2 - Tell me all the students studying in Data Science class?, 
      the SQL command will be something like this SELECT * FROM STUDENT 
      where CLASS="Data Science"; 
      also the sql code should not have ``` in beginning or end and sql word in output

      """


]

## Streamlit app

st.set_page_config(page_title="Retrive Any SQL query")
st.header("Gemini App to Retrieve SQL Data")

question = st.text_input("input: ", key='input')
submit = st.button("Ask the question")

#if submit is clicked
if submit:
    response = get_gimini_response(question, prompt)
    print(response)
    response = read_sql_query(response, 'student.db')
    st.subheader("The Response is:")
    for row in response:
        print(row)
        st.header(row)
