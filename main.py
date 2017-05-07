from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route('/story')
def create():
    selected_story = []
    selected = ['', '', '', '', '']
    title = "Super Sprinter 3000 - Add new Story"
    id = ""
    return render_template('update.html', sel_list=selected_story, id=id, selected=selected, title=title)


@app.route("/story", methods=['POST'])
def create_save():
    title = request.form['title']
    story = request.form['story']
    criteria = request.form['criteria']
    business = request.form['business']
    estimation = request.form['estimation']
    progress = request.form['progress']
    criteria = str(criteria).replace("\n", "")
    with open('database.csv') as data:
        data_list = data.read().splitlines()
        data_list = [item.split("ß¤") for item in data_list]
        next_id = '0'
        if len(data_list) > 0:
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
        title = "Super Sprinter 3000 - Edit Story"
        return render_template('update.html', sel_list=selected_story, id=('/'+str(id)), selected=selected, title=title)


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


@app.route("/", methods=['GET'])
@app.route("/list", methods=['GET'])
def main_list():
    with open('database.csv') as data:
        data_list = data.read().splitlines()
        data_list = [item.split("ß¤") for item in data_list]
    menu = ['ID', 'Story Title', 'User Story', 'Acceptance Criteria',
            'Business Value', 'Estimation', 'Status', 'Edit', 'Delete']
    title = "Super Sprinter 3000"
    return render_template('list.html', menu=menu, data_list=data_list, title=title)


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
    return render_template('list.html', menu=menu, data_list=data_list, id=('/' + str(id)))


@app.route("/search", methods=['POST'])
def search():
    search = request.form['search']
    with open('database.csv') as data:
        data_list = data.read().splitlines()
        data_list = [item.split("ß¤") for item in data_list]
        selected_row = []
        for item in data_list:
            if str(search) in item:
                selected_row.append(item)
        menu = ['ID', 'Story Title', 'User Story', 'Acceptance Criteria', 'Business Value',
                'Estimation', 'Status', 'Edit', 'Delete']
        title = "Super Sprinter 3000"
        if len(search) > 0:
            return render_template('list.html', menu=menu, data_list=selected_row, title=title)
        else:
            return redirect("/list")


@app.route("/sortby", methods=['POST'])
def sortby():
    search = str(request.form['sortby'])
    menu = ['ID', 'Story Title', 'User Story', 'Acceptance Criteria', 'Business Value',
            'Estimation', 'Status', 'Edit', 'Delete']
    title = "Super Sprinter 3000"
    with open('database.csv') as data:
        data_list = data.read().splitlines()
        data_list = [item.split("ß¤") for item in data_list]
        if search == 'ID':
            data_list = sorted(data_list, key=lambda x: int(x[0]))
        elif search == 'Title':
            data_list = sorted(data_list, key=lambda x: str(x[1]))
        elif search == 'User Story':
            data_list = sorted(data_list, key=lambda x: str(x[2]))
        elif search == 'Acceptance Criteria':
            data_list = sorted(data_list, key=lambda x: str(x[3]))
        elif search == 'Business Value':
            data_list = sorted(data_list, key=lambda x: int(x[4]))
        elif search == 'Estimation (h)':
            data_list = sorted(data_list, key=lambda x: float(x[5]))
        elif search == 'Status':
            data_list = sorted(data_list, key=lambda x: str(x[6]))
    return render_template('list.html', menu=menu, data_list=data_list, title=title)


if __name__ == "__main__":
    app.run(debug=None)
