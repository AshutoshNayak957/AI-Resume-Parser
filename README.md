🚀 AI Resume Parser

An AI-powered Resume Parser built using Python, Flask, spaCy NLP, and PDF processing to automatically extract and organize candidate information from resumes 📄. This project helps improve HR screening by reducing manual effort and providing structured candidate evaluation with ATS-style scoring 🎯.

---

✨ Features

✅ Resume upload support (PDF, DOC, DOCX)
✅ Automatic extraction of:

- 👤 Name
- 📧 Email
- 📱 Phone Number
- 💻 Skills
- 🎓 Education
- 🏢 Experience
- 🏆 Certificates
- 📊 CGPA

✅ AI/NLP-based resume parsing using spaCy
✅ ATS-style candidate scoring system
✅ Recommendation status generation
✅ Clean and modern dark UI 🌙
✅ Drag and drop resume upload interface 📂

---

🛠 Tech Stack

Backend ⚙️

- Python 🐍
- Flask 🌐

AI / NLP 🤖

- spaCy
- Regex-based intelligent parsing
- Rule-based NLP extraction

Frontend 🎨

- HTML
- CSS
- JavaScript

PDF Processing 📄

- pdfplumber

---

📁 Project Structure

AI-Resume-Parser/
│
├── app.py
├── parser.py
├── scorer.py
├── requirements.txt
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
└── uploads/

---

⚡ Installation

Step 1: Clone the Repository 📥

git clone https://github.com/AshutoshNayak957/AI-Resume-Parser.git
cd AI-Resume-Parser

---

Step 2: Create Virtual Environment 🧪

python -m venv venv

Activate it:

Windows 🪟

venv\Scripts\activate

Mac/Linux 🍎🐧

source venv/bin/activate

---

Step 3: Install Dependencies 📦

pip install -r requirements.txt

---

Step 4: Install spaCy Model 🧠

python -m spacy download en_core_web_sm

---

Step 5: Run the Project ▶️

python app.py

Open browser and visit:

http://127.0.0.1:5000/

---

🔍 How It Works

Step 1️⃣

User uploads a resume file 📄

Step 2️⃣

System extracts raw text using pdfplumber

Step 3️⃣

spaCy NLP + Regex intelligently parse candidate details 🤖

Step 4️⃣

ATS-style scoring logic evaluates the resume 📊

Step 5️⃣

Final structured output is displayed on the web interface 💡

---

📌 Example Output

Name: Ashutosh Nayak
Email: ashutoshn957@gmail.com
Skills: PYTHON, SQL, MACHINE LEARNING, HTML, CSS
Score: 92 / 100
Status: Highly Recommended

---

🔥 Future Improvements

🚀 Resume vs Job Description Matching
🚀 ML-based Candidate Ranking
🚀 Resume Shortlisting Dashboard
🚀 Admin Panel for HR Teams
🚀 PDF Download of Parsed Results
🚀 Database Integration
🚀 Live Deployment on Cloud

---

📚 Learning Outcome

This project helped in understanding:

✅ Real-world NLP applications
✅ Resume parsing systems
✅ Flask web development
✅ ATS scoring systems
✅ HR automation workflows
✅ Backend + Frontend integration

---

👨‍💻 Author

Ashutosh Nayak

Artificial Intelligence Intern 🤖
Passionate about AI, Machine Learning, NLP, and Real-World Problem Solving 🚀

🔗 GitHub: https://github.com/AshutoshNayak957


---

📜 License

This project is created for learning, internship, portfolio, and professional development purposes ✨
