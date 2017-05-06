from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route('/story')
def create():
    return render_template('create.html')


@app.route("/story", methods=['POST'])
def create_save():
    title = request.form['title']
    story = request.form['story']
    criteria = request.form['criteria']
    business = request.form['business']
    estimation = request.form['estimation']
    progress = request.form['progress']
    with open('database.csv') as data:
        data_list = data.read().splitlines()
        data_list = [item.split("ß¤") for item in data_list]
        next_id = str(int(data_list[-1][0]) + 1)

    with open('database.csv', 'a') as file:
        file.write(str(next_id + "ß¤"))
        file.write(str(title + "ß¤"))
        file.write(str(story + "ß¤"))
        file.write(str(criteria + "ß¤"))
        file.write(str(business + "ß¤"))
        file.write(str(estimation + "ß¤"))
        file.write(str(progress + "\n"))
    return redirect("/list")


@app.route("/story/<int:id>", methods=["GET"])
def update_show(id):
    with open('database.csv') as data:
        data_list = data.read().splitlines()
        data_list = [item.split("ß¤") for item in data_list]
        selected_story = []
        for item in data_list:
            if int(item[0]) == int(id):
                selected_story = item

        selected = ['', '', '', '', '']
        options = ["Planning", "TODO", "In Progress", "Review", "Done"]
        for i in range(len(selected)):
            if selected_story[6] == options[i]:
                selected[i] = "selected"
        return render_template('update.html', sel_list=selected_story, id=id, selected=selected)


@app.route("/story/<int:id>", methods=['POST'])
def update_save(id):
    title = request.form['title']
    story = request.form['story']
    criteria = request.form['criteria']
    business = request.form['business']
    estimation = request.form['estimation']
    progress = request.form['progress']
    new_list = [str(id), title, story, criteria, business, estimation, progress]
    final_list = []
    with open('database.csv') as data:
        data_list = data.read().splitlines()
        data_list = [item.split("ß¤") for item in data_list]
        for item in data_list:
            if int(item[0]) == int(id):
                final_list.append(new_list)
            else:
                final_list.append(item)

    with open('database.csv', 'w') as file:
        for item in final_list:
            asd = "ß¤".join(item)
            file.write(str(asd) + "\n")
    return redirect("/list")


# redirect


@app.route("/", methods=['GET'])
@app.route("/list", methods=['GET'])
def main_list():
    with open('database.csv') as data:
        data_list = data.read().splitlines()
        data_list = [item.split("ß¤") for item in data_list]
    menu = ['ID', 'Story Title', 'User Story', 'Acceptance Criteria',
            'Business Value', 'Estimation', 'Status', 'Edit', 'Delete']
    return render_template('list.html', menu=menu, data_list=data_list)


@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    with open('database.csv') as data:
        data_list = data.read().splitlines()
        data_list = [item.split("ß¤") for item in data_list]
        for item in data_list:
            if int(item[0]) == int(id):
                data_list.remove(item)

    with open('database.csv', 'w') as file:
        for item in data_list:
            datas = "ß¤".join(item)
            file.write(str(datas) + "\n")
    menu = ['ID', 'Story Title', 'User Story', 'Acceptance Criteria',
            'Business Value', 'Estimation', 'Status', 'Edit', 'Delete']
    return render_template('list.html', menu=menu, data_list=data_list, id=str(id))


if __name__ == "__main__":
    app.run(debug=None)
