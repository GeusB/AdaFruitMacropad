import displayio
import terminalio
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import label
from adafruit_macropad import MacroPad

macropad = MacroPad()
macropad.pixels.brightness = 0.1
last_position = 0
current_layer = 1
max_layer = 4

yellow = (255,255,0)
red = (255, 0, 0)
white = (255,255,255)
green = (0, 255, 0)
lightBlue = (0, 255, 255)
blue = (0, 0, 255)
pink = (255, 0, 255)

while True:
    macropad.pixels[0] = red
    macropad.pixels[1] = red
    macropad.pixels[2] = red
    macropad.pixels[3] = red
    macropad.pixels[4] = white
    macropad.pixels[5] = white
    macropad.pixels[6] = green
    macropad.pixels[7] = green
    macropad.pixels[8] = green
    macropad.pixels[9] = yellow
    macropad.pixels[10] = lightBlue
    macropad.pixels[11] = pink

    text_lines = macropad.display_text()
    text_lines[0].text = "Ctrl+X Ctrl+C Ctrl+V"    
    text_lines[1].text = "Ctrl+A"
    text_lines[2].text = "Prev   Pause  Next"
    text_lines[3].text = "Left   Mute   Right"
    text_lines.show()   

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
            if key_event.key_number == 6:
                macropad.consumer_control.send(
                    macropad.ConsumerControlCode.SCAN_PREVIOUS_TRACK
                )
            if key_event.key_number == 7:
                macropad.consumer_control.send(
                    macropad.ConsumerControlCode.PLAY_PAUSE
                )
            if key_event.key_number == 8:
                macropad.consumer_control.send(
                    macropad.ConsumerControlCode.SCAN_NEXT_TRACK
                )
            if key_event.key_number == 9:
                macropad.mouse.move(x=-1)
            if key_event.key_number == 10:
                macropad.consumer_control.send(
                    macropad.ConsumerControlCode.MUTE
                )
            if key_event.key_number == 11:
                macropad.mouse.move(x=+1)

    macropad.encoder_switch_debounced.update()

    if macropad.encoder_switch_debounced.pressed:
        macropad.mouse.click(macropad.Mouse.RIGHT_BUTTON)

    current_position = macropad.encoder

    if macropad.encoder > last_position:
        macropad.consumer_control.send(
            macropad.ConsumerControlCode.VOLUME_INCREMENT
        )
        last_position = current_position

    if macropad.encoder < last_position:        
        macropad.consumer_control.send(
            macropad.ConsumerControlCode.VOLUME_DECREMENT
        )
        last_position = current_position
