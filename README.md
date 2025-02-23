# pvz_cocos2d
创意来源:花花僵尸,pvz结合飞机小游戏

制作这个小游戏，主要是采用一个面向对象的一个思想，在这里，我们将每一个小的模块或者是对象，都单独的封装起来，有利于我们相互之间引用。

我们在这里主要建立了三个对象类型，分别是植物类型，僵尸类型和豌豆粒子类型。其实不难想到，这三个类型就分别对应飞机类型，敌机类型和子弹类型。三个类型对象之间，通过豌豆粒子来创建一定的联系与关系。比如说植物通过发射豌豆粒子，建立植物与豌豆粒子间的关系，而豌豆粒子击打僵尸，又创建了豌豆粒子和僵尸之间的关系，通过豌豆粒子，植物与僵尸之间也创建了间接的联系。

![image](https://github.com/yyyy-lab/pvz_cocos2d/blob/main/video/i1.png)
