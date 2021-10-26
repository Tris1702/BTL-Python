class Settings:
    
    def __init__(self):
        self.screen_width = 1080
        self.screen_height = 720
        self.button_width = self.screen_width/10 # kích thước 1 ô menu
        self.spacing_width = self.screen_width/7 # khoảng cách hàng cột đầu vói màn hình ở menu
        self.spacing_height = self.screen_width/15 # khoảng cách hàng đầu với màn hình ở menu
        self.block_size = 60 # kích thước 1 ô