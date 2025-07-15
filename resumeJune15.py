from fpdf import FPDF
from datetime import datetime
import os



# Enhanced resume data with all projects and links
resume_data = {
    "name": "Majd Adel Abualnour",
    "title": "AI & IoT Developer | Full-Stack Developer | Tech Entrepreneur",
    "contact": {
        "location": "Gaza, Palestine",
        "phone": "+972 56 714 6842",
        "email": "majdapoalnoor@gmail.com",
        "github": "github.com/majdabualnour",
        "portfolio": "https://portfolio-5aue.vercel.app/",
        "linkedin": "https://www.linkedin.com/in/majd-abu-al-nour-500aba21b",
        "whatsapp": "wa.me/972567146842"
    },
    "summary": "19-year-old visionary AI & IoT Engineer and Full-Stack Developer with 6+ years of hands-on experience building cutting-edge, impactful tech solutions. Founder of Magic Tech MT and Dashxslash, with a proven track record driving humanitarian innovation (serving 200,000+ people) and transforming edtech (benefiting 5,000+ students). Award-winning technologist and published author, passionate about leveraging advanced technologies to solve complex real-world challenges with a focus on seamless user experience and robust performance.",
    "technical_skills": {
        "AI/ML": ["Python", "TensorFlow","OpenCV", "CNN", "Computer Vision","Google Colab"],
        "IoT & Embedded": ["Arduino", "Raspberry Pi", "ESP32", "Sensor Networks", "Embedded C++"],
        "Web/PC Development": ["Next.js", "Flask", "Django","FastAPI", "JavaScript", "TypeScript" ,"PyQt6"], # Added UI/UX Design
        "Data & Algorithms": ["SQL", "PostgreSQL", "Firebase",  "Data Analytics", "Data Structures", "Algorithms"],
        "DevOps & Tools": ["Docker", "CI/CD", "Linux", "Bash", "Vercel", "Git/GitHub/GitLab"]
    },
    "experience": [
        {
            "title": "Founder",
            "company": "Magic Tech MT",
            "period": "2023–Present",
            "location": "Gaza, Palestine",
            "details": [
                "Led a 10-person tech consultancy, delivering over 15 custom AI and full-stack solutions to diverse international clients.",
                "Developed advanced commercial projects, including automated inventory systems and sophisticated computer vision applications.",
                "Reduced client operational costs by 30-60% through strategic implementation of custom automation solutions."
            ],
            "link": "https://magicattech.onrender.com/"
        },
        {
            "title": "Founder",
            "company": "Dashxslash",
            "period": "2023–Present",
            "location": "Remote",
            "details": [
                "Founded and scaled an edtech platform, providing free access to premium courses for over 5,000 students.",
                "Implemented an AI-powered recommendation system that significantly increased user engagement by 40%.",
                "Optimized backend architecture, enabling the platform to handle 10x user growth without additional server resources."
            ],
            "link": "https://dashxslash.com"
        },
        {
            "title": "Lead Developer (Contract)",
            "company": "World Central Kitchen & WFP",
            "period": "2023",
            "location": "North Gaza",
            "details": [
                "Designed and deployed a critical wartime aid distribution system, improving efficiency by 9x and serving over 200,000 beneficiaries.",
                "Integrated thermal printing and multi-device synchronization capabilities, drastically reducing data errors from 4% to 0.01%.",
                "Trained 50+ staff on system operation, ensuring seamless functionality under high-pressure crisis conditions."
            ]
        }
    ],
    "projects": [
        {
            "name": "Aid Distribution System (WCK/WFP)",
            "tech": "Python, IoT, Thermal Printing, Real-time Databases",
            "details": [
                "Accelerated wartime aid distribution by 9x, ensuring critical supplies reached over 200,000 people in North Gaza.",
                "Achieved an exceptional 0.01% error rate, a significant reduction from the previous 4%."
            ],
            "impact": "Featured in WFP crisis response reports, demonstrating significant humanitarian impact.",
            "link": "https://portfolio-5aue.vercel.app/work/aid-distribution-system"
        },
        {
            "name": "SMART ASSIS Smart Home – Tech Talent 2022 Winner",
            "tech": "CNN, RNN, IoT, Home Automation",
            "details": [
                "Developed a voice and vision-controlled smart home system for intuitive automation.",
                "Enabled energy optimization, leading to 30% savings on utility costs for users.",
                "Awarded NASA-sponsored innovation trip for groundbreaking work."
            ],
            "impact": "Successfully deployed in 3 pilot homes, validating real-world applicability and energy savings.",
            "link": "https://portfolio-5aue.vercel.app/work/future-home"
        },
        {
            "name": "TSC Road Safety System – Silver Medal (Sri Lanka 2022)",
            "tech": "Computer Vision, Deep Learning, Sensor Integration",
            "details": [
                "Engineered a real-time accident prevention system to enhance road safety.",
                "Achieved 85% accuracy in hazardous object and condition detection.",
                "Supported by Persatuan Cinta Gaza Malaysia for community deployment."
            ],
            "impact": "Implemented and tested in 2 key Gaza intersections, demonstrating immediate safety improvements.",
            "link": "https://portfolio-5aue.vercel.app/work/next-generation-car"
        },
        {
            "name": "Learner Guide – Palestine Hackathon Finalist",
            "tech": "Augmented Reality (AR), Voice Recognition, Accessibility Tools",
            "details": [
                "Created an innovative educational assistant specifically designed for students with special needs.",
                "Improved learning retention by 40% through interactive AR and voice-controlled features.",
                "Successfully adopted by 3 local schools, enhancing inclusive education."
            ],
            "impact": "Received recognition from the Ministry of Education for its significant contribution to accessibility in education.",
            "link": "https://portfolio-5aue.vercel.app/work/learnerguide"
        },
        {
            "name": "Projects Management System",
            "tech": "Flask, Python, Firebase, Bootstrap",
            "details": [
                "Developed a robust project management system with role-based access control for diverse teams.",
                "Implemented real-time task tracking and comprehensive reporting functionalities.",
                "Automated status logs and generated insightful analytics to streamline project oversight."
            ],
            "impact": "Successfully adopted by small teams and freelancers to enhance collaboration and efficiency.",
            "link": "https://portfolio-5aue.vercel.app/work/project-management-system"
        }
    ],
    "education": [
        {
            "degree": "International Baccalaureate (IB) Diploma Program",
            "institution": "UWC Waterford",
            "period": "Accepted for Jan 2026",
            "location": "Mbabane, Eswatini",
            "details": ["Full scholarship recipient (if applicable and you want to mention it)", "Joining a globally diverse cohort focused on academic rigor and social impact"]
        },
        {
            "degree": "Participant, Gaza Summer School",
            "institution": "Horizons Academy (in partnership with Code.X)",
            "period": "Summer [2023]", # **IMPORTANT: Replace with your actual year**

            "location": "Gaza, Palestine (Online/Hybrid)",
            "details": [
                "Engaged in intensive workshops focused on [e.g., AI & Creative Programming, React Native, University Applications].", # **CUSTOMIZE**
                "Developed critical skills for [e.g., advanced programming, university admissions, leadership]." # **CUSTOMIZE**
            ]
        },
        {
            "degree": "Data Structures & Algorithms in Python",
            "institution": "Jovian",
            "period": "[May 2023]", # e.g., "May 2025" - **IMPORTANT: Fill this in**
            "details": [
                "Completed comprehensive curriculum covering fundamental data structures (e.g., arrays, linked lists, trees, graphs) and algorithms (e.g., sorting, searching, dynamic programming).",
                "Applied concepts through coding challenges and practical problem-solving exercises."
            ]
        },
        {
            "degree": "Self-Taught Engineer",
            "institution": "Project-Based Learning & Online Certifications",
            "period": "2018–Present",
            "details": [
                "Mastered AI/ML concepts and applications through the completion of 50+ diverse projects and competitive participation.",
                "Developed a strong specialization in humanitarian technology, applying engineering principles to solve critical societal challenges."
            "Engaged in intensive workshops focused on [e.g., AI & Creative Programming, React Native, University Applications].", # **CUSTOMIZE**
            "Developed critical skills for [e.g., advanced programming, university admissions, leadership]." # **CUSTOMIZE**
            ]
        },

    ],
    "achievements": [
        "Tech Talent 2022 Winner – Awarded A Scientific Trip to NASA USA.",
        "Silver Medalist – Ahasak Nimavum 2022, Sri Lanka (International Competition).",
        "Published Author – Authored 'Introduction to Computer Vision' (2024).",
        "1st Place – 7th National Exhibition Competition, Palestine.",
        "2nd Place National Level – Chess Tournament Champion."
    ],
    "research": [
        {
            "title": "Examining the Role of Islamic Moral Gradation in Contemporary Vaccination Practices",
            "status": "Published (2025)",
            "collaborators": "Northwestern University, Harvard University Researchers",
            "link": "https://www.cureus.com/articles/376159-examining-the-role-of-islamic-moral-gradation-in-contemporary-vaccination-practices#!/"
        },
        {
            "title": "Sleep Health Among Civilians in the Gaza Strip During Ongoing Armed Conflict",
            "status": "Published (SLEEP 2025 – Abstract)",
            "collaborators": "International Public Health Consortium",
            "link": "https://academic.oup.com/sleep/article/48/Supplement_1/A581/8134910"
        },
        {
            "title": "Sleep Quality Among West Bank Civilians During the Ongoing Israel–Gaza Conflict",
            "status": "Published (SLEEP 2025 – Abstract)",
            "collaborators": "International Public Health Consortium",
            "link": "https://academic.oup.com/sleep/article/48/Supplement_1/A583/8134910"
        }
    ],
    "languages": [
        {"name": "Arabic", "level": "Native"},
        {"name": "English", "level": "Professional Working Proficiency"}
    ],
    "communities": [
        {
            "name": "TA Community Group",
            "role": "Founder & Lead Mentor",
            "period": "2021-Present",
            "details": "Founded and mentored a community group, guiding 150+ aspiring programmers through workshops and collaborative projects."
        },
        {
            "name": "Qattan Programmers Club",
            "role": "Active Member",
            "period": "2018-Present"
        }
    ]
}
your_name = str(resume_data["name"]).replace(' ' , '_')

