import streamlit as st

# ============================================================
# SKILL SPHERE AI
# Intelligent Skill Assessment & Career Guidance System
# ============================================================

st.set_page_config(
    page_title="Skill Sphere AI",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------- CSS -----------------------------

st.markdown("""
<style>

.block-container {
    max-width: 1400px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

.hero {
    padding: 2rem;
    border-radius: 20px;
    background: linear-gradient(135deg, #eef2ff, #f5f3ff);
    border: 1px solid #dbeafe;
    margin-bottom: 1.5rem;
}

.hero h1 {
    font-size: 2.8rem;
    margin-bottom: 0.3rem;
}

.hero p {
    font-size: 1.1rem;
}

div.stButton > button {
    border-radius: 10px;
    font-weight: 600;
    min-height: 2.7rem;
}

[data-testid="stMetric"] {
    border: 1px solid #e5e7eb;
    padding: 0.8rem;
    border-radius: 14px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# CAREER DATA
# ============================================================

CAREERS = {

    "Python Developer": {
        "skills": {
            "Python": 5,
            "Data Structures": 4,
            "SQL": 3,
            "Git": 2,
            "Problem Solving": 4
        },

        "roadmap": [
            "Python fundamentals",
            "Functions, OOP and modules",
            "Data Structures and Algorithms",
            "SQL and databases",
            "Git and GitHub",
            "Build 2-3 Python projects"
        ]
    },

    "Java Developer": {
        "skills": {
            "Java": 5,
            "OOP": 5,
            "Data Structures": 4,
            "SQL": 3,
            "Git": 2
        },

        "roadmap": [
            "Java fundamentals",
            "OOP and exception handling",
            "Collections framework",
            "Data Structures and Algorithms",
            "SQL and JDBC",
            "Build Java projects"
        ]
    },

    "Web Developer": {
        "skills": {
            "HTML": 3,
            "CSS": 3,
            "JavaScript": 5,
            "SQL": 2,
            "Git": 3
        },

        "roadmap": [
            "HTML and semantic web",
            "CSS and responsive design",
            "JavaScript fundamentals",
            "DOM and APIs",
            "Git and GitHub",
            "Build responsive web projects"
        ]
    },

    "Data Scientist": {
        "skills": {
            "Python": 4,
            "SQL": 4,
            "Statistics": 5,
            "Machine Learning": 5,
            "Data Visualization": 4
        },

        "roadmap": [
            "Python for data analysis",
            "Statistics and probability",
            "NumPy and Pandas",
            "Data visualization",
            "Machine Learning",
            "Build data science projects"
        ]
    },

    "AI / ML Engineer": {
        "skills": {
            "Python": 4,
            "Machine Learning": 5,
            "Data Structures": 3,
            "Statistics": 4,
            "Deep Learning": 5
        },

        "roadmap": [
            "Python programming",
            "Linear algebra and statistics",
            "Machine Learning",
            "Neural networks",
            "Deep Learning",
            "Build AI/ML projects"
        ]
    }
}


# ============================================================
# SKILLS
# ============================================================

ALL_SKILLS = sorted({
    skill
    for career in CAREERS.values()
    for skill in career["skills"]
})


# ============================================================
# QUIZ QUESTIONS
# ============================================================

QUIZ = [

    {
        "question": "Which data structure follows LIFO?",
        "options": [
            "Queue",
            "Stack",
            "Tree",
            "Graph"
        ],
        "answer": "Stack"
    },

    {
        "question": "Which language is commonly used with Streamlit?",
        "options": [
            "Python",
            "Java",
            "C",
            "HTML"
        ],
        "answer": "Python"
    },

    {
        "question": "Which SQL command is used to retrieve data?",
        "options": [
            "INSERT",
            "UPDATE",
            "SELECT",
            "DELETE"
        ],
        "answer": "SELECT"
    },

    {
        "question": "Which keyword defines a class in Java?",
        "options": [
            "object",
            "class",
            "define",
            "struct"
        ],
        "answer": "class"
    },

    {
        "question": "What does HTML mainly define?",
        "options": [
            "Web page structure",
            "Database tables",
            "Operating systems",
            "Machine learning models"
        ],
        "answer": "Web page structure"
    },

    {
        "question": "Which keyword is used to define a function in Python?",
        "options": [
            "function",
            "define",
            "def",
            "fun"
        ],
        "answer": "def"
    },

    {
        "question": "Which of the following is a database?",
        "options": [
            "MySQL",
            "Python",
            "HTML",
            "CSS"
        ],
        "answer": "MySQL"
    },

    {
        "question": "What does AI stand for?",
        "options": [
            "Automatic Internet",
            "Artificial Intelligence",
            "Advanced Information",
            "Application Interface"
        ],
        "answer": "Artificial Intelligence"
    }
]


# ============================================================
# SESSION STATE
# ============================================================

defaults = {

    "page": "Home",

    "name": "",

    "education": "B.Tech / B.E.",

    "year": "2nd Year",

    "career": "",

    "skills": {},

    "assessment_done": False,

    "quiz_score": None,

    "completed_steps": set()
}


for key, value in defaults.items():

    if key not in st.session_state:

        st.session_state[key] = value


# ============================================================
# FUNCTIONS
# ============================================================

def career_match(skill_scores):

    results = []

    for career_name, info in CAREERS.items():

        total_weight = sum(info["skills"].values())

        earned = 0

        for skill, weight in info["skills"].items():

            level = skill_scores.get(skill, 0)

            earned += min(level, 5) / 5 * weight

        percentage = round(
            (earned / total_weight) * 100
        )

        results.append(
            (career_name, percentage)
        )

    results.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return results


def level_text(score):

    if score >= 4:
        return "Advanced"

    elif score >= 3:
        return "Intermediate"

    elif score >= 1:
        return "Beginner"

    else:
        return "Not Started"


def get_overall_score(skill_scores):

    if not skill_scores:
        return 0

    return round(
        sum(skill_scores.values())
        /
        (len(skill_scores) * 5)
        * 100
    )


def get_career_roadmap(career):

    if career in CAREERS:

        return CAREERS[career]["roadmap"]

    return [
        f"Learn the fundamentals of {career}",
        f"Identify the core skills required for {career}",
        f"Practice the important tools and technologies",
        f"Complete small projects related to {career}",
        f"Build 2-3 strong projects for your portfolio",
        f"Prepare for interviews or opportunities in {career}"
    ]


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🎯 Skill Sphere AI")

    st.caption(
        "Smart Skill Assessment & Career Guidance"
    )

    if st.session_state.name:

        st.success(
            f"Welcome, {st.session_state.name}!"
        )

    st.markdown("---")

    pages = [
        "Home",
        "Student Profile",
        "Skill Assessment",
        "AI Analysis",
        "Career Roadmap",
        "AI Quiz",
        "Dashboard"
    ]

    selected_page = st.radio(
        "Navigation",
        pages,
        index=pages.index(
            st.session_state.page
        )
    )

    st.session_state.page = selected_page


# ============================================================
# HOME
# ============================================================

if st.session_state.page == "Home":

    st.subheader(
        "🚀 Welcome to Skill Sphere AI"
    )

    st.write(
        """
        Skill Sphere AI helps students understand
        their technical skills, identify skill gaps,
        find suitable career paths and follow a
        personalized learning roadmap.
        """
    )

    st.divider()

    st.subheader(
        "✨ Main Features"
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.markdown("### 👤")

        st.write(
            "**Student Profile**"
        )

        st.write(
            "Create your personal profile."
        )

    with c2:

        st.markdown("### 🧠")

        st.write(
            "**Skill Assessment**"
        )

        st.write(
            "Rate your technical skills."
        )

    with c3:

        st.markdown("### 🤖")

        st.write(
            "**AI Analysis**"
        )

        st.write(
            "Analyze strengths and skill gaps."
        )

    with c4:

        st.markdown("### 📚")

        st.write(
            "**Learning Roadmap**"
        )

        st.write(
            "Follow a career learning path."
        )

    st.divider()

    st.subheader(
        "🔄 How It Works"
    )

    st.info(
        """
        Student Profile → Skill Assessment →
        AI Analysis → Career Recommendation →
        Learning Roadmap → AI Quiz → Dashboard
        """
    )

    st.divider()

    st.subheader(
        "💡 Project Objective"
    )

    st.write(
        """
        The objective of Skill Sphere AI is to help
        students identify their strengths and weaknesses
        and understand which skills they need to improve
        for their desired career.
        """
    )


# ============================================================
# STUDENT PROFILE
# ============================================================

elif st.session_state.page == "Student Profile":

    st.title(
        "👤 Student Profile"
    )

    st.write(
        "Enter your details."
    )

    with st.form("profile_form"):

        name = st.text_input(
            "Full Name",
            value=st.session_state.name
        )

        education_options = [
            "B.Tech / B.E.",
            "B.Sc",
            "BCA",
            "MCA",
            "M.Tech",
            "Other"
        ]

        education = st.selectbox(
            "Education",
            education_options,
            index=education_options.index(
                st.session_state.education
            )
        )

        year_options = [
            "1st Year",
            "2nd Year",
            "3rd Year",
            "4th Year",
            "Graduate"
        ]

        year = st.selectbox(
            "Current Year",
            year_options,
            index=year_options.index(
                st.session_state.year
            )
        )

        career = st.text_input(
            "Target Career",
            value=st.session_state.career,
            placeholder="Enter your desired career"
        )

        submitted = st.form_submit_button(
            "💾 Save Profile",
            use_container_width=True
        )

    if submitted:

        if not name.strip():

            st.error(
                "Please enter your name."
            )

        elif not career.strip():

            st.error(
                "Please enter your target career."
            )

        else:

            old_career = st.session_state.career

            st.session_state.name = name.strip()

            st.session_state.education = education

            st.session_state.year = year

            st.session_state.career = career.strip()

            if old_career != st.session_state.career:

                st.session_state.completed_steps = set()

            st.success(
                "Profile saved successfully! 🎉"
            )

    if st.session_state.name:

        st.divider()

        st.subheader(
            "📋 Current Profile"
        )

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Name",
            st.session_state.name
        )

        c2.metric(
            "Education",
            st.session_state.education
        )

        c3.metric(
            "Year",
            st.session_state.year
        )

        c4.metric(
            "Career",
            st.session_state.career
        )


# ============================================================
# SKILL ASSESSMENT
# ============================================================

elif st.session_state.page == "Skill Assessment":

    st.title(
        "🧠 Skill Assessment"
    )

    st.write(
        """
        Rate your current skill level from
        **0 = No Knowledge** to
        **5 = Advanced**.
        """
    )

    current_scores = {}

    with st.form("skill_form"):

        st.subheader(
            "Rate Your Technical Skills"
        )

        cols = st.columns(2)

        for index, skill in enumerate(ALL_SKILLS):

            old_value = st.session_state.skills.get(
                skill,
                0
            )

            with cols[index % 2]:

                current_scores[skill] = st.slider(
                    skill,
                    0,
                    5,
                    int(old_value)
                )

        submitted = st.form_submit_button(
            "🔍 Analyze My Skills",
            use_container_width=True
        )

    if submitted:

        st.session_state.skills = current_scores

        st.session_state.assessment_done = True

        st.success(
            "Skill assessment completed! 🎉"
        )

        st.info(
            "Open **AI Analysis** from the sidebar."
        )


# ============================================================
# AI ANALYSIS
# ============================================================

elif st.session_state.page == "AI Analysis":

    st.title(
        "🤖 AI Skill Analysis"
    )

    if not st.session_state.assessment_done:

        st.warning(
            "Please complete the Skill Assessment first."
        )

    elif not st.session_state.career:

        st.warning(
            "Please enter your target career in Student Profile first."
        )

    else:

        scores = st.session_state.skills

        overall = get_overall_score(
            scores
        )

        matches = career_match(
            scores
        )

        selected_career = st.session_state.career

        st.subheader(
            "📊 Overall Performance"
        )

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Overall Skill Score",
            f"{overall}%"
        )

        c2.metric(
            "Target Career",
            selected_career
        )

        c3.metric(
            "Best Career Match",
            f"{matches[0][0]} - {matches[0][1]}%"
        )

        st.progress(
            overall / 100
        )

        st.divider()

        st.subheader(
            "💪 Your Strengths"
        )

        strengths = sorted(
            [
                (skill, score)
                for skill, score in scores.items()
                if score >= 4
            ],
            key=lambda x: x[1],
            reverse=True
        )

        if strengths:

            for skill, score in strengths:

                st.success(
                    f"✅ {skill} — {score}/5"
                )

        else:

            st.info(
                "Keep practicing to build strong skills."
            )

        st.subheader(
            "🎯 Skill Gaps"
        )

        if selected_career in CAREERS:

            required = CAREERS[
                selected_career
            ]["skills"]

            gaps = []

            for skill, required_level in required.items():

                current = scores.get(
                    skill,
                    0
                )

                if current < required_level:

                    gaps.append(
                        (
                            skill,
                            current,
                            required_level
                        )
                    )

            if gaps:

                for skill, current, needed in gaps:

                    st.warning(
                        f"📌 {skill} | "
                        f"Current: {current}/5 | "
                        f"Recommended: {needed}/5"
                    )

            else:

                st.success(
                    "🎉 You meet the recommended levels!"
                )

        else:

            st.info(
                f"Your target career is **{selected_career}**. "
                "Use the Career Roadmap to build the skills needed for this career."
            )

        st.divider()

        st.subheader(
            "🏆 Career Match Ranking"
        )

        for rank, (
            career_name,
            percentage
        ) in enumerate(matches, 1):

            st.write(
                f"**{rank}. {career_name} — {percentage}%**"
            )

            st.progress(
                percentage / 100
            )


# ============================================================
# CAREER ROADMAP
# ============================================================

elif st.session_state.page == "Career Roadmap":

    st.title(
        "📚 Personalized Career Roadmap"
    )

    career = st.session_state.career

    if not career:

        st.warning(
            "Please enter your target career in Student Profile first."
        )

    else:

        roadmap = get_career_roadmap(
            career
        )

        st.subheader(
            f"🎯 Career: {career}"
        )

        st.write(
            "Complete each step to build your career."
        )

        completed = (
            st.session_state.completed_steps
        )

        for i, step in enumerate(
            roadmap,
            1
        ):

            checked = st.checkbox(
                f"Step {i}: {step}",
                value=(i in completed),
                key=f"roadmap_{career}_{i}"
            )

            if checked:

                completed.add(i)

            else:

                completed.discard(i)

        progress = (
            len(completed)
            /
            len(roadmap)
        )

        st.divider()

        st.subheader(
            "📈 Roadmap Progress"
        )

        st.progress(
            progress
        )

        st.write(
            f"**{round(progress * 100)}% completed**"
        )

        if progress == 1:

            st.balloons()

            st.success(
                "🏆 Congratulations! You completed your roadmap."
            )


# ============================================================
# AI QUIZ
# ============================================================

elif st.session_state.page == "AI Quiz":

    st.title(
        "📝 Skill Sphere AI Quiz"
    )

    st.write(
        "Answer all questions and submit the quiz."
    )

    with st.form("quiz_form"):

        answers = {}

        for i, question in enumerate(
            QUIZ,
            1
        ):

            answers[i] = st.radio(
                f"**{i}. {question['question']}**",
                question["options"],
                index=None,
                key=f"quiz_{i}"
            )

        submitted = st.form_submit_button(
            "🚀 Submit Quiz",
            use_container_width=True
        )

    if submitted:

        unanswered = [
            i
            for i in range(1, len(QUIZ) + 1)
            if answers[i] is None
        ]

        if unanswered:

            st.warning(
                "Please answer all quiz questions before submitting."
            )

        else:

            score = 0

            for i, question in enumerate(
                QUIZ,
                1
            ):

                if answers[i] == question["answer"]:

                    score += 1

            st.session_state.quiz_score = score

            percentage = round(
                score / len(QUIZ) * 100
            )

            st.divider()

            st.subheader(
                "📊 Quiz Result"
            )

            c1, c2 = st.columns(2)

            c1.metric(
                "Correct Answers",
                f"{score}/{len(QUIZ)}"
            )

            c2.metric(
                "Quiz Score",
                f"{percentage}%"
            )

            st.progress(
                percentage / 100
            )

            if percentage == 100:

                st.balloons()

                st.success(
                    "🏆 Perfect Score!"
                )

            elif percentage >= 80:

                st.success(
                    "👏 Excellent performance!"
                )

            elif percentage >= 60:

                st.info(
                    "👍 Good job! Keep practicing."
                )

            else:

                st.warning(
                    "📚 Keep learning and try again."
                )

            st.divider()

            st.subheader(
                "🔍 Answer Review"
            )

            for i, question in enumerate(
                QUIZ,
                1
            ):

                user_answer = answers[i]

                correct_answer = (
                    question["answer"]
                )

                st.markdown(
                    f"### Question {i}"
                )

                st.write(
                    question["question"]
                )

                if user_answer == correct_answer:

                    st.success(
                        f"✅ Correct! Your answer: **{user_answer}**"
                    )

                else:

                    st.error(
                        f"❌ Wrong answer: **{user_answer}**"
                    )

                    st.success(
                        f"✅ Correct answer: **{correct_answer}**"
                    )

                st.markdown("---")

            st.subheader(
                "🎯 Final Feedback"
            )

            if percentage == 100:

                st.success(
                    "🌟 Excellent! You answered every question correctly."
                )

            elif percentage >= 80:

                st.success(
                    "👏 Excellent performance. Review the few mistakes."
                )

            elif percentage >= 60:

                st.info(
                    "👍 Good performance. Review your wrong answers."
                )

            else:

                st.warning(
                    "📚 Review the correct answers and try the quiz again."
                )


# ============================================================
# DASHBOARD
# ============================================================

elif st.session_state.page == "Dashboard":

    st.title(
        "📊 Student Dashboard"
    )

    if not st.session_state.name:

        st.warning(
            "Please create your Student Profile first."
        )

    elif not st.session_state.career:

        st.warning(
            "Please enter your target career in Student Profile first."
        )

    else:

        overall = get_overall_score(
            st.session_state.skills
        )

        career = st.session_state.career

        roadmap = get_career_roadmap(
            career
        )

        roadmap_progress = (
            len(
                st.session_state.completed_steps
            )
            /
            len(roadmap)
        )

        if st.session_state.skills:

            best_match = career_match(
                st.session_state.skills
            )[0]

        else:

            best_match = (
                "Not assessed",
                0
            )

        if st.session_state.quiz_score is not None:

            quiz_percentage = round(
                st.session_state.quiz_score
                /
                len(QUIZ)
                *
                100
            )

        else:

            quiz_percentage = 0

        st.subheader(
            f"Welcome back, {st.session_state.name}! 👋"
        )

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Skill Score",
            f"{overall}%"
        )

        c2.metric(
            "Target Career",
            career
        )

        c3.metric(
            "Best Match",
            f"{best_match[1]}%"
        )

        c4.metric(
            "Quiz Score",
            (
                f"{quiz_percentage}%"
                if st.session_state.quiz_score is not None
                else "Not Attempted"
            )
        )

        st.divider()

        st.subheader(
            "📚 Learning Progress"
        )

        st.progress(
            roadmap_progress
        )

        st.write(
            f"{round(roadmap_progress * 100)}% "
            "of your roadmap completed."
        )

        st.divider()

        st.subheader(
            "🧠 Skill Overview"
        )

        if st.session_state.skills:

            for skill, score in sorted(
                st.session_state.skills.items(),
                key=lambda x: x[1],
                reverse=True
            ):

                st.write(
                    f"**{skill}** — {score}/5 "
                    f"({level_text(score)})"
                )

                st.progress(
                    score / 5
                )

        else:

            st.info(
                "Complete the Skill Assessment first."
            )

        st.divider()

        st.subheader(
            "🎯 Next Actions"
        )

        if not st.session_state.assessment_done:

            st.write(
                "1. 🧠 Complete the Skill Assessment"
            )

        else:

            st.write(
                "1. ✅ Skill Assessment completed"
            )

        st.write(
            "2. 🤖 Review your AI Analysis"
        )

        st.write(
            "3. 📚 Follow your Career Roadmap"
        )

        st.write(
            "4. 📝 Complete the AI Quiz"
        )

        st.write(
            "5. 🏆 Improve your skills and progress"
        )