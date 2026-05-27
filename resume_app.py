import streamlit as st

st.title("📄 Resume Analyzer")

resume_text = st.text_area("Paste your resume or skill here")

skills = [
    "python", "sql", "machine learning", "excel", "data analysis", "power bi", "c", "c++", "communication",
    "DSA",
    "DBMS",
    "OOP",
    "problem solving",
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "backend development",
    "APIs",
    "Java",
    "Kotlin",
    "Flutter",
    "Android Studio",
    "UI design",
    "mathematics",
    "deep learning",
    "networking",
    "ethical hacking",
    "Linux",
    "security tools",
    "AWS",
    "Azure",
    "cloud services",
    "database management",
    "backup and recovery",
    "troubleshooting",
    "operating systems",
    "Windows administration",
    "server management",
    "routing",
    "switching",
    "network protocols",
    "network security",
    "manual testing",
    "automation testing",
    "debugging",
    "microcontrollers",
    "Embedded C",
    "circuit design",
    "digital electronics",
    "Verilog",
    "VHDL",
    "semiconductor concepts",
    "sensors",
    "Arduino",
    "Raspberry Pi",
    "programming",
    "PCB tools",
    "circuit analysis",
    "electronics basics",
    "power systems",
    "AutoCAD Electrical",
    "electrical machines",
    "safety standards",
    "PLC",
    "SCADA",
    "automation",
    "instrumentation",
    "CAD software",
    "machine design",
    "creativity",
    "manufacturing processes",
    "quality control",
    "planning",
    "inspection",
    "testing methods",
    "quality standards",
    "automobile systems",
    "engine basics",
    "diagnostics",
    "thermodynamics",
    "refrigeration",
    "system design",
    "construction management",
    "surveying",
    "AutoCAD",
    "structural analysis",
    "design software",
    "project management",
    "estimation",
    "leadership",
    "cost estimation",
    "BOQ preparation",
    "budgeting",
    "process calculations",
    "plant operations",
    "analysis",
    "industrial safety",
    "hazard analysis",
    "regulations",
    "maintenance",
    "production systems",
    "research methodology",
    "documentation",
    "biotechnology",
    "laboratory skills",
    "process control",
    "analytical skills",
    "CI/CD",
    "Docker",
    "Kubernetes",
    "cloud computing",
    "Unity",
    "Unreal Engine",
    "game physics",
    "robotics",
    "drafting",
    "design principles",
    "solar systems",
    "wind systems",
    "energy management",
    "subject knowledge",
    "teaching",
    "aptitude",
    "reasoning",
    "technical knowledge",
    "current affairs"
]

roles = {
    "Data Analyst": ["python", "sql", "excel", "power bi"],
    "ML Engineer": ["python", "machine learning"],
    "Data Scientist": ["python", "machine learning", "data analysis"],
    "Software Developer": ["programming", "DSA", "DBMS", "OOP", "problem solving"],
    "Web Developer": ["HTML", "CSS", "JavaScript", "React", "backend development", "APIs"],
    "App Developer": ["Java", "Kotlin", "Flutter", "Android Studio", "UI design"],
    "AI/ML Engineer": ["Python", "machine learning", "mathematics", "deep learning"],
    "Cybersecurity Analyst": ["networking", "ethical hacking", "Linux", "security tools"],
    "Cloud Engineer": ["AWS", "Azure", "Linux", "networking", "cloud services"],
    "Database Administrator": ["SQL", "database management", "backup and recovery"],
    "IT Support Engineer": ["troubleshooting", "operating systems", "networking"],
    "System Administrator": ["Linux", "Windows administration", "server management"],
    "Network Engineer": ["routing", "switching", "network protocols", "network security"],
    "Software Tester": ["manual testing", "automation testing", "debugging"],
    "Embedded Systems Engineer": ["microcontrollers", "Embedded C", "circuit design"],
    "VLSI Engineer": ["digital electronics", "Verilog", "VHDL", "semiconductor concepts"],
    "IoT Developer": ["sensors", "Arduino", "Raspberry Pi", "networking", "programming"],
    "PCB Design Engineer": ["PCB tools", "circuit analysis", "electronics basics"],
    "Electrical Design Engineer": ["power systems", "AutoCAD Electrical", "circuit analysis"],
    "Maintenance Engineer": ["electrical machines", "troubleshooting", "safety standards"],
    "Control Systems Engineer": ["PLC", "SCADA", "automation", "instrumentation"],
    "Design Engineer": ["CAD software", "machine design", "creativity"],
    "Production Engineer": ["manufacturing processes", "quality control", "planning"],
    "Quality Engineer": ["inspection", "testing methods", "quality standards"],
    "Automobile Engineer": ["automobile systems", "engine basics", "diagnostics"],
    "HVAC Engineer": ["thermodynamics", "refrigeration", "system design"],
    "Site Engineer": ["construction management", "surveying", "AutoCAD"],
    "Structural Engineer": ["structural analysis", "design software", "mathematics"],
    "Construction Manager": ["project management", "estimation", "leadership"],
    "Quantity Surveyor": ["cost estimation", "BOQ preparation", "budgeting"],
    "Process Engineer": ["process calculations", "plant operations", "analysis"],
    "Safety Engineer": ["industrial safety", "hazard analysis", "regulations"],
    "Plant Engineer": ["maintenance", "production systems", "troubleshooting"],
    "Research Associate": ["research methodology", "data analysis", "documentation"],
    "Bioprocess Engineer": ["biotechnology", "laboratory skills", "process control"],
    "Quality Control Analyst": ["testing", "documentation", "analytical skills"],
    "DevOps Engineer": ["CI/CD", "Docker", "Kubernetes", "cloud computing"],
    "Game Developer": ["Unity", "Unreal Engine", "C++", "game physics"],
    "Robotics Engineer": ["robotics", "automation", "programming", "sensors"],
    "CAD Engineer": ["AutoCAD", "SolidWorks", "drafting", "design principles"],
    "Renewable Energy Engineer": ["solar systems", "wind systems", "energy management"],
    "Professor/Lecturer": ["subject knowledge", "teaching", "communication"],
    "Government Officer": ["aptitude", "reasoning", "technical knowledge", "current affairs"]
}

if st.button("Analyze Resume"):

    if not resume_text:
        st.warning("Please paste your resume")
    else:
        resume_text = resume_text.lower()

        found_skills = []

        for skill in skills:
            if skill in resume_text:
                found_skills.append(skill)

        best_role = None
        best_score = 0

        for role, role_skills in roles.items():
            match_count = 0

            for skill in role_skills:
                if skill in found_skills:
                    match_count += 1

            score = match_count / len(role_skills)

            if score > best_score:
                best_score = score
                best_role = role

        if best_role is None:
            st.error("No matching role found")
        else:
            missing_skills = []

            for skill in roles[best_role]:
                if skill not in found_skills:
                    missing_skills.append(skill)

            st.subheader("Result")
            st.write("Skills Found:", found_skills)
            st.write("Best Role:", best_role)
            st.write("Match %:", round(best_score * 100, 2))
            st.write("Missing Skills:", missing_skills)