import time
import displayio
import terminalio
from adafruit_display_shapes.rect import Rect 
from adafruit_display_text import label
from adafruit_macropad import MacroPad
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode


macropad = MacroPad()
macropad.pixels.brightness = 0.15
last_position = 0
current_layer = 1
max_layer = 4
move = 0

class Colors:
    Yellow = (255,255,0)
    Orange = (255,100,0)
    Red = (255, 0, 0)
    White = (255,255,255)
    Green = (0, 255, 0)
    LightBlue = (0, 255, 255)
    Blue = (0, 0, 255)
    Pink = (255, 0, 255)    
    Black = (0,0,0)

last_encoder_switch = macropad.encoder_switch_debounced.pressed    

while True:
    if current_layer == 1:
        title = 'Home'
        macros = [
            (Colors.Red, 'Ctrl+X', [Keycode.CONTROL, 'x']),
            (Colors.Red, 'Ctrl+C', [Keycode.CONTROL, 'c']),
            (Colors.Red, 'Ctrl+V', [Keycode.CONTROL, 'v']),
            (Colors.Red, 'WinTab', [Keycode.WINDOWS, Keycode.TAB]), 
            (Colors.Orange, 'Ctrl+W', [Keycode.CONTROL, 'W']),
            (Colors.Blue, 'Ctrl+D', [Keycode.CONTROL, 'D']),
            (Colors.Green, '<<', [[ConsumerControlCode.SCAN_PREVIOUS_TRACK]]),
            (Colors.Green, 'Pauze', [[ConsumerControlCode.PLAY_PAUSE]]),
            (Colors.Green, '>>', [[ConsumerControlCode.SCAN_NEXT_TRACK]]),
            (Colors.Yellow, 'Next', [Keycode.COMMAND, 'n', -Keycode.COMMAND, 'www.adafruit.com\n']), 
            (Colors.LightBlue, 'Mute', [Keycode.COMMAND, 'n', -Keycode.COMMAND, 'www.digikey.com\n']),
            (Colors.Pink, 'Prev', [Keycode.COMMAND, 'n', -Keycode.COMMAND, 'www.hackaday.com\n']),
            #encoder click
            (0x000000, '', [Keycode.COMMAND, 'w'])
        ]
        macropad.display.auto_refresh = False 
        macropad.pixels.auto_write = False

        # display setup
        display_group = displayio.Group()
        for key_index in range(12):
            x = key_index % 3
            y = key_index // 3
            display_group.append(label.Label(terminalio.FONT, text='', color=Colors.White, anchored_position=((macropad.display.width - 1) * x /2,macropad.display.height - 1 -(3 - y) * 12), anchor_point=(x / 2, 1.0)))
        display_group.append(Rect(0, 0, macropad.display.width, 12, fill=Colors.White)) 
        display_group.append(label.Label(terminalio.FONT, text='', color=Colors.Black, anchored_position=(macropad.display.width//2, -2), anchor_point=(0.5, 0.0)))
        macropad.display.show(display_group)

        # display labels and set leds
        display_group[13].text = title 
        for i in range(12):
            if i < len(macros): 
                macropad.pixels[i] = macros[i][0]
                display_group[i].text = macros[i][1]
            else: 
                macropad.pixels[i] = 0
                display_group[i].text = ''
        macropad.keyboard.release_all() 
        macropad.consumer_control.release() 
        macropad.mouse.release_all() 
        macropad.stop_tone() 
        macropad.pixels.show() 
        macropad.display.refresh()

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
                    macropad.keyboard.press(macropad.Keycode.WINDOWS, macropad.Keycode.TAB)
                    macropad.keyboard.release_all() 
                if key_event.key_number == 4:
                    macropad.keyboard.press(macropad.Keycode.CONTROL, macropad.Keycode.W)
                    macropad.keyboard.release_all()
                if key_event.key_number == 5:
                    macropad.keyboard.press(macropad.Keycode.WINDOWS, macropad.Keycode.D)
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
                    if current_layer > 1:
                        current_layer= current_layer - 1
                    else:
                        current_layer = max_layer
                if key_event.key_number == 10:
                    macropad.consumer_control.send(
                        macropad.ConsumerControlCode.MUTE
                    )
                if key_event.key_number == 11:
                    if current_layer < max_layer:
                        current_layer = current_layer + 1
                    else:
                        current_layer = 1

        macropad.encoder_switch_debounced.update()

        if macropad.encoder_switch_debounced.pressed:
            if move == 0:
                move = 1
            else:
                move = 0

        if move == 1:
            macropad.mouse.move(x=+1)
            macropad.mouse.move(x=-1)
            macropad.pixels[11] = Colors.Red
            
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

    if current_layer != 1:
        title = 'Debug'
        macros = [
            (Colors.Red, 'Debug', [Keycode.F5]),
            (Colors.Red, 'Run', [Keycode.SHIFT, Keycode.F5]),
            (Colors.Red, 'F9', [Keycode.F9]),
            (Colors.Red, 'Step', [Keycode.F10]), 
            (Colors.Orange, 'StepIn', [Keycode.F11]),
            (Colors.Blue, 'StepOut', [Keycode.SHIFT, Keycode.F11]),
            (Colors.Green, '<<', [[ConsumerControlCode.SCAN_PREVIOUS_TRACK]]),
            (Colors.Green, 'Pauze', [[ConsumerControlCode.PLAY_PAUSE]]),
            (Colors.Green, '>>', [[ConsumerControlCode.SCAN_NEXT_TRACK]]),
            (Colors.Yellow, 'Next', [Keycode.COMMAND, 'n', -Keycode.COMMAND, 'www.adafruit.com\n']), 
            (Colors.LightBlue, 'Mute', [Keycode.COMMAND, 'n', -Keycode.COMMAND, 'www.digikey.com\n']),
            (Colors.Pink, 'Prev', [Keycode.COMMAND, 'n', -Keycode.COMMAND, 'www.hackaday.com\n']),
            # encoder click
            (0x000000, '', [Keycode.WINDOWS, Keycode.TAB])
        ]
        macropad.display.auto_refresh = False 
        macropad.pixels.auto_write = False

        # display setup
        display_group = displayio.Group()
        for key_index in range(12):
            x = key_index % 3
            y = key_index // 3
            display_group.append(label.Label(terminalio.FONT, text='', color=Colors.White, anchored_position=((macropad.display.width - 1) * x /2, macropad.display.height - 1 -(3 - y) * 12), anchor_point=(x / 2, 1.0)))
        display_group.append(Rect(0, 0, macropad.display.width, 12, fill=Colors.White)) 
        display_group.append(label.Label(terminalio.FONT, text='', color=Colors.Black, anchored_position=(macropad.display.width//2, -2), anchor_point=(0.5, 0.0)))
        macropad.display.show(display_group)

        # display labels and set leds
        display_group[13].text = title 
        for i in range(12):
            if i < len(macros): 
                macropad.pixels[i] = macros[i][0]
                display_group[i].text = macros[i][1]
            else: 
                macropad.pixels[i] = 0
                display_group[i].text = ''
        macropad.keyboard.release_all() 
        macropad.consumer_control.release() 
        macropad.mouse.release_all() 
        macropad.stop_tone() 
        macropad.pixels.show() 
        macropad.display.refresh()

        # WIP
        position = macropad.encoder
        if position != last_position:
            # app_index = position % len(apps)
            # apps[app_index].switch()
            last_position = position

        macropad.encoder_switch_debounced.update()
        encoder_switch = macropad.encoder_switch_debounced.pressed
        if encoder_switch != last_encoder_switch:
            last_encoder_switch = encoder_switch
            if len(macros) < 13:
                continue
            key_number = 12
            pressed = encoder_switch
        else:
            event = macropad.keys.events.get()
            if not event or event.key_number >= len(macros):
                continue
            key_number = event.key_number
            pressed = event.pressed

        

        sequence = macros[key_number][2]
        if pressed:
            # 'sequence' is an arbitrary-length list, each item is one of:
            # Positive integer (e.g. Keycode.KEYPAD_MINUS): key pressed
            # Negative integer: (absolute value) key released
            # Float (e.g. 0.25): delay in seconds
            # String (e.g. "Foo"): corresponding keys pressed & released
            # List []: one or more Consumer Control codes (can also do float delay)
            # Dict {}: mouse buttons/motion (might extend in future)
            if key_number < 12: # No pixel for encoder button
                macropad.pixels[key_number] = 0xFFFFFF
                macropad.pixels.show()
            for item in sequence:
                if isinstance(item, int):
                    if item >= 0:
                        macropad.keyboard.press(item)
                    else:
                        macropad.keyboard.release(-item)
                elif isinstance(item, float):
                    time.sleep(item)
                elif isinstance(item, str):
                    macropad.keyboard_layout.write(item)
                elif isinstance(item, list):
                    for code in item:
                        if isinstance(code, int):
                            macropad.consumer_control.release()
                            macropad.consumer_control.press(code)
                        if isinstance(code, float):
                            time.sleep(code)
                elif isinstance(item, dict):
                    if 'buttons' in item:
                        if item['buttons'] >= 0:
                            macropad.mouse.press(item['buttons'])
                        else:
                            macropad.mouse.release(-item['buttons'])
                    macropad.mouse.move(item['x'] if 'x' in item else 0,
                                        item['y'] if 'y' in item else 0,
                                        item['wheel'] if 'wheel' in item else 0)
                    if 'tone' in item:
                        if item['tone'] > 0:
                            macropad.stop_tone()
                            macropad.start_tone(item['tone'])
                        else:
                            macropad.stop_tone()
                    elif 'play' in item:
                        macropad.play_file(item['play'])
        else:
            # Release any still-pressed keys, consumer codes, mouse buttons
            # Keys and mouse buttons are individually released this way (rather
            # than release_all()) because pad supports multi-key rollover, e.g.
            # could have a meta key or right-mouse held down by one macro and
            # press/release keys/buttons with others. Navigate popups, etc.
            for item in sequence:
                if isinstance(item, int):
                    if item >= 0:
                        macropad.keyboard.release(item)
                elif isinstance(item, dict):
                    if 'buttons' in item:
                        if item['buttons'] >= 0:
                            macropad.mouse.release(item['buttons'])
                    elif 'tone' in item:
                        macropad.stop_tone()
            macropad.consumer_control.release()
            if key_number < 12: # No pixel for encoder button
                macropad.pixels[key_number] = macros[key_number][0]
                macropad.pixels.show()
