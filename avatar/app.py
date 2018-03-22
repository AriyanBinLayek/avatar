
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER

AVATAR_TYPES = {
    'Default': 'https://robohash.org/{}.png',
    'Monsters': 'https://robohash.org/{}.png?set=set2',
    'Robot Heads': 'https://robohash.org/{}.png?set=set3',
    'Kitties': 'https://robohash.org/{}.png?set=set4',
}


class RobotHash(toga.App):
    def generate(self, widget):
        if self.input.value:
            url = AVATAR_TYPES[self.avatar_type.value].format(self.input.value)
        else:
            url = AVATAR_TYPES[self.avatar_type.value].format('beeware')

        self.avatar.image = toga.Image(url)

    def startup(self):
        # Create a main window with a name matching the app
        self.main_window = toga.MainWindow(self.name)

        self.input = toga.TextInput(style=Pack(flex=1))
        self.avatar_type = toga.Selection(
            items=sorted(AVATAR_TYPES.keys()),
            style=Pack(padding_left=10),
            on_select=self.generate
        )
        self.button = toga.Button(
            'Go!',
            style=Pack(padding_left=10),
            on_press=self.generate
        )

        input_box = toga.Box(
            children=[
                self.input,
                self.avatar_type,
                self.button
            ],
            style=Pack(direction=ROW, padding=10, alignment=CENTER)
        )

        self.avatar = toga.ImageView()

        # Create a main content box
        main_box = toga.Box(
            children=[
                input_box,
                self.avatar
            ],
            style=Pack(direction=COLUMN)
        )

        # Add the content on the main window
        self.main_window.content = main_box

        # Show the main window
        self.main_window.show()


def main():
    return RobotHash('Robot Hash', 'org.beeware.avatar')
