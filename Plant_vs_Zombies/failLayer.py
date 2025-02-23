import cocos
import gameplay_scene

class FailLayer(cocos.layer.Layer):
    def __init__(self):
        super(FailLayer, self).__init__()

    def on_enter(self):
        super(FailLayer, self).on_enter()

        if len(self.get_children()) != 0:
            return

        # 获得导演窗口的宽度和高度，是一个二元组
        width, height = cocos.director.director.get_window_size()

        sad=cocos.sprite.Sprite("images/sad.jpg")
        sad.position=width // 2, height // 2+150
        self.scale=0.7
        self.add(sad)

        # 创建标签！！！！！！！
        label = cocos.text.Label('Fail',
                                 font_name='Times New Roman',
                                 font_size=32,
                                 color=(255,50,100,255),
                                 anchor_x='center', anchor_y='center')

        # 设置标签的位置
        label.position = width // 2, height // 2  # //整数除法 去掉小数部分
        # 添加标签到FailLayer层
        self.add(label)

#创建Home菜单类
class HomeMenu(cocos.menu.Menu):
    def __init__(self):
        super(HomeMenu, self).__init__()
        self.font_item['font_size']=50
        self.font_item_selected['font_size']=50
        self.font_item['color']=(180,190,255,255)
        self.font_item_selected['color']=(180,190,255,255)

    def on_enter(self):
        super(HomeMenu, self).on_enter()
        #判断其他层资源是否加载完成
        if len(self.get_children())!=0:
            return

        #菜单事件绑定对象
        start_item = cocos.menu.ImageMenuItem('images/again.png',self.on_start_item_callback)
        # setting_item = cocos.menu.ImageMenuItem('images/setting-up.png',self.on_setting_item_callback)
        # help_item = cocos.menu.ImageMenuItem('images/help-up.png',self.on_help_item_callback)

        #菜单坐标
        s_width,s_height=cocos.director.director.get_window_size()
        x=s_width//2
        y=s_height//2-60
        dist=60
        self.create_menu([start_item],
                         layout_strategy=cocos.menu.fixedPositionMenuLayout(
                             [(x,y)]
                         ),
                         selected_effect=cocos.menu.zoom_in(),
                         unselected_effect=cocos.menu.zoom_out()
                         )

    def on_start_item_callback(self):
        '''切换场景'''
        next_scene = gameplay_scene.create_scene()
        ts = cocos.scenes.FadeTransition(next_scene, 1.0)
        cocos.director.director.push(next_scene)
    #
    # def on_setting_item_callback(self):
    #     pass
    #
    # def on_help_item_callback(self):
    #     '''切换场景'''
    #     next_scene = HelpScene.create_scene()
    #     ts=cocos.scenes.FadeTransition(next_scene,1.0)
    #     cocos.director.director.push(next_scene)

def create_scene():
    #创建FailLayer场景
    scene=cocos.scene.Scene(FailLayer())
    # 菜单添加至场景中
    scene.add(HomeMenu())
    return scene