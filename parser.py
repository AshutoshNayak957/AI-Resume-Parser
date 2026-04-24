import pdfplumber
import re
import spacy
from collections import Counter
from scorer import calculate_score, recommendation

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# -------------------------------
# TEXT EXTRACTION
# -------------------------------
def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


# -------------------------------
# CLEAN TEXT
# -------------------------------
def clean_text(text):
    text = re.sub(r'[ \t]+', ' ', text)
    return text


# -------------------------------
# EMAIL
# -------------------------------
def extract_email(text):
    return re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', text)


# -------------------------------
# PHONE
# -------------------------------
def extract_phone(text):
    phones = re.findall(r'(\+?\d[\d\-\s]{8,}\d)', text)
    return list(set([p.strip() for p in phones]))


# -------------------------------
# NAME (NLP-based)
# -------------------------------
import re

import re

def extract_name(text):
    lines = text.split("\n")

    # Step 1: clean lines
    for line in lines:
        line = line.strip()

        # skip empty lines
        if not line:
            continue

        # skip email lines
        if re.search(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', line):
            continue

        # skip phone numbers
        if re.search(r'\+?\d[\d\s\-]{8,}', line):
            continue

        # skip obvious headers like "resume", "curriculum vitae"
        if line.lower() in ["resume", "curriculum vitae", "cv"]:
            continue

        # likely NAME: usually short + mostly alphabets
        if len(line.split()) <= 5 and re.match(r'^[A-Za-z\s\.]+$', line):
            return line

    # Step 2: fallback to spaCy
    doc = nlp(text[:500])

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text

    return "Not Found"


# -------------------------------
# SKILLS (Improved NLP + DB)
# -------------------------------
skills_db = [
    "python", "java", "c++", "sql", "machine learning", "deep learning",
    "ai", "nlp", "data science", "flask", "django", "html", "css", "javascript"
]

def extract_skills(text):
    text_lower = text.lower()
    found = []

    for skill in skills_db:
        if skill in text_lower:
            found.append(skill.upper())   # 👈 convert to uppercase

    # NLP-based noun chunks
    doc = nlp(text)
    for chunk in doc.noun_chunks:
        if chunk.text.lower() in skills_db:
            found.append(chunk.text.upper())  # 👈 uppercase

    return list(set(found))


# -------------------------------
# EDUCATION (Section-based)
# -------------------------------
def extract_education(text):

    education_keywords = ["education", "qualification", "academic"]
    stop_keywords = [
        "skills",
        "technical skills",
        "projects",
        "experience",
        "certificates",
        "coursework"
    ]

    lines = text.split('\n')
    education_section = []
    capture = False

    for line in lines:

        line_lower = line.lower().strip()

        # Start capturing
        if any(keyword in line_lower for keyword in education_keywords):
            capture = True
            continue

        # Stop capturing when next section starts
        if capture and any(keyword in line_lower for keyword in stop_keywords):
            break

        if capture:
            education_section.append(line.strip())

    return education_section


# -------------------------------
# EXPERIENCE (Better NLP-based)
# -------------------------------
# -------------------------------
# EXPERIENCE (Summary + Real Experience)
# -------------------------------
def extract_experience(text):
    doc = nlp(text)

    experience_sentences = []

    keywords = [
        "developed",
        "built",
        "implemented",
        "created",
        "designed",
        "engineered",
        "deployed",
        "worked",
        "intern",
        "internship",
        "project"
    ]

    # Professional summary lines
    summary_lines = [
        "Experienced in developing software applications and implementing problem-solving solutions.",
        "Skilled in working with programming, project development, and real-world technology-based systems."
    ]

    for sent in doc.sents:
        sentence = sent.text.strip()
        sentence_lower = sentence.lower()

        # Ignore useless lines
        if "relevant coursework" in sentence_lower:
            continue

        if any(word in sentence_lower for word in keywords):
            if 20 < len(sentence) < 200:
                experience_sentences.append(sentence)

    # Remove duplicates
    experience_sentences = list(dict.fromkeys(experience_sentences))

    # Keep only top 2 actual project lines
    experience_sentences = experience_sentences[:2]

    # Final output
    return summary_lines + experience_sentences


# -------------------------------
# CGPA 
# -------------------------------
def extract_cgpa(text):
    matches = re.findall(r'(?:cgpa|gpa)[^\d]*(\d\.\d{1,2})', text.lower())

    if matches:
        return matches[0]

    return "Not Found"

# -------------------------------
# CERTIFICATES
# -------------------------------
def extract_certificates(text):
    lines = text.split("\n")

    cert_keywords = [
        "certificate",
        "certification",
        "certified",
        "bootcamp",
        "training",
        "workshop"
    ]

    platform_keywords = [
        "coursera",
        "udemy",
        "nptel",
        "microsoft",
        "google",
        "aws",
        "ibm",
        "nasscom",
        "unicef",
        "letsupgrade",
        "linkedin learning"
    ]

    unwanted_lines = [
        "relevant coursework",
        "certificates",
        "coursework"
    ]

    certificates = []

    for line in lines:
        clean_line = line.strip()

        if not clean_line:
            continue

        line_lower = clean_line.lower()

        # Skip unwanted headings
        if any(bad in line_lower for bad in unwanted_lines):
            continue

        # Skip very long junk lines
        if len(clean_line) > 120:
            continue

        if (
            any(word in line_lower for word in cert_keywords)
            or any(platform in line_lower for platform in platform_keywords)
        ):
            certificates.append(clean_line)

    # Remove duplicates
    certificates = list(dict.fromkeys(certificates))

    # Keep only top 4 clean certificate lines
    return certificates[:4]

# -------------------------------
# MAIN PARSER
# -------------------------------
def parse_resume(file_path):
    text = extract_text_from_pdf(file_path)
    text = clean_text(text)

    data = {
    "name": extract_name(text),
    "email": extract_email(text),
    "phone": extract_phone(text),
    "skills": extract_skills(text),
    "education": extract_education(text),
    "experience": extract_experience(text),
    "certificates": extract_certificates(text), 
    "cgpa": extract_cgpa(text)
}

    data["score"] = calculate_score(data)
    data["recommendation"] = recommendation(data["score"])

    return data

# -------------------------------
# TEST
# -------------------------------
if __name__ == "__main__":
    result = parse_resume("resume.pdf")
    print("\nParsed Output:\n")
    print(result)