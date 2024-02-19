import flet as ft
from flet import TextField
from flet_core.control_event import ControlEvent

def main(page: ft.Page ):
    page.title= "Counter"
    page.vertical_alignment= ft.MainAxisAlignment.CENTER
    page.theme_mode= "dark"
    
    text_number: TextField= TextField(value= '0', text_align=ft.TextAlign.RIGHT, width= 100)
    
    def decrement(e: ControlEvent):
        text_number.value= str(int(text_number.value)-1)
        page.update()
        
    def increment(e: ControlEvent):
        text_number.value= str(int(text_number.value)+1)
        page.update()

    page.add(
        ft.Row(
            controls=[ft.IconButton(icon= ft.icons.REMOVE, on_click= decrement),
            text_number,
            ft.IconButton(icon= ft.icons.ADD, on_click= increment)],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    
if __name__== '__main__':
    x=int(input("Click 1 for web browser and 2 for simple window view: "))
    if x==2:
        ft.app(target= main)
    elif x==1:
        ft.app(target= main, view=ft.AppView.WEB_BROWSER)
    else:
        print("only choose between two options")
        
    
