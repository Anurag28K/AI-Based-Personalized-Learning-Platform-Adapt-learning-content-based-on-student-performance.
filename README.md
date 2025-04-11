# 🎓** AI-Based Personalized Learning Platform**

**Introduction**

Welcome to the AI-Based Personalized Learning Platform! This project focuses on classifying educational YouTube videos (specifically from Khan Academy) into different difficulty levels using a deep learning model. The goal is to recommend the most suitable learning content to users based on their input topic.

**Objective**

The primary objective of this project is to build a predictive model that categorizes YouTube videos into Remedial, Standard, or Advanced levels of difficulty. By analyzing features such as view count, like/dislike ratio, sentiment scores, and engagement metrics, we aim to provide personalized video recommendations to enhance learning experiences.

**Technologies Used**

Python: Used for data analysis, model development, and app creation

Libraries: Pandas, NumPy: Data manipulation and preprocessing

Scikit-learn: Feature scaling and encoding

PyTorch: Deep learning model development

Streamlit: Web app interface

Ngrok: For public deployment of the app

**Dataset Description**

The dataset used in this project contains metadata from YouTube videos related to Khan Academy content. It includes attributes like:

View count

Like/Dislike count

Comment count

Sentiment scores from comments

Description readability scores

Video length, title, and topic

**Project Overview**

**Data Preprocessing:**

Selected relevant features, handled missing values, and scaled numerical data for better model performance.

**Label Creation:**

Created custom difficulty levels based on view counts:

0 → Remedial

1 → Standard

2 → Advanced

**Model Building:**

Built a 3-layer feedforward neural network using PyTorch to classify video difficulty levels.

**Model Evaluation:**

Evaluated model performance using accuracy on test data to ensure prediction reliability.

**Web App Interface:**

Developed an interactive app using Streamlit that accepts a topic name and returns relevant video recommendations based on the trained model.

**Deployment:**

Used Ngrok to generate a public link and make the app accessible online.
