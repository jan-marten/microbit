def on_button_pressed_a():
    basic.show_string("A")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    basic.show_icon(IconNames.HEART)
    basic.show_icon(IconNames.SMALL_HEART)
basic.forever(on_forever)
