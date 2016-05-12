# Internal
import Computer.driver.driver_main as driver
import Computer.gui.edit_bindings_gui as gui
import Computer.settings as settings
from Computer.driver.button_bindings import ButtonBindings


button_bindings = ButtonBindings()  # instantiate the button bindings object
# by modifying this object you can change what keys are activated when pressing the buttons

driver_thread = driver.DriverThread(button_bindings)  # create a driver thread and pass it the bindings object

driver_thread.daemon = True if settings.gui else False
# Python terminates the program when only Daemon threads exist.
# We want the program to terminate when the user closes the main (gui) thread, so the driver is set as a Daemon

driver_thread.start()

if settings.gui:
    gui.run_gui(button_bindings)  # pass the bindings object to the gui as well
