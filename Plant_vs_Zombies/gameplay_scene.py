import cocos
from collections import defaultdict
from cocos.sprite import Sprite
from cocos.director import director
from cocos.scene import Scene
from cocos.layer import Layer
from cocos.particle_systems import ParticleSystem

import pyglet.image
import enum
import random
from actor import Fighter,Bullet,Enemy,EnemyType

import successLayer
import failLayer

class GamePlayLayer(Layer):

    is_event_handler = True
    def __init__(self):
        super(GamePlayLayer,self).__init__()
        self.s_width,self.s_height=director.get_window_size()

        self.init_bg()
        # self.init_statusbar()
        self.init_gamesprite()
        self.init_score()

    def init_bg(self):
        background=cocos.sprite.Sprite('images/bg.jpg')
        background.position=self.s_width//2,self.s_height//2
        background.scale=0.5
        self.add(background,0)

    def init_statusbar(self):
        self.pause_button=Sprite('images/start-up.png')               #按钮图片地址
        self.pause_button.position=30,400           #按钮坐标
        self.add(self.pause_button,2)

        self.resume_button = Sprite('images/setting-up.png')
        self.resume_button = self.s_width // 2, self.s_height // 2 + 30
        self.add(self.resume_button, 2)
        self.resume_button.visible = False

        self.back_button = Sprite('images/help-up.png')
        self.back_button.position=self.s_width//2,self.s_height//2-30
        self.add(self.back_button,2)
        self.back_button.visible=False

        self.pause_status=0       #0暂停1继续


    def init_gamesprite(self):
        #初始化僵尸
        self.jiangshi1=Enemy(EnemyType.jiangshi1)
        self.add(self.jiangshi1,1)

        self.jiangshi2 = Enemy(EnemyType.jiangshi2)
        self.add(self.jiangshi2,1)
        #初始化飞机
        self.player=Fighter()
        self.player.score=0   #得分
        self.player.position=self.s_width//2,50
        self.add(self.player,1)
        self.duration=0
        self.schedule(self.update)

    def init_score(self):
        pass
    #     # 创建标签！！！！！！！
    #     self.label = cocos.text.Label('%d' % self.player.score,
    #                                   font_name='Times New Roman',
    #                                   font_size=32,
    #                                   anchor_x='center', anchor_y='center')
    #     # 获得导演窗口的宽度和高度，是一个二元组
    #     width, height = cocos.director.director.get_window_size()
    #     # 设置标签的位置
    #     self.label.position = width // 2, height // 2  # //整数除法 去掉小数部分
    #     # 添加标签到HelpScene层
    #     self.add(self.label)


    def on_mouse_drag(self,x,y,dx,dy,buttons,modifiers):
        #self.player.move((x,y))
        self.player.position=x,y

    def on_mouse_press(self,x,y,button,mofifiers):
        pass
        # if button == pyglet.window.mouse.LEFT:
        #     pause_button_rect=self.pause_button.get_rect()
        #     if pause_button_rect.contains(x,y) and self.pause_status==0:
        #         self.resume_button.visible =True
        #         self.back_button.visible =True
        #         self.pause_button.visible =False
        #         self.pause_status = 1
        #         self.jiangshi1.pause_enemy()
        #         self.jiangshi2.pause_enemy()
        #         self.unschedule(self.update)
        #
        #     resume_button_rect = self.resume_button.get_rect()
        #     if resume_button_rect.contains(x, y) and self.pause_status == 1:
        #         self.resume_button.visible = False
        #         self.back_button.visible = False
        #         self.pause_button.visible = True
        #         self.pause_status = 0
        #         self.jiangshi1.resume_enemy()
        #         self.jiangshi2.resume_enemy()
        #         self.schedule(self.update)

    def update(self,dt):
        self.duration+=dt

        if self.duration>1.5:#5秒一个子弹
            self.duration=0
            bullet = Bullet()
            bullet.shoot_bullet(self.player)
            self.add(bullet, 2)

        for node in self.get_children():
            if not node.visible and isinstance(node,Bullet):
                self.remove(node)
        self.collition_obj()

    def collition_obj(self):
        for node in self.get_children():
            if node.visible and isinstance(node, Fighter):
                bulletrect = node.get_rect()
                if bulletrect.intersect(self.jiangshi1.get_rect()) or bulletrect.intersect(self.jiangshi2.get_rect()):
                    '''切换场景'''
                    next_scene = failLayer.create_scene()
                    ts = cocos.scenes.FadeTransition(next_scene, 1.0)
                    cocos.director.director.push(next_scene)
            if  node.visible and isinstance(node, Bullet):
                bulletrect=node.get_rect()
                if bulletrect.intersect(self.jiangshi1.get_rect()):
                    node.visible=False
                    self.handle_collition(self.jiangshi1)
                    continue
                if bulletrect.intersect(self.jiangshi2.get_rect()):
                    node.visible=False
                    self.handle_collition(self.jiangshi2)
                    continue

    def handle_collition(self,enemy):
        enemy.hit_points-=1                            #被打中生命值减少
        if enemy.hit_points<=0:
            enemy.visible=False
            enemy.spawn()
            if enemy.type==EnemyType.jiangshi1:
                self.player.score+=5
            if enemy.type==EnemyType.jiangshi2:
                self.player.score+=10
            if self.player.score>=300:
                '''切换场景'''
                next_scene =successLayer.create_scene()
                ts = cocos.scenes.FadeTransition(next_scene, 1.0)
                cocos.director.director.push(next_scene)


def create_scene():
    scene=Scene(GamePlayLayer())
    return scene