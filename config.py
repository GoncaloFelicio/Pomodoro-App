import platform


# System specific config for OS and Windows
system = platform.system()
if system == 'Windows':
    font_text_size = 16
    font_number_size = 12
    font_timer_size = 30
    butt_img_size = (270, 45)
    font_butt_size = 14
    butt_width = 6
    butt_height = 1
    butt_pady = 6
    Lbutt_padx = (25,5)
    Mbutt_padx = 15
    Rbutt_padx = (5,25)
    butt_bg_color='#af7f7f'
    butt_bg_color_act = '#af9f9f'
    timer_win_size = "284x255"
elif system == 'Darwin':
    font_text_size = 20
    font_number_size = 16
    font_timer_size = 40
    butt_img_size = (270, 33)
    font_butt_size = 20
    butt_width = 3
    butt_height = 1
    butt_pady = 3
    Lbutt_padx = (25,5)
    Mbutt_padx = 15
    Rbutt_padx = (5,25)
    butt_bg_color='#660000'
    butt_bg_color_act = '#660000'
    timer_win_size = "281x237"
            
text_color = 'white'
text_bg_color = '#313131'
entry_bg_color = '#171717'
