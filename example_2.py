import flet as ft

def main(page: ft.Page):
    page.title = 'My first app'

    greeting_history = []

    favorite_history = []

    favorite_text = ft.Text("Favorities:")

    greeting_text = ft.Text("List of the name:")
    
    def text_name(e): 
        global name
        name = text_input.value.strip()
                
        if name:
            text_hello.value = f"Hello, {text_input.value}"
            text_hello.color = ft.Colors.GREEN_100
            greeting_history.append(name)
            greeting_text.value = f'List:\n' + "\n".join(greeting_history)
            text_input.value = ""
            
        else:
            text_hello.value = f"Enter your name !"
            text_hello.color = ft.Colors.RED

    def favorite(e):
        favorite_history.append(name) 
        favorite_text.value = f'Favorites:\n' + "\n".join(favorite_history)

    def clear_history(e):
        greeting_history.clear()
        greeting_text.value = f"New list:"  
        favorite_history.clear()
        favorite_text.value = f"New favorites" 
        

    text_hello = ft.Text('Hello', size = 20)
    text_input = ft.TextField(label = "Enter your name", on_submit = text_name, expand = True)# on_submit = :enter di baskanda ishtoo uchun
    
    btn = ft.Button('send', on_click = text_name)

    clear_btn = ft.IconButton(icon = ft.Icons.DELETE, on_click = clear_history)
    
    fav_btn = ft.IconButton(icon = ft.Icons.FAVORITE, on_click = favorite)

    main_object = ft.Row([text_input, btn, clear_btn])

    text_row = ft.Row([greeting_text, fav_btn, favorite_text])

    page.add(main_object, text_row)

ft.app(target = main, view = ft.AppView.WEB_BROWSER)

