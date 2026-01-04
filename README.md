# AI-Driven Mental Health Triage & Safe Support System

## Project Overview
Mental health concerns are often expressed quietly through text such as chats, messages, or personal notes, but these early signs are easy to miss. Many individuals delay seeking help due to stigma, lack of awareness, or limited access to mental health professionals.

This project focuses on building a safe and ethical AI-based chatbot that helps identify potential emotional risk patterns from user-provided text and provides supportive, non-judgmental feedback.  
The goal is early awareness and responsible support, not diagnosis or treatment.

## Live Demo Application
The live Demo version of the project is available at:

https://safe-support-system.youware.app/

## Problem We Are Addressing
- Mental health issues such as depression and emotional distress are increasing, especially among students  
- People often express feelings through text rather than direct conversation  
- Early warning signs are frequently overlooked  
- Professional mental health support is not always immediately available  
- There is a need for a scalable and ethical system to assist with early mental health awareness using text data  

## Approach
We developed an AI-driven mental health triage chatbot that:
- Accepts user-written text describing emotions or thoughts  
- Uses machine learning techniques to analyze emotional patterns  
- Categorizes risk into Low, Moderate, or High levels  
- Provides safe and supportive feedback  
- Encourages users to seek human or professional help when necessary  

## How the System Works
├── dataset/
│ └── mental_health_data.csv
├── chatbot.py
├── requirements.txt
└── README.md


### Workflow
1. The user enters text through the chatbot interface  
2. The text is cleaned and preprocessed  
3. A machine learning model analyzes emotional indicators  
4. The system generates a risk score and category  
5. Safety rules ensure ethical and responsible responses  
6. The user receives a clear and supportive message  

## Technologies Used
- Python  
- Machine Learning using scikit-learn  
- TF-IDF for text representation  
- Logistic Regression for classification  
- Streamlit for the chatbot interface  
- Pandas and NumPy for data processing  

## Risk Levels Explained
The web application classifies text into three levels:
- **Low Risk**: No strong indicators of emotional distress  
- **Moderate Risk**: Possible emotional stress or discomfort  
- **High Risk**: Strong indicators of emotional distress  

## Responsible AI and Safety Principles
This project is designed with responsible AI principles:
- The system does not provide medical diagnosis or treatment  
- It avoids harmful or absolute statements  
- A clear disclaimer is presented to users  
- High-risk outputs encourage seeking professional or trusted human support  

## Impact and Use Cases
- Promotes early mental health awareness  
- Supports students and young adults  
- Useful as a screening assistant in educational settings  
- Can be integrated with chat platforms or wellness tools  

## Limitations
- This is not a medical or diagnostic tool  
- Results depend on the quality of user input  
- Cultural and language differences may affect accuracy  
- Human intervention is essential for high-risk cases  

## Future Improvements
- Support for multiple languages  
- Voice-based emotion analysis  
- Continuous mood tracking  
- Integration with counselors or telehealth services  

## Conclusion
This project demonstrates how artificial intelligence can be used responsibly and ethically to support early mental health awareness. By combining machine learning with strong safety measures, the system provides meaningful assistance while ensuring that human care remains central.
