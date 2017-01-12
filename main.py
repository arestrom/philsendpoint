from flask import Flask

app = Flask(__name__)

@app.route('/phils_endpoint')
def phil():
    import random
    hiphil = 'WELCOME TO PHIL''S ENDPOINT! '
    string = ''
    colors = ['#C0C0C0', '#808080', '#000000', '#FF0000', '#800000',
             '#FFFF00', '#808000', '#00FF00', '#008000', '#00FFFF',
              '#008080', '#0000FF', '#000080', '#FF00FF', '#800080']


    for i in range(0, 5000):
        color = colors[random.randrange(len(colors))]
        string += '<span style=\"color:' + color + '\">' + hiphil
    return '<title>Phils ENDPOINT</title>' + string

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0') #this will make webserver visible on network
    app.run()