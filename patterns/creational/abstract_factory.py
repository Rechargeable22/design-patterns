"""Abstract Factory is a creational patter that lets you produce families of related
objects without specifying their concrete classes."""


# Abstract Product Interfaces
class Button:
    def paint(self):
        pass


class Checkbox:
    def paint(self):
        pass


# Concrete Product Classes
class WindowsButton(Button):
    def paint(self):
        return "Rendering a button in a Windows style"


class MacOSButton(Button):
    def paint(self):
        return "Rendering a button in a MacOS style"


class LinuxButton(Button):
    def paint(self):
        return "Rendering a button in a Linux style"


class WindowsCheckbox(Checkbox):
    def paint(self):
        return "Rendering a checkbox in a Windows style"


class MacOSCheckbox(Checkbox):
    def paint(self):
        return "Rendering a checkbox in a MacOS style"


class LinuxCheckbox(Checkbox):
    def paint(self):
        return "Rendering a checkbox in a Linux style"


# Abstract Factory Interface
class GUIFactory:
    def create_button(self):
        pass

    def create_checkbox(self):
        pass


# Concrete Factory Class
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


class MacOSFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

    def create_checkbox(self):
        return MacOSCheckbox()


class LinuxFactory(GUIFactory):
    def create_button(self):
        return LinuxButton()

    def create_checkbox(self):
        return LinuxCheckbox()


# Client Code
def application(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.paint())
    print(checkbox.paint())


if __name__ == '__main__':
    current_os = "MacOS"
    if current_os == "Windows":
        factory = WindowsFactory()
    elif current_os == "MacOS":
        factory = MacOSFactory()
    else:
        factory = LinuxFactory()

    application(factory)
