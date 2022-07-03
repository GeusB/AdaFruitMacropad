import displayio
import terminalio
from adafruit_display_shapes.rect import Rect 
from adafruit_display_text import label
from adafruit_macropad import MacroPad
from adafruit_hid.keycode import Keycode


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

    

while True:
    # if current_layer == 2:
    #     macropad.pixels[0] = Colors.Green
    #     macropad.pixels[1] = Colors.Green
    #     macropad.pixels[2] = Colors.Green
    #     macropad.pixels[3] = Colors.Green
    #     macropad.pixels[4] = Colors.Green
    #     macropad.pixels[5] = Colors.Green
    #     macropad.pixels[6] = Colors.Green
    #     macropad.pixels[7] = Colors.Green
    #     macropad.pixels[8] = Colors.Green
    #     macropad.pixels[9] = Colors.Green
    #     macropad.pixels[10] = Colors.Green
    #     macropad.pixels[11] = Colors.Green

    #     text_lines = macropad.display_text()
    #     text_lines[0].text = "Ctrl+X Ctrl+C Ctrl+V"    
    #     text_lines[1].text = "WinTab Ctrl+W Ctrl+D"
    #     text_lines[2].text = "  <<   Pause    >>"
    #     text_lines[3].text = f"Next   Mute   Prev {current_layer}"
    #     text_lines.show()   

    #     key_event = macropad.keys.events.get()

    #     if key_event:
    #         if key_event.pressed:
    #             if key_event.key_number == 0:
    #                 macropad.keyboard.press(macropad.Keycode.CONTROL, macropad.Keycode.X)
    #                 macropad.keyboard.release_all()
    #             if key_event.key_number == 1:
    #                 macropad.keyboard.press(macropad.Keycode.CONTROL, macropad.Keycode.C)
    #                 macropad.keyboard.release_all()
    #             if key_event.key_number == 2:
    #                 macropad.keyboard.press(macropad.Keycode.CONTROL, macropad.Keycode.V)
    #                 macropad.keyboard.release_all()
    #             if key_event.key_number == 3:
    #                 macropad.keyboard.press(macropad.Keycode.WINDOWS, macropad.Keycode.TAB)
    #                 macropad.keyboard.release_all() 
    #             if key_event.key_number == 4:
    #                 macropad.keyboard.press(macropad.Keycode.CONTROL, macropad.Keycode.W)
    #                 macropad.keyboard.release_all()
    #             if key_event.key_number == 5:
    #                 macropad.keyboard.press(macropad.Keycode.WINDOWS, macropad.Keycode.D)
    #                 macropad.keyboard.release_all()           
    #             if key_event.key_number == 6:
    #                 macropad.consumer_control.send(
    #                     macropad.ConsumerControlCode.SCAN_PREVIOUS_TRACK
    #                 )
    #             if key_event.key_number == 7:
    #                 macropad.consumer_control.send(
    #                     macropad.ConsumerControlCode.PLAY_PAUSE
    #                 )
    #             if key_event.key_number == 8:
    #                 macropad.consumer_control.send(
    #                     macropad.ConsumerControlCode.SCAN_NEXT_TRACK
    #                 )
    #             if key_event.key_number == 9:
    #                 if current_layer > 1:
    #                     current_layer = current_layer - 1
    #                 else:
    #                     current_layer = max_layer
    #             if key_event.key_number == 10:
    #                 macropad.consumer_control.send(
    #                     macropad.ConsumerControlCode.MUTE
    #                 )
    #             if key_event.key_number == 11:
    #                 if current_layer < max_layer:
    #                     current_layer= current_layer + 1
    #                 else:
    #                     current_layer = 1
    
    #     macropad.encoder_switch_debounced.update()

    #     if macropad.encoder_switch_debounced.pressed:
    #         if move == 0:
    #             move = 1
    #         else:
    #             move = 0

    #     if move == 1:
    #         macropad.mouse.move(x=+1)
    #         macropad.mouse.move(x=-1)
    #         macropad.pixels[11] = Colors.Red
            
    #     current_position = macropad.encoder

    #     if macropad.encoder > last_position:
    #         macropad.consumer_control.send(
    #             macropad.ConsumerControlCode.VOLUME_INCREMENT
    #         )
    #         last_position = current_position

    #     if macropad.encoder < last_position:        
    #         macropad.consumer_control.send(
    #             macropad.ConsumerControlCode.VOLUME_DECREMENT
    #         )
    #         last_position = current_position

        
    name = 'Home'
    macros = [
        (Colors.Red, 'Ctrl+X', [Keycode.CONTROL, 'x']),
        (Colors.Red, 'Ctrl+C', [Keycode.CONTROL, 'c']),
        (Colors.Red, 'Ctrl+V', [Keycode.CONTROL, 'v']),
        (Colors.Red, 'WinTab', [Keycode.WINDOWS, Keycode.TAB]), 
        (Colors.Orange, 'Ctrl+W', [Keycode.CONTROL, 'W']),
        (Colors.Blue, 'Ctrl+D', [Keycode.CONTROL, 'D']),
        (Colors.Green, '<<', [Keycode.COMMAND, 'r']),
        (Colors.Green, 'Pauze', [Keycode.COMMAND, 'H']),
        (Colors.Green, '>>', [Keycode.COMMAND, 'N']),
        (Colors.Yellow, 'Next', [Keycode.COMMAND, 'n', -Keycode.COMMAND, 'www.adafruit.com\n']), 
        (Colors.LightBlue, 'Mute', [Keycode.COMMAND, 'n', -Keycode.COMMAND, 'www.digikey.com\n']),
        (Colors.Pink, 'Prev', [Keycode.COMMAND, 'n', -Keycode.COMMAND, 'www.hackaday.com\n']),
        # Encoder button
        (0x000000, '', [Keycode.COMMAND, 'w'])
    ]
    macropad.display.auto_refresh = False 
    macropad.pixels.auto_write = False

    #display setup
    group = displayio.Group()
    for key_index in range(12):
        x = key_index % 3
        y = key_index // 3
        group.append(label.Label(terminalio.FONT, text='', color=Colors.White, anchored_position=((macropad.display.width - 1) * x /2,macropad.display.height - 1 -(3 - y) * 12), anchor_point=(x / 2, 1.0)))
    group.append(Rect(0, 0, macropad.display.width, 12, fill=Colors.White)) 
    group.append(label.Label(terminalio.FONT, text='', color=Colors.Black, anchored_position=(macropad.display.width//2, -2), anchor_point=(0.5, 0.0)))
    macropad.display.show(group)

    # text_lines = macropad.display_text()
    # text_lines[0].text = "Ctrl+X Ctrl+C Ctrl+V"    
    # text_lines[1].text = "WinTab Ctrl+W Ctrl+D"
    # text_lines[2].text = "  <<   Pause    >>"
    # text_lines[3].text = f"Next   Mute   Prev {current_layer}"
    # text_lines.show()   

    # display labels and set leds
    group[13].text = name 
    for i in range(12):
        if i < len(macros): 
            macropad.pixels[i] = macros[i][0]
            group[i].text = macros[i][1]
        else: 
            macropad.pixels[i] = 0
            group[i].text = ''
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
        # macropad.pixels[11] = Colors.Red
        
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
