# AI-Based-Civic-Feedback-System
Civic issue and feedback management system

## Project Description
The AI-Based Civic Feedback System is a web-based application designed to help citizens report civic issues and provide feedback in an efficient and transparent manner. The system automatically analyzes user-submitted text and assigns issues to the appropriate municipal departments using intelligent text analysis techniques.

## Problem Statement
Urban civic authorities receive a large number of complaints and feedback every day. Traditional systems rely on manual processing, which leads to delays, misclassification, and lack of transparency. Unstructured text submissions further increase the difficulty of analyzing and routing issues correctly.

## Proposed Solution
This project provides an automated solution that:
- Analyzes civic issues and feedback
- Predicts the appropriate department
- Allows departments to update issue status
- Enables citizens to track issue progress

## Key Features
- User registration and login
- Issue and feedback submission
- Automated department prediction
- Department dashboard for issue handling
- Status tracking and comments
- Admin monitoring and control

## Technologies Used
- Backend: Python, Django
- Frontend: HTML, CSS, JavaScript
- Database: SQLite
- Machine Learning: Scikit-learn (Naive Bayes)
- NLP: TF-IDF text processing
- Development Tool: VS Code

## System Workflow
1. User submits issue or feedback
2. Text is analyzed automatically
3. Issue is assigned to correct department
4. Department updates status and comments
5. User tracks updates in real time

## How to Run the Project
1. Clone the repository
2. Install required packages using:
   pip install -r requirements.txt
3. Run migrations:
   python manage.py migrate
4. Start server:
   python manage.py runserver
5. Open browser and access:
   http://127.0.0.1:8000/

## Use Case
This system can be used by municipal corporations to improve service delivery, reduce manual workload, and increase transparency in handling civic issues and public feedback.

## Conclusion
The AI-Based Civic Feedback System demonstrates how intelligent automation can enhance digital governance by ensuring faster issue resolution, better department coordination, and improved citizen satisfaction.
