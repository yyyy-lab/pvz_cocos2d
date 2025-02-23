import cocos
from cocos.scene import Scene
from LoadingLayer import create_scene

if __name__ == '__main__':
    #初始化导演，设置窗口的高、宽、标题
    cocos.director.director.init(width=400,height=640,caption="植物大战僵尸")

    #创建主场景
    main_scene=cocos.scene.Scene(create_scene())

    #开始启动主场景
    cocos.director.director.run(main_scene)