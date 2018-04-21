from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('index.html', msg = "")

@app.route('/', methods = ['POST', 'GET'])
def plagiarism():
    m = check(request.form['text'])
    return render_template('index.html', msg = m)

def check(str1):
    file_data = open("data.txt").read()
    unwanted_chars = ".,;:?!"
    for char in unwanted_chars:
        file_data = file_data.replace(char, "")
        str1 = str1.replace(char, "")
        
    data = file_data.lower().split()
    s = str1.lower().split()
    
    print "Copied keywords:"
    count = 0
    for i in s:
        if i in data:
            count += 1
            print str(count) + ") " + i
            
    per = float(count) / len(s) * 100
    msg = "Plagiarism score = " + str(per) + "%"
    print msg
    return msg

if(__name__ == "__main__"):
    app.run()