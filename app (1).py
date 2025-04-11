# Importing necessary libraries
import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the dataset (ensure the path is correct)
df = pd.read_csv("/content/youtube_khan_academy.csv")

# Assuming 'title' is the column for video titles
topic_column = 'title'

# Label Encoding for the video titles
le = LabelEncoder()
df['topic_encoded'] = le.fit_transform(df[topic_column])

# Streamlit App Title
st.title("📚 AI-Based Personalized Learning Platform")

# User input for video title
user_topic = st.text_input("🔍 Enter a learning topic (video title):")

# When user inputs a topic, this block runs
if user_topic:
    try:
        # Encoding the input title
        encoded = le.transform([user_topic])[0]
        st.success(f"✅ Encoded topic: {encoded}")

        # Getting recommended videos based on encoded title
        recommended = df[df['topic_encoded'] == encoded].head(5)

        # Displaying the recommended videos
        st.write("🎯 Recommended videos:")

        for index, row in recommended.iterrows():
            title = row['title']
            video_url = row.get('url', '')  # Ensure CSV has 'url' column

            # Check if the URL exists and is valid
            if pd.notna(video_url) and video_url != '':
                st.markdown(f"- [{title}]({video_url})")  # Link the title to the URL
            else:
                st.markdown(f"- {title} (No URL available)")  # If no URL is available

    except ValueError:
        # If the title is not found in the encoding
        st.error("⚠️ Topic not seen in training data. Try a different title.")
