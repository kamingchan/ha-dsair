# Daikin DS-AIR Custom Component For Home Assistant

此项目是Home Assistant平台[金制空气](https://www.daikin-china.com.cn/newha/products/4/19/jzkq/)自定义组件的实现


fork了 mypel 的 https://github.com/mypal/ha-dsair   DS-dsair的版本
支持的网关设备型号为DTA117C611，mypel的版本号中间字母是B，设备支持的类型多了几个


# 接入方法

1. 将项目ha-air目录部署到自定义组件目录，一般路径为```~/.homeassistant/custom_components/``
2. 在配置文件```~/.homeassistant/configuration.yaml``中添加配置  
```yaml
climate:
  - platform: ds_air
    host: 192.168.1.150  # 空调网关IP地址，默认：192.168.1.150
    port: 8008           # 网关端口号，默认：8008
```
3. 重启HA服务

# TODO

根据APP反解显示，网关可控制新风、地暖、HD、新版空调、老版空调和浴室设备。此版本支持新版室内机,也支持老版本的室内机，后面会继续开发支持新风和空气传感器。

# 开发过程

fork了 mypel 的 https://github.com/mypal/ha-dsair   DS-dsair的版本
