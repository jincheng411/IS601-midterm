import importlib
import pkgutil

from app.commands import CommandHandler, Command



class App():
    def __init__(self):
        self.command_handler = CommandHandler()
        self.load_plugins()  # Load plugins dynamically

    def start(self):
        print("Welcome to the calculator, type 'exit' to stop.")
        self.command_handler.execute_command('menu')
        while True:
            user_input = input(">>> ").strip()
            self.command_handler.execute_command(user_input)

    def load_plugins(self):
        plugin_package = 'app.plugins'  # Package name for plugins
        # Iterate over all plugin folders in the plugins package
        for _, module_name, is_pkg in pkgutil.iter_modules([plugin_package.replace('.', '/')]):
            if is_pkg:
                module = importlib.import_module(f'{plugin_package}.{module_name}')
                # Import all command classes from the plugin module
                for command_class in dir(module):
                    cls = getattr(module, command_class)
                    try:
                        if issubclass(cls, (Command)) and hasattr(cls, 'execute'):
                            self.command_handler.register_command(module_name.lower(), cls())
                    except TypeError:
                        continue
