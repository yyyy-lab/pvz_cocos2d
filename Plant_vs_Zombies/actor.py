
from cocos.collision_model import AARectShape
from cocos.euclid import Vector2
from pyglet.window import key
from cocos.director import director
import cocos
import cocos.actions.instant_actions
from cocos.sprite import Sprite

import pyglet.image
import enum
import random
#飞机=植物
class Fighter(Sprite):
    def __init__(self):
        super(Fighter, self).__init__(image='images/plant.png')

    def move(self, delta):

        fx, fy = self.position
        dx, dy = delta
        fx += dx
        fy += dy

        width_half = self.width // 2
        height_half = self.height // 2
        s_wight, s_height = director.get_window_size()

        if fx < width_half:
            fx = width_half
        elif fx > (s_wight - width_half):
            fx = s_wight - width_half
        if fy < height_half:
            fy = height_half
        elif fy > (s_height - height_half):
            fy = s_height - height_half

        self.position = fx, fy



#子弹
class Bullet(Sprite):
    def __init__(self):
        super(Bullet, self).__init__(image='images/peas.png')

        self.velocity=360

    def shoot_bullet(self, node):
        x, y = node.position

        self.position = x, y + node.height // 2
        self.schedule(self.update)

    def update(self, dt):
        if not self.visible:
            self.unschedule(self.update)
            return

        s_wight, s_height = director.get_window_size()
        posx, posy = self.position
        posy += self.velocity * dt

        self.position = posx, posy

        if posy>s_height:
            self.visible=False
            self.unschedule(self.update)

#僵尸枚举
class EnemyType(enum.Enum):
    jiangshi1=1
    jiangshi2=2
#僵尸生命值
enemyhitpoint={  EnemyType.jiangshi1:3, EnemyType.jiangshi2 : 4}
#击败僵尸获得分数
enemyscore={EnemyType.jiangshi1:5,EnemyType.jiangshi2:10}
#僵尸速度
enemyvelocity={EnemyType.jiangshi1:-20,EnemyType.jiangshi2:-25}

#僵尸类
class Enemy(Sprite):
    def __init__(self,type=EnemyType.jiangshi1):
        super(Enemy,self).__init__('images/jiangshi1.png')
        self.type=type                                         #僵尸类型
        self.velocity=enemyvelocity[EnemyType.jiangshi1]           #僵尸速度
        self.initial_hit_points=enemyhitpoint[EnemyType.jiangshi1] #僵尸生命值
        self.hit_points=self.initial_hit_points                    #僵尸当前生命

        if self.type==EnemyType.jiangshi1:
            self.image=pyglet.resource.image('images/jiangshi1.png')
            self.initial_hit_points=enemyhitpoint[EnemyType.jiangshi1]
            self.velocity=enemyvelocity[EnemyType.jiangshi1]

        elif self.type== EnemyType.jiangshi2:
            self.image = pyglet.resource.image('images/jiangshi2.png')
            self.initial_hit_points = enemyhitpoint[EnemyType.jiangshi2]
            self.velocity = enemyvelocity[EnemyType.jiangshi2]

        self.visible=False
        self.spawn()
        self.schedule(self.update)

    def pause_enemy(self):
        self.pause_scheduler()
    def resume_enemy(self):
        self.resume_scheduler()
    def update(self,dt):

        posx,posy=self.position
        posy+=self.velocity*dt
        self.do(cocos.actions.instant_actions.Place((posx,posy)))

    def spawn(self):
        s_wi,s_he=director.get_window_size()
        wi_ha=self.width//2
        he_ha=self.height//2
        posy=s_he+he_ha
        posx=random.randint(wi_ha,s_wi-wi_ha)
        self.do(cocos.actions.instant_actions.Place((posx, posy)))
        self.hit_points=self.initial_hit_points
        self.visible=True