class CVGenerator(FPDF):
    def __init__(self):
        super().__init__()
        self.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
        self.add_font('DejaVu', 'B', 'DejaVuSans-Bold.ttf', uni=True)
        self.add_font('DejaVu', 'I', 'DejaVuSans-Oblique.ttf', uni=True)
    
    def header(self):
        self.set_font('DejaVu', 'B', 16)
        self.cell(0, 10, resume_data['name'], 0, 1, 'C')
        self.set_font('DejaVu', '', 12)
        self.cell(0, 6, resume_data['title'], 0, 1, 'C')
        
        # Contact line with clickable links
        contacts = [
            resume_data['contact']['email'],
            resume_data['contact']['phone'],
            f"GitHub: {resume_data['contact']['github']}",
            f"Portfolio: {resume_data['contact']['portfolio']}"
        ]
        self.set_font('DejaVu', '', 10)
        self.cell(0, 5, " | ".join(contacts), 0, 1, 'C')
        self.ln(5)
    
    def footer(self):
        self.set_y(-15)
        self.set_font('DejaVu', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')
    
    def section_title(self, title):
        self.set_font('DejaVu', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 8, title, 0, 1, 'L', 1)
        self.ln(2)
    
    def skill_bubbles(self, skills_dict):
        self.set_font('DejaVu', '', 10)
        for category, skills in skills_dict.items():
            self.set_font('DejaVu', 'B', 10)
            self.cell(40, 6, f"{category}:", 0, 0)
            self.set_font('DejaVu', '', 10)
            self.multi_cell(
                w=0,
                h=6,
                txt=", ".join(skills),
                border=0,
                new_x="LMARGIN",
                new_y="NEXT",
                align="L"
            )
            self.ln(2)
    
    def experience_item(self, exp):
        # Header
        self.set_font('DejaVu', 'B', 11)
        self.cell(0, 6, f"{exp['title']}, {exp['company']}", 0, 1)
        
        # Meta line with optional link
        self.set_font('DejaVu', 'I', 10)
        meta = f"{exp['period']} | {exp['location']}"
        if 'link' in exp:
            meta += f" | {exp['link']}"
        self.cell(0, 4, meta, 0, 1)
        
        # Bullet points
        self.set_font('DejaVu', '', 10)
        for detail in exp['details']:
            self.cell(5, 5, "•", 0, 0)
            self.multi_cell(w=self.w - 2 * self.l_margin, h=5, txt=detail)
        self.ln(3)


    def project_card(self, project):
        # Header with link
        self.set_font('DejaVu', 'B', 11)
        self.cell(0, 6, project['name'], 0, 1)
        
        # Tech stack and link
        self.set_font('DejaVu', 'I', 9)
        tech_line = f"Tech: {project['tech']} | Link: {project['link']}"
        self.cell(0, 4, tech_line, 0, 1)
        
        # Bullet points
        self.set_font('DejaVu', '', 10)
        for detail in project['details']:
            self.cell(5, 5, "•", 0, 0)
            self.multi_cell(w=self.w - 2 * self.l_margin, h=5, txt=detail)
        
        # Impact
        self.set_font('DejaVu', 'I', 9)
        self.cell(0, 4, f"Impact: {project['impact']}", 0, 1)
        self.ln(3)

def generate_pdf_cv():
    pdf = CVGenerator()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Summary
    pdf.section_title('PROFESSIONAL PROFILE')
    pdf.set_font('DejaVu', '', 10)
    pdf.multi_cell(0, 5, resume_data['summary'])
    pdf.ln(8)
    
    # Skills
    pdf.section_title('TECHNICAL SKILLS')
    pdf.skill_bubbles(resume_data['technical_skills'])
    
    # Experience
    pdf.section_title('PROFESSIONAL EXPERIENCE')
    for exp in resume_data['experience']:
        pdf.experience_item(exp)
    
    # Projects
    pdf.section_title('KEY PROJECTS (7 TOTAL)')
    for project in resume_data['projects']:
        pdf.project_card(project)
    
    # Education
    pdf.section_title('EDUCATION & CERTIFICATIONS')
    for edu in resume_data['education']:
        pdf.set_font('DejaVu', 'B', 11)
        pdf.cell(0, 6, f"{edu['degree']}, {edu['institution']}", 0, 1)
        pdf.set_font('DejaVu', 'I', 9)
        meta = edu['period']
        if 'link' in edu:
            meta += f" | {edu['link']}"
        pdf.cell(0, 4, meta, 0, 1)
        if 'details' in edu:
            pdf.set_font('DejaVu', '', 9)
            for detail in edu['details']:
                pdf.cell(5, 4, "•", 0, 0)
                pdf.multi_cell(w=pdf.w - 2 * pdf.l_margin, h=4, txt=detail)
        pdf.ln(3)
    
    # Achievements
    pdf.section_title('ACHIEVEMENTS & AWARDS (5+)')
    pdf.set_font('DejaVu', '', 10)
    for achievement in resume_data['achievements']:
        pdf.cell(5, 5, "•", 0, 0)
        available_width = pdf.w - pdf.l_margin - pdf.r_margin  # total page width minus margins
        pdf.multi_cell(available_width, 5, achievement)
    
    # Communities
    pdf.section_title('COMMUNITY LEADERSHIP')
    pdf.set_font('DejaVu', '', 10)
    for community in resume_data['communities']:
        pdf.set_font('DejaVu', 'B', 10)
        pdf.cell(0, 5, f"{community['name']} ({community['period']})", 0, 1)
        pdf.set_font('DejaVu', 'I', 9)
        pdf.cell(0, 4, f"Role: {community['role']}", 0, 1)
        if 'details' in community:
            pdf.set_font('DejaVu', '', 9)
            pdf.multi_cell(0, 4, community['details'])
        pdf.ln(2)
    
    pdf.output(f'{your_name}_CV.pdf')

def generate_html_cv():
    with open(f'{your_name}_CV.html', 'w', encoding='utf-8') as f:
        f.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Majd Abualnour - CV</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
        }
        .header {
            text-align: center;
            margin-bottom: 20px;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }
        h1 {
            color: #2c3e50;
            margin-bottom: 5px;
        }
        .title {
            color: #7f8c8d;
            font-weight: normal;
        }
        .contact {
            font-size: 0.9em;
            color: #555;
            margin-bottom: 10px;
        }
        .contact a {
            color: #3498db;
            text-decoration: none;
        }
        h2 {
            color: #3498db;
            border-bottom: 1px solid #eee;
            padding-bottom: 5px;
            margin-top: 25px;
        }
        .section {
            margin-bottom: 20px;
        }
        .job, .project, .edu, .community {
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 1px solid #f0f0f0;
        }
        .job-header, .project-header, .edu-header {
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
        }
        .job-title, .project-name, .edu-degree {
            font-weight: bold;
        }
        .job-company, .project-tech, .edu-school {
            font-style: italic;
            color: #555;
        }
        .job-period, .project-link, .edu-period {
            color: #7f8c8d;
            font-size: 0.9em;
        }
        .project-link a, .job-link a {
            color: #3498db;
            text-decoration: none;
        }
        ul {
            margin-top: 5px;
            padding-left: 20px;
        }
        li {
            margin-bottom: 3px;
        }
        .skills-container {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
        }
        .skill-category {
            flex: 1;
            min-width: 200px;
        }
        .skill-category h3 {
            margin-bottom: 5px;
            color: #2c3e50;
            font-size: 1em;
        }
        .skill-list {
            font-size: 0.9em;
        }
        .project-impact {
            font-style: italic;
            color: #27ae60;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>''' + resume_data['name'] + '''</h1>
        <div class="title">''' + resume_data['title'] + '''</div>
        <div class="contact">
            <a href="''' + resume_data['contact']['portfolio'].strip() + '''" target="_blank"> Portfolio </a> | 
            <a href="''' + resume_data['contact']['linkedin'].strip() + '''" target="_blank"> LinkedIn </a> | 
            <a href="mailto:''' + resume_data['contact']['email'].strip() + '''">''' + resume_data['contact']['email'] + '''</a> | 
            <a href="tel:''' + resume_data['contact']['phone'].strip().replace(' ', '') + '''">''' + resume_data['contact']['phone'] + '''</a> | 
            <a href="https://''' + resume_data['contact']['github'].strip() + '''" target="_blank">''' + resume_data['contact']['github'] + '''</a> 
           
        </div>
    </div>

    <div class="section">
        <h2>Professional Profile</h2>
        <p>''' + resume_data['summary'] + '''</p>
    </div>

    <div class="section">
        <h2>Technical Skills</h2>
        <div class="skills-container">
''')
        
        # Skills
        for category, skills in resume_data['technical_skills'].items():
            f.write(f'''            <div class="skill-category">
                <h3>{category}</h3>
                <div class="skill-list">{", ".join(skills)}</div>
            </div>
''')
        f.write('''        </div>
    </div>

    <div class="section">
        <h2>Professional Experience</h2>
''')
        
        # Experience
        for exp in resume_data['experience']:
            f.write(f'''        <div class="job">
            <div class="job-header">
                <div>
                    <span class="job-title">{exp['title']}</span>, 
                    <span class="job-company">{exp['company']}</span>
                </div>
                <div class="job-period">{exp['period']} | {exp['location']}</div>
            </div>
''')
            if 'link' in exp:
                f.write(f'''            <div class="job-link"><a href="{exp['link']}" target="_blank">{exp['link']}</a></div>
''')
            f.write('''            <ul>
''')
            for detail in exp['details']:
                f.write(f'                <li>{detail}</li>\n')
            f.write('''            </ul>
        </div>
''')
        
        f.write('''    <div class="section">
        <h2>Research</h2>
''')

        # Research
        for research in resume_data['research']:
            f.write(f'''        <div class="job">
            <div class="job-header">
                <div>
                    <span class="job-title">{research['title']}</span>
                </div>
                <div class="job-period">{research['status']}</div>
            </div>
            <div class="job-company">Collaborators: {research['collaborators']}</div>
''')
            if 'link' in research and research['link'] != "#":
                f.write(f'''            <div class="job-link"><a href="{research['link']}" target="_blank">{research['link']}</a></div>
''')
            f.write('''        </div>
''')


        f.write('''    </div>

    <div class="section">
        <h2>Key Projects (7 Total)</h2>
''')
        
        # Projects
        for project in resume_data['projects']:
            f.write(f'''        <div class="project">
            <div class="project-header">
                <div class="project-name">{project['name']}</div>
                <div class="project-link"><a href="{project['link']}" target="_blank">View Project</a></div>
            </div>
            <div class="project-tech">Tech: {project['tech']}</div>
            <ul>
''')
            for detail in project['details']:
                f.write(f'                <li>{detail}</li>\n')
            f.write(f'''            </ul>
            <div class="project-impact">Impact: {project['impact']}</div>
        </div>
''')
        
        f.write('''    </div>

    <div class="section">
        <h2>Education</h2>
''')
        
        # Education
        for edu in resume_data['education']:
            f.write(f'''        <div class="edu">
            <div class="edu-header">
                <div>
                    <span class="edu-degree">{edu['degree']}</span>, 
                    <span class="edu-school">{edu['institution']}</span>
                </div>
                <div class="edu-period">{edu['period']}</div>
            </div>
''')
            if 'link' in edu:
                f.write(f'''            <div><a href="{edu['link']}" target="_blank">{edu['link']}</a></div>
''')
            if 'details' in edu:
                f.write('''            <ul>
''')
                for detail in edu['details']:
                    f.write(f'                <li>{detail}</li>\n')
                f.write('''            </ul>
''')
            f.write('''        </div>
''')
        
        f.write('''    </div>

    <div class="section">
        <h2>Achievements & Awards (5+)</h2>
        <ul>
''')
        
        # Achievements
        for achievement in resume_data['achievements']:
            f.write(f'            <li>{achievement}</li>\n')
        
        f.write('''        </ul>
    </div>

    <div class="section">
        <h2>Community Leadership</h2>
''')
        
        # Communities
        for community in resume_data['communities']:
            f.write(f'''        <div class="community">
            <div><strong>{community['name']}</strong> ({community['period']})</div>
            <div><em>Role:</em> {community['role']}</div>
''')
            if 'details' in community:
                f.write(f'''            <div>{community['details']}</div>
''')
            f.write('''        </div>
''')
        
        f.write('''    </div>
</body>
</html>''')

def generate_txt_cv():
    with open(f'{your_name}_CV.txt', 'w', encoding='utf-8') as f:
        # Header
        f.write(resume_data['name'] + '\n')
        f.write('=' * len(resume_data['name']) + '\n\n')
        f.write(resume_data['title'] + '\n')
        f.write('\n'.join([f"{k}: {v}" for k, v in resume_data['contact'].items()]) + '\n\n')
        
        # Summary
        f.write('PROFESSIONAL PROFILE:\n')
        f.write(resume_data['summary'] + '\n\n')
        
        # Skills
        f.write('TECHNICAL SKILLS:\n')
        for category, skills in resume_data['technical_skills'].items():
            f.write(f'- {category}: {", ".join(skills)}\n')
        f.write('\n')
        
        # Experience
        f.write('PROFESSIONAL EXPERIENCE:\n')
        for exp in resume_data['experience']:
            f.write(f"{exp['title']}, {exp['company']}\n")
            f.write(f"{exp['period']} | {exp['location']}\n")
            if 'link' in exp:
                f.write(f"Link: {exp['link']}\n")
            for detail in exp['details']:
                f.write(f"  • {detail}\n")
            f.write('\n')

        f.write('RE:\n')
        for exp in resume_data['experience']:
            f.write(f"{exp['title']}, {exp['company']}\n")
            f.write(f"{exp['period']} | {exp['location']}\n")
            if 'link' in exp:
                f.write(f"Link: {exp['link']}\n")
            for detail in exp['details']:
                f.write(f"  • {detail}\n")
            f.write('\n')
        
        # Projects
        f.write('KEY PROJECTS (7 TOTAL):\n')
        for project in resume_data['projects']:
            f.write(f"{project['name']}\n")
            f.write(f"Tech: {project['tech']}\n")
            f.write(f"Link: {project['link']}\n")
            for detail in project['details']:
                f.write(f"  • {detail}\n")
            f.write(f"Impact: {project['impact']}\n\n")
        
        # Education
        f.write('EDUCATION:\n')
        for edu in resume_data['education']:
            f.write(f"{edu['degree']}, {edu['institution']}\n")
            f.write(f"{edu['period']}\n")
            if 'link' in edu:
                f.write(f"Link: {edu['link']}\n")
            if 'details' in edu:
                for detail in edu['details']:
                    f.write(f"  • {detail}\n")
            f.write('\n')
        
        # Achievements
        f.write('ACHIEVEMENTS & AWARDS (5+):\n')
        for achievement in resume_data['achievements']:
            f.write(f"  • {achievement}\n")
        
        # Communities
        f.write('\nCOMMUNITY LEADERSHIP:\n')
        for community in resume_data['communities']:
            f.write(f"{community['name']} ({community['period']})\n")
            f.write(f"Role: {community['role']}\n")
            if 'details' in community:
                f.write(f"  • {community['details']}\n")
            f.write('\n')

def generate_all_formats():
    print("Generating Ultimate CV in all formats...")
    generate_pdf_cv()
    generate_html_cv()
    generate_txt_cv()
    print("Successfully generated:")
    print(f"- {your_name}_CV.pdf (Professional PDF version)")
    print(f"- {your_name}_CV.html (Interactive web version)")
    print(f"- {your_name}_CV.txt (ATS-friendly text version)")
    print("\nYour CV now includes all 7 projects with live links!")

if __name__ == "__main__":
    generate_all_formats()