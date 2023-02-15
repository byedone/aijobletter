import streamlit as st
import os
from dotenv import load_dotenv
import openai

load_dotenv()  # 读取 .env 文件中的环境变量
# Read OpenAI API key from environment variable

openai.api_key = os.getenv("OPENAI_API_KEY")

# Define a function to generate job letter
def generate_job_letter(name, email, job_title, job_description, tone, word_count):
    # Set up the prompt based on the user input
    prompt = f"Dear Hiring Manager, my name is {name} and I am writing to express my interest in the {job_title} position at your company. {job_description} "
    if tone == "Formal":
        prompt += "I look forward to the opportunity to discuss my qualifications further. Thank you for your time and consideration."
    else:
        prompt += "I'm really excited about this position and would love to chat more about it. Thanks for considering my application!"
    
    # Generate job letter using OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=word_count,
    )
    
    # Return generated job letter
    return response.choices[0].text

# Set up the Streamlit app
def main():
    st.title("Job Letter Generator")
    st.write("Please enter your personal details and job description:")

    name = st.text_input("Name")
    email = st.text_input("Email")
    job_title = st.text_input("Job Title")
    job_description = st.text_area("Job Description")

    tone = st.selectbox(
        "Select the tone of your job letter",
        ("Formal", "Informal")
    )

    word_count = st.slider(
        "Select the number of words in your job letter",
        min_value=50,
        max_value=500,
        value=200
    )

    # Generate job letter on button click
    if st.button("Generate Job Letter"):
        job_letter = generate_job_letter(name, email, job_title, job_description, tone, word_count)
        st.write("Here is your job letter:")
        st.write(job_letter)

        # Save job letter to a file
        with open(f"{name}_job_letter.txt", "w") as file:
            file.write(job_letter)

if __name__ == "__main__":
    main()