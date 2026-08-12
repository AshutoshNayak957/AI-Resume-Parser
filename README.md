# 🚀 AI Resume Parser

An AI-powered Resume Parser built using **Python, Flask, spaCy NLP, and PDF processing** to automatically extract and organize candidate information from resumes 📄.

This project helps improve HR screening by reducing manual effort and providing structured candidate evaluation with **ATS-style scoring** 🎯.

----

## ✨ Features

* ✅ Resume upload support (PDF, DOC, DOCX)
* 👤 Automatic extraction of:

  * Name
  * Email
  * Phone Number
  * Skills
  * Education
  * Experience
  * Certificates
  * CGPA
* 🤖 AI/NLP-based resume parsing using spaCy
* 🧠 Regex-based intelligent parsing
* 📌 Rule-based NLP extraction
* 📊 ATS-style candidate scoring system
* 💡 Recommendation status generation
* 🌙 Clean and modern dark UI
* 📂 Drag-and-drop resume upload interface

---

## 🛠️ Tech Stack

### Backend ⚙️

* Python
* Flask

### AI / NLP 🤖

* spaCy
* Regex
* Rule-based NLP

### Frontend 🎨

* HTML
* CSS
* JavaScript

### PDF Processing 📄

* pdfplumber

---

## 📁 Project Structure

```text
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
```

---

## ⚡ Installation

### Step 1: Clone the Repository 📥

```bash
git clone https://github.com/AshutoshNayak957/AI-Resume-Parser.git
cd AI-Resume-Parser
```

### Step 2: Create a Virtual Environment 🧪

```bash
python -m venv venv
```

### Activate the Virtual Environment

#### Windows 🪟

```bash
venv\Scripts\activate
```

#### Mac/Linux 🐧

```bash
source venv/bin/activate
```

### Step 3: Install Dependencies 📦

```bash
pip install -r requirements.txt
```

### Step 4: Install spaCy Model 🧠

```bash
python -m spacy download en_core_web_sm
```

### Step 5: Run the Project ▶️

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

---

## 🔍 How It Works

### Step 1️⃣ — Resume Upload

The user uploads a resume through the web interface.

### Step 2️⃣ — Text Extraction

The system extracts raw text from the uploaded resume using **pdfplumber**.

### Step 3️⃣ — Information Extraction

**spaCy NLP and Regex-based parsing** are used to identify candidate information such as:

* 👤 Name
* 📧 Email
* 📱 Phone Number
* 💻 Skills
* 🎓 Education
* 🏢 Experience
* 🏆 Certifications
* 📊 CGPA

### Step 4️⃣ — ATS Scoring

The extracted information is evaluated using an **ATS-style scoring system**.

### Step 5️⃣ — Result Generation

The system generates a structured candidate profile along with a score and recommendation status.

---

## 📊 Example Output

```text
Name: Ashutosh Nayak
Email: ashutoshn957@gmail.com

Skills:
PYTHON
SQL
MACHINE LEARNING
HTML
CSS

Score: 92 / 100
Status: Highly Recommended
```

---

## 🔥 Future Improvements

* 🚀 Resume vs Job Description Matching
* 🤖 ML-based Candidate Ranking
* 📊 Resume Shortlisting Dashboard
* 👨‍💼 Admin Panel for HR Teams
* 📄 PDF Download of Parsed Results
* 🗄️ Database Integration
* ☁️ Live Deployment on Cloud

---

## 📚 Learning Outcomes

This project helped in understanding:

* ✅ Real-world NLP applications
* ✅ Resume parsing systems
* ✅ Flask web development
* ✅ ATS scoring systems
* ✅ HR automation workflows
* ✅ Backend and frontend integration
* ✅ PDF text extraction
* ✅ Rule-based information extraction

---

## 👨‍💻 Author

### Ashutosh Nayak

**Artificial Intelligence Intern 🤖**

Passionate about **AI, Machine Learning, NLP, and Real-World Problem Solving** 🚀

🔗 **GitHub:** https://github.com/AshutoshNayak957

---

## 📜 License

This project is created for **learning, internship, portfolio, and professional development purposes** ✨.
