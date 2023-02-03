from flask import Flask, render_template, request
import check
import gongtong

app = Flask(__name__)

@app.route('/')
def formpage():
    return render_template('Form.html')

@app.route('/Data',methods=['post'])
def view():
    id = request.form['id']
    id2 = request.form['id2'] 
    todo = request.form['todo']
    if todo == 'View':
        subject_name, subject_list_final = check.check(id)
        return render_template('Data.html', subject_name=subject_name, subject_list_final=subject_list_final)
    if todo == 'Same':
        if id2 == '':
            return render_template('Form.html')
        result = gongtong.gongtong(id, id2)
        return render_template('Same.html', result=result)

if __name__ == "__main__":
    app.run()