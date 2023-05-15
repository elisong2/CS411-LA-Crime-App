""" Specifies routing for the application"""
from flask import render_template, request, jsonify
from app import app
from app import database as db_helper
import pandas as pd

@app.route("/delete/<int:case_id>", methods=['POST'])
def delete(case_id):
    """ recieved post requests for entry delete """
    print("went in delete")
    try:
        print("went in try")
        db_helper.delete_Event(case_id)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/edit/<int:task_id>", methods=['POST'])
def update(task_id):
    """ recieved post requests for entry updates """
    data = request.get_json()

    try:
        if "description" in data:
            db_helper.update_Event(data["description"])
            result = {'success': True, 'response': 'Task Updated'}
        else:
            result = {'success': True, 'response': 'Nothing Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/create", methods=['POST'])
def create():
    """ recieves post requests to add new task """
    data = request.get_json()
    db_helper.insert_Event(data['description'])
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)

search_output = pd.DataFrame({'A' : []})
@app.route("/search", methods=['POST','GET'])
def search():
    """ recieves post requests to add new task """
    print("in route")
    data = request.get_json()
    print(data)
    #print(data['description'][0], data['description'][1])
    global search_output
    search_output = db_helper.search_Table(data['description'][0], data['description'][1])
    print(search_output)
    result = {'success': True, 'response': 'Done'}
    return render_template("search.html", items = search_output)

@app.route("/search2", methods=['POST','GET'])
def search2():
    print('final search output')
    print(search_output)
    #lobal search_output
    return render_template("search.html", items = search_output)

@app.route("/advanced1", methods=['POST','GET'])
def advanced1():
    """ recieves post requests to add new task """
    data = request.get_json()
    output = db_helper.top_weapons()
    print(output)
    result = {'success': True, 'response': 'Done'}
    print("-----------")
    #return jsonify(result)
    #return redirect("advanced1.html", messages = output)
    print("render_template running")
    return render_template("advanced1.html", items = output)
    #return jsonify(result)

    #return render_template("advanced1.html", items = output)

@app.route("/userinsert", methods=['POST','GET'])
def userInsert():
    """ recieves post requests to add new task """
    data = request.get_json()
    output = db_helper.user_insert()
    result = {'success': True, 'response': 'Done'}
    print("-----------")
    #return jsonify(result)
    #return redirect("advanced1.html", messages = output)
    print("render_template running")
    return render_template("userInserted.html", items = output)


@app.route("/agebreakdown", methods=['POST','GET'])
def agebreakdown():
    """ recieves post requests to add new task """
    data = request.get_json()
    output = db_helper.categorize_ages()
    result = {'success': True, 'response': 'Done'}
    print("-----------")
    #return jsonify(result)
    #return redirect("advanced1.html", messages = output)
    print("render_template running")
    return render_template("ageBreakdown.html", items = output)

@app.route("/weaponbreakdown", methods=['POST','GET'])
def weaponbreakdown():
    """ recieves post requests to add new task """
    data = request.get_json()
    output = db_helper.categorize_weapons()
    result = {'success': True, 'response': 'Done'}
    print("-----------")
    #return jsonify(result)
    #return redirect("advanced1.html", messages = output)
    print("render_template running")
    return render_template("weaponsBreakdown.html", items = output)

@app.route("/advanced2", methods=['POST','GET'])
def advanced2():
    """ recieves post requests to add new task """
    data = request.get_json()
    output = db_helper.top_victim_ages()
    result = {'success': True, 'response': 'Done'}
    #return jsonify(result)
    return render_template("advanced2.html", items = output)


@app.route("/")
def homepage():
    """ returns rendered homepage """
    items = db_helper.fetch_Crime_Status().head(25)
    items['Date_of_Occurrence'] = items['Date_of_Occurrence'].apply(lambda x : x.split()[0])
    items['Location'] = items['Location'].apply(lambda x : x.replace(" ",""))


    formatTime = lambda x : "00:"+str(x) \
if len(str(x)) == 2 else ("0"+str(x)[0]+":" + str(x)[1:3] if len(str(x)) == 3 \
               else str(x)[0:2] + ":" + str(x)[2:4])
    items['Time_of_Occurrence'] = items['Time_of_Occurrence'].apply(formatTime)
    return render_template("index.html", items = items)