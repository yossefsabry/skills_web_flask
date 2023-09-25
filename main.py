from flask import Flask,render_template

skills_app = Flask(__name__)


# start skills page
my_skills = [("css", 70), ("html", 65), ("javascript", 90), ("python", 80), ("sql", 70)]


@skills_app.route('/')
def skillspage():
    return render_template( "skills.html" ,heading ="Welcome In My Skills || Yossef", 
                            description = "all my skills and the progress for each skill", 
                            customcss = 'skills',
                            title="skills",
                            skills = my_skills)



if __name__ == "__main__": 
    skills_app.run(debug=True, port=60)