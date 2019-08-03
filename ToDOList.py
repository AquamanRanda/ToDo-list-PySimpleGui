import PySimpleGUI as sg
from file_function import write,read,deleteContent
fname = 'file1'
comp =[]
tasks = read(fname)

layout = [
    [sg.Text('ToDo')],
    [sg.InputText('', key='Entity'), sg.Button(button_text='Add', key="add_button")],
    [sg.Text("ToDo List")],
    [sg.Listbox(values=tasks, size=(40, 10), key="items")],[sg.Text("Completed List")],[sg.Listbox(values=tasks, size=(40, 10), key="Completed")],
    [sg.Button('Delete'), sg.Button('Edit'),sg.Button("Complete"),sg.Button("prioritize"),sg.Button('Exit')],
]

window = sg.Window('ToDo App', layout)
while True:
    event, values = window.Read()
    if event == "add_button":
        tasks.append(values['Entity'])
        window.FindElement('items').Update(values=tasks)
        window.FindElement('add_button').Update("Add")
        window.FindElement('Entity').Update('')
        write(fname, tasks)

    elif event == "Delete":
        tasks.remove(values["items"][0])
        window.FindElement('items').Update(values=tasks)
        write(fname, tasks)

    elif (event == "prioritize"):
        for i in range(len(tasks)):
            min = i
            for j in range(i + 1, len(tasks)):
                if (tasks[min][-1] > tasks[j][-1]):
                    min = j
            tasks[i], tasks[min] = tasks[min], tasks[i]
        window.FindElement("items").Update(tasks)
        write(fname, tasks)

    elif event == "Edit":
        edit = values["items"][0]
        tasks.remove(values["items"][0])
        window.FindElement('items').Update(values=tasks)
        window.FindElement('Entity').Update(value=edit)
        window.FindElement('add_button').Update("Save")
        write(fname, tasks)
    elif event == 'Complete':
        tasks.remove(''.join(values["items"]))
        comp.append(''.join(values["items"]))
        window.FindElement("items").Update(tasks)
        window.FindElement("Completed").Update(comp)
        write(fname, tasks)
    elif event == None or event == "Exit":
        f = open('file1.txt','w')
        temp = deleteContent(f)
        f.close()
        break

window.Close()

