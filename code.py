from adafruit_macropad import MacroPad

macropad = MacroPad()

last_position = 0
current_layer = 1
max_layer = 4

while True:
    key_event = macropad.keys.events.get()

    if key_event:
        if key_event.pressed:
            if key_event.key_number == 0:
                macropad.keyboard.press(macropad.Keycode.CONTROL, macropad.Keycode.X)
                macropad.keyboard.release_all()
            if key_event.key_number == 1:
                macropad.keyboard.press(macropad.Keycode.CONTROL, macropad.Keycode.C)
                macropad.keyboard.release_all()
            if key_event.key_number == 2:
                macropad.keyboard.press(macropad.Keycode.CONTROL, macropad.Keycode.V)
                macropad.keyboard.release_all()
            if key_event.key_number == 3:
                macropad.keyboard.press(macropad.Keycode.CONTROL, macropad.Keycode.A)
                macropad.keyboard.release_all()
            if key_event.key_number == 4:
                macropad.keyboard.press(macropad.Keycode.CONTROL, macropad.Keycode.A)
                macropad.keyboard.release_all()
            if key_event.key_number == 7:
                macropad.consumer_control.send(
                    macropad.ConsumerControlCode.PLAY_PAUSE
                )
            if key_event.key_number == 9:
                macropad.consumer_control.send(
                    macropad.ConsumerControlCode.VOLUME_DECREMENT
                )
            if key_event.key_number == 10:
                macropad.consumer_control.send(
                    macropad.ConsumerControlCode.MUTE
                )
            if key_event.key_number == 11:
                macropad.consumer_control.send(
                    macropad.ConsumerControlCode.VOLUME_INCREMENT
                )

    macropad.encoder_switch_debounced.update()

    if macropad.encoder_switch_debounced.pressed:
        macropad.mouse.click(macropad.Mouse.RIGHT_BUTTON)

    current_position = macropad.encoder

    if macropad.encoder > last_position:
        macropad.mouse.move(x=+1)
        macropad.consumer_control.send(
            macropad.ConsumerControlCode.VOLUME_INCREMENT
        )
        last_position = current_position

    if macropad.encoder < last_position:
        macropad.mouse.move(x=-1)
        macropad.consumer_control.send(
            macropad.ConsumerControlCode.VOLUME_DECREMENT
        )
        last_position = current_position
