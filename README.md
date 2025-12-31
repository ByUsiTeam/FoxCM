# FoxCM - Go 语言高性能媒体分享平台

![FoxCM Logo](https://img.shields.io/badge/FoxCM-Go语言媒体分享平台-blue)
![License](https://img.shields.io/badge/License-Apache%202.0-green)
![Go Version](https://img.shields.io/badge/Go-1.16+-00ADD8)
![Gin Framework](https://img.shields.io/badge/Gin-Web%20Framework-red)

## 📖 项目简介

**FoxCM** 是一个基于 Go 语言和 Gin 框架构建的高性能、轻量级媒体分享平台。项目旨在提供一套完整的视频分享解决方案，具备用户管理、视频上传、播放、评论互动、实时通知等核心功能。采用现代化的响应式设计，完美适配桌面端和移动端，为创作者和观众提供流畅的观看体验。

### 🌟 核心特性

- **🚀 高性能后端**：基于 Go + Gin，支持高并发请求处理
- **📱 响应式前端**：适配所有设备的现代化界面设计
- **🎯 智能排序算法**：多种排序方式（热门、最新、点赞、播放）
- **🔔 实时通知**：WebSocket 实时消息推送
- **🔍 智能搜索**：关键词搜索 + 分类筛选
- **📊 完整的数据统计**：用户、视频、评论全方位统计
- **🛡️ 安全可靠**：用户认证、权限控制、文件安全检查
- **📱 移动优先**：专为移动设备优化的交互体验

## 📋 目录结构

```
FoxCM/
├── main.go                 # 主程序入口文件
├── go.mod                  # Go 模块管理
├── go.sum                  # 依赖校验文件
├── data/                   # 数据存储目录
│   ├── users.json         # 用户数据
│   ├── videos.json        # 视频数据
│   ├── comments.json      # 评论数据
│   └── system.json        # 系统配置
├── static/                 # 静态资源目录
│   ├── uploads/
│   │   ├── videos/        # 视频文件存储
│   │   ├── covers/        # 封面图片存储
│   │   └── avatars/       # 用户头像存储
│   └── favicon.ico        # 网站图标
├── templates/              # HTML模板文件
│   ├── base.html          # 基础布局模板
│   ├── index.html         # 首页模板
│   ├── login.html         # 登录页面模板
│   ├── register.html      # 注册页面模板
│   ├── upload.html        # 上传页面模板
│   ├── play.html          # 播放页面模板
│   ├── user_profile.html  # 用户主页模板
│   ├── search_results.html# 搜索结果模板
│   └── admin.html         # 管理后台模板
├── README.md              # 项目说明文档
└── LICENSE               # Apache License 2.0
```

## 🚀 快速开始

### 环境要求

- Go 1.16 或更高版本
- 支持视频播放的现代浏览器
- 500MB 以上可用存储空间（用于视频文件）

### 安装步骤

1. **克隆项目**
```bash
# 从 GitHub 克隆
git clone https://github.com/ByUsiTeam/FoxCM.git
cd FoxCM

# 或从 Gitee 克隆
git clone https://gitee.com/byusi/FoxCM.git
cd FoxCM
```

2. **安装依赖**
```bash
go mod download
```

3. **创建必要目录**
```bash
mkdir -p data static/uploads/videos static/uploads/covers static/uploads/avatars templates
```

4. **编译运行**
```bash
# 标准编译
go build -o foxcm main.go
./foxcm

# 交叉编译（Android ARM64）
CGO_ENABLED=0 GOOS=android GOARCH=arm64 go build -o foxcm_android main.go

# 交叉编译（Linux ARM64）
CGO_ENABLED=0 GOOS=linux GOARCH=arm64 go build -o foxcm_linux_arm64 main.go

# 交叉编译（Windows）
CGO_ENABLED=0 GOOS=windows GOARCH=amd64 go build -o foxcm.exe main.go
```

5. **访问应用**
打开浏览器访问：http://localhost:6544

首次使用请先注册账户，默认第一个注册用户为普通用户，可通过修改代码设置管理员。

## 🎮 功能演示

### 首页展示
- 智能排序的视频列表
- 响应式网格布局
- 播放量、点赞数、评论数实时显示
- 多种排序方式切换

### 视频播放
- HTML5 原生视频播放器
- 支持播放进度控制
- 视频信息展示
- 相关推荐视频

### 用户互动
- 评论发布与展示
- 视频点赞功能
- 评论点赞功能
- 实时通知提醒

### 内容管理
- 视频上传（支持 500MB 以内）
- 封面图片上传
- 用户头像管理
- 视频分类管理

### 搜索系统
- 关键词全文搜索
- 分类筛选
- 搜索结果相关度排序
- 热门分类展示

### 管理后台
- 用户管理（查看、删除）
- 视频管理（查看、删除）
- 系统统计（用户数、视频数、评论数）
- 系统设置（网站标题配置）

## 🔧 配置说明

### 服务器配置
默认配置在 `main.go` 中设置：

```go
const (
    Port           = "6544"                # 服务端口号
    SecretKey      = "foxcm-key"           # Session 加密密钥
    DataFolder     = "./data"              # 数据存储目录
    UploadFolder   = "./static/uploads/videos" # 视频文件目录
    CoverFolder    = "./static/uploads/covers"  # 封面目录
    AvatarFolder   = "./static/uploads/avatars" # 头像目录
)
```

### 文件上传限制
- **视频文件**：最大 500MB，支持格式：mp4, avi, mov, mkv, webm
- **封面图片**：最大 10MB，支持格式：jpg, jpeg, png, gif, webp
- **用户头像**：最大 5MB，支持格式：jpg, jpeg, png, gif, webp

### 安全设置
- Session 超时：浏览器会话期间有效
- 文件类型验证：严格检查上传文件类型
- 权限验证：管理员和普通用户权限分离

## 📊 系统架构

### 技术栈
- **后端框架**：Gin + Go HTTP Server
- **前端模板**：HTML + CSS + JavaScript（原生）
- **数据存储**：JSON 文件存储（简单易用）
- **实时通信**：WebSocket（Gorilla WebSocket）
- **文件处理**：标准 Go 文件系统操作
- **用户认证**：Session + Cookie

### 核心模块
1. **用户模块**：注册、登录、个人资料、权限管理
2. **视频模块**：上传、播放、管理、分类
3. **互动模块**：评论、点赞、通知、搜索
4. **管理模块**：用户管理、视频管理、系统统计
5. **API 模块**：RESTful API 接口

### 排序算法
FoxCM 采用智能热度排序算法，综合考虑：
- 播放次数
- 点赞数（权重×2）
- 评论数（权重×3）
- 时间衰减（24小时衰减一半）

## 📱 响应式设计

### 移动端优化
- **触控友好**：按钮大小适合手指操作
- **单列布局**：在小屏幕上自动调整为单列
- **隐藏菜单**：移动端自动折叠导航菜单
- **图片优化**：根据屏幕尺寸调整图片大小

### 桌面端体验
- **网格布局**：充分利用屏幕空间
- **多列显示**：同时展示多个视频卡片
- **悬停效果**：鼠标悬停时显示交互效果
- **固定导航**：顶部导航栏始终可见

## 🔌 API 接口

### 公共接口
| 方法 | 端点 | 描述 |
|------|------|------|
| GET | `/api/v1/videos` | 获取视频列表（支持分页、排序） |
| GET | `/api/v1/video/:filename` | 获取单个视频信息 |
| GET | `/api/v1/categories` | 获取所有分类及数量 |
| GET | `/api/v1/stats` | 获取系统统计信息 |

### 认证接口
| 方法 | 端点 | 描述 |
|------|------|------|
| POST | `/api/v1/video/:filename/like` | 点赞视频 |
| POST | `/api/v1/video/:filename/comment` | 发表评论 |

### WebSocket
- 端点：`/ws`
- 消息类型：notification, play_count, like
- 实时推送：新视频、新评论、点赞通知

## 🚢 部署指南

### 本地开发
```bash
# 1. 克隆项目
git clone https://github.com/ByUsiTeam/FoxCM.git

# 2. 进入目录
cd FoxCM

# 3. 安装依赖
go mod download

# 4. 创建目录结构
mkdir -p data static/uploads/videos static/uploads/covers static/uploads/avatars templates

# 5. 创建模板文件（使用前面提供的HTML模板）

# 6. 运行应用
go run main.go
```

### 生产部署
1. **编译为可执行文件**
```bash
go build -o foxcm main.go
```

2. **使用系统服务**
```bash
# Linux (Systemd)
sudo cp foxcm /usr/local/bin/
sudo cp foxcm.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable foxcm
sudo systemctl start foxcm
```

3. **配置反向代理（Nginx）**
```nginx
server {
    listen 80;
    server_name your-domain.com;
    
    location / {
        proxy_pass http://127.0.0.1:6544;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    # 静态文件优化
    location /static {
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
}
```

4. **HTTPS 配置**
```bash
# 使用 Let's Encrypt
sudo certbot --nginx -d your-domain.com
```

### Docker 部署
```dockerfile
# Dockerfile
FROM golang:1.19-alpine AS builder
WORKDIR /app
COPY . .
RUN go mod download
RUN CGO_ENABLED=0 GOOS=linux go build -o foxcm main.go

FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=builder /app/foxcm .
COPY --from=builder /app/templates ./templates
RUN mkdir -p data static
EXPOSE 6544
CMD ["./foxcm"]
```

构建并运行：
```bash
docker build -t foxcm .
docker run -d -p 6544:6544 -v ./data:/root/data -v ./static:/root/static --name foxcm foxcm
```

## 📈 性能优化

### 已实施的优化
1. **Go 语言优势**：原生高并发支持，内存占用低
2. **Gin 框架**：高性能 HTTP 路由和中间件
3. **静态文件缓存**：浏览器缓存静态资源
4. **视频流处理**：支持 HTTP Range 请求，断点续传
5. **WebSocket 连接池**：高效管理实时连接

### 建议的扩展优化
1. **数据库迁移**：从 JSON 文件迁移到 PostgreSQL/MySQL
2. **缓存层**：添加 Redis 缓存热点数据
3. **CDN 集成**：静态资源使用 CDN 加速
4. **视频处理**：添加视频转码和缩略图生成
5. **负载均衡**：多实例部署，Nginx 负载均衡

## 🛠️ 开发指南

### 代码结构
```go
// 主要数据结构
type User struct { ... }      // 用户模型
type Video struct { ... }     // 视频模型
type Comment struct { ... }   // 评论模型

// 主要函数
func setupWebRoutes(r *gin.Engine)   // 设置Web路由
func setupAPIRoutes(r *gin.Engine)   // 设置API路由
func authRequired() gin.HandlerFunc  // 认证中间件
func adminRequired() gin.HandlerFunc // 管理员中间件
```

### 添加新功能
1. **定义数据结构**：在相应结构体中添加字段
2. **添加路由处理**：在 `setupWebRoutes` 或 `setupAPIRoutes` 中添加
3. **更新模板**：如果需要前端界面，更新 HTML 模板
4. **数据持久化**：确保数据正确保存到 JSON 文件

### 测试运行
```bash
# 运行测试
go test ./...

# 代码检查
go vet ./...

# 性能分析
go test -bench=.
```

## 🔒 安全性

### 已实现的安全措施
- **用户认证**：Session + Cookie 认证机制
- **权限控制**：普通用户和管理员权限分离
- **文件验证**：严格验证上传文件类型和大小
- **XSS 防护**：模板自动转义 HTML 内容
- **CSRF 防护**：表单提交验证
- **安全头**：HTTP 安全头部设置

### 安全建议
1. 生产环境更换默认的 Session 密钥
2. 配置 HTTPS 加密传输
3. 定期备份数据文件
4. 监控系统日志和安全事件
5. 实施速率限制防止暴力破解

## 📄 开源协议

本项目采用 **Apache License 2.0** 开源协议。

```
Copyright 2024 FoxHome

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

## 🤝 贡献指南

我们欢迎任何形式的贡献！请参考以下步骤：

### 报告问题
1. 在 [GitHub Issues](https://github.com/ByUsiTeam/FoxCM/issues) 或 [Gitee Issues](https://gitee.com/byusi/FoxCM/issues) 提交问题
2. 清晰描述问题现象和复现步骤
3. 提供相关的日志或截图

### 提交代码
1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/your-feature`)
3. 提交更改 (`git commit -m 'Add some feature'`)
4. 推送到分支 (`git push origin feature/your-feature`)
5. 创建 Pull Request

### 开发规范
- 遵循 Go 语言官方代码规范
- 提交信息使用英文，清晰描述变更内容
- 添加适当的测试用例
- 更新相关文档

## 📞 联系方式

- **GitHub**: https://github.com/ByUsiTeam/FoxCM
- **Gitee**: https://gitee.com/byusi/FoxCM
- **问题反馈**: 请使用 GitHub 或 Gitee 的 Issues 功能
- **功能建议**: 欢迎提交 Pull Request 或 Feature Request

## 🙏 致谢

感谢以下开源项目和社区：

- [Gin Web Framework](https://github.com/gin-gonic/gin) - 高性能 Go Web 框架
- [Gorilla WebSocket](https://github.com/gorilla/websocket) - WebSocket 实现
- [Google UUID](https://github.com/google/uuid) - UUID 生成库
- [Gin Sessions](https://github.com/gin-contrib/sessions) - Session 中间件

感谢所有为项目做出贡献的开发者！

## 📈 项目路线图

### 长期规划
- [ ] 用户订阅功能
- [ ] 多语言支持
- [ ] 第三方登录（OAuth2）
- [ ] ~~移动端应用（Flutter/React Native）~~

---

**FoxCM** - 用 Go 语言构建的现代媒体分享平台 🦊

让分享变得更简单，让内容更有价值！