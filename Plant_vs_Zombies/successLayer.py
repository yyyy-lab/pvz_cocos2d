import cocos
import gameplay_scene
import HelpScene

class VictoryLayer(cocos.layer.Layer):
    def __init__(self):
        super(VictoryLayer, self).__init__()

    def on_enter(self):
        super(VictoryLayer, self).on_enter()

        if len(self.get_children()) != 0:
            return

        # 获取屏幕大小
        s_width, s_height = cocos.director.director.get_window_size()
        # 创建背景精灵
        background = cocos.sprite.Sprite('images/victory.jpg')
        background.position = s_width // 2, s_height // 2
        background.scale=0.5
        self.add(background)

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
        start_item = cocos.menu.ImageMenuItem('images/start-up.png',self.on_start_item_callback)
        # setting_item = cocos.menu.ImageMenuItem('images/setting-up.png',self.on_setting_item_callback)
        help_item = cocos.menu.ImageMenuItem('images/setting-up.png',self.on_help_item_callback)

        #菜单坐标
        s_width,s_height=cocos.director.director.get_window_size()
        x=s_width//2
        y=s_height//2
        dist=60
        self.create_menu([start_item,help_item],
                         layout_strategy=cocos.menu.fixedPositionMenuLayout(
                             [
                             (x,y-dist),
                             (x,y-dist*2)]
                         ),
                         selected_effect=cocos.menu.zoom_in(),
                         unselected_effect=cocos.menu.zoom_out()
                         )

    def on_start_item_callback(self):
        '''切换场景'''
        next_scene = gameplay_scene.create_scene()
        ts = cocos.scenes.FadeTransition(next_scene, 1.0)
        cocos.director.director.push(next_scene)

    def on_setting_item_callback(self):
        pass

    def on_help_item_callback(self):
        '''切换场景'''
        next_scene = HelpScene.create_scene()
        ts=cocos.scenes.FadeTransition(next_scene,1.0)
        cocos.director.director.push(next_scene)

def create_scene():
    #创建victory场景
    scene=cocos.scene.Scene(VictoryLayer())
    # 菜单添加至场景中
    scene.add(HomeMenu())
    return scene