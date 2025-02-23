import cocos
import pyglet
import threading
import time
import HomeScene
import cocos.scenes

class LoadingLayer(cocos.layer.Layer):
    def __init__(self):
        super(LoadingLayer,self).__init__()

        #获取屏幕大小
        s_width,s_height=cocos.director.director.get_window_size()
        #创建背景精灵
        background=cocos.sprite.Sprite('images/background.png')
        background.position=s_width//2,s_height//2
        background.scale=1.5
        self.add(background)

        #创建加载动画
        textures = []
        for i in range(1, 26):
            name_i = str(i)#loading_wps图片_14
            load_name_i = 'images/loading_wps图片/loading_wps图片_'+name_i+'.png'
            texture = pyglet.resource.image(load_name_i)
            textures.append(texture)
        animation = pyglet.image.Animation.from_image_sequence(textures, 0.08 ,True)
        loading_gif=cocos.sprite.Sprite(animation)
        loading_gif.position=s_width//2,s_height//2
        loading_gif.scale=0.5
        self.add(loading_gif)

        #创建子线程
        threading.Thread(target=self.thread_jump_home).start()

    def thread_jump_home(self):
        time.sleep(3)
        '''切换场景'''
        next_scene=HomeScene.create_scene()
        ts=cocos.scenes.FadeTransition(next_scene,1.0)
        cocos.director.director.push(next_scene)

def create_scene():
    #创建loading场景
    scene=cocos.scene.Scene(LoadingLayer())

    return scene