from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_mail import  Message, Mail
from decouple import config


app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = config('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = config('MAIL_PASSWORD')

app.config['MAIL_DEFAULT_SENDER'] = config('MAIL_USERNAME')

mail = Mail(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)


@app.route('/')
def index():
    return render_template('main.html')

@app.route('/sendemail/', methods=['POST'])
def send_email():
    # Get form data
    name = request.form['name']
    subject = request.form['Subject']
    email = request.form['_replyto']
    message = request.form['message']

    # Create message
    msg = Message(subject, sender='ogolasospeter62@gmail.com', recipients=['email',])
    msg.body = f"From: {name}\nEmail: {email}\n\n{message}"

    # Send email
    mail.send(msg)

    return 'The Email sent successfully!'


#Create an education details API for my portfolio
@app.route('/education/')

def educationData():
    data = [
        {
        'levelTitle': "Bachelor's Computer Technology",
        'institution': 'JOMO KENYATTA UNIVERSITY of AGRICULTURE and TECHNOLOGY.',
        'year': '2021 - Current',
        'projects': [
            {'name': 'In-Person Service Finder', 'description': 'ALX-SE Team Project'},
            {'name': 'Customizable Recipe Website', 'description': 'ALX-SE Solo Project'},
        ]
        },
        {
            'levelTitle': "Kenya Certificate of Secondary Education",
            'institution': 'HomaBay High School',
            'year': '2016 - 2019',
            'projects': [
                {'name': 'School Voting System', 'description': 'KCSE Project'}
            ]
        },
        {
            'levelTitle': "Kenya Certificate of Primary Education",
            'institution': 'Ogande Junior Academy',
            'year': '2008 - 2015',
            'projects': [
                {'name': 'School Voting System', 'description': 'KCPE Project'}
            ]
        },
        {
            'levelTitle': "Other Certifications",
            'institution': 'ALX Africa',
            'year': '2020 - Current',
            'projects': [
                {'name': 'ALX Africa', 'description': 'ALX Africa'},
            ]
        },
        {
            'levelTitle': "Other Certifications",
            'institution': 'Microsoft Learn',
            'year': 'May - July,2023',
            'projects': [
                {'name': 'Microsoft Learn', 'description': 'Microsoft Learn'},
            ]
        }
    ]

    return jsonify(data)
    
@app.route('/programminglanguages')
def programLang():
    langData = [
       
        {
            'name': 'HTML',
            'title': 'Frontend Development of my Website Projects',
            'description': 'Used in my projects for the frontend development/ the Graphical User Interface..',
            'image': 'https://www.w3.org/html/logo/downloads/HTML5_Logo_512.png',
            'level': 'Intermediate'
        },
        {
            'name': 'CSS',
            'title': 'Styling of my Website Projects',
            'description': 'Has played a major role in the styling of my website projects..',
            'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSIB8xYDdx2TWL5IkMRT8zPQZV12Pqi_t_eUKzjjg1CsA&s',
            'level': 'Intermediate'
        },
        {
            'name': 'Kotlin',
            'title': 'Android Applications Development Language',
            'description': 'Kotlin is a cross-platform, statically typed, general-purpose programming language with type inference, mostly used for android Applicationsdevelopment..',
            'image': 'data:image/jpeg;base64,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',
            'level': 'Intermediate'
        },
         {
            'name': 'Python',
            'title': 'Backend Development[Routing, API management] of my Website Projects',
            'description': 'Python has allowed me to work quickly and integrate systems more effectively, thus a fast realization of my projects..',
            'image': 'https://www.python.org/static/community_logos/python-logo-master-v3-TM.png',
            'level': 'Intermediate'
        },
        {
            'name': 'JavaScript',
            'title': 'Backend Development and Interactivity of my Website Projects',
            'description': 'I have used JavaScript to add to the  interactivity of my website projects..',
            'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/JavaScript-logo.png/600px-JavaScript-logo.png',
            'level': 'Intermediate'

        },
        {
            'name': 'SQL',
            'description': 'In my recently worked projects, I have used SQL to store, retrieve and manipulate the database records..',
            'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Postgresql_elephant.svg/512px-Postgresql_elephant.svg.png',
            'level': 'Intermediate'
        }
    ]

    return jsonify(langData)


@app.route('/technicalskills')
def frameworks():
    frameData = [
        {
            'name':'Tools',
            'decs': [
                {'name':'NumPy'},
                {'name':'MS Excel'}
            ]
        },
        {
            'name':'Database Management Systems',
            'decs': [
                {'name':'MySQL'},
                {'name':'SQLite3'}
            ]
        },
        {
            'name':'Internet Technologies',
            'decs': [
                {'name':'Flask'},
                {'name':'HTML5'},
                {'name':'CSS'},
                {'name':'Bootstrap'}
            ]
        },
        {
            'name': 'Android App Development',
            'decs': [
                {'name':'Kotlin'},
                {'name':'Android Studio'}
            ]
        },
        {
            'name': 'Version Control',
            'decs': [
                {'name':'Git'},
                {'name':'GitHub'}
            ]
        },
        
    ]

    return jsonify(frameData)

@app.route('/projects')
def projectsViews():
    projectsData = [
        {
            'name': 'In-Person Service Finder',
            'description': 'This is a web application that allows users to find in-person services within their locality. The services include; Hospitals, Schools, Restaurants, Hotels, etc. The application also allows users to rate the services they receive from the service providers.',
            'image': 'https://github.com/gims-inc/IPSP/blob/master/web_dynamic/static/images/on_phone2.jpeg?raw=true',
            'link': 'https://github.com/gims-inc/IPSP',
            'year':'2023'
        },
        {
            'name': 'Customizable Recipe Website',
            'description': 'This is a web application that allows users to find recipes for their favorite meals. The application also allows users to add their own recipes.',
            'image': 'https://github.com/ogolaSospeter/WebstackPortfolioProject/raw/main/templates/images/main.jpg',
            'link': 'https://github.com/ogolaSospeter/WebstackPortfolioProject',
            'year':'2023'
        }
    ]

    return jsonify(projectsData)