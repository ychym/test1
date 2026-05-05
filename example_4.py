import flet as ft

def main(page: ft.Page):
    page.title = 'My first app'

    greeting_history = []

    greeting_text = ft.Text("List of the name:")

    def text_name(e): 
        name = text_input.value.strip()
        
        if name:

            text_hello.value = f"Hello, {name.value}"
            text_hello.color = ft.Colors.GREEN_100
            greeting_history.append(name)
            greeting_text.value = f'List:\n' + "\n".join(greeting_history[-5:])
            text_input.value = ""
        else:
            text_hello.value = f"Enter your name !"
            text_hello.color = ft.Colors.RED

    def clear_history(e):
        greeting_history.clear()
        greeting_text.value = f"New list:"  


    text_hello = ft.Text('Hello', size = 20)
    text_input = ft.TextField(label = "Enter your name", on_submit = text_name, expand = True)
    btn = ft.Button('send', on_click = text_name)

    clear_btn = ft.IconButton(icon = ft.Icons.DELETE, on_click = clear_history)
    
  
    main_object = ft.Row([text_input, btn, clear_btn])

    page.add(text_hello, main_object, greeting_text)

ft.app(target = main, view = ft.AppView.WEB_BROWSER)

