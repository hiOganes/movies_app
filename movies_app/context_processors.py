menu = [
    {'name': 'Search', 'name_url': 'search'}, 
    {'name': 'Rated', 'name_url': 'rated'},
    ]

def get_menu(request):
    return {'mainmenu': menu}