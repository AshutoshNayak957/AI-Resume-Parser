def calculate_score(data):
    score = 0

    # Name
    if data.get("name") and data["name"] != "Not Found":
        score += 8

    # Email
    if data.get("email") and len(data["email"]) > 0:
        score += 8

    # Phone
    if data.get("phone") and len(data["phone"]) > 0:
        score += 8

    # Skills (important but controlled)
    skills_count = len(data.get("skills", []))

    if skills_count >= 5:
        score += 18
    elif skills_count >= 3:
        score += 14
    elif skills_count >= 1:
        score += 8

    # Education
    if data.get("education") and len(data["education"]) > 0:
        score += 12

    # Experience / Projects
    exp_count = len(data.get("experience", []))

    if exp_count >= 2:
        score += 15
    elif exp_count >= 1:
        score += 10

    # Certificates
    cert_count = len(data.get("certificates", []))

    if cert_count >= 3:
        score += 12
    elif cert_count >= 1:
        score += 8

    # CGPA
    if data.get("cgpa") and data["cgpa"] != "Not Found":
        score += 10

    # Small realism deduction so perfect resumes don't become 100
    if score > 95:
        score = 92

    return min(score, 95)


def recommendation(score):
    if score >= 85:
        return "Highly Recommended"
    elif score >= 70:
        return "Recommended"
    elif score >= 50:
        return "Consider"
    else:
        return "Not Recommended"