"""
Here you can create samples of your widgets by providing default parameters,
inserting them in a container widget, mixing them with other widgets, etc...
These samples will appear in the WidgetBrowser

See http://toscawidgets.org/documentation/WidgetBrowser for more information
"""

import tw2.core as twc, widgets as twf

options = ['Red', 'Orange', 'Yellow', 'Green', 'Blue']

class DemoChildren(twc.CompoundWidget):
    title = twf.TextField()
    priority = twf.SingleSelectField(options=['', 'Normal', 'High'])
    description = twf.TextArea()

class DemoCheckBox(twf.CheckBox):
    value = True

class DemoSingleSelectField(twf.SingleSelectField):
    options = options

class DemoMultipleSelectField(twf.MultipleSelectField):
    options = options

class DemoRadioButtonList(twf.RadioButtonList):
    options = options

class DemoCheckBoxList(twf.CheckBoxList):
    options = options

class DemoRadioButtonTable(twf.RadioButtonTable):
    options = options
    cols = 2

class DemoCheckBoxTable(twf.CheckBoxTable):
    options = options
    cols = 2

class DemoTableLayout(twf.TableLayout, DemoChildren):
    pass

class DemoListLayout(twf.ListLayout, DemoChildren):
    pass

class DemoSpacer(twf.TableLayout):
    demo_for = twf.Spacer
    title = twf.TextField()
    xx = twf.Spacer()
    description = twf.TextArea()

class DemoLabel(twf.TableLayout):
    demo_for = twf.Label
    title = twf.TextField()
    xx = twf.Label(text='Please enter as much information as possible in the description.')
    description = twf.TextArea()

class DemoFieldSet(twf.FieldSet):
    legend = 'FieldSet'
    child = DemoTableLayout()

class DemoForm(twf.Form):
    child = DemoTableLayout()

class DemoButton(twf.Button):
    value = 'Click me'
    attrs = {'onclick': 'alert("Hello")'}

class DemoGridLayout(twf.GridLayout):
    id = 'x'
    extra_reps = 3
    title = twf.TextField()
    priority = twf.SingleSelectField(options=['', 'Normal', 'High'])

class DemoImageButton(twf.ImageButton):
    modname = 'tw2.forms'
    filename = 'static/edit-undo.png'
