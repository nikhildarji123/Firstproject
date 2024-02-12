from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        name = request.form['MyName']
        lastname = request.form['MyLast']
        gender = request.form['myGender']
        email = request.form['MyEmail']
        date = request.form['MyDate']
        stud_grno = request.form['MyNumber']
        courses = request.form['myCourse']
        cgpa = request.form['Mycgpa']
        eligible = 'MyEligible' in request.form  # Check if checkbox is checked

        # Create a DataFrame with form data
        data = {
            'Name': [name],
            'LastName': [lastname],
            'Gender': [gender],
            'Email': [email],
            'Date': [date],
            'Stud_GRNO': [stud_grno],
            'Courses': [courses],
            'CGPA': [cgpa],
            'Eligible': [eligible]
        }
        df = pd.DataFrame(data)

        # Append data to Excel file
        with pd.ExcelWriter('form_data.xlsx', mode='a', engine='openpyxl') as writer:
            df.to_excel(writer, index=False, header=not writer.sheets['Sheet1'])

        return 'Form submitted successfully'

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

