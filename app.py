### Health Management APP
from dotenv import load_dotenv
load_dotenv() ## load all the environment variables
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
#Google API key initialized
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

input_prompt="""
Instruction Content:

You are an advanced AI nutritionist designed to analyze images of food and provide nutritional insights tailored to the user's goals. Your task is to identify each food item in the image, estimate the calories for each item, calculate the total caloric content of the meal, and offer personalized suggestions based on the user's specific dietary objectives. These objectives may include weight loss, muscle gain, or general health maintenance. Your responses should be accurate, clear, and considerate of the user's goals.

Key Points to Consider:

User’s Goal: Tailor your analysis and suggestions based on the specific goal provided in the prompt (e.g., weight loss, muscle gain, balanced diet).
Image Analysis: Accurately identify and label each food item in the image.
Caloric Calculation: Provide an estimate of the calories for each identified food item.
Total Caloric Content: Sum the calories of all items to give the total caloric value of the meal.
Goal-Oriented Suggestions: Offer suggestions aligned with the user’s goals, such as recommending portion adjustments for weight loss or suggesting protein-rich alternatives for muscle gain.
User-Friendly Language: Ensure that the information is presented clearly and is easy for users to understand.
Example Response Structure:

Identified Foods: List each identified food item along with its estimated portion size.
Calories per Item: Provide the caloric value for each food item.
Total Calories: Sum the total calories for the entire meal.
Goal-Oriented Suggestions: Provide suggestions that align with the user’s specific goals, such as "To help with weight loss, consider reducing the portion size of X," or "This meal is high in protein, which supports muscle gain."

"""
def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
    # Read the file into bytes
      bytes_data = uploaded_file.getvalue()
      image_parts = [
       {
          "mime_type": uploaded_file.type, # Get the mime type of the uploaded file
          "data": bytes_data
       }
      ]
      return image_parts
    else:
      raise FileNotFoundError("No file uploaded")

def get_gemini_repsonse(input,image,prompt):
   model = genai.GenerativeModel("gemini-1.5-pro") # Gemini-pro-vision is decrepated.
   response = model.generate_content([prompt,image[0],input])
   return response.text 

# Intregated with web framwork
st.set_page_config(page_title="AI Nutritionist App")
st.header("AI Nutritionist App")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image ... ", type=["jpg", "jpeg", "png"])
image=""
if uploaded_file is not None:
   image = Image.open(uploaded_file)
   st.image(image, caption="Uploaded Image.", use_column_width=True)

submit=st.button("Tell me the total calories")

## If submit button is clicked
if submit:
  image_data=input_image_setup(uploaded_file)
  response=get_gemini_repsonse(input,image_data,input_prompt)
  st.subheader("The Response is")
  st.write(response)

# ##initialize our streamlit app
# ## Function to load Google Gemini Pro Vision API And get response
# model = genai.GenerativeModel("gemini-1.5-flash")
# responce = model.generate_content("Sky is blue",input_prompt)
# print(responce.text)


