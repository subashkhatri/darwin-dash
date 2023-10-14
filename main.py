from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivy.lang import Builder
# from database.connectdb 


# Load the kv files
Builder.load_file('cardactivity.kv')
CARD_INFO = {
    'balance': '$100.19',
    'number': '3085 2203 6384 8637',
    'type': 'Adult'
}

TRANSACTIONS = [
    {'start_time': '8:19am', 'end_time': '8:50am', 'pickup': 'Circular Quay, No. 3 Wharf', 'dropoff': 'Manly Ferry', 'icon': 'bus'},
    {'start_time': '7:29am', 'end_time': '7:55am', 'pickup': 'Granville', 'dropoff': 'Circular Quay', 'icon': 'bus'},
    {'start_time': '8:19am', 'end_time': '8:50am', 'pickup': 'Circular Quay, No. 3 Wharf', 'dropoff': 'Manly Ferry', 'icon': 'bus'},
    {'start_time': '7:29am', 'end_time': '7:55am', 'pickup': 'Granville', 'dropoff': 'Circular Quay', 'icon': 'bus'},
    {'start_time': '8:19am', 'end_time': '8:50am', 'pickup': 'Circular Quay, No. 3 Wharf', 'dropoff': 'Manly Ferry', 'icon': 'bus'},
    {'start_time': '7:29am', 'end_time': '7:55am', 'pickup': 'Granville', 'dropoff': 'Circular Quay', 'icon': 'bus'}
]

# Builder.load_file('carddetails.kv')

class CardActivityScreen(Screen):
    def on_enter(self):
        # Clear existing transactions first to avoid duplicates
        self.ids.transaction_list.clear_widgets()
        
        # Populate with new transactions
        for trans in TRANSACTIONS:
            trip_info = f"{trans['start_time']} to {trans['end_time']} - {trans['pickup']} to {trans['dropoff']}"
            item = OneLineIconListItem(text=trip_info)
            icon = IconLeftWidget(icon=trans["icon"])
            item.add_widget(icon)
            self.ids.transaction_list.add_widget(item)

class OrderCardScreen(Screen):
    pass


class WindowManager(ScreenManager):
    pass

class MainApp(MDApp):
    card_info = CARD_INFO
    def go_back(self):
        self.root.current = 'card_activity'

    def build(self):
        sm = WindowManager()
        sm.add_widget(CardActivityScreen(name="card_activity"))
        sm.add_widget(OrderCardScreen(name="order_card"))  
        return sm


if __name__ == '__main__':
    MainApp().run()

