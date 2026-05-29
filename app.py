from flask import Flask, request, render_template

app=Flask(__name__)
def grade_assignment(marks):
        marks=float(marks)
        if marks>=90:
            return 'S'
        elif marks>=80:
            return 'A'
        elif marks>=70:
            return 'B'
        elif marks>=60:
            return 'C'
        elif marks>=50:
            return 'D'
        elif marks>=40:
            return 'E'
        else:
            return 'F'
def final_verdict(Percentage):
    if Percentage>=35:
        return "PASS"
    else:
        return 'FAIL'
            
@app.route("/",methods=["GET","POST"])
def calculate():
    result=None
    if request.method=='POST':
        name=request.form.get("name")

        first_lang=int(request.form.get("1st_language"))
        second_lang=int(request.form.get("2nd_language"))
        maths=int(request.form.get("maths"))
        science=int(request.form.get("science"))
        social=int(request.form.get("social"))

        total=first_lang+second_lang+maths+science+social
        Percentage=(total/500)*100

        import pandas as pd

        df = pd.DataFrame({
            "Name": [name],
            "Class": [request.form.get("class")],
            "Roll Number": [request.form.get("rollnumber")],

            "1st Language": [first_lang],
            "2nd Language": [second_lang],
            "Maths": [maths],
            "Science": [science],
           "Social": [social],

           "Total": [total],
           "Percentage": [round(Percentage, 2)],
           "Grade": [grade_assignment(Percentage)],
           "Status": [final_verdict(Percentage)]
})
        student_class = request.form.get("class")

        filename = f"{student_class}.csv"

        df.to_csv(filename, mode="a", index=False, header=False)

        result={
            "name":name,
            "class":request.form.get("class"),
            "rollnumber":request.form.get("rollnumber"),
            "first_lang_grade":grade_assignment(first_lang),
            "second_lang_grade":grade_assignment(second_lang), 
            "maths_grade":grade_assignment(maths), 
            "science_grade":grade_assignment(science), 
            "social_grade":grade_assignment(social),
            "Total":total,
            "percentage":Percentage,
            "Grade":grade_assignment(Percentage),
            "Status":final_verdict(Percentage)
        }

        return render_template("main.html",result=result)

    return render_template("main.html")

    
if __name__ == "__main__":
    app.run(debug=True)