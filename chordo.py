from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy 
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/calculate", methods = ['GET','POST'])
def calculate():
    values_C = ["C", "Dm", "Em", "F", "G", "Am", "Bb"]
    values_D = ["D", "Em", "F#m", "G", "A", "Bm", "C"]
    values_E = ["E", "F#m", "G#m", "A", "B", "C#m", "D"]
    values_F = ["F", "Gm", "Am", "Bb", "C", "Dm", "Eb"]
    values_G = ["G", "Am", "Bm", "C", "D", "Em", "F"]
    values_A = ["A", "Bm", "C#m", "D", "E", "F#m", "G"]
    values_B = ["B", "C#m", "D#m", "E", "F#", "G#m", "A"]
    selection = request.form.get('keysig')
    numselection = request.form.get('numchords')
    numselection1 = int(numselection)
    numselection2 = str(numselection1)
    final_list = []
    #if request.method=='POST':
    if selection == "C Major":
        for i in range(0,numselection1):
            num = random.randrange(numselection1)
            chord = values_C.pop(num)
            numselection1 = numselection1 -1
            final_list.append(chord)
            finale = str(final_list)
            print(f"{finale}")
            ffinale = print("Here are your chords: ", finale)
        return final_list 
    elif selection == "D Major":
        for i in range(0,numselection1):
            num = random.randrange(numselection1)
            chord = values_D.pop(num)
            numselection1 = numselection1 -1
            final_list.append(chord)
            finale = str(final_list)
            print(f"{finale}")
            ffinale = print("Here are your chords: ", finale)
        return final_list
    elif selection == "E Major":
        for i in range(0,numselection1):
            num = random.randrange(numselection1)
            chord = values_E.pop(num)
            numselection1 = numselection1 -1
            final_list.append(chord)
            finale = str(final_list)
            print(f"{finale}")
            ffinale = print("Here are your chords: ", finale)
        return final_list
    elif selection == "F Major":
        for i in range(0,numselection1):
            num = random.randrange(numselection1)
            chord = values_F.pop(num)
            numselection1 = numselection1 -1
            final_list.append(chord)
            finale = str(final_list)
            print(f"{finale}")
            ffinale = print("Here are your chords: ", finale)
        return final_list
    elif selection == "G Major":
        for i in range(0,numselection1):
            num = random.randrange(numselection1)
            chord = values_G.pop(num)
            numselection1 = numselection1 -1
            final_list.append(chord)
            finale = str(final_list)
            print(f"{finale}")
            ffinale = print("Here are your chords: ", finale)
        return final_list
    elif selection == "A Major":
        for i in range(0,numselection1):
            num = random.randrange(numselection1)
            chord = values_A.pop(num)
            numselection1 = numselection1 -1
            final_list.append(chord)
            finale = str(final_list)
            print(f"{finale}")
            ffinale = print("Here are your chords: ", finale)
        return final_list
    elif selection == "B Major":
        for i in range(0,numselection1):
            num = random.randrange(numselection1)
            chord = values_B.pop(num)
            numselection1 = numselection1 -1
            final_list.append(chord)
            finale = str(final_list)
            print(f"{finale}")
            ffinale = print("Here are your chords: ", finale)
        return final_list
           
    else:
        pass        

if __name__ == "__main__":
    app.run(debug=True)
