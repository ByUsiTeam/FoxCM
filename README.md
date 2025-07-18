# FoxCM 媒体分享平台 - 介绍文档

## 项目概述

FoxCM 是一个基于 Python Flask 框架开发的现代媒体分享平台，采用 Apache License Version 2.0 开源协议。该项目提供了一个功能完整的视频分享解决方案，支持用户注册、视频上传、播放、评论、点赞、用户管理等功能，并集成了 WebDav 远程存储支持。

## 核心功能

### 1. 用户系统
- 用户注册与登录
- 个人资料管理
- 头像上传与更新
- 用户主页展示

### 2. 视频管理
- 视频上传（支持 MP4/AVI/MOV 格式）
- 封面图片上传（支持 JPG/PNG）
- 视频播放页面
- 播放次数统计
- 视频搜索功能

### 3. 社交互动
- 视频评论系统
- 评论点赞功能
- 用户主页展示个人视频

### 4. 存储管理
- 本地存储支持
- WebDav 远程存储集成
- 智能存储代理（支持断点续传）

### 5. 后台管理
- 用户管理（删除用户）
- 视频管理（删除视频）
- 系统配置管理

### 6. 高级特性
- 响应式设计
- 实时日志系统（使用 Rich 库）
- 系统配置管理（标题、WebDav 设置）
- 代理文件请求（支持 Range 请求）

## 技术栈

- **核心框架**: Flask
- **前端**: HTML5, CSS3, JavaScript
- **日志系统**: Rich 库（支持彩色输出和详细追踪）
- **数据存储**: JSON 文件（用户数据、视频数据、评论数据）
- **文件处理**: Werkzeug
- **WebDav 集成**: Requests 库
- **用户界面**: Bootstrap（基于模板推断）

## 安装与运行

### 环境要求
- Python 3.7+

### 运行步骤
1. 克隆仓库或下载源代码
2. 创建虚拟环境（推荐）:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate    # Windows
   ```
3. 安装依赖:
   ```bash
   pip install -e .
   ```
4. 运行应用:
   ```bash
   python app.py
   ```
5. 访问：`http://localhost:6544`

### 首次运行
系统会自动创建必要的目录结构：
- `/data`：存储用户、视频和系统数据
- `/static/uploads`：存储上传的视频、封面和头像
- `/templates`：HTML 模板文件

## 配置文件说明

系统配置文件位于 `/data/system.json`，包含以下配置项：

```json
{
  "title": "FoxCM",
  "webdav_video": {
    "enabled": false,
    "url": "https://your-webdav-server/videos/",
    "username": "your-username",
    "password": "your-password"
  },
  "webdav_cover": {
    "enabled": false,
    "url": "https://your-webdav-server/covers/",
    "username": "your-username",
    "password": "your-password"
  }
}
```

## 使用指南

### 普通用户
1. 注册新账号或使用现有账号登录
2. 在"上传"页面提交视频文件和封面
3. 在首页浏览视频或通过搜索查找内容
4. 观看视频并发表评论
5. 访问个人主页管理头像和查看自己的视频

### 管理员
1. 使用管理员账号登录（默认无管理员，需在代码中设置 ADMIN = True）
2. 访问 `/admin` 页面
3. 管理用户（删除账户）
4. 管理视频（删除违规内容）

### WebDav 配置
1. 编辑 `data/system.json`
2. 启用并配置 WebDav 视频和封面存储
3. 重启应用后新上传的文件将自动同步到 WebDav 服务器

## 开源协议

FoxCM 采用 **Apache License Version 2.0** 开源协议，主要特点：

- 允许商业使用
- 允许修改和分发
- 允许专利使用
- 需要保留版权声明
- 提供明确的专利授权
- 不承担作者责任

完整协议内容请访问：[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)

## 贡献指南

欢迎开发者贡献代码！贡献流程：
1. Fork 本项目
2. 创建新分支（`git checkout -b feature/your-feature`）
3. 提交修改
4. 推送分支（`git push origin feature/your-feature`）
5. 创建 Pull Request

## 作者信息
- **开发者**: FoxHome
- **版本**: 1.2.0
- **联系方式**: 项目仓库提交 issue

## 项目优势

1. **轻量级设计**：基于Flask框架，资源占用低
2. **开箱即用**：无需数据库，JSON文件存储数据
3. **扩展性强**：模块化设计便于功能扩展
4. **存储灵活**：支持本地和远程WebDav存储
5. **专业日志**：Rich库提供彩色日志和详细错误追踪
6. **响应式布局**：适配不同设备屏幕

FoxCM 是个人媒体分享和小型视频社区的理想解决方案，结合了易用性、灵活性和可扩展性。