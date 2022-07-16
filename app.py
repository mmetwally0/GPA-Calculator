
from flask import Flask, redirect, render_template, session, request

# Configure Application
app = Flask(__name__)

# Defining a function to get credit values


def get_gpa(mark, ch):
    """Calculates the GPA, takes in two arguments, The mark, and the subject"""
    if mark >= 93:
        gpa = 4.0 * ch
    elif mark >= 89:
        gpa = 3.7 * ch
    elif mark >= 84:
        gpa = 3.3 * ch
    elif mark >= 80:
        gpa = 3.0 * ch
    elif mark >= 76:
        gpa = 2.7 * ch
    elif mark >= 73:
        gpa = 2.3 * ch
    elif mark >= 70:
        gpa = 2.0 * ch
    elif mark >= 67:
        gpa = 1.7 * ch
    elif mark >= 64:
        gpa = 1.3 * ch
    else:
        gpa = 1.0 * ch
    return gpa


# Dictionaries containing the subjects and their credit hours
first = [
    {'Anatomy 1': 3},
    {'Physiology 1': 3},
    {'Histology 1': 3},
    {'Biophysics': 4},
    {'Ethics': 2},
    {'English': 2},
    {'Psychology': 2},
    {'Human rights': 2},
]

second = [
    {'Anatomy 2': 3},
    {'Physiology 2': 3},
    {'Histology 2': 2},
    {'Pathology': 3},
    {'Molecular biology': 1},
    {'IT': 2},
    {'Research ethics': 2},
    {'Kinesiology': 2},
    {'Biochemistry 1': 3},

]

third = [
    {'Neuroanatomy': 3},
    {'Physiology 3': 3},
    {'Biochemistry 2': 3},
    {'Muscle Test 1': 3},
    {'Hydrotherapy': 2},
    {'Biomechanics 1': 3},
    {'Electrotherapy 1': 3},
    {'Public Health': 1},
]

forth = [
    {'Anatomy 3': 3},
    {'Physiology 4': 2},
    {'Exercise Physiology': 2},
    {'Muscle test 2': 3},
    {'Electrotherapy 2': 3},
    {'Therapeutic Exercise 1': 3},
    {'Manual Therapy': 2},
    {'Biomechanics 2': 3},
]

# list of all the semesters
semesters = ["placeholder", first, second, third, forth]


@app.route('/', methods=["POST", "GET"])
def index():
    # If request method is GET
    if request.method == 'GET':
        return render_template("index.html")

    # If request method is Post
    else:
        try:
            semester = request.form.get("semesters")
            return render_template("subjects.html", subjects=semesters[int(semester)], sem_num=int(semester))
        except:
            return render_template("index.html")


@app.route('/subjects', methods=["POST"])
def subjects():
    try:
        semester = int(request.form.get("sem_num"))
        total_score = 0
        total_hours = 0 
        for subject in semesters[semester]:
            for name, credit in subject.items():
                grade = int(request.form.get(name))
                score = get_gpa(grade, credit)
                total_score += score
                total_hours += credit
        gpa = round((total_score/total_hours), 2)
        return render_template("score.html", gpa=gpa)
    except:
        return render_template("index.html")


@app.route('/score')
def score():
    return render_template("score.html")


if __name__ == "__main__":
    app.run(debug=True)
