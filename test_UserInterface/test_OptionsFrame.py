import customtkinter
import sys

sys.path.append("..")

from UserInterface.OptionsFrame import OptionsFrame 

def genericCallback(option):
    print(f"Callback: {option}")

def test_OptionsInit():
    print(f"Function: test_OptionsInit")
    options = ["a", "b", "c"]
    callback = genericCallback
    
    app = customtkinter.CTk()
    frame = OptionsFrame(app, options, callback)

    assert type(frame) == OptionsFrame
    for i, option in enumerate(frame.getOptions()):
        assert option == options[i]
    assert callback == frame.getCallback()
    app.destroy()

def test_getSetOptions():
    print("Function: test_getSetOptions")
    options = []
    callback = genericCallback
    app = customtkinter.CTk()
    frame = OptionsFrame(app, options, callback)

    options = ["1", "2", "3"]
    frame.setOptions(options)
    for i, option in enumerate(frame.getOptions()):
        assert option == options[i]
    print("Numbers Passed")

    options = ["Blue", "Green", "Yellow"]
    frame.setOptions(options)
    for i, option in enumerate(frame.getOptions()):
        assert option == options[i]
    print("Color Passed")

    option = list("abcdefghijklmnopqrstuvwxyz")
    frame.setOptions(options)
    frameOptions = frame.getOptions()
    print(f"Frame Options: {frameOptions}")
    for i, option in enumerate(frameOptions):
        assert option == options[i]
    print("Alphabet Passed")
    app.destroy()
    print("----------------------")

def test_addDeleteOptions():
    print("Function: test_addDeleteOptions")
    options = []
    callback = genericCallback
    app = customtkinter.CTk()
    frame = OptionsFrame(app, options, callback)

    options = ["1", "2", "3"]
    for i, option in enumerate(options):
        print(f"Adding {option}")
        frame.addOption(option)

    for i, option in enumerate(frame.getOptions()):
        assert options[i] == option

    print("Numbers Passed")

    [options.append(i) for i in ["Blue", "Green", "Yellow"]]
    for i, option in enumerate(options[3:]):
        print(f"Adding {option}")
        frame.addOption(option)
    

    options.remove("2")
    options.remove("Blue")
    frame.deleteOption("2")
    frame.deleteOption("Blue")

    for i, option in enumerate(frame.getOptions()):
        assert option == options[i]
    print("Color Passed")
    
    app.destroy()

    print("----------------------")



def test_reloadButtons():
    print("test_reloadButtons")

    options = ["test1", "test2", "test3"]
    callback = genericCallback
    app = customtkinter.CTk()
    frame = OptionsFrame(app, options, callback)

    frame.grid(row=0, column=0)

    frame.reloadButtons(["a", "b", "c"], callback, colCount=1, padding=50)

    app.mainloop()


test_OptionsInit()
test_getSetOptions()
test_addDeleteOptions()
test_reloadButtons()

