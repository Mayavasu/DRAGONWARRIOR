from nicegui import ui, app  #type: ignore
app.add_static_files('/img', 'img')

@ui.page('/')
def home_page():
    with ui.column().classes(
        'w-full gap-0 bg-no-repeat bg-cover bg-[url(/img/background.png)]'
    ).style('height: calc(100vh)'):
        with ui.row().classes('w-full h-24'):
            ui.image('/img/logo.png').classes('h-24 w-32')
            ui.label('')
            ui.label('label 3')
        with ui.row().classes('w-full h-40'):
            ui.label('label 1')
            ui.label('label 2')
            ui.label('label 3')
        with ui.row().classes('w-full grow'):
            ui.label('label 1')
            ui.label('label 2')
            ui.label('label 3')
@ui.page('/map/{lat}/{lon}')
def map_page(lat: float, lon: float):
    ui.leaflet(center=(lat, lon), zoom=10)
    ui.link('Back to home', '/')
ui.add_css('''
:root {
    --nicegui-default-padding: 0rem;
    --nicegui-default-gap: 0rem;
}
''')
ui.run()