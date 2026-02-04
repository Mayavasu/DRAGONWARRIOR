from nicegui import ui, app
from data import topics
import random
app.add_static_files('/img', 'img')



def home_page():
    with ui.column().classes(
        'w-full gap-0 bg-no-repeat bg-cover bg-[url(/img/background.png)]'
    ).style('height: calc(100vh)'):
        with ui.row().classes('w-full h-24 items-center justify-between pr-10'):
            ui.image('/img/logo.png').classes('h-28 w-36')
            with ui.row().classes('items-center gap-4'):
                ui.image('/img/avatar.png').classes('h-20 w-16 ')
                ui.label('Maya').classes('inline-block align-middle text-white text-bold text-xl')
            with ui.row().classes('items-center gap-4'):
                ui.image('/img/coin.png').classes('h-18 w-18')
                ui.label('100').classes('text-white text-bold inline-block align-middle text-xl')
            with ui.row().classes('items-center gap-4'):
                ui.button('MY LESSONS').classes('').props('color=white size=xl outline padding=xs').style('padding-left: 15px; padding-right: 15px;')
                ui.button('MY STUFF').classes('').props('color=white size=xl outline padding=xs').style('padding-left: 15px; padding-right: 15px;')
            with ui.row().classes('items-center gap-4'):
                ui.button(icon='settings').classes('').props('q-btn round color="purple"')
                ui.button(icon='close').classes('').props('q-btn round color="purple"')

        with ui.row().classes('w-full h-40 justify-end pr-30 pt-10 pb-10'): 
            with ui.column().classes('text-white bg-indigo-950 px-5 py-1 rounded-sm text-xl'):
                with ui.row().classes('items-center'):
                    ui.label('Weekly Goal').classes('mr-5')
                    with ui.row().classes('gap-3'):
                        for i in range(1,6):
                                ui.row().classes('rounded-full border border-white h-4 w-4 ' )
                with ui.row().classes('w-full justify-end'):
                    ui.label('Lessons Completed This Week:  0')

        with ui.row().classes('w-full grow pl-30 pr-30 pb-30'):
            with ui.column().classes('bg-indigo-950 w-full h-full p-5 rounded-xl'):
                ui.label('RECOMMENDATIONS').classes('text-xl text-bold text-white')
                with ui.grid(columns=4).classes('w-full gap-5 h-full p-10'):
                    for i in random.sample(topics, 8):
                        
                        with ui.row().classes('bg-purple w-full h-full rounded-2xl'):
                            with ui.card().tight().classes('h-full'):
                                with ui.card_section().classes('bg-purple w-full h-25'):
                                    with ui.row().classes('items-center h-full w-full justify-center'):
                                        ui.label(i['topic']).classes('text-3xl text-bold text-white')    
                                with ui.card_section():
                                    ui.label(i['description'])                   
ui.add_css('''
:root {
    --nicegui-default-padding: 0rem;
    --nicegui-default-gap: 0rem;
}
''')

home_page()
ui.run(host="127.0.0.1", port=6767, reload=True)