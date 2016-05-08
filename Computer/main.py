# Internal
import Computer.gui.edit_bindings_gui as gui
from Computer.button_bindings import ButtonBindings
import Computer.driver_main as driver
import Computer.settings as settings

button_bindings = ButtonBindings()

input_thread = driver.DriverThread(button_bindings)
input_thread.setDaemon(True)
input_thread.start()

if settings.gui:
    gui.run_gui(button_bindings)
