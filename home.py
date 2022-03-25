from flask import Flask

myobj = Flask(__name__)

name = "Selim"
city_names = ["Istanbul", "Ankara", "Izmir", "Bursa"]


@myobj.route('/')
def home():
    response = f"""
    <!DOCTYPE HTML>
    <html>
        <body>
            <h1>Welcome {name}</h1>
            <p><a href="www.google.com">not google</a></p>
            <ul>"""
    for city in city_names:
        response += f"""
                <li>{city}</li>"""
    response += """
            </ul>
        </body>
    </html>"""

    return response


myobj.run()
