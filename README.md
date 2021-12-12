下面文件夹来自官方 https://github.com/mrdoob/three.js，用于学习之用。


```
/build/
/examples/
```

Three.js 中文文档：http://www.yanhuangxueyuan.com/threejs/docs/index.html

Three.js 零基础入门教程：http://www.yanhuangxueyuan.com/Three.js/

![](./test/assets/20211211160448.png)


## 场景 Scene



## 网格模型 Mesh



## 光源 Light



## 相机 Camera



## 渲染器 Renderer





## skybox

六面顺序：right/left/up/down/front/back

右侧，左侧，上面，下面，前面，背面

```
const cubeTextureLoader = new THREE.CubeTextureLoader();
cubeTextureLoader.setPath( './img/' );
const cubeTexture = cubeTextureLoader.load( [
  'mobile_r.jpg', 'mobile_l.jpg',
  'mobile_u.jpg', 'mobile_d.jpg',
  'mobile_f.jpg', 'mobile_b.jpg'
] );
scene.background = cubeTexture;

```

