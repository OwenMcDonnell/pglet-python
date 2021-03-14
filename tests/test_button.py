import pytest
import pglet
from pglet import Button
from pglet import button

def test_button_primary_must_be_bool():
    with pytest.raises(Exception):
        Button(id="button1", text="My button", primary="1")

def test_button_add():
    b = Button(id="button1", text="My button", primary=True, data='this is data')
    assert isinstance(b, pglet.Control)
    assert isinstance(b, pglet.Button)
    assert b.get_cmd_str() == ('button id="button1" data="this is data" primary="true" text="My button"'), "Test failed"

def test_button_with_all_properties():
    b = Button(primary=False, compound=False, action=False, toolbar=True, split=False, text='This is text', 
        secondary_text='This is secondary text', url='https://google.com', new_window=True, title='This is title',
        icon='Mail', icon_color='red', data='data', items=[
            button.Item(text='Item1 text', secondary_text='Item1 secondary text', url='https://google.com', new_window=False,
            icon='Mail', icon_color='blue', icon_only=True, split=False, divider=False, items=[
                button.Item('Item1Item1'),
                button.Item('Item1Item2')
            ]),
            button.Item(text='Item2 text')
        ])

    assert isinstance(b, pglet.Control)
    assert isinstance(b, pglet.Button)
    assert b.get_cmd_str() == ('button action="false" compound="false" data="data" icon="Mail" '
    'iconColor="red" newWindow="true" primary="false" secondaryText="This is secondary text" '
    'split="false" text="This is text" title="This is title" toolbar="true" url="https://google.com"\n'
    '  item divider="false" icon="Mail" iconColor="blue" iconOnly="true" newWindow="false" '
    'secondaryText="Item1 secondary text" split="false" text="Item1 text" url="https://google.com"\n'
    '    item text="Item1Item1"\n'
    '    item text="Item1Item2"\n'
    '  item text="Item2 text"'), "Test failed"

