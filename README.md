Project Overview
Mental health concerns are often expressed quietly through text—such as chats, messages, or personal notes—but these early signs are easy to miss. Many people delay seeking help due to stigma, lack of awareness, or limited access to professionals.This project focuses on building a safe and ethical AI-based chatbot that helps identify potential emotional risk patterns from text and provides supportive, non-judgmental feedback. The goal is early awareness and responsible support, not diagnosis or treatment.
Live Application
You can access the live version of our project here:
🔗 https://safe-support-system.youware.app/
Problem We Are Addressing
Mental health issues like depression and emotional distress are increasing, especially among students
People often express feelings through text rather than direct conversation
Early warning signs are easily overlooked
Professional mental health support is not always immediately available
There is a need for a scalable, ethical system that can assist with early mental health awareness using text data.
Approach
We developed an AI-driven mental health triage chatbot that:
Accepts user-written text describing emotions or thoughts
Uses machine learning to analyze emotional patterns
Categorizes risk into Low, Moderate, or High levels
Provides safe, supportive feedback
Encourages users to seek human or professional help when needed
How the System Works
├── dataset/
│   └── mental_health_data.csv
├── chatbot.py
├── requirements.txt
└── README.md
The user enters text through the chatbot interface
The text is cleaned and preprocessed
A machine learning model analyzes emotional indicators
The system generates a risk score and category
Safety rules ensure ethical and responsible responses
The user receives a supportive and clear message
Technologies Used
Python
Machine Learning (scikit-learn)
TF-IDF for text representation
Logistic Regression for classification
Streamlit for the chatbot interface
Pandas & NumPy for data processing
Risk Levels Explained
The Web App classifies text into three levels:
Low Risk – No strong indicators of distress
Moderate Risk – Possible emotional stress or discomfort
High Risk – Strong indicators of emotional distress
We designed this project with responsible AI principles in mind:
This system does not provide medical diagnosis or treatment
It avoids harmful or absolute statements
A clear disclaimer is shown to users
High-risk outputs encourage seeking professional support
Impact and Use Cases
Helps promote early mental health awareness
Can support students and young adults
Useful as a screening assistant in educational settings
Can be integrated with chat platforms or wellness tools
Limitations
This is not a medical or diagnostic tool
Results depend on the quality of user input
Cultural and language differences may affect accuracy
Human intervention is essential for high-risk cases
Future Improvements
Support for multiple languages
Voice-based emotion analysis
Continuous mood tracking
Integration with counselors or telehealth services
Conclusion
This project demonstrates how AI can be used responsibly and ethically to support early mental health awareness. By combining machine learning with strong safety measures, the system provides meaningful assistance while keeping human care at the center.
