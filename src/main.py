from nicegui import ui, app
from data import topics
import random
from tinydb import TinyDB, Query
db = TinyDB('db.json')

class Settings:
    def __init__(self):
        self.page = "login"
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

settings = Settings() 

app.add_static_files('/img', 'img')

def set_page(page_name):
    settings.email = ""
    settings.password = ""
    settings.first_name = ""
    settings.last_name = ""
    settings.page = page_name

def check_login():
    User = Query()    
    users = db.search(User.email == settings.email and User.password == settings.password)
    if len(users) == 0:
        ui.notify('Invalid Login', type = 'negative', position = 'top-right')
    else: 
        user = users[0]
        settings.first_name = user["first_name"]
        settings.page = 'home'

def check_signup():
    User = Query()
    users = db.search(User.email == settings.email)
    if len(users) == 1:
        ui.notify('User Already Exists', type = 'negative', position = 'top-right')
    elif settings.first_name.strip() == "" or settings.last_name.strip() == "" or settings.email.strip() == "" or settings.password.strip() == "":
        ui.notify('All Fields Are Required', type = 'negative', position = 'top-right')
    else:  
        db.insert({'first_name': settings.first_name, 'last_name': settings.last_name, 'email': settings.email, 'password': settings.password})
        settings.email = ""
        settings.password = ""
        settings.first_name = ""
        settings.last_name = ""
        settings.page = 'login'
        

def login_page():
    with ui.row().bind_visibility_from(settings, "page", backward=lambda x: x=="login").classes(
        'w-full gap-0 bg-no-repeat bg-cover bg-[url(/img/background.png)] items-center justify-center'
    ).style('height: calc(100vh)'):
        with ui.card().tight().classes('h-160 w-150 items-center gap-8').style('border-width: 5px; border-style: solid; border-color: indigo;'):
            with ui.row().classes(''):
                ui.image('/img/logo.png').classes('w-75 h-50')
            with ui.row():
                ui.input(label='Email', placeholder='start typing',).props('outlined').classes('w-100').bind_value(settings, "email")
            with ui.row():
                ui.input(label='Password', placeholder='start typing', password=True,).props('outlined').classes('w-100').bind_value(settings, "password")
            with ui.row():
                ui.button('Login', on_click=lambda: check_login()).classes('bg-indigo').style('border-color: purple; border-style: solid; border-width: 3px;')
            with ui.row():
                ui.button('Sign-Up', on_click=lambda: set_page("signup")).classes('bg-indigo').style('border-color: purple; border-style: solid; border-width: 3px;')
    
def signup_page():
    with ui.row().bind_visibility_from(settings, "page", backward=lambda x: x=="signup").classes(
        'w-full gap-0 bg-no-repeat bg-cover bg-[url(/img/background.png)] items-center justify-center'
    ).style('height: calc(100vh)'):
        with ui.card().tight().classes('h-180 w-150 items-center gap-8').style('border-width: 5px; border-style: solid; border-color: indigo;'):
            with ui.row().classes(''):
                ui.image('/img/logo.png').classes('w-75 h-50')
            with ui.row():
                ui.input(label='First Name', placeholder='start typing',).props('outlined').classes('w-100').bind_value(settings, "first_name")
            with ui.row():
                ui.input(label='Last Name', placeholder='start typing',).props('outlined').classes('w-100').bind_value(settings, "last_name")
            with ui.row():
                ui.input(label='Email', placeholder='start typing',).props('outlined').classes('w-100').bind_value(settings, "email")
            with ui.row():
                ui.input(label='Password', placeholder='start typing', password=True,).props('outlined').classes('w-100').bind_value(settings, "password")
            with ui.row():
                ui.button('Sign-Up', on_click=lambda: check_signup()).classes('bg-indigo').style('border-color: purple; border-style: solid; border-width: 3px;')
            with ui.row():
                ui.button('Login', on_click=lambda: set_page("login")).classes('bg-indigo').style('border-color: purple; border-style: solid; border-width: 3px;')

def home_page():    
    with ui.column().classes(
        'w-full gap-0 bg-no-repeat bg-cover bg-[url(/img/background.png)]'
    ).style('height: calc(100vh)').bind_visibility_from(settings, "page", backward=lambda x: x=="home"):
        with ui.row().classes('w-full h-24 items-center justify-between pr-10'):
            ui.image('/img/logo.png').classes('h-28 w-36')
            with ui.row().classes('items-center gap-4'):
                ui.image('/img/avatar.png').classes('h-20 w-16 ')
                ui.label().classes('inline-block align-middle text-white text-bold text-xl text-italic').bind_text_from(settings,"first_name")
            with ui.row().classes('items-center gap-4').style(''):
                ui.image('/img/coin.png').classes('h-18 w-18')
                ui.label('100').classes('text-white text-bold inline-block align-middle text-xl text-italic')
            with ui.row().classes('items-center gap-4'):
                ui.button('MY LESSONS').classes('').props('color=white size=xl outline padding=xs').style('padding-left: 15px; padding-right: 15px;')
                ui.button('MY STUFF').classes('').props('color=white size=xl outline padding=xs').style('padding-left: 15px; padding-right: 15px;')
            with ui.row().classes('items-center gap-4'):
                ui.button(icon='settings').classes('').props('q-btn round color="indigo.950"')
                ui.button(icon='close', on_click=lambda: set_page("login")).classes('').props('q-btn round color="indigo.950"')

        with ui.row().classes('w-full h-40 justify-end pr-30 pt-10 pb-10'): 
            with ui.column().classes('text-white bg-indigo-950 px-5 py-1 rounded-sm text-xl'):
                with ui.row().classes('items-center text-italic'):
                    ui.label('Weekly Goal').classes('mr-5 text-')
                    with ui.row().classes('gap-3'):
                        for i in range(1,6):
                                ui.row().classes('rounded-full border border-white h-4 w-4 ' )
                with ui.row().classes('w-full justify-end'):
                    ui.label('Lessons Completed This Week:  0').classes('text-italic')

        with ui.row().classes('w-full grow pl-30 pr-30 pb-30'):
            with ui.column().classes('bg-indigo-950 w-full h-full p-5 rounded-xl'):
                ui.label('RECOMMENDATIONS').classes('text-xl text-bold text-italic text-white')
                with ui.grid(columns=4).classes('w-full gap-5 h-full p-10'):
                    for i in random.sample(topics, 8):  
                        with ui.row().classes('bg-purple w-full h-full rounded-2xl'):
                            with ui.card().tight().classes('h-full'):
                                with ui.card_section().classes('bg-purple w-full h-25'):
                                    with ui.row().classes('items-center h-full w-full justify-center'):
                                        ui.label(i['topic']).classes('text-3xl text-bold text-white text-italic')    
                                with ui.card_section():
                                    ui.label(i['description'])    


ui.add_css('''
:root {
    --nicegui-default-padding: 0rem;
    --nicegui-default-gap: 0rem;
}
''')


home_page()
login_page()
signup_page()
ui.run(host="127.0.0.1", port=6767, reload=True)