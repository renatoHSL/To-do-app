import FreeSimpleGUI as sg
from converters import converter

sg.theme("Black")

label_feet = sg.Text("Enter feet:")
input_feet = sg.InputText(key="feet")
print(input_feet)

label_inches = sg.Text("Enter inches:")
input_inches = sg.InputText(key="inches")

convert_button = sg.Button("Convert")
output_label = sg.Text(key="output")
exit_button = sg.Button("Exit")

window = sg.Window("Convertor",
                   layout=[[label_feet, input_feet],
                           [label_inches, input_inches],
                           [convert_button, exit_button, output_label]])

while True:
    event, values = window.read()
    match event:
        case "Convert":
            user_input_feet = values['feet']
            user_input_inches = values['inches']

            converted_value = converter(user_input_feet, user_input_inches)
            window["output"].update(value=f"{converted_value} m")

        case "Exit":
            break


window.close()