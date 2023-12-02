# 自定义推送插件

**自用**， 主要为了实现企业微信推送。

但是推送的服务器不是企业微信服务器，而是自建的服务器，封装了推送消息的接口，简化调用。

## 配置说明

```yaml
sensor:
  - platform: ha-wecom-notify
    api_url: https://yourdomain.com/push_message
    push_key: abc123
```
