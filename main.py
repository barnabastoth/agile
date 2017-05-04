from flask import Flask, render_template, request
import csv


app = Flask(__name__)


@app.route('/create')
def create():
    return render_template('create.html')


@app.route("/create", methods=['POST'])
def create_save():
    title = request.form['title']
    story = request.form['story']
    criteria = request.form['criteria']
    business = request.form['business']
    estimation = request.form['estimation']
    progress = request.form['progress']
    with open('database.csv') as data:
        data_list = data.read().splitlines()
        next_id = str(len(data_list))

    with open('database.csv', 'a') as file:
        file.write(str(next_id + ','))
        file.write(str(title + ','))
        file.write(str(story + ','))
        file.write(str(criteria + ','))
        file.write(str(business + ','))
        file.write(str(estimation + ','))
        file.write(str(progress + "\n"))
    return render_template('create.html', name="Thank you, your story has been saved")


@app.route("/update/<int:id>", methods=["GET"])
def update_show(id):
    with open('database.csv') as data:
        data_list = data.read().splitlines()
        data_list = [item.split(',') for item in data_list]
        selected_story = []
        for item in data_list:
            if int(item[0]) == int(id):
                selected_story = item
        selected_story.append(id)
        selected_story.append("Thank you, your changes has been saved!")
        # 0-6 items, 7 id, 8 thanks txt
        return render_template('update.html', sel_list=selected_story)


@app.route("/update/<int:id>", methods=['POST'])
def update_save(id):
    title = request.form['title']
    story = request.form['story']
    criteria = request.form['criteria']
    business = request.form['business']
    estimation = request.form['estimation']
    progress = request.form['progress']
    new_list = [str(id), str(title), str(story), str(criteria), str(business), str(estimation), str(progress)]
    final_list = []
    with open('database.csv') as data:
        data_list = data.read().splitlines()
        data_list = [item.split(',') for item in data_list]
        for item in data_list:
            if int(item[0]) == int(id):
                final_list.append(new_list)
            else:
                final_list.append(item)

    with open('database.csv', 'w') as file:
        for item in final_list:
            asd = ",".join(item)
            file.write(str(asd) + "\n")
    return "csa"


if __name__ == "__main__":
    app.run(debug=None)
