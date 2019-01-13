# ETCD v3 FaaS操作实例

本实例使用FaaS的方法操作etcd v3版本。

## Requirements

- Functions API
- fn 
- ETCD v3 server([好雨部署](etcd_v3_server.md))

## Development

### 构建本地镜像

```
# 修改func.yaml文件，将name改成你自己的镜像名称。
# build it

fn build

```
### 本地测试
```
fn run

```

### 部署应用到仓库

```
fn deploy etcd_v3
```

## 在平台运行

### 首先设置必须的环境变量

```
# Set your Function server address
# Eg. api.faas.pro

FUNCAPI=YOUR_FUNCTIONS_ADDRESS

# ETCD服务端地址需要先部署etcd,参考： (Requirements)[#Requirements]

ETCD_SERVER=""
```

### Running with Functions

创建应用

```
curl -X POST --data '{
    "app": {
        "name": "etcd_v3",
        "config": { 
            "ETCD_SERVER": "'$ETCD_SERVER'",
        }
    }
}' http://$FUNCAPI/v1/apps
```

创建路由

```
curl -X POST --data '{
    "route": {
        "image": "<镜像名>",
        "path": "/command",
    }
}' http://$FUNCAPI/v1/apps/etcd_v3/routes
```

#### 云端运行试试？

```
curl -X POST --data '{"method": "put","key":"/hello","value":"hello word"}' http://$FUNCAPI/r/etcd_v3/command
curl -X POST --data '{"method": "get","key":"/hello"}' http://$FUNCAPI/r/etcd_v3/command

```