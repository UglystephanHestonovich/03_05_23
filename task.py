from flask import Flask, request

app = Flask(__name__)



dog_years = {1:14, 1.5:20, 2:24, 3:30, 4:36, 5:40, 6:42, 7:49, 8:56, 9:63, 10:65, 11:71, 12:75}
human_years = {14:1, 20:1.5, 24:2, 30:3, 36:4, 40:5, 42:6, 49:7, 56:8, 63:9, 65:10, 71:11, 75:12}
dog_months = {2:14, 6:5, 8:9}
human_months = {14:2, 5:6, 9:8}
@app.route('/lebo1/', methods=['POST'])
def hello_world7():
    if request.json['type'] == 'dog' and request.json['units'] == 'years':
        a = dog_years[request.json['n']]
        return {'n': a, 'units': 'years', 'type': 'human'}
    elif request.json['type'] == 'human' and request.json['units'] == 'years' and request.json['n'] >= 14:
        b = human_years[request.json['n']]
        return {'n': b, 'units': 'years', 'type': 'dog'}
    elif request.json['type'] == 'human' and request.json['units'] == 'month' and request.json['n'] == 14:
        b = human_months[request.json['n']]
        return {'n': b, 'units': 'month', 'type': 'dog'}
    elif request.json['type'] == 'dog' and request.json['units'] == 'month' and request.json['n'] > 2:
        a = dog_months[request.json['n']]
        return {'n': a, 'units': 'years', 'type': 'human'}
    elif request.json['type'] == 'dog' and request.json['units'] == 'month' and request.json['n'] == 2:
        a = dog_months[request.json['n']]
        return {'n': a, 'units': 'month', 'type': 'human'}
    elif request.json['type'] == 'human' and request.json['units'] == 'years' and request.json['n'] <= 9:
        b = human_months[request.json['n']]
        return {'n': b, 'units': 'month', 'type': 'dog'}

a = {}
@app.route('/queueclear/', methods=['POST'])
def hello_world8():
    a.clear()
    if len(a) == 0:
        return {'status': "ok"}

@app.route('/queue/', methods=['POST'])
def hello_world8_1():
    global person
    person = request.json["person_to_add"]
    a.append(person)
    print(a)
    if len(a) > 0:
        return {'status': "ok"}


@app.route('/queue/', methods=['GET'])
def hello_world8_2():
    print(a)
    if len(a) != 0:
        man = a.pop(0)
        return {'status': 'ok', 'person': man}
    else:
        return {'status': 'fail'}



big_plate = {'type':'Большая'}
big_plate['plate'] = list()

medium_plate = {'type':'Средняя'}
medium_plate['plate'] = list()

small_plate = {'type':'Маленькая'}
small_plate['plate'] = list()


@app.route('/clearall/', methods = ['POST'])
def task_13():
    big_plate['plate'].clear()
    medium_plate['plate'].clear()
    small_plate['plate'].clear()
    return {'status': 'ok'}


@app.route('/wash/', methods = ['POST'])
def task_13_1():
    if request.json['type'] == 'Маленькая':
        small_plate['plate'].append(request.json['color'])

    if request.json['type'] == 'Средняя':
        medium_plate['plate'].append(request.json['color'])
    if request.json['type'] == 'Большая':
        big_plate['plate'].append(request.json['color'])
    return {'status':'ok'}


@app.route('/take/', methods=['POST'])
def task_13_2():
    if request.json['type'] == 'Маленькая':
        if len(small_plate['plate']) == 0 :
            return {'status':'fail'}
        else :
            x = small_plate['plate'].pop(-1)
            return {'status':'ok','color':x}

    if request.json['type'] == 'Средняя':
        if len(medium_plate['plate']) == 0:
            return {'status':'fail'}
        else :
            x = medium_plate['plate'].pop(-1)
            print({'status':'ok','color':x})
            return {'status':'ok','color':x}
    if request.json['type'] == 'Большая':
        if len(big_plate['plate']) == 0:
            return {'status':'fail'}
        else :
            x = big_plate['plate'].pop(-1)
            print({'status': 'ok','color': x})
            return {'status':'ok','color':x}



















app.run(host="128.1.12.94", port= 5000)