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

## TREE
```txt
./
├── LICENSE
├── README.md
├── app.py
├── data/
│ ├── comments.json
│ ├── foxcm-sp.json
│ ├── system.json
│ └── user.json
├── dependent-installation.sh
├── manifest.json
├── pyproject.toml
├── start.bat
├── start.sh
├── static/
│ ├── Font/
│ │ ├── css/
│ │ │ ├── all.css
│ │ │ ├── all.min.css
│ │ │ ├── brands.css
│ │ │ ├── brands.min.css
│ │ │ ├── fontawesome.css
│ │ │ ├── fontawesome.min.css
│ │ │ ├── regular.css
│ │ │ ├── regular.min.css
│ │ │ ├── solid.css
│ │ │ ├── solid.min.css
│ │ │ ├── svg-with-js.css
│ │ │ ├── svg-with-js.min.css
│ │ │ ├── v4-font-face.css
│ │ │ ├── v4-font-face.min.css
│ │ │ ├── v4-shims.css
│ │ │ ├── v4-shims.min.css
│ │ │ ├── v5-font-face.css
│ │ │ └── v5-font-face.min.css
│ │ ├── js/
│ │ │ ├── all.js
│ │ │ ├── all.min.js
│ │ │ ├── brands.js
│ │ │ ├── brands.min.js
│ │ │ ├── conflict-detection.js
│ │ │ ├── conflict-detection.min.js
│ │ │ ├── fontawesome.js
│ │ │ ├── fontawesome.min.js
│ │ │ ├── regular.js
│ │ │ ├── regular.min.js
│ │ │ ├── solid.js
│ │ │ ├── solid.min.js
│ │ │ ├── v4-shims.js
│ │ │ └── v4-shims.min.js
│ │ ├── less/
│ │ │ ├── _animated.less
│ │ │ ├── _bordered-pulled.less
│ │ │ ├── _core.less
│ │ │ ├── _fixed-width.less
│ │ │ ├── _icons.less
│ │ │ ├── _list.less
│ │ │ ├── _mixins.less
│ │ │ ├── _rotated-flipped.less
│ │ │ ├── _screen-reader.less
│ │ │ ├── _shims.less
│ │ │ ├── _sizing.less
│ │ │ ├── _stacked.less
│ │ │ ├── _variables.less
│ │ │ ├── brands.less
│ │ │ ├── fontawesome.less
│ │ │ ├── regular.less
│ │ │ ├── solid.less
│ │ │ └── v4-shims.less
│ │ ├── metadata/
│ │ │ ├── categories.yml
│ │ │ ├── icon-families.json
│ │ │ ├── icon-families.yml
│ │ │ ├── icons.json
│ │ │ ├── icons.yml
│ │ │ ├── shims.json
│ │ │ ├── shims.yml
│ │ │ └── sponsors.yml
│ │ ├── scss/
│ │ │ ├── _animated.scss
│ │ │ ├── _bordered-pulled.scss
│ │ │ ├── _core.scss
│ │ │ ├── _fixed-width.scss
│ │ │ ├── _functions.scss
│ │ │ ├── _icons.scss
│ │ │ ├── _list.scss
│ │ │ ├── _mixins.scss
│ │ │ ├── _rotated-flipped.scss
│ │ │ ├── _screen-reader.scss
│ │ │ ├── _shims.scss
│ │ │ ├── _sizing.scss
│ │ │ ├── _stacked.scss
│ │ │ ├── _variables.scss
│ │ │ ├── brands.scss
│ │ │ ├── fontawesome.scss
│ │ │ ├── regular.scss
│ │ │ ├── solid.scss
│ │ │ └── v4-shims.scss
│ │ ├── sprites/
│ │ │ ├── brands.svg
│ │ │ ├── regular.svg
│ │ │ └── solid.svg
│ │ ├── svgs/
│ │ │ ├── brands/
│ │ │ │ ├── 42-group.svg
│ │ │ │ ├── 500px.svg
│ │ │ │ ├── accessible-icon.svg
│ │ │ │ ├── accusoft.svg
│ │ │ │ ├── adn.svg
│ │ │ │ ├── adversal.svg
│ │ │ │ ├── affiliatetheme.svg
│ │ │ │ ├── airbnb.svg
│ │ │ │ ├── algolia.svg
│ │ │ │ ├── alipay.svg
│ │ │ │ ├── amazon-pay.svg
│ │ │ │ ├── amazon.svg
│ │ │ │ ├── amilia.svg
│ │ │ │ ├── android.svg
│ │ │ │ ├── angellist.svg
│ │ │ │ ├── angrycreative.svg
│ │ │ │ ├── angular.svg
│ │ │ │ ├── app-store-ios.svg
│ │ │ │ ├── app-store.svg
│ │ │ │ ├── apper.svg
│ │ │ │ ├── apple-pay.svg
│ │ │ │ ├── apple.svg
│ │ │ │ ├── artstation.svg
│ │ │ │ ├── asymmetrik.svg
│ │ │ │ ├── atlassian.svg
│ │ │ │ ├── audible.svg
│ │ │ │ ├── autoprefixer.svg
│ │ │ │ ├── avianex.svg
│ │ │ │ ├── aviato.svg
│ │ │ │ ├── aws.svg
│ │ │ │ ├── bandcamp.svg
│ │ │ │ ├── battle-net.svg
│ │ │ │ ├── behance.svg
│ │ │ │ ├── bilibili.svg
│ │ │ │ ├── bimobject.svg
│ │ │ │ ├── bitbucket.svg
│ │ │ │ ├── bitcoin.svg
│ │ │ │ ├── bity.svg
│ │ │ │ ├── black-tie.svg
│ │ │ │ ├── blackberry.svg
│ │ │ │ ├── blogger-b.svg
│ │ │ │ ├── blogger.svg
│ │ │ │ ├── bluesky.svg
│ │ │ │ ├── bluetooth-b.svg
│ │ │ │ ├── bluetooth.svg
│ │ │ │ ├── bootstrap.svg
│ │ │ │ ├── bots.svg
│ │ │ │ ├── brave-reverse.svg
│ │ │ │ ├── brave.svg
│ │ │ │ ├── btc.svg
│ │ │ │ ├── buffer.svg
│ │ │ │ ├── buromobelexperte.svg
│ │ │ │ ├── buy-n-large.svg
│ │ │ │ ├── buysellads.svg
│ │ │ │ ├── canadian-maple-leaf.svg
│ │ │ │ ├── cc-amazon-pay.svg
│ │ │ │ ├── cc-amex.svg
│ │ │ │ ├── cc-apple-pay.svg
│ │ │ │ ├── cc-diners-club.svg
│ │ │ │ ├── cc-discover.svg
│ │ │ │ ├── cc-jcb.svg
│ │ │ │ ├── cc-mastercard.svg
│ │ │ │ ├── cc-paypal.svg
│ │ │ │ ├── cc-stripe.svg
│ │ │ │ ├── cc-visa.svg
│ │ │ │ ├── centercode.svg
│ │ │ │ ├── centos.svg
│ │ │ │ ├── chrome.svg
│ │ │ │ ├── chromecast.svg
│ │ │ │ ├── cloudflare.svg
│ │ │ │ ├── cloudscale.svg
│ │ │ │ ├── cloudsmith.svg
│ │ │ │ ├── cloudversify.svg
│ │ │ │ ├── cmplid.svg
│ │ │ │ ├── codepen.svg
│ │ │ │ ├── codiepie.svg
│ │ │ │ ├── confluence.svg
│ │ │ │ ├── connectdevelop.svg
│ │ │ │ ├── contao.svg
│ │ │ │ ├── cotton-bureau.svg
│ │ │ │ ├── cpanel.svg
│ │ │ │ ├── creative-commons-by.svg
│ │ │ │ ├── creative-commons-nc-eu.svg
│ │ │ │ ├── creative-commons-nc-jp.svg
│ │ │ │ ├── creative-commons-nc.svg
│ │ │ │ ├── creative-commons-nd.svg
│ │ │ │ ├── creative-commons-pd-alt.svg
│ │ │ │ ├── creative-commons-pd.svg
│ │ │ │ ├── creative-commons-remix.svg
│ │ │ │ ├── creative-commons-sa.svg
│ │ │ │ ├── creative-commons-sampling-plus.svg
│ │ │ │ ├── creative-commons-sampling.svg
│ │ │ │ ├── creative-commons-share.svg
│ │ │ │ ├── creative-commons-zero.svg
│ │ │ │ ├── creative-commons.svg
│ │ │ │ ├── critical-role.svg
│ │ │ │ ├── css.svg
│ │ │ │ ├── css3-alt.svg
│ │ │ │ ├── css3.svg
│ │ │ │ ├── cuttlefish.svg
│ │ │ │ ├── d-and-d-beyond.svg
│ │ │ │ ├── d-and-d.svg
│ │ │ │ ├── dailymotion.svg
│ │ │ │ ├── dart-lang.svg
│ │ │ │ ├── dashcube.svg
│ │ │ │ ├── debian.svg
│ │ │ │ ├── deezer.svg
│ │ │ │ ├── delicious.svg
│ │ │ │ ├── deploydog.svg
│ │ │ │ ├── deskpro.svg
│ │ │ │ ├── dev.svg
│ │ │ │ ├── deviantart.svg
│ │ │ │ ├── dhl.svg
│ │ │ │ ├── diaspora.svg
│ │ │ │ ├── digg.svg
│ │ │ │ ├── digital-ocean.svg
│ │ │ │ ├── discord.svg
│ │ │ │ ├── discourse.svg
│ │ │ │ ├── dochub.svg
│ │ │ │ ├── docker.svg
│ │ │ │ ├── draft2digital.svg
│ │ │ │ ├── dribbble.svg
│ │ │ │ ├── dropbox.svg
│ │ │ │ ├── drupal.svg
│ │ │ │ ├── dyalog.svg
│ │ │ │ ├── earlybirds.svg
│ │ │ │ ├── ebay.svg
│ │ │ │ ├── edge-legacy.svg
│ │ │ │ ├── edge.svg
│ │ │ │ ├── elementor.svg
│ │ │ │ ├── ello.svg
│ │ │ │ ├── ember.svg
│ │ │ │ ├── empire.svg
│ │ │ │ ├── envira.svg
│ │ │ │ ├── erlang.svg
│ │ │ │ ├── ethereum.svg
│ │ │ │ ├── etsy.svg
│ │ │ │ ├── evernote.svg
│ │ │ │ ├── expeditedssl.svg
│ │ │ │ ├── facebook-f.svg
│ │ │ │ ├── facebook-messenger.svg
│ │ │ │ ├── facebook.svg
│ │ │ │ ├── fantasy-flight-games.svg
│ │ │ │ ├── fedex.svg
│ │ │ │ ├── fedora.svg
│ │ │ │ ├── figma.svg
│ │ │ │ ├── files-pinwheel.svg
│ │ │ │ ├── firefox-browser.svg
│ │ │ │ ├── firefox.svg
│ │ │ │ ├── first-order-alt.svg
│ │ │ │ ├── first-order.svg
│ │ │ │ ├── firstdraft.svg
│ │ │ │ ├── flickr.svg
│ │ │ │ ├── flipboard.svg
│ │ │ │ ├── flutter.svg
│ │ │ │ ├── fly.svg
│ │ │ │ ├── font-awesome.svg
│ │ │ │ ├── fonticons-fi.svg
│ │ │ │ ├── fonticons.svg
│ │ │ │ ├── fort-awesome-alt.svg
│ │ │ │ ├── fort-awesome.svg
│ │ │ │ ├── forumbee.svg
│ │ │ │ ├── foursquare.svg
│ │ │ │ ├── free-code-camp.svg
│ │ │ │ ├── freebsd.svg
│ │ │ │ ├── fulcrum.svg
│ │ │ │ ├── galactic-republic.svg
│ │ │ │ ├── galactic-senate.svg
│ │ │ │ ├── get-pocket.svg
│ │ │ │ ├── gg-circle.svg
│ │ │ │ ├── gg.svg
│ │ │ │ ├── git-alt.svg
│ │ │ │ ├── git.svg
│ │ │ │ ├── github-alt.svg
│ │ │ │ ├── github.svg
│ │ │ │ ├── gitkraken.svg
│ │ │ │ ├── gitlab.svg
│ │ │ │ ├── gitter.svg
│ │ │ │ ├── glide-g.svg
│ │ │ │ ├── glide.svg
│ │ │ │ ├── gofore.svg
│ │ │ │ ├── golang.svg
│ │ │ │ ├── goodreads-g.svg
│ │ │ │ ├── goodreads.svg
│ │ │ │ ├── google-drive.svg
│ │ │ │ ├── google-pay.svg
│ │ │ │ ├── google-play.svg
│ │ │ │ ├── google-plus-g.svg
│ │ │ │ ├── google-plus.svg
│ │ │ │ ├── google-scholar.svg
│ │ │ │ ├── google-wallet.svg
│ │ │ │ ├── google.svg
│ │ │ │ ├── gratipay.svg
│ │ │ │ ├── grav.svg
│ │ │ │ ├── gripfire.svg
│ │ │ │ ├── grunt.svg
│ │ │ │ ├── guilded.svg
│ │ │ │ ├── gulp.svg
│ │ │ │ ├── hacker-news.svg
│ │ │ │ ├── hackerrank.svg
│ │ │ │ ├── hashnode.svg
│ │ │ │ ├── hips.svg
│ │ │ │ ├── hire-a-helper.svg
│ │ │ │ ├── hive.svg
│ │ │ │ ├── hooli.svg
│ │ │ │ ├── hornbill.svg
│ │ │ │ ├── hotjar.svg
│ │ │ │ ├── houzz.svg
│ │ │ │ ├── html5.svg
│ │ │ │ ├── hubspot.svg
│ │ │ │ ├── ideal.svg
│ │ │ │ ├── imdb.svg
│ │ │ │ ├── instagram.svg
│ │ │ │ ├── instalod.svg
│ │ │ │ ├── intercom.svg
│ │ │ │ ├── internet-explorer.svg
│ │ │ │ ├── invision.svg
│ │ │ │ ├── ioxhost.svg
│ │ │ │ ├── itch-io.svg
│ │ │ │ ├── itunes-note.svg
│ │ │ │ ├── itunes.svg
│ │ │ │ ├── java.svg
│ │ │ │ ├── jedi-order.svg
│ │ │ │ ├── jenkins.svg
│ │ │ │ ├── jira.svg
│ │ │ │ ├── joget.svg
│ │ │ │ ├── joomla.svg
│ │ │ │ ├── js.svg
│ │ │ │ ├── jsfiddle.svg
│ │ │ │ ├── jxl.svg
│ │ │ │ ├── kaggle.svg
│ │ │ │ ├── keybase.svg
│ │ │ │ ├── keycdn.svg
│ │ │ │ ├── kickstarter-k.svg
│ │ │ │ ├── kickstarter.svg
│ │ │ │ ├── korvue.svg
│ │ │ │ ├── laravel.svg
│ │ │ │ ├── lastfm.svg
│ │ │ │ ├── leanpub.svg
│ │ │ │ ├── less.svg
│ │ │ │ ├── letterboxd.svg
│ │ │ │ ├── line.svg
│ │ │ │ ├── linkedin-in.svg
│ │ │ │ ├── linkedin.svg
│ │ │ │ ├── linode.svg
│ │ │ │ ├── linux.svg
│ │ │ │ ├── lyft.svg
│ │ │ │ ├── magento.svg
│ │ │ │ ├── mailchimp.svg
│ │ │ │ ├── mandalorian.svg
│ │ │ │ ├── markdown.svg
│ │ │ │ ├── mastodon.svg
│ │ │ │ ├── maxcdn.svg
│ │ │ │ ├── mdb.svg
│ │ │ │ ├── medapps.svg
│ │ │ │ ├── medium.svg
│ │ │ │ ├── medrt.svg
│ │ │ │ ├── meetup.svg
│ │ │ │ ├── megaport.svg
│ │ │ │ ├── mendeley.svg
│ │ │ │ ├── meta.svg
│ │ │ │ ├── microblog.svg
│ │ │ │ ├── microsoft.svg
│ │ │ │ ├── mintbit.svg
│ │ │ │ ├── mix.svg
│ │ │ │ ├── mixcloud.svg
│ │ │ │ ├── mixer.svg
│ │ │ │ ├── mizuni.svg
│ │ │ │ ├── modx.svg
│ │ │ │ ├── monero.svg
│ │ │ │ ├── napster.svg
│ │ │ │ ├── neos.svg
│ │ │ │ ├── nfc-directional.svg
│ │ │ │ ├── nfc-symbol.svg
│ │ │ │ ├── nimblr.svg
│ │ │ │ ├── node-js.svg
│ │ │ │ ├── node.svg
│ │ │ │ ├── npm.svg
│ │ │ │ ├── ns8.svg
│ │ │ │ ├── nutritionix.svg
│ │ │ │ ├── octopus-deploy.svg
│ │ │ │ ├── odnoklassniki.svg
│ │ │ │ ├── odysee.svg
│ │ │ │ ├── old-republic.svg
│ │ │ │ ├── opencart.svg
│ │ │ │ ├── openid.svg
│ │ │ │ ├── opensuse.svg
│ │ │ │ ├── opera.svg
│ │ │ │ ├── optin-monster.svg
│ │ │ │ ├── orcid.svg
│ │ │ │ ├── osi.svg
│ │ │ │ ├── padlet.svg
│ │ │ │ ├── page4.svg
│ │ │ │ ├── pagelines.svg
│ │ │ │ ├── palfed.svg
│ │ │ │ ├── patreon.svg
│ │ │ │ ├── paypal.svg
│ │ │ │ ├── perbyte.svg
│ │ │ │ ├── periscope.svg
│ │ │ │ ├── phabricator.svg
│ │ │ │ ├── phoenix-framework.svg
│ │ │ │ ├── phoenix-squadron.svg
│ │ │ │ ├── php.svg
│ │ │ │ ├── pied-piper-alt.svg
│ │ │ │ ├── pied-piper-hat.svg
│ │ │ │ ├── pied-piper-pp.svg
│ │ │ │ ├── pied-piper.svg
│ │ │ │ ├── pinterest-p.svg
│ │ │ │ ├── pinterest.svg
│ │ │ │ ├── pix.svg
│ │ │ │ ├── pixiv.svg
│ │ │ │ ├── playstation.svg
│ │ │ │ ├── product-hunt.svg
│ │ │ │ ├── pushed.svg
│ │ │ │ ├── python.svg
│ │ │ │ ├── qq.svg
│ │ │ │ ├── quinscape.svg
│ │ │ │ ├── quora.svg
│ │ │ │ ├── r-project.svg
│ │ │ │ ├── raspberry-pi.svg
│ │ │ │ ├── ravelry.svg
│ │ │ │ ├── react.svg
│ │ │ │ ├── reacteurope.svg
│ │ │ │ ├── readme.svg
│ │ │ │ ├── rebel.svg
│ │ │ │ ├── red-river.svg
│ │ │ │ ├── reddit-alien.svg
│ │ │ │ ├── reddit.svg
│ │ │ │ ├── redhat.svg
│ │ │ │ ├── renren.svg
│ │ │ │ ├── replyd.svg
│ │ │ │ ├── researchgate.svg
│ │ │ │ ├── resolving.svg
│ │ │ │ ├── rev.svg
│ │ │ │ ├── rocketchat.svg
│ │ │ │ ├── rockrms.svg
│ │ │ │ ├── rust.svg
│ │ │ │ ├── safari.svg
│ │ │ │ ├── salesforce.svg
│ │ │ │ ├── sass.svg
│ │ │ │ ├── schlix.svg
│ │ │ │ ├── screenpal.svg
│ │ │ │ ├── scribd.svg
│ │ │ │ ├── searchengin.svg
│ │ │ │ ├── sellcast.svg
│ │ │ │ ├── sellsy.svg
│ │ │ │ ├── servicestack.svg
│ │ │ │ ├── shirtsinbulk.svg
│ │ │ │ ├── shoelace.svg
│ │ │ │ ├── shopify.svg
│ │ │ │ ├── shopware.svg
│ │ │ │ ├── signal-messenger.svg
│ │ │ │ ├── simplybuilt.svg
│ │ │ │ ├── sistrix.svg
│ │ │ │ ├── sith.svg
│ │ │ │ ├── sitrox.svg
│ │ │ │ ├── sketch.svg
│ │ │ │ ├── skyatlas.svg
│ │ │ │ ├── skype.svg
│ │ │ │ ├── slack.svg
│ │ │ │ ├── slideshare.svg
│ │ │ │ ├── snapchat.svg
│ │ │ │ ├── soundcloud.svg
│ │ │ │ ├── sourcetree.svg
│ │ │ │ ├── space-awesome.svg
│ │ │ │ ├── speakap.svg
│ │ │ │ ├── speaker-deck.svg
│ │ │ │ ├── spotify.svg
│ │ │ │ ├── square-behance.svg
│ │ │ │ ├── square-bluesky.svg
│ │ │ │ ├── square-dribbble.svg
│ │ │ │ ├── square-facebook.svg
│ │ │ │ ├── square-font-awesome-stroke.svg
│ │ │ │ ├── square-font-awesome.svg
│ │ │ │ ├── square-git.svg
│ │ │ │ ├── square-github.svg
│ │ │ │ ├── square-gitlab.svg
│ │ │ │ ├── square-google-plus.svg
│ │ │ │ ├── square-hacker-news.svg
│ │ │ │ ├── square-instagram.svg
│ │ │ │ ├── square-js.svg
│ │ │ │ ├── square-lastfm.svg
│ │ │ │ ├── square-letterboxd.svg
│ │ │ │ ├── square-odnoklassniki.svg
│ │ │ │ ├── square-pied-piper.svg
│ │ │ │ ├── square-pinterest.svg
│ │ │ │ ├── square-reddit.svg
│ │ │ │ ├── square-snapchat.svg
│ │ │ │ ├── square-steam.svg
│ │ │ │ ├── square-threads.svg
│ │ │ │ ├── square-tumblr.svg
│ │ │ │ ├── square-twitter.svg
│ │ │ │ ├── square-upwork.svg
│ │ │ │ ├── square-viadeo.svg
│ │ │ │ ├── square-vimeo.svg
│ │ │ │ ├── square-web-awesome-stroke.svg
│ │ │ │ ├── square-web-awesome.svg
│ │ │ │ ├── square-whatsapp.svg
│ │ │ │ ├── square-x-twitter.svg
│ │ │ │ ├── square-xing.svg
│ │ │ │ ├── square-youtube.svg
│ │ │ │ ├── squarespace.svg
│ │ │ │ ├── stack-exchange.svg
│ │ │ │ ├── stack-overflow.svg
│ │ │ │ ├── stackpath.svg
│ │ │ │ ├── staylinked.svg
│ │ │ │ ├── steam-symbol.svg
│ │ │ │ ├── steam.svg
│ │ │ │ ├── sticker-mule.svg
│ │ │ │ ├── strava.svg
│ │ │ │ ├── stripe-s.svg
│ │ │ │ ├── stripe.svg
│ │ │ │ ├── stubber.svg
│ │ │ │ ├── studiovinari.svg
│ │ │ │ ├── stumbleupon-circle.svg
│ │ │ │ ├── stumbleupon.svg
│ │ │ │ ├── superpowers.svg
│ │ │ │ ├── supple.svg
│ │ │ │ ├── suse.svg
│ │ │ │ ├── swift.svg
│ │ │ │ ├── symfony.svg
│ │ │ │ ├── teamspeak.svg
│ │ │ │ ├── telegram.svg
│ │ │ │ ├── tencent-weibo.svg
│ │ │ │ ├── the-red-yeti.svg
│ │ │ │ ├── themeco.svg
│ │ │ │ ├── themeisle.svg
│ │ │ │ ├── think-peaks.svg
│ │ │ │ ├── threads.svg
│ │ │ │ ├── tiktok.svg
│ │ │ │ ├── trade-federation.svg
│ │ │ │ ├── trello.svg
│ │ │ │ ├── tumblr.svg
│ │ │ │ ├── twitch.svg
│ │ │ │ ├── twitter.svg
│ │ │ │ ├── typo3.svg
│ │ │ │ ├── uber.svg
│ │ │ │ ├── ubuntu.svg
│ │ │ │ ├── uikit.svg
│ │ │ │ ├── umbraco.svg
│ │ │ │ ├── uncharted.svg
│ │ │ │ ├── uniregistry.svg
│ │ │ │ ├── unity.svg
│ │ │ │ ├── unsplash.svg
│ │ │ │ ├── untappd.svg
│ │ │ │ ├── ups.svg
│ │ │ │ ├── upwork.svg
│ │ │ │ ├── usb.svg
│ │ │ │ ├── usps.svg
│ │ │ │ ├── ussunnah.svg
│ │ │ │ ├── vaadin.svg
│ │ │ │ ├── viacoin.svg
│ │ │ │ ├── viadeo.svg
│ │ │ │ ├── viber.svg
│ │ │ │ ├── vimeo-v.svg
│ │ │ │ ├── vimeo.svg
│ │ │ │ ├── vine.svg
│ │ │ │ ├── vk.svg
│ │ │ │ ├── vnv.svg
│ │ │ │ ├── vuejs.svg
│ │ │ │ ├── watchman-monitoring.svg
│ │ │ │ ├── waze.svg
│ │ │ │ ├── web-awesome.svg
│ │ │ │ ├── webflow.svg
│ │ │ │ ├── weebly.svg
│ │ │ │ ├── weibo.svg
│ │ │ │ ├── weixin.svg
│ │ │ │ ├── whatsapp.svg
│ │ │ │ ├── whmcs.svg
│ │ │ │ ├── wikipedia-w.svg
│ │ │ │ ├── windows.svg
│ │ │ │ ├── wirsindhandwerk.svg
│ │ │ │ ├── wix.svg
│ │ │ │ ├── wizards-of-the-coast.svg
│ │ │ │ ├── wodu.svg
│ │ │ │ ├── wolf-pack-battalion.svg
│ │ │ │ ├── wordpress-simple.svg
│ │ │ │ ├── wordpress.svg
│ │ │ │ ├── wpbeginner.svg
│ │ │ │ ├── wpexplorer.svg
│ │ │ │ ├── wpforms.svg
│ │ │ │ ├── wpressr.svg
│ │ │ │ ├── x-twitter.svg
│ │ │ │ ├── xbox.svg
│ │ │ │ ├── xing.svg
│ │ │ │ ├── y-combinator.svg
│ │ │ │ ├── yahoo.svg
│ │ │ │ ├── yammer.svg
│ │ │ │ ├── yandex-international.svg
│ │ │ │ ├── yandex.svg
│ │ │ │ ├── yarn.svg
│ │ │ │ ├── yelp.svg
│ │ │ │ ├── yoast.svg
│ │ │ │ ├── youtube.svg
│ │ │ │ └── zhihu.svg
│ │ │ ├── regular/
│ │ │ │ ├── address-book.svg
│ │ │ │ ├── address-card.svg
│ │ │ │ ├── bell-slash.svg
│ │ │ │ ├── bell.svg
│ │ │ │ ├── bookmark.svg
│ │ │ │ ├── building.svg
│ │ │ │ ├── calendar-check.svg
│ │ │ │ ├── calendar-days.svg
│ │ │ │ ├── calendar-minus.svg
│ │ │ │ ├── calendar-plus.svg
│ │ │ │ ├── calendar-xmark.svg
│ │ │ │ ├── calendar.svg
│ │ │ │ ├── chart-bar.svg
│ │ │ │ ├── chess-bishop.svg
│ │ │ │ ├── chess-king.svg
│ │ │ │ ├── chess-knight.svg
│ │ │ │ ├── chess-pawn.svg
│ │ │ │ ├── chess-queen.svg
│ │ │ │ ├── chess-rook.svg
│ │ │ │ ├── circle-check.svg
│ │ │ │ ├── circle-dot.svg
│ │ │ │ ├── circle-down.svg
│ │ │ │ ├── circle-left.svg
│ │ │ │ ├── circle-pause.svg
│ │ │ │ ├── circle-play.svg
│ │ │ │ ├── circle-question.svg
│ │ │ │ ├── circle-right.svg
│ │ │ │ ├── circle-stop.svg
│ │ │ │ ├── circle-up.svg
│ │ │ │ ├── circle-user.svg
│ │ │ │ ├── circle-xmark.svg
│ │ │ │ ├── circle.svg
│ │ │ │ ├── clipboard.svg
│ │ │ │ ├── clock.svg
│ │ │ │ ├── clone.svg
│ │ │ │ ├── closed-captioning.svg
│ │ │ │ ├── comment-dots.svg
│ │ │ │ ├── comment.svg
│ │ │ │ ├── comments.svg
│ │ │ │ ├── compass.svg
│ │ │ │ ├── copy.svg
│ │ │ │ ├── copyright.svg
│ │ │ │ ├── credit-card.svg
│ │ │ │ ├── envelope-open.svg
│ │ │ │ ├── envelope.svg
│ │ │ │ ├── eye-slash.svg
│ │ │ │ ├── eye.svg
│ │ │ │ ├── face-angry.svg
│ │ │ │ ├── face-dizzy.svg
│ │ │ │ ├── face-flushed.svg
│ │ │ │ ├── face-frown-open.svg
│ │ │ │ ├── face-frown.svg
│ │ │ │ ├── face-grimace.svg
│ │ │ │ ├── face-grin-beam-sweat.svg
│ │ │ │ ├── face-grin-beam.svg
│ │ │ │ ├── face-grin-hearts.svg
│ │ │ │ ├── face-grin-squint-tears.svg
│ │ │ │ ├── face-grin-squint.svg
│ │ │ │ ├── face-grin-stars.svg
│ │ │ │ ├── face-grin-tears.svg
│ │ │ │ ├── face-grin-tongue-squint.svg
│ │ │ │ ├── face-grin-tongue-wink.svg
│ │ │ │ ├── face-grin-tongue.svg
│ │ │ │ ├── face-grin-wide.svg
│ │ │ │ ├── face-grin-wink.svg
│ │ │ │ ├── face-grin.svg
│ │ │ │ ├── face-kiss-beam.svg
│ │ │ │ ├── face-kiss-wink-heart.svg
│ │ │ │ ├── face-kiss.svg
│ │ │ │ ├── face-laugh-beam.svg
│ │ │ │ ├── face-laugh-squint.svg
│ │ │ │ ├── face-laugh-wink.svg
│ │ │ │ ├── face-laugh.svg
│ │ │ │ ├── face-meh-blank.svg
│ │ │ │ ├── face-meh.svg
│ │ │ │ ├── face-rolling-eyes.svg
│ │ │ │ ├── face-sad-cry.svg
│ │ │ │ ├── face-sad-tear.svg
│ │ │ │ ├── face-smile-beam.svg
│ │ │ │ ├── face-smile-wink.svg
│ │ │ │ ├── face-smile.svg
│ │ │ │ ├── face-surprise.svg
│ │ │ │ ├── face-tired.svg
│ │ │ │ ├── file-audio.svg
│ │ │ │ ├── file-code.svg
│ │ │ │ ├── file-excel.svg
│ │ │ │ ├── file-image.svg
│ │ │ │ ├── file-lines.svg
│ │ │ │ ├── file-pdf.svg
│ │ │ │ ├── file-powerpoint.svg
│ │ │ │ ├── file-video.svg
│ │ │ │ ├── file-word.svg
│ │ │ │ ├── file-zipper.svg
│ │ │ │ ├── file.svg
│ │ │ │ ├── flag.svg
│ │ │ │ ├── floppy-disk.svg
│ │ │ │ ├── folder-closed.svg
│ │ │ │ ├── folder-open.svg
│ │ │ │ ├── folder.svg
│ │ │ │ ├── font-awesome.svg
│ │ │ │ ├── futbol.svg
│ │ │ │ ├── gem.svg
│ │ │ │ ├── hand-back-fist.svg
│ │ │ │ ├── hand-lizard.svg
│ │ │ │ ├── hand-peace.svg
│ │ │ │ ├── hand-point-down.svg
│ │ │ │ ├── hand-point-left.svg
│ │ │ │ ├── hand-point-right.svg
│ │ │ │ ├── hand-point-up.svg
│ │ │ │ ├── hand-pointer.svg
│ │ │ │ ├── hand-scissors.svg
│ │ │ │ ├── hand-spock.svg
│ │ │ │ ├── hand.svg
│ │ │ │ ├── handshake.svg
│ │ │ │ ├── hard-drive.svg
│ │ │ │ ├── heart.svg
│ │ │ │ ├── hospital.svg
│ │ │ │ ├── hourglass-half.svg
│ │ │ │ ├── hourglass.svg
│ │ │ │ ├── id-badge.svg
│ │ │ │ ├── id-card.svg
│ │ │ │ ├── image.svg
│ │ │ │ ├── images.svg
│ │ │ │ ├── keyboard.svg
│ │ │ │ ├── lemon.svg
│ │ │ │ ├── life-ring.svg
│ │ │ │ ├── lightbulb.svg
│ │ │ │ ├── map.svg
│ │ │ │ ├── message.svg
│ │ │ │ ├── money-bill-1.svg
│ │ │ │ ├── moon.svg
│ │ │ │ ├── newspaper.svg
│ │ │ │ ├── note-sticky.svg
│ │ │ │ ├── object-group.svg
│ │ │ │ ├── object-ungroup.svg
│ │ │ │ ├── paper-plane.svg
│ │ │ │ ├── paste.svg
│ │ │ │ ├── pen-to-square.svg
│ │ │ │ ├── rectangle-list.svg
│ │ │ │ ├── rectangle-xmark.svg
│ │ │ │ ├── registered.svg
│ │ │ │ ├── share-from-square.svg
│ │ │ │ ├── snowflake.svg
│ │ │ │ ├── square-caret-down.svg
│ │ │ │ ├── square-caret-left.svg
│ │ │ │ ├── square-caret-right.svg
│ │ │ │ ├── square-caret-up.svg
│ │ │ │ ├── square-check.svg
│ │ │ │ ├── square-full.svg
│ │ │ │ ├── square-minus.svg
│ │ │ │ ├── square-plus.svg
│ │ │ │ ├── square.svg
│ │ │ │ ├── star-half-stroke.svg
│ │ │ │ ├── star-half.svg
│ │ │ │ ├── star.svg
│ │ │ │ ├── sun.svg
│ │ │ │ ├── thumbs-down.svg
│ │ │ │ ├── thumbs-up.svg
│ │ │ │ ├── trash-can.svg
│ │ │ │ ├── user.svg
│ │ │ │ ├── window-maximize.svg
│ │ │ │ ├── window-minimize.svg
│ │ │ │ └── window-restore.svg
│ │ │ └── solid/
│ │ │     ├── 0.svg
│ │ │     ├── 1.svg
│ │ │     ├── 2.svg
│ │ │     ├── 3.svg
│ │ │     ├── 4.svg
│ │ │     ├── 5.svg
│ │ │     ├── 6.svg
│ │ │     ├── 7.svg
│ │ │     ├── 8.svg
│ │ │     ├── 9.svg
│ │ │     ├── a.svg
│ │ │     ├── address-book.svg
│ │ │     ├── address-card.svg
│ │ │     ├── align-center.svg
│ │ │     ├── align-justify.svg
│ │ │     ├── align-left.svg
│ │ │     ├── align-right.svg
│ │ │     ├── anchor-circle-check.svg
│ │ │     ├── anchor-circle-exclamation.svg
│ │ │     ├── anchor-circle-xmark.svg
│ │ │     ├── anchor-lock.svg
│ │ │     ├── anchor.svg
│ │ │     ├── angle-down.svg
│ │ │     ├── angle-left.svg
│ │ │     ├── angle-right.svg
│ │ │     ├── angle-up.svg
│ │ │     ├── angles-down.svg
│ │ │     ├── angles-left.svg
│ │ │     ├── angles-right.svg
│ │ │     ├── angles-up.svg
│ │ │     ├── ankh.svg
│ │ │     ├── apple-whole.svg
│ │ │     ├── archway.svg
│ │ │     ├── arrow-down-1-9.svg
│ │ │     ├── arrow-down-9-1.svg
│ │ │     ├── arrow-down-a-z.svg
│ │ │     ├── arrow-down-long.svg
│ │ │     ├── arrow-down-short-wide.svg
│ │ │     ├── arrow-down-up-across-line.svg
│ │ │     ├── arrow-down-up-lock.svg
│ │ │     ├── arrow-down-wide-short.svg
│ │ │     ├── arrow-down-z-a.svg
│ │ │     ├── arrow-down.svg
│ │ │     ├── arrow-left-long.svg
│ │ │     ├── arrow-left.svg
│ │ │     ├── arrow-pointer.svg
│ │ │     ├── arrow-right-arrow-left.svg
│ │ │     ├── arrow-right-from-bracket.svg
│ │ │     ├── arrow-right-long.svg
│ │ │     ├── arrow-right-to-bracket.svg
│ │ │     ├── arrow-right-to-city.svg
│ │ │     ├── arrow-right.svg
│ │ │     ├── arrow-rotate-left.svg
│ │ │     ├── arrow-rotate-right.svg
│ │ │     ├── arrow-trend-down.svg
│ │ │     ├── arrow-trend-up.svg
│ │ │     ├── arrow-turn-down.svg
│ │ │     ├── arrow-turn-up.svg
│ │ │     ├── arrow-up-1-9.svg
│ │ │     ├── arrow-up-9-1.svg
│ │ │     ├── arrow-up-a-z.svg
│ │ │     ├── arrow-up-from-bracket.svg
│ │ │     ├── arrow-up-from-ground-water.svg
│ │ │     ├── arrow-up-from-water-pump.svg
│ │ │     ├── arrow-up-long.svg
│ │ │     ├── arrow-up-right-dots.svg
│ │ │     ├── arrow-up-right-from-square.svg
│ │ │     ├── arrow-up-short-wide.svg
│ │ │     ├── arrow-up-wide-short.svg
│ │ │     ├── arrow-up-z-a.svg
│ │ │     ├── arrow-up.svg
│ │ │     ├── arrows-down-to-line.svg
│ │ │     ├── arrows-down-to-people.svg
│ │ │     ├── arrows-left-right-to-line.svg
│ │ │     ├── arrows-left-right.svg
│ │ │     ├── arrows-rotate.svg
│ │ │     ├── arrows-spin.svg
│ │ │     ├── arrows-split-up-and-left.svg
│ │ │     ├── arrows-to-circle.svg
│ │ │     ├── arrows-to-dot.svg
│ │ │     ├── arrows-to-eye.svg
│ │ │     ├── arrows-turn-right.svg
│ │ │     ├── arrows-turn-to-dots.svg
│ │ │     ├── arrows-up-down-left-right.svg
│ │ │     ├── arrows-up-down.svg
│ │ │     ├── arrows-up-to-line.svg
│ │ │     ├── asterisk.svg
│ │ │     ├── at.svg
│ │ │     ├── atom.svg
│ │ │     ├── audio-description.svg
│ │ │     ├── austral-sign.svg
│ │ │     ├── award.svg
│ │ │     ├── b.svg
│ │ │     ├── baby-carriage.svg
│ │ │     ├── baby.svg
│ │ │     ├── backward-fast.svg
│ │ │     ├── backward-step.svg
│ │ │     ├── backward.svg
│ │ │     ├── bacon.svg
│ │ │     ├── bacteria.svg
│ │ │     ├── bacterium.svg
│ │ │     ├── bag-shopping.svg
│ │ │     ├── bahai.svg
│ │ │     ├── baht-sign.svg
│ │ │     ├── ban-smoking.svg
│ │ │     ├── ban.svg
│ │ │     ├── bandage.svg
│ │ │     ├── bangladeshi-taka-sign.svg
│ │ │     ├── barcode.svg
│ │ │     ├── bars-progress.svg
│ │ │     ├── bars-staggered.svg
│ │ │     ├── bars.svg
│ │ │     ├── baseball-bat-ball.svg
│ │ │     ├── baseball.svg
│ │ │     ├── basket-shopping.svg
│ │ │     ├── basketball.svg
│ │ │     ├── bath.svg
│ │ │     ├── battery-empty.svg
│ │ │     ├── battery-full.svg
│ │ │     ├── battery-half.svg
│ │ │     ├── battery-quarter.svg
│ │ │     ├── battery-three-quarters.svg
│ │ │     ├── bed-pulse.svg
│ │ │     ├── bed.svg
│ │ │     ├── beer-mug-empty.svg
│ │ │     ├── bell-concierge.svg
│ │ │     ├── bell-slash.svg
│ │ │     ├── bell.svg
│ │ │     ├── bezier-curve.svg
│ │ │     ├── bicycle.svg
│ │ │     ├── binoculars.svg
│ │ │     ├── biohazard.svg
│ │ │     ├── bitcoin-sign.svg
│ │ │     ├── blender-phone.svg
│ │ │     ├── blender.svg
│ │ │     ├── blog.svg
│ │ │     ├── bold.svg
│ │ │     ├── bolt-lightning.svg
│ │ │     ├── bolt.svg
│ │ │     ├── bomb.svg
│ │ │     ├── bone.svg
│ │ │     ├── bong.svg
│ │ │     ├── book-atlas.svg
│ │ │     ├── book-bible.svg
│ │ │     ├── book-bookmark.svg
│ │ │     ├── book-journal-whills.svg
│ │ │     ├── book-medical.svg
│ │ │     ├── book-open-reader.svg
│ │ │     ├── book-open.svg
│ │ │     ├── book-quran.svg
│ │ │     ├── book-skull.svg
│ │ │     ├── book-tanakh.svg
│ │ │     ├── book.svg
│ │ │     ├── bookmark.svg
│ │ │     ├── border-all.svg
│ │ │     ├── border-none.svg
│ │ │     ├── border-top-left.svg
│ │ │     ├── bore-hole.svg
│ │ │     ├── bottle-droplet.svg
│ │ │     ├── bottle-water.svg
│ │ │     ├── bowl-food.svg
│ │ │     ├── bowl-rice.svg
│ │ │     ├── bowling-ball.svg
│ │ │     ├── box-archive.svg
│ │ │     ├── box-open.svg
│ │ │     ├── box-tissue.svg
│ │ │     ├── box.svg
│ │ │     ├── boxes-packing.svg
│ │ │     ├── boxes-stacked.svg
│ │ │     ├── braille.svg
│ │ │     ├── brain.svg
│ │ │     ├── brazilian-real-sign.svg
│ │ │     ├── bread-slice.svg
│ │ │     ├── bridge-circle-check.svg
│ │ │     ├── bridge-circle-exclamation.svg
│ │ │     ├── bridge-circle-xmark.svg
│ │ │     ├── bridge-lock.svg
│ │ │     ├── bridge-water.svg
│ │ │     ├── bridge.svg
│ │ │     ├── briefcase-medical.svg
│ │ │     ├── briefcase.svg
│ │ │     ├── broom-ball.svg
│ │ │     ├── broom.svg
│ │ │     ├── brush.svg
│ │ │     ├── bucket.svg
│ │ │     ├── bug-slash.svg
│ │ │     ├── bug.svg
│ │ │     ├── bugs.svg
│ │ │     ├── building-circle-arrow-right.svg
│ │ │     ├── building-circle-check.svg
│ │ │     ├── building-circle-exclamation.svg
│ │ │     ├── building-circle-xmark.svg
│ │ │     ├── building-columns.svg
│ │ │     ├── building-flag.svg
│ │ │     ├── building-lock.svg
│ │ │     ├── building-ngo.svg
│ │ │     ├── building-shield.svg
│ │ │     ├── building-un.svg
│ │ │     ├── building-user.svg
│ │ │     ├── building-wheat.svg
│ │ │     ├── building.svg
│ │ │     ├── bullhorn.svg
│ │ │     ├── bullseye.svg
│ │ │     ├── burger.svg
│ │ │     ├── burst.svg
│ │ │     ├── bus-simple.svg
│ │ │     ├── bus.svg
│ │ │     ├── business-time.svg
│ │ │     ├── c.svg
│ │ │     ├── cable-car.svg
│ │ │     ├── cake-candles.svg
│ │ │     ├── calculator.svg
│ │ │     ├── calendar-check.svg
│ │ │     ├── calendar-day.svg
│ │ │     ├── calendar-days.svg
│ │ │     ├── calendar-minus.svg
│ │ │     ├── calendar-plus.svg
│ │ │     ├── calendar-week.svg
│ │ │     ├── calendar-xmark.svg
│ │ │     ├── calendar.svg
│ │ │     ├── camera-retro.svg
│ │ │     ├── camera-rotate.svg
│ │ │     ├── camera.svg
│ │ │     ├── campground.svg
│ │ │     ├── candy-cane.svg
│ │ │     ├── cannabis.svg
│ │ │     ├── capsules.svg
│ │ │     ├── car-battery.svg
│ │ │     ├── car-burst.svg
│ │ │     ├── car-on.svg
│ │ │     ├── car-rear.svg
│ │ │     ├── car-side.svg
│ │ │     ├── car-tunnel.svg
│ │ │     ├── car.svg
│ │ │     ├── caravan.svg
│ │ │     ├── caret-down.svg
│ │ │     ├── caret-left.svg
│ │ │     ├── caret-right.svg
│ │ │     ├── caret-up.svg
│ │ │     ├── carrot.svg
│ │ │     ├── cart-arrow-down.svg
│ │ │     ├── cart-flatbed-suitcase.svg
│ │ │     ├── cart-flatbed.svg
│ │ │     ├── cart-plus.svg
│ │ │     ├── cart-shopping.svg
│ │ │     ├── cash-register.svg
│ │ │     ├── cat.svg
│ │ │     ├── cedi-sign.svg
│ │ │     ├── cent-sign.svg
│ │ │     ├── certificate.svg
│ │ │     ├── chair.svg
│ │ │     ├── chalkboard-user.svg
│ │ │     ├── chalkboard.svg
│ │ │     ├── champagne-glasses.svg
│ │ │     ├── charging-station.svg
│ │ │     ├── chart-area.svg
│ │ │     ├── chart-bar.svg
│ │ │     ├── chart-column.svg
│ │ │     ├── chart-diagram.svg
│ │ │     ├── chart-gantt.svg
│ │ │     ├── chart-line.svg
│ │ │     ├── chart-pie.svg
│ │ │     ├── chart-simple.svg
│ │ │     ├── check-double.svg
│ │ │     ├── check-to-slot.svg
│ │ │     ├── check.svg
│ │ │     ├── cheese.svg
│ │ │     ├── chess-bishop.svg
│ │ │     ├── chess-board.svg
│ │ │     ├── chess-king.svg
│ │ │     ├── chess-knight.svg
│ │ │     ├── chess-pawn.svg
│ │ │     ├── chess-queen.svg
│ │ │     ├── chess-rook.svg
│ │ │     ├── chess.svg
│ │ │     ├── chevron-down.svg
│ │ │     ├── chevron-left.svg
│ │ │     ├── chevron-right.svg
│ │ │     ├── chevron-up.svg
│ │ │     ├── child-combatant.svg
│ │ │     ├── child-dress.svg
│ │ │     ├── child-reaching.svg
│ │ │     ├── child.svg
│ │ │     ├── children.svg
│ │ │     ├── church.svg
│ │ │     ├── circle-arrow-down.svg
│ │ │     ├── circle-arrow-left.svg
│ │ │     ├── circle-arrow-right.svg
│ │ │     ├── circle-arrow-up.svg
│ │ │     ├── circle-check.svg
│ │ │     ├── circle-chevron-down.svg
│ │ │     ├── circle-chevron-left.svg
│ │ │     ├── circle-chevron-right.svg
│ │ │     ├── circle-chevron-up.svg
│ │ │     ├── circle-dollar-to-slot.svg
│ │ │     ├── circle-dot.svg
│ │ │     ├── circle-down.svg
│ │ │     ├── circle-exclamation.svg
│ │ │     ├── circle-h.svg
│ │ │     ├── circle-half-stroke.svg
│ │ │     ├── circle-info.svg
│ │ │     ├── circle-left.svg
│ │ │     ├── circle-minus.svg
│ │ │     ├── circle-nodes.svg
│ │ │     ├── circle-notch.svg
│ │ │     ├── circle-pause.svg
│ │ │     ├── circle-play.svg
│ │ │     ├── circle-plus.svg
│ │ │     ├── circle-question.svg
│ │ │     ├── circle-radiation.svg
│ │ │     ├── circle-right.svg
│ │ │     ├── circle-stop.svg
│ │ │     ├── circle-up.svg
│ │ │     ├── circle-user.svg
│ │ │     ├── circle-xmark.svg
│ │ │     ├── circle.svg
│ │ │     ├── city.svg
│ │ │     ├── clapperboard.svg
│ │ │     ├── clipboard-check.svg
│ │ │     ├── clipboard-list.svg
│ │ │     ├── clipboard-question.svg
│ │ │     ├── clipboard-user.svg
│ │ │     ├── clipboard.svg
│ │ │     ├── clock-rotate-left.svg
│ │ │     ├── clock.svg
│ │ │     ├── clone.svg
│ │ │     ├── closed-captioning.svg
│ │ │     ├── cloud-arrow-down.svg
│ │ │     ├── cloud-arrow-up.svg
│ │ │     ├── cloud-bolt.svg
│ │ │     ├── cloud-meatball.svg
│ │ │     ├── cloud-moon-rain.svg
│ │ │     ├── cloud-moon.svg
│ │ │     ├── cloud-rain.svg
│ │ │     ├── cloud-showers-heavy.svg
│ │ │     ├── cloud-showers-water.svg
│ │ │     ├── cloud-sun-rain.svg
│ │ │     ├── cloud-sun.svg
│ │ │     ├── cloud.svg
│ │ │     ├── clover.svg
│ │ │     ├── code-branch.svg
│ │ │     ├── code-commit.svg
│ │ │     ├── code-compare.svg
│ │ │     ├── code-fork.svg
│ │ │     ├── code-merge.svg
│ │ │     ├── code-pull-request.svg
│ │ │     ├── code.svg
│ │ │     ├── coins.svg
│ │ │     ├── colon-sign.svg
│ │ │     ├── comment-dollar.svg
│ │ │     ├── comment-dots.svg
│ │ │     ├── comment-medical.svg
│ │ │     ├── comment-nodes.svg
│ │ │     ├── comment-slash.svg
│ │ │     ├── comment-sms.svg
│ │ │     ├── comment.svg
│ │ │     ├── comments-dollar.svg
│ │ │     ├── comments.svg
│ │ │     ├── compact-disc.svg
│ │ │     ├── compass-drafting.svg
│ │ │     ├── compass.svg
│ │ │     ├── compress.svg
│ │ │     ├── computer-mouse.svg
│ │ │     ├── computer.svg
│ │ │     ├── cookie-bite.svg
│ │ │     ├── cookie.svg
│ │ │     ├── copy.svg
│ │ │     ├── copyright.svg
│ │ │     ├── couch.svg
│ │ │     ├── cow.svg
│ │ │     ├── credit-card.svg
│ │ │     ├── crop-simple.svg
│ │ │     ├── crop.svg
│ │ │     ├── cross.svg
│ │ │     ├── crosshairs.svg
│ │ │     ├── crow.svg
│ │ │     ├── crown.svg
│ │ │     ├── crutch.svg
│ │ │     ├── cruzeiro-sign.svg
│ │ │     ├── cube.svg
│ │ │     ├── cubes-stacked.svg
│ │ │     ├── cubes.svg
│ │ │     ├── d.svg
│ │ │     ├── database.svg
│ │ │     ├── delete-left.svg
│ │ │     ├── democrat.svg
│ │ │     ├── desktop.svg
│ │ │     ├── dharmachakra.svg
│ │ │     ├── diagram-next.svg
│ │ │     ├── diagram-predecessor.svg
│ │ │     ├── diagram-project.svg
│ │ │     ├── diagram-successor.svg
│ │ │     ├── diamond-turn-right.svg
│ │ │     ├── diamond.svg
│ │ │     ├── dice-d20.svg
│ │ │     ├── dice-d6.svg
│ │ │     ├── dice-five.svg
│ │ │     ├── dice-four.svg
│ │ │     ├── dice-one.svg
│ │ │     ├── dice-six.svg
│ │ │     ├── dice-three.svg
│ │ │     ├── dice-two.svg
│ │ │     ├── dice.svg
│ │ │     ├── disease.svg
│ │ │     ├── display.svg
│ │ │     ├── divide.svg
│ │ │     ├── dna.svg
│ │ │     ├── dog.svg
│ │ │     ├── dollar-sign.svg
│ │ │     ├── dolly.svg
│ │ │     ├── dong-sign.svg
│ │ │     ├── door-closed.svg
│ │ │     ├── door-open.svg
│ │ │     ├── dove.svg
│ │ │     ├── down-left-and-up-right-to-center.svg
│ │ │     ├── down-long.svg
│ │ │     ├── download.svg
│ │ │     ├── dragon.svg
│ │ │     ├── draw-polygon.svg
│ │ │     ├── droplet-slash.svg
│ │ │     ├── droplet.svg
│ │ │     ├── drum-steelpan.svg
│ │ │     ├── drum.svg
│ │ │     ├── drumstick-bite.svg
│ │ │     ├── dumbbell.svg
│ │ │     ├── dumpster-fire.svg
│ │ │     ├── dumpster.svg
│ │ │     ├── dungeon.svg
│ │ │     ├── e.svg
│ │ │     ├── ear-deaf.svg
│ │ │     ├── ear-listen.svg
│ │ │     ├── earth-africa.svg
│ │ │     ├── earth-americas.svg
│ │ │     ├── earth-asia.svg
│ │ │     ├── earth-europe.svg
│ │ │     ├── earth-oceania.svg
│ │ │     ├── egg.svg
│ │ │     ├── eject.svg
│ │ │     ├── elevator.svg
│ │ │     ├── ellipsis-vertical.svg
│ │ │     ├── ellipsis.svg
│ │ │     ├── envelope-circle-check.svg
│ │ │     ├── envelope-open-text.svg
│ │ │     ├── envelope-open.svg
│ │ │     ├── envelope.svg
│ │ │     ├── envelopes-bulk.svg
│ │ │     ├── equals.svg
│ │ │     ├── eraser.svg
│ │ │     ├── ethernet.svg
│ │ │     ├── euro-sign.svg
│ │ │     ├── exclamation.svg
│ │ │     ├── expand.svg
│ │ │     ├── explosion.svg
│ │ │     ├── eye-dropper.svg
│ │ │     ├── eye-low-vision.svg
│ │ │     ├── eye-slash.svg
│ │ │     ├── eye.svg
│ │ │     ├── f.svg
│ │ │     ├── face-angry.svg
│ │ │     ├── face-dizzy.svg
│ │ │     ├── face-flushed.svg
│ │ │     ├── face-frown-open.svg
│ │ │     ├── face-frown.svg
│ │ │     ├── face-grimace.svg
│ │ │     ├── face-grin-beam-sweat.svg
│ │ │     ├── face-grin-beam.svg
│ │ │     ├── face-grin-hearts.svg
│ │ │     ├── face-grin-squint-tears.svg
│ │ │     ├── face-grin-squint.svg
│ │ │     ├── face-grin-stars.svg
│ │ │     ├── face-grin-tears.svg
│ │ │     ├── face-grin-tongue-squint.svg
│ │ │     ├── face-grin-tongue-wink.svg
│ │ │     ├── face-grin-tongue.svg
│ │ │     ├── face-grin-wide.svg
│ │ │     ├── face-grin-wink.svg
│ │ │     ├── face-grin.svg
│ │ │     ├── face-kiss-beam.svg
│ │ │     ├── face-kiss-wink-heart.svg
│ │ │     ├── face-kiss.svg
│ │ │     ├── face-laugh-beam.svg
│ │ │     ├── face-laugh-squint.svg
│ │ │     ├── face-laugh-wink.svg
│ │ │     ├── face-laugh.svg
│ │ │     ├── face-meh-blank.svg
│ │ │     ├── face-meh.svg
│ │ │     ├── face-rolling-eyes.svg
│ │ │     ├── face-sad-cry.svg
│ │ │     ├── face-sad-tear.svg
│ │ │     ├── face-smile-beam.svg
│ │ │     ├── face-smile-wink.svg
│ │ │     ├── face-smile.svg
│ │ │     ├── face-surprise.svg
│ │ │     ├── face-tired.svg
│ │ │     ├── fan.svg
│ │ │     ├── faucet-drip.svg
│ │ │     ├── faucet.svg
│ │ │     ├── fax.svg
│ │ │     ├── feather-pointed.svg
│ │ │     ├── feather.svg
│ │ │     ├── ferry.svg
│ │ │     ├── file-arrow-down.svg
│ │ │     ├── file-arrow-up.svg
│ │ │     ├── file-audio.svg
│ │ │     ├── file-circle-check.svg
│ │ │     ├── file-circle-exclamation.svg
│ │ │     ├── file-circle-minus.svg
│ │ │     ├── file-circle-plus.svg
│ │ │     ├── file-circle-question.svg
│ │ │     ├── file-circle-xmark.svg
│ │ │     ├── file-code.svg
│ │ │     ├── file-contract.svg
│ │ │     ├── file-csv.svg
│ │ │     ├── file-excel.svg
│ │ │     ├── file-export.svg
│ │ │     ├── file-fragment.svg
│ │ │     ├── file-half-dashed.svg
│ │ │     ├── file-image.svg
│ │ │     ├── file-import.svg
│ │ │     ├── file-invoice-dollar.svg
│ │ │     ├── file-invoice.svg
│ │ │     ├── file-lines.svg
│ │ │     ├── file-medical.svg
│ │ │     ├── file-pdf.svg
│ │ │     ├── file-pen.svg
│ │ │     ├── file-powerpoint.svg
│ │ │     ├── file-prescription.svg
│ │ │     ├── file-shield.svg
│ │ │     ├── file-signature.svg
│ │ │     ├── file-video.svg
│ │ │     ├── file-waveform.svg
│ │ │     ├── file-word.svg
│ │ │     ├── file-zipper.svg
│ │ │     ├── file.svg
│ │ │     ├── fill-drip.svg
│ │ │     ├── fill.svg
│ │ │     ├── film.svg
│ │ │     ├── filter-circle-dollar.svg
│ │ │     ├── filter-circle-xmark.svg
│ │ │     ├── filter.svg
│ │ │     ├── fingerprint.svg
│ │ │     ├── fire-burner.svg
│ │ │     ├── fire-extinguisher.svg
│ │ │     ├── fire-flame-curved.svg
│ │ │     ├── fire-flame-simple.svg
│ │ │     ├── fire.svg
│ │ │     ├── fish-fins.svg
│ │ │     ├── fish.svg
│ │ │     ├── flag-checkered.svg
│ │ │     ├── flag-usa.svg
│ │ │     ├── flag.svg
│ │ │     ├── flask-vial.svg
│ │ │     ├── flask.svg
│ │ │     ├── floppy-disk.svg
│ │ │     ├── florin-sign.svg
│ │ │     ├── folder-closed.svg
│ │ │     ├── folder-minus.svg
│ │ │     ├── folder-open.svg
│ │ │     ├── folder-plus.svg
│ │ │     ├── folder-tree.svg
│ │ │     ├── folder.svg
│ │ │     ├── font-awesome.svg
│ │ │     ├── font.svg
│ │ │     ├── football.svg
│ │ │     ├── forward-fast.svg
│ │ │     ├── forward-step.svg
│ │ │     ├── forward.svg
│ │ │     ├── franc-sign.svg
│ │ │     ├── frog.svg
│ │ │     ├── futbol.svg
│ │ │     ├── g.svg
│ │ │     ├── gamepad.svg
│ │ │     ├── gas-pump.svg
│ │ │     ├── gauge-high.svg
│ │ │     ├── gauge-simple-high.svg
│ │ │     ├── gauge-simple.svg
│ │ │     ├── gauge.svg
│ │ │     ├── gavel.svg
│ │ │     ├── gear.svg
│ │ │     ├── gears.svg
│ │ │     ├── gem.svg
│ │ │     ├── genderless.svg
│ │ │     ├── ghost.svg
│ │ │     ├── gift.svg
│ │ │     ├── gifts.svg
│ │ │     ├── glass-water-droplet.svg
│ │ │     ├── glass-water.svg
│ │ │     ├── glasses.svg
│ │ │     ├── globe.svg
│ │ │     ├── golf-ball-tee.svg
│ │ │     ├── gopuram.svg
│ │ │     ├── graduation-cap.svg
│ │ │     ├── greater-than-equal.svg
│ │ │     ├── greater-than.svg
│ │ │     ├── grip-lines-vertical.svg
│ │ │     ├── grip-lines.svg
│ │ │     ├── grip-vertical.svg
│ │ │     ├── grip.svg
│ │ │     ├── group-arrows-rotate.svg
│ │ │     ├── guarani-sign.svg
│ │ │     ├── guitar.svg
│ │ │     ├── gun.svg
│ │ │     ├── h.svg
│ │ │     ├── hammer.svg
│ │ │     ├── hamsa.svg
│ │ │     ├── hand-back-fist.svg
│ │ │     ├── hand-dots.svg
│ │ │     ├── hand-fist.svg
│ │ │     ├── hand-holding-dollar.svg
│ │ │     ├── hand-holding-droplet.svg
│ │ │     ├── hand-holding-hand.svg
│ │ │     ├── hand-holding-heart.svg
│ │ │     ├── hand-holding-medical.svg
│ │ │     ├── hand-holding.svg
│ │ │     ├── hand-lizard.svg
│ │ │     ├── hand-middle-finger.svg
│ │ │     ├── hand-peace.svg
│ │ │     ├── hand-point-down.svg
│ │ │     ├── hand-point-left.svg
│ │ │     ├── hand-point-right.svg
│ │ │     ├── hand-point-up.svg
│ │ │     ├── hand-pointer.svg
│ │ │     ├── hand-scissors.svg
│ │ │     ├── hand-sparkles.svg
│ │ │     ├── hand-spock.svg
│ │ │     ├── hand.svg
│ │ │     ├── handcuffs.svg
│ │ │     ├── hands-asl-interpreting.svg
│ │ │     ├── hands-bound.svg
│ │ │     ├── hands-bubbles.svg
│ │ │     ├── hands-clapping.svg
│ │ │     ├── hands-holding-child.svg
│ │ │     ├── hands-holding-circle.svg
│ │ │     ├── hands-holding.svg
│ │ │     ├── hands-praying.svg
│ │ │     ├── hands.svg
│ │ │     ├── handshake-angle.svg
│ │ │     ├── handshake-simple-slash.svg
│ │ │     ├── handshake-simple.svg
│ │ │     ├── handshake-slash.svg
│ │ │     ├── handshake.svg
│ │ │     ├── hanukiah.svg
│ │ │     ├── hard-drive.svg
│ │ │     ├── hashtag.svg
│ │ │     ├── hat-cowboy-side.svg
│ │ │     ├── hat-cowboy.svg
│ │ │     ├── hat-wizard.svg
│ │ │     ├── head-side-cough-slash.svg
│ │ │     ├── head-side-cough.svg
│ │ │     ├── head-side-mask.svg
│ │ │     ├── head-side-virus.svg
│ │ │     ├── heading.svg
│ │ │     ├── headphones-simple.svg
│ │ │     ├── headphones.svg
│ │ │     ├── headset.svg
│ │ │     ├── heart-circle-bolt.svg
│ │ │     ├── heart-circle-check.svg
│ │ │     ├── heart-circle-exclamation.svg
│ │ │     ├── heart-circle-minus.svg
│ │ │     ├── heart-circle-plus.svg
│ │ │     ├── heart-circle-xmark.svg
│ │ │     ├── heart-crack.svg
│ │ │     ├── heart-pulse.svg
│ │ │     ├── heart.svg
│ │ │     ├── helicopter-symbol.svg
│ │ │     ├── helicopter.svg
│ │ │     ├── helmet-safety.svg
│ │ │     ├── helmet-un.svg
│ │ │     ├── hexagon-nodes-bolt.svg
│ │ │     ├── hexagon-nodes.svg
│ │ │     ├── highlighter.svg
│ │ │     ├── hill-avalanche.svg
│ │ │     ├── hill-rockslide.svg
│ │ │     ├── hippo.svg
│ │ │     ├── hockey-puck.svg
│ │ │     ├── holly-berry.svg
│ │ │     ├── horse-head.svg
│ │ │     ├── horse.svg
│ │ │     ├── hospital-user.svg
│ │ │     ├── hospital.svg
│ │ │     ├── hot-tub-person.svg
│ │ │     ├── hotdog.svg
│ │ │     ├── hotel.svg
│ │ │     ├── hourglass-end.svg
│ │ │     ├── hourglass-half.svg
│ │ │     ├── hourglass-start.svg
│ │ │     ├── hourglass.svg
│ │ │     ├── house-chimney-crack.svg
│ │ │     ├── house-chimney-medical.svg
│ │ │     ├── house-chimney-user.svg
│ │ │     ├── house-chimney-window.svg
│ │ │     ├── house-chimney.svg
│ │ │     ├── house-circle-check.svg
│ │ │     ├── house-circle-exclamation.svg
│ │ │     ├── house-circle-xmark.svg
│ │ │     ├── house-crack.svg
│ │ │     ├── house-fire.svg
│ │ │     ├── house-flag.svg
│ │ │     ├── house-flood-water-circle-arrow-right.svg
│ │ │     ├── house-flood-water.svg
│ │ │     ├── house-laptop.svg
│ │ │     ├── house-lock.svg
│ │ │     ├── house-medical-circle-check.svg
│ │ │     ├── house-medical-circle-exclamation.svg
│ │ │     ├── house-medical-circle-xmark.svg
│ │ │     ├── house-medical-flag.svg
│ │ │     ├── house-medical.svg
│ │ │     ├── house-signal.svg
│ │ │     ├── house-tsunami.svg
│ │ │     ├── house-user.svg
│ │ │     ├── house.svg
│ │ │     ├── hryvnia-sign.svg
│ │ │     ├── hurricane.svg
│ │ │     ├── i-cursor.svg
│ │ │     ├── i.svg
│ │ │     ├── ice-cream.svg
│ │ │     ├── icicles.svg
│ │ │     ├── icons.svg
│ │ │     ├── id-badge.svg
│ │ │     ├── id-card-clip.svg
│ │ │     ├── id-card.svg
│ │ │     ├── igloo.svg
│ │ │     ├── image-portrait.svg
│ │ │     ├── image.svg
│ │ │     ├── images.svg
│ │ │     ├── inbox.svg
│ │ │     ├── indent.svg
│ │ │     ├── indian-rupee-sign.svg
│ │ │     ├── industry.svg
│ │ │     ├── infinity.svg
│ │ │     ├── info.svg
│ │ │     ├── italic.svg
│ │ │     ├── j.svg
│ │ │     ├── jar-wheat.svg
│ │ │     ├── jar.svg
│ │ │     ├── jedi.svg
│ │ │     ├── jet-fighter-up.svg
│ │ │     ├── jet-fighter.svg
│ │ │     ├── joint.svg
│ │ │     ├── jug-detergent.svg
│ │ │     ├── k.svg
│ │ │     ├── kaaba.svg
│ │ │     ├── key.svg
│ │ │     ├── keyboard.svg
│ │ │     ├── khanda.svg
│ │ │     ├── kip-sign.svg
│ │ │     ├── kit-medical.svg
│ │ │     ├── kitchen-set.svg
│ │ │     ├── kiwi-bird.svg
│ │ │     ├── l.svg
│ │ │     ├── land-mine-on.svg
│ │ │     ├── landmark-dome.svg
│ │ │     ├── landmark-flag.svg
│ │ │     ├── landmark.svg
│ │ │     ├── language.svg
│ │ │     ├── laptop-code.svg
│ │ │     ├── laptop-file.svg
│ │ │     ├── laptop-medical.svg
│ │ │     ├── laptop.svg
│ │ │     ├── lari-sign.svg
│ │ │     ├── layer-group.svg
│ │ │     ├── leaf.svg
│ │ │     ├── left-long.svg
│ │ │     ├── left-right.svg
│ │ │     ├── lemon.svg
│ │ │     ├── less-than-equal.svg
│ │ │     ├── less-than.svg
│ │ │     ├── life-ring.svg
│ │ │     ├── lightbulb.svg
│ │ │     ├── lines-leaning.svg
│ │ │     ├── link-slash.svg
│ │ │     ├── link.svg
│ │ │     ├── lira-sign.svg
│ │ │     ├── list-check.svg
│ │ │     ├── list-ol.svg
│ │ │     ├── list-ul.svg
│ │ │     ├── list.svg
│ │ │     ├── litecoin-sign.svg
│ │ │     ├── location-arrow.svg
│ │ │     ├── location-crosshairs.svg
│ │ │     ├── location-dot.svg
│ │ │     ├── location-pin-lock.svg
│ │ │     ├── location-pin.svg
│ │ │     ├── lock-open.svg
│ │ │     ├── lock.svg
│ │ │     ├── locust.svg
│ │ │     ├── lungs-virus.svg
│ │ │     ├── lungs.svg
│ │ │     ├── m.svg
│ │ │     ├── magnet.svg
│ │ │     ├── magnifying-glass-arrow-right.svg
│ │ │     ├── magnifying-glass-chart.svg
│ │ │     ├── magnifying-glass-dollar.svg
│ │ │     ├── magnifying-glass-location.svg
│ │ │     ├── magnifying-glass-minus.svg
│ │ │     ├── magnifying-glass-plus.svg
│ │ │     ├── magnifying-glass.svg
│ │ │     ├── manat-sign.svg
│ │ │     ├── map-location-dot.svg
│ │ │     ├── map-location.svg
│ │ │     ├── map-pin.svg
│ │ │     ├── map.svg
│ │ │     ├── marker.svg
│ │ │     ├── mars-and-venus-burst.svg
│ │ │     ├── mars-and-venus.svg
│ │ │     ├── mars-double.svg
│ │ │     ├── mars-stroke-right.svg
│ │ │     ├── mars-stroke-up.svg
│ │ │     ├── mars-stroke.svg
│ │ │     ├── mars.svg
│ │ │     ├── martini-glass-citrus.svg
│ │ │     ├── martini-glass-empty.svg
│ │ │     ├── martini-glass.svg
│ │ │     ├── mask-face.svg
│ │ │     ├── mask-ventilator.svg
│ │ │     ├── mask.svg
│ │ │     ├── masks-theater.svg
│ │ │     ├── mattress-pillow.svg
│ │ │     ├── maximize.svg
│ │ │     ├── medal.svg
│ │ │     ├── memory.svg
│ │ │     ├── menorah.svg
│ │ │     ├── mercury.svg
│ │ │     ├── message.svg
│ │ │     ├── meteor.svg
│ │ │     ├── microchip.svg
│ │ │     ├── microphone-lines-slash.svg
│ │ │     ├── microphone-lines.svg
│ │ │     ├── microphone-slash.svg
│ │ │     ├── microphone.svg
│ │ │     ├── microscope.svg
│ │ │     ├── mill-sign.svg
│ │ │     ├── minimize.svg
│ │ │     ├── minus.svg
│ │ │     ├── mitten.svg
│ │ │     ├── mobile-button.svg
│ │ │     ├── mobile-retro.svg
│ │ │     ├── mobile-screen-button.svg
│ │ │     ├── mobile-screen.svg
│ │ │     ├── mobile.svg
│ │ │     ├── money-bill-1-wave.svg
│ │ │     ├── money-bill-1.svg
│ │ │     ├── money-bill-transfer.svg
│ │ │     ├── money-bill-trend-up.svg
│ │ │     ├── money-bill-wave.svg
│ │ │     ├── money-bill-wheat.svg
│ │ │     ├── money-bill.svg
│ │ │     ├── money-bills.svg
│ │ │     ├── money-check-dollar.svg
│ │ │     ├── money-check.svg
│ │ │     ├── monument.svg
│ │ │     ├── moon.svg
│ │ │     ├── mortar-pestle.svg
│ │ │     ├── mosque.svg
│ │ │     ├── mosquito-net.svg
│ │ │     ├── mosquito.svg
│ │ │     ├── motorcycle.svg
│ │ │     ├── mound.svg
│ │ │     ├── mountain-city.svg
│ │ │     ├── mountain-sun.svg
│ │ │     ├── mountain.svg
│ │ │     ├── mug-hot.svg
│ │ │     ├── mug-saucer.svg
│ │ │     ├── music.svg
│ │ │     ├── n.svg
│ │ │     ├── naira-sign.svg
│ │ │     ├── network-wired.svg
│ │ │     ├── neuter.svg
│ │ │     ├── newspaper.svg
│ │ │     ├── not-equal.svg
│ │ │     ├── notdef.svg
│ │ │     ├── note-sticky.svg
│ │ │     ├── notes-medical.svg
│ │ │     ├── o.svg
│ │ │     ├── object-group.svg
│ │ │     ├── object-ungroup.svg
│ │ │     ├── oil-can.svg
│ │ │     ├── oil-well.svg
│ │ │     ├── om.svg
│ │ │     ├── otter.svg
│ │ │     ├── outdent.svg
│ │ │     ├── p.svg
│ │ │     ├── pager.svg
│ │ │     ├── paint-roller.svg
│ │ │     ├── paintbrush.svg
│ │ │     ├── palette.svg
│ │ │     ├── pallet.svg
│ │ │     ├── panorama.svg
│ │ │     ├── paper-plane.svg
│ │ │     ├── paperclip.svg
│ │ │     ├── parachute-box.svg
│ │ │     ├── paragraph.svg
│ │ │     ├── passport.svg
│ │ │     ├── paste.svg
│ │ │     ├── pause.svg
│ │ │     ├── paw.svg
│ │ │     ├── peace.svg
│ │ │     ├── pen-clip.svg
│ │ │     ├── pen-fancy.svg
│ │ │     ├── pen-nib.svg
│ │ │     ├── pen-ruler.svg
│ │ │     ├── pen-to-square.svg
│ │ │     ├── pen.svg
│ │ │     ├── pencil.svg
│ │ │     ├── people-arrows.svg
│ │ │     ├── people-carry-box.svg
│ │ │     ├── people-group.svg
│ │ │     ├── people-line.svg
│ │ │     ├── people-pulling.svg
│ │ │     ├── people-robbery.svg
│ │ │     ├── people-roof.svg
│ │ │     ├── pepper-hot.svg
│ │ │     ├── percent.svg
│ │ │     ├── person-arrow-down-to-line.svg
│ │ │     ├── person-arrow-up-from-line.svg
│ │ │     ├── person-biking.svg
│ │ │     ├── person-booth.svg
│ │ │     ├── person-breastfeeding.svg
│ │ │     ├── person-burst.svg
│ │ │     ├── person-cane.svg
│ │ │     ├── person-chalkboard.svg
│ │ │     ├── person-circle-check.svg
│ │ │     ├── person-circle-exclamation.svg
│ │ │     ├── person-circle-minus.svg
│ │ │     ├── person-circle-plus.svg
│ │ │     ├── person-circle-question.svg
│ │ │     ├── person-circle-xmark.svg
│ │ │     ├── person-digging.svg
│ │ │     ├── person-dots-from-line.svg
│ │ │     ├── person-dress-burst.svg
│ │ │     ├── person-dress.svg
│ │ │     ├── person-drowning.svg
│ │ │     ├── person-falling-burst.svg
│ │ │     ├── person-falling.svg
│ │ │     ├── person-half-dress.svg
│ │ │     ├── person-harassing.svg
│ │ │     ├── person-hiking.svg
│ │ │     ├── person-military-pointing.svg
│ │ │     ├── person-military-rifle.svg
│ │ │     ├── person-military-to-person.svg
│ │ │     ├── person-praying.svg
│ │ │     ├── person-pregnant.svg
│ │ │     ├── person-rays.svg
│ │ │     ├── person-rifle.svg
│ │ │     ├── person-running.svg
│ │ │     ├── person-shelter.svg
│ │ │     ├── person-skating.svg
│ │ │     ├── person-skiing-nordic.svg
│ │ │     ├── person-skiing.svg
│ │ │     ├── person-snowboarding.svg
│ │ │     ├── person-swimming.svg
│ │ │     ├── person-through-window.svg
│ │ │     ├── person-walking-arrow-loop-left.svg
│ │ │     ├── person-walking-arrow-right.svg
│ │ │     ├── person-walking-dashed-line-arrow-right.svg
│ │ │     ├── person-walking-luggage.svg
│ │ │     ├── person-walking-with-cane.svg
│ │ │     ├── person-walking.svg
│ │ │     ├── person.svg
│ │ │     ├── peseta-sign.svg
│ │ │     ├── peso-sign.svg
│ │ │     ├── phone-flip.svg
│ │ │     ├── phone-slash.svg
│ │ │     ├── phone-volume.svg
│ │ │     ├── phone.svg
│ │ │     ├── photo-film.svg
│ │ │     ├── piggy-bank.svg
│ │ │     ├── pills.svg
│ │ │     ├── pizza-slice.svg
│ │ │     ├── place-of-worship.svg
│ │ │     ├── plane-arrival.svg
│ │ │     ├── plane-circle-check.svg
│ │ │     ├── plane-circle-exclamation.svg
│ │ │     ├── plane-circle-xmark.svg
│ │ │     ├── plane-departure.svg
│ │ │     ├── plane-lock.svg
│ │ │     ├── plane-slash.svg
│ │ │     ├── plane-up.svg
│ │ │     ├── plane.svg
│ │ │     ├── plant-wilt.svg
│ │ │     ├── plate-wheat.svg
│ │ │     ├── play.svg
│ │ │     ├── plug-circle-bolt.svg
│ │ │     ├── plug-circle-check.svg
│ │ │     ├── plug-circle-exclamation.svg
│ │ │     ├── plug-circle-minus.svg
│ │ │     ├── plug-circle-plus.svg
│ │ │     ├── plug-circle-xmark.svg
│ │ │     ├── plug.svg
│ │ │     ├── plus-minus.svg
│ │ │     ├── plus.svg
│ │ │     ├── podcast.svg
│ │ │     ├── poo-storm.svg
│ │ │     ├── poo.svg
│ │ │     ├── poop.svg
│ │ │     ├── power-off.svg
│ │ │     ├── prescription-bottle-medical.svg
│ │ │     ├── prescription-bottle.svg
│ │ │     ├── prescription.svg
│ │ │     ├── print.svg
│ │ │     ├── pump-medical.svg
│ │ │     ├── pump-soap.svg
│ │ │     ├── puzzle-piece.svg
│ │ │     ├── q.svg
│ │ │     ├── qrcode.svg
│ │ │     ├── question.svg
│ │ │     ├── quote-left.svg
│ │ │     ├── quote-right.svg
│ │ │     ├── r.svg
│ │ │     ├── radiation.svg
│ │ │     ├── radio.svg
│ │ │     ├── rainbow.svg
│ │ │     ├── ranking-star.svg
│ │ │     ├── receipt.svg
│ │ │     ├── record-vinyl.svg
│ │ │     ├── rectangle-ad.svg
│ │ │     ├── rectangle-list.svg
│ │ │     ├── rectangle-xmark.svg
│ │ │     ├── recycle.svg
│ │ │     ├── registered.svg
│ │ │     ├── repeat.svg
│ │ │     ├── reply-all.svg
│ │ │     ├── reply.svg
│ │ │     ├── republican.svg
│ │ │     ├── restroom.svg
│ │ │     ├── retweet.svg
│ │ │     ├── ribbon.svg
│ │ │     ├── right-from-bracket.svg
│ │ │     ├── right-left.svg
│ │ │     ├── right-long.svg
│ │ │     ├── right-to-bracket.svg
│ │ │     ├── ring.svg
│ │ │     ├── road-barrier.svg
│ │ │     ├── road-bridge.svg
│ │ │     ├── road-circle-check.svg
│ │ │     ├── road-circle-exclamation.svg
│ │ │     ├── road-circle-xmark.svg
│ │ │     ├── road-lock.svg
│ │ │     ├── road-spikes.svg
│ │ │     ├── road.svg
│ │ │     ├── robot.svg
│ │ │     ├── rocket.svg
│ │ │     ├── rotate-left.svg
│ │ │     ├── rotate-right.svg
│ │ │     ├── rotate.svg
│ │ │     ├── route.svg
│ │ │     ├── rss.svg
│ │ │     ├── ruble-sign.svg
│ │ │     ├── rug.svg
│ │ │     ├── ruler-combined.svg
│ │ │     ├── ruler-horizontal.svg
│ │ │     ├── ruler-vertical.svg
│ │ │     ├── ruler.svg
│ │ │     ├── rupee-sign.svg
│ │ │     ├── rupiah-sign.svg
│ │ │     ├── s.svg
│ │ │     ├── sack-dollar.svg
│ │ │     ├── sack-xmark.svg
│ │ │     ├── sailboat.svg
│ │ │     ├── satellite-dish.svg
│ │ │     ├── satellite.svg
│ │ │     ├── scale-balanced.svg
│ │ │     ├── scale-unbalanced-flip.svg
│ │ │     ├── scale-unbalanced.svg
│ │ │     ├── school-circle-check.svg
│ │ │     ├── school-circle-exclamation.svg
│ │ │     ├── school-circle-xmark.svg
│ │ │     ├── school-flag.svg
│ │ │     ├── school-lock.svg
│ │ │     ├── school.svg
│ │ │     ├── scissors.svg
│ │ │     ├── screwdriver-wrench.svg
│ │ │     ├── screwdriver.svg
│ │ │     ├── scroll-torah.svg
│ │ │     ├── scroll.svg
│ │ │     ├── sd-card.svg
│ │ │     ├── section.svg
│ │ │     ├── seedling.svg
│ │ │     ├── server.svg
│ │ │     ├── shapes.svg
│ │ │     ├── share-from-square.svg
│ │ │     ├── share-nodes.svg
│ │ │     ├── share.svg
│ │ │     ├── sheet-plastic.svg
│ │ │     ├── shekel-sign.svg
│ │ │     ├── shield-cat.svg
│ │ │     ├── shield-dog.svg
│ │ │     ├── shield-halved.svg
│ │ │     ├── shield-heart.svg
│ │ │     ├── shield-virus.svg
│ │ │     ├── shield.svg
│ │ │     ├── ship.svg
│ │ │     ├── shirt.svg
│ │ │     ├── shoe-prints.svg
│ │ │     ├── shop-lock.svg
│ │ │     ├── shop-slash.svg
│ │ │     ├── shop.svg
│ │ │     ├── shower.svg
│ │ │     ├── shrimp.svg
│ │ │     ├── shuffle.svg
│ │ │     ├── shuttle-space.svg
│ │ │     ├── sign-hanging.svg
│ │ │     ├── signal.svg
│ │ │     ├── signature.svg
│ │ │     ├── signs-post.svg
│ │ │     ├── sim-card.svg
│ │ │     ├── sink.svg
│ │ │     ├── sitemap.svg
│ │ │     ├── skull-crossbones.svg
│ │ │     ├── skull.svg
│ │ │     ├── slash.svg
│ │ │     ├── sleigh.svg
│ │ │     ├── sliders.svg
│ │ │     ├── smog.svg
│ │ │     ├── smoking.svg
│ │ │     ├── snowflake.svg
│ │ │     ├── snowman.svg
│ │ │     ├── snowplow.svg
│ │ │     ├── soap.svg
│ │ │     ├── socks.svg
│ │ │     ├── solar-panel.svg
│ │ │     ├── sort-down.svg
│ │ │     ├── sort-up.svg
│ │ │     ├── sort.svg
│ │ │     ├── spa.svg
│ │ │     ├── spaghetti-monster-flying.svg
│ │ │     ├── spell-check.svg
│ │ │     ├── spider.svg
│ │ │     ├── spinner.svg
│ │ │     ├── splotch.svg
│ │ │     ├── spoon.svg
│ │ │     ├── spray-can-sparkles.svg
│ │ │     ├── spray-can.svg
│ │ │     ├── square-arrow-up-right.svg
│ │ │     ├── square-binary.svg
│ │ │     ├── square-caret-down.svg
│ │ │     ├── square-caret-left.svg
│ │ │     ├── square-caret-right.svg
│ │ │     ├── square-caret-up.svg
│ │ │     ├── square-check.svg
│ │ │     ├── square-envelope.svg
│ │ │     ├── square-full.svg
│ │ │     ├── square-h.svg
│ │ │     ├── square-minus.svg
│ │ │     ├── square-nfi.svg
│ │ │     ├── square-parking.svg
│ │ │     ├── square-pen.svg
│ │ │     ├── square-person-confined.svg
│ │ │     ├── square-phone-flip.svg
│ │ │     ├── square-phone.svg
│ │ │     ├── square-plus.svg
│ │ │     ├── square-poll-horizontal.svg
│ │ │     ├── square-poll-vertical.svg
│ │ │     ├── square-root-variable.svg
│ │ │     ├── square-rss.svg
│ │ │     ├── square-share-nodes.svg
│ │ │     ├── square-up-right.svg
│ │ │     ├── square-virus.svg
│ │ │     ├── square-xmark.svg
│ │ │     ├── square.svg
│ │ │     ├── staff-snake.svg
│ │ │     ├── stairs.svg
│ │ │     ├── stamp.svg
│ │ │     ├── stapler.svg
│ │ │     ├── star-and-crescent.svg
│ │ │     ├── star-half-stroke.svg
│ │ │     ├── star-half.svg
│ │ │     ├── star-of-david.svg
│ │ │     ├── star-of-life.svg
│ │ │     ├── star.svg
│ │ │     ├── sterling-sign.svg
│ │ │     ├── stethoscope.svg
│ │ │     ├── stop.svg
│ │ │     ├── stopwatch-20.svg
│ │ │     ├── stopwatch.svg
│ │ │     ├── store-slash.svg
│ │ │     ├── store.svg
│ │ │     ├── street-view.svg
│ │ │     ├── strikethrough.svg
│ │ │     ├── stroopwafel.svg
│ │ │     ├── subscript.svg
│ │ │     ├── suitcase-medical.svg
│ │ │     ├── suitcase-rolling.svg
│ │ │     ├── suitcase.svg
│ │ │     ├── sun-plant-wilt.svg
│ │ │     ├── sun.svg
│ │ │     ├── superscript.svg
│ │ │     ├── swatchbook.svg
│ │ │     ├── synagogue.svg
│ │ │     ├── syringe.svg
│ │ │     ├── t.svg
│ │ │     ├── table-cells-column-lock.svg
│ │ │     ├── table-cells-large.svg
│ │ │     ├── table-cells-row-lock.svg
│ │ │     ├── table-cells-row-unlock.svg
│ │ │     ├── table-cells.svg
│ │ │     ├── table-columns.svg
│ │ │     ├── table-list.svg
│ │ │     ├── table-tennis-paddle-ball.svg
│ │ │     ├── table.svg
│ │ │     ├── tablet-button.svg
│ │ │     ├── tablet-screen-button.svg
│ │ │     ├── tablet.svg
│ │ │     ├── tablets.svg
│ │ │     ├── tachograph-digital.svg
│ │ │     ├── tag.svg
│ │ │     ├── tags.svg
│ │ │     ├── tape.svg
│ │ │     ├── tarp-droplet.svg
│ │ │     ├── tarp.svg
│ │ │     ├── taxi.svg
│ │ │     ├── teeth-open.svg
│ │ │     ├── teeth.svg
│ │ │     ├── temperature-arrow-down.svg
│ │ │     ├── temperature-arrow-up.svg
│ │ │     ├── temperature-empty.svg
│ │ │     ├── temperature-full.svg
│ │ │     ├── temperature-half.svg
│ │ │     ├── temperature-high.svg
│ │ │     ├── temperature-low.svg
│ │ │     ├── temperature-quarter.svg
│ │ │     ├── temperature-three-quarters.svg
│ │ │     ├── tenge-sign.svg
│ │ │     ├── tent-arrow-down-to-line.svg
│ │ │     ├── tent-arrow-left-right.svg
│ │ │     ├── tent-arrow-turn-left.svg
│ │ │     ├── tent-arrows-down.svg
│ │ │     ├── tent.svg
│ │ │     ├── tents.svg
│ │ │     ├── terminal.svg
│ │ │     ├── text-height.svg
│ │ │     ├── text-slash.svg
│ │ │     ├── text-width.svg
│ │ │     ├── thermometer.svg
│ │ │     ├── thumbs-down.svg
│ │ │     ├── thumbs-up.svg
│ │ │     ├── thumbtack-slash.svg
│ │ │     ├── thumbtack.svg
│ │ │     ├── ticket-simple.svg
│ │ │     ├── ticket.svg
│ │ │     ├── timeline.svg
│ │ │     ├── toggle-off.svg
│ │ │     ├── toggle-on.svg
│ │ │     ├── toilet-paper-slash.svg
│ │ │     ├── toilet-paper.svg
│ │ │     ├── toilet-portable.svg
│ │ │     ├── toilet.svg
│ │ │     ├── toilets-portable.svg
│ │ │     ├── toolbox.svg
│ │ │     ├── tooth.svg
│ │ │     ├── torii-gate.svg
│ │ │     ├── tornado.svg
│ │ │     ├── tower-broadcast.svg
│ │ │     ├── tower-cell.svg
│ │ │     ├── tower-observation.svg
│ │ │     ├── tractor.svg
│ │ │     ├── trademark.svg
│ │ │     ├── traffic-light.svg
│ │ │     ├── trailer.svg
│ │ │     ├── train-subway.svg
│ │ │     ├── train-tram.svg
│ │ │     ├── train.svg
│ │ │     ├── transgender.svg
│ │ │     ├── trash-arrow-up.svg
│ │ │     ├── trash-can-arrow-up.svg
│ │ │     ├── trash-can.svg
│ │ │     ├── trash.svg
│ │ │     ├── tree-city.svg
│ │ │     ├── tree.svg
│ │ │     ├── triangle-exclamation.svg
│ │ │     ├── trophy.svg
│ │ │     ├── trowel-bricks.svg
│ │ │     ├── trowel.svg
│ │ │     ├── truck-arrow-right.svg
│ │ │     ├── truck-droplet.svg
│ │ │     ├── truck-fast.svg
│ │ │     ├── truck-field-un.svg
│ │ │     ├── truck-field.svg
│ │ │     ├── truck-front.svg
│ │ │     ├── truck-medical.svg
│ │ │     ├── truck-monster.svg
│ │ │     ├── truck-moving.svg
│ │ │     ├── truck-pickup.svg
│ │ │     ├── truck-plane.svg
│ │ │     ├── truck-ramp-box.svg
│ │ │     ├── truck.svg
│ │ │     ├── tty.svg
│ │ │     ├── turkish-lira-sign.svg
│ │ │     ├── turn-down.svg
│ │ │     ├── turn-up.svg
│ │ │     ├── tv.svg
│ │ │     ├── u.svg
│ │ │     ├── umbrella-beach.svg
│ │ │     ├── umbrella.svg
│ │ │     ├── underline.svg
│ │ │     ├── universal-access.svg
│ │ │     ├── unlock-keyhole.svg
│ │ │     ├── unlock.svg
│ │ │     ├── up-down-left-right.svg
│ │ │     ├── up-down.svg
│ │ │     ├── up-long.svg
│ │ │     ├── up-right-and-down-left-from-center.svg
│ │ │     ├── up-right-from-square.svg
│ │ │     ├── upload.svg
│ │ │     ├── user-astronaut.svg
│ │ │     ├── user-check.svg
│ │ │     ├── user-clock.svg
│ │ │     ├── user-doctor.svg
│ │ │     ├── user-gear.svg
│ │ │     ├── user-graduate.svg
│ │ │     ├── user-group.svg
│ │ │     ├── user-injured.svg
│ │ │     ├── user-large-slash.svg
│ │ │     ├── user-large.svg
│ │ │     ├── user-lock.svg
│ │ │     ├── user-minus.svg
│ │ │     ├── user-ninja.svg
│ │ │     ├── user-nurse.svg
│ │ │     ├── user-pen.svg
│ │ │     ├── user-plus.svg
│ │ │     ├── user-secret.svg
│ │ │     ├── user-shield.svg
│ │ │     ├── user-slash.svg
│ │ │     ├── user-tag.svg
│ │ │     ├── user-tie.svg
│ │ │     ├── user-xmark.svg
│ │ │     ├── user.svg
│ │ │     ├── users-between-lines.svg
│ │ │     ├── users-gear.svg
│ │ │     ├── users-line.svg
│ │ │     ├── users-rays.svg
│ │ │     ├── users-rectangle.svg
│ │ │     ├── users-slash.svg
│ │ │     ├── users-viewfinder.svg
│ │ │     ├── users.svg
│ │ │     ├── utensils.svg
│ │ │     ├── v.svg
│ │ │     ├── van-shuttle.svg
│ │ │     ├── vault.svg
│ │ │     ├── vector-square.svg
│ │ │     ├── venus-double.svg
│ │ │     ├── venus-mars.svg
│ │ │     ├── venus.svg
│ │ │     ├── vest-patches.svg
│ │ │     ├── vest.svg
│ │ │     ├── vial-circle-check.svg
│ │ │     ├── vial-virus.svg
│ │ │     ├── vial.svg
│ │ │     ├── vials.svg
│ │ │     ├── video-slash.svg
│ │ │     ├── video.svg
│ │ │     ├── vihara.svg
│ │ │     ├── virus-covid-slash.svg
│ │ │     ├── virus-covid.svg
│ │ │     ├── virus-slash.svg
│ │ │     ├── virus.svg
│ │ │     ├── viruses.svg
│ │ │     ├── voicemail.svg
│ │ │     ├── volcano.svg
│ │ │     ├── volleyball.svg
│ │ │     ├── volume-high.svg
│ │ │     ├── volume-low.svg
│ │ │     ├── volume-off.svg
│ │ │     ├── volume-xmark.svg
│ │ │     ├── vr-cardboard.svg
│ │ │     ├── w.svg
│ │ │     ├── walkie-talkie.svg
│ │ │     ├── wallet.svg
│ │ │     ├── wand-magic-sparkles.svg
│ │ │     ├── wand-magic.svg
│ │ │     ├── wand-sparkles.svg
│ │ │     ├── warehouse.svg
│ │ │     ├── water-ladder.svg
│ │ │     ├── water.svg
│ │ │     ├── wave-square.svg
│ │ │     ├── web-awesome.svg
│ │ │     ├── weight-hanging.svg
│ │ │     ├── weight-scale.svg
│ │ │     ├── wheat-awn-circle-exclamation.svg
│ │ │     ├── wheat-awn.svg
│ │ │     ├── wheelchair-move.svg
│ │ │     ├── wheelchair.svg
│ │ │     ├── whiskey-glass.svg
│ │ │     ├── wifi.svg
│ │ │     ├── wind.svg
│ │ │     ├── window-maximize.svg
│ │ │     ├── window-minimize.svg
│ │ │     ├── window-restore.svg
│ │ │     ├── wine-bottle.svg
│ │ │     ├── wine-glass-empty.svg
│ │ │     ├── wine-glass.svg
│ │ │     ├── won-sign.svg
│ │ │     ├── worm.svg
│ │ │     ├── wrench.svg
│ │ │     ├── x-ray.svg
│ │ │     ├── x.svg
│ │ │     ├── xmark.svg
│ │ │     ├── xmarks-lines.svg
│ │ │     ├── y.svg
│ │ │     ├── yen-sign.svg
│ │ │     ├── yin-yang.svg
│ │ │     └── z.svg
│ │ └── webfonts/
│ │     ├── fa-brands-400.ttf
│ │     ├── fa-brands-400.woff2
│ │     ├── fa-regular-400.ttf
│ │     ├── fa-regular-400.woff2
│ │     ├── fa-solid-900.ttf
│ │     ├── fa-solid-900.woff2
│ │     ├── fa-v4compatibility.ttf
│ │     └── fa-v4compatibility.woff2
│ ├── bootstrap-icons/
│ │ ├── 0-circle-fill.svg
│ │ ├── 0-circle.svg
│ │ ├── 0-square-fill.svg
│ │ ├── 0-square.svg
│ │ ├── 1-circle-fill.svg
│ │ ├── 1-circle.svg
│ │ ├── 1-square-fill.svg
│ │ ├── 1-square.svg
│ │ ├── 123.svg
│ │ ├── 2-circle-fill.svg
│ │ ├── 2-circle.svg
│ │ ├── 2-square-fill.svg
│ │ ├── 2-square.svg
│ │ ├── 3-circle-fill.svg
│ │ ├── 3-circle.svg
│ │ ├── 3-square-fill.svg
│ │ ├── 3-square.svg
│ │ ├── 4-circle-fill.svg
│ │ ├── 4-circle.svg
│ │ ├── 4-square-fill.svg
│ │ ├── 4-square.svg
│ │ ├── 5-circle-fill.svg
│ │ ├── 5-circle.svg
│ │ ├── 5-square-fill.svg
│ │ ├── 5-square.svg
│ │ ├── 6-circle-fill.svg
│ │ ├── 6-circle.svg
│ │ ├── 6-square-fill.svg
│ │ ├── 6-square.svg
│ │ ├── 7-circle-fill.svg
│ │ ├── 7-circle.svg
│ │ ├── 7-square-fill.svg
│ │ ├── 7-square.svg
│ │ ├── 8-circle-fill.svg
│ │ ├── 8-circle.svg
│ │ ├── 8-square-fill.svg
│ │ ├── 8-square.svg
│ │ ├── 9-circle-fill.svg
│ │ ├── 9-circle.svg
│ │ ├── 9-square-fill.svg
│ │ ├── 9-square.svg
│ │ ├── activity.svg
│ │ ├── airplane-engines-fill.svg
│ │ ├── airplane-engines.svg
│ │ ├── airplane-fill.svg
│ │ ├── airplane.svg
│ │ ├── alarm-fill.svg
│ │ ├── alarm.svg
│ │ ├── alexa.svg
│ │ ├── align-bottom.svg
│ │ ├── align-center.svg
│ │ ├── align-end.svg
│ │ ├── align-middle.svg
│ │ ├── align-start.svg
│ │ ├── align-top.svg
│ │ ├── alipay.svg
│ │ ├── alphabet-uppercase.svg
│ │ ├── alphabet.svg
│ │ ├── alt.svg
│ │ ├── amazon.svg
│ │ ├── amd.svg
│ │ ├── android.svg
│ │ ├── android2.svg
│ │ ├── app-indicator.svg
│ │ ├── app.svg
│ │ ├── apple.svg
│ │ ├── archive-fill.svg
│ │ ├── archive.svg
│ │ ├── arrow-90deg-down.svg
│ │ ├── arrow-90deg-left.svg
│ │ ├── arrow-90deg-right.svg
│ │ ├── arrow-90deg-up.svg
│ │ ├── arrow-bar-down.svg
│ │ ├── arrow-bar-left.svg
│ │ ├── arrow-bar-right.svg
│ │ ├── arrow-bar-up.svg
│ │ ├── arrow-clockwise.svg
│ │ ├── arrow-counterclockwise.svg
│ │ ├── arrow-down-circle-fill.svg
│ │ ├── arrow-down-circle.svg
│ │ ├── arrow-down-left-circle-fill.svg
│ │ ├── arrow-down-left-circle.svg
│ │ ├── arrow-down-left-square-fill.svg
│ │ ├── arrow-down-left-square.svg
│ │ ├── arrow-down-left.svg
│ │ ├── arrow-down-right-circle-fill.svg
│ │ ├── arrow-down-right-circle.svg
│ │ ├── arrow-down-right-square-fill.svg
│ │ ├── arrow-down-right-square.svg
│ │ ├── arrow-down-right.svg
│ │ ├── arrow-down-short.svg
│ │ ├── arrow-down-square-fill.svg
│ │ ├── arrow-down-square.svg
│ │ ├── arrow-down-up.svg
│ │ ├── arrow-down.svg
│ │ ├── arrow-left-circle-fill.svg
│ │ ├── arrow-left-circle.svg
│ │ ├── arrow-left-right.svg
│ │ ├── arrow-left-short.svg
│ │ ├── arrow-left-square-fill.svg
│ │ ├── arrow-left-square.svg
│ │ ├── arrow-left.svg
│ │ ├── arrow-repeat.svg
│ │ ├── arrow-return-left.svg
│ │ ├── arrow-return-right.svg
│ │ ├── arrow-right-circle-fill.svg
│ │ ├── arrow-right-circle.svg
│ │ ├── arrow-right-short.svg
│ │ ├── arrow-right-square-fill.svg
│ │ ├── arrow-right-square.svg
│ │ ├── arrow-right.svg
│ │ ├── arrow-through-heart-fill.svg
│ │ ├── arrow-through-heart.svg
│ │ ├── arrow-up-circle-fill.svg
│ │ ├── arrow-up-circle.svg
│ │ ├── arrow-up-left-circle-fill.svg
│ │ ├── arrow-up-left-circle.svg
│ │ ├── arrow-up-left-square-fill.svg
│ │ ├── arrow-up-left-square.svg
│ │ ├── arrow-up-left.svg
│ │ ├── arrow-up-right-circle-fill.svg
│ │ ├── arrow-up-right-circle.svg
│ │ ├── arrow-up-right-square-fill.svg
│ │ ├── arrow-up-right-square.svg
│ │ ├── arrow-up-right.svg
│ │ ├── arrow-up-short.svg
│ │ ├── arrow-up-square-fill.svg
│ │ ├── arrow-up-square.svg
│ │ ├── arrow-up.svg
│ │ ├── arrows-angle-contract.svg
│ │ ├── arrows-angle-expand.svg
│ │ ├── arrows-collapse-vertical.svg
│ │ ├── arrows-collapse.svg
│ │ ├── arrows-expand-vertical.svg
│ │ ├── arrows-expand.svg
│ │ ├── arrows-fullscreen.svg
│ │ ├── arrows-move.svg
│ │ ├── arrows-vertical.svg
│ │ ├── arrows.svg
│ │ ├── aspect-ratio-fill.svg
│ │ ├── aspect-ratio.svg
│ │ ├── asterisk.svg
│ │ ├── at.svg
│ │ ├── award-fill.svg
│ │ ├── award.svg
│ │ ├── back.svg
│ │ ├── backpack-fill.svg
│ │ ├── backpack.svg
│ │ ├── backpack2-fill.svg
│ │ ├── backpack2.svg
│ │ ├── backpack3-fill.svg
│ │ ├── backpack3.svg
│ │ ├── backpack4-fill.svg
│ │ ├── backpack4.svg
│ │ ├── backspace-fill.svg
│ │ ├── backspace-reverse-fill.svg
│ │ ├── backspace-reverse.svg
│ │ ├── backspace.svg
│ │ ├── badge-3d-fill.svg
│ │ ├── badge-3d.svg
│ │ ├── badge-4k-fill.svg
│ │ ├── badge-4k.svg
│ │ ├── badge-8k-fill.svg
│ │ ├── badge-8k.svg
│ │ ├── badge-ad-fill.svg
│ │ ├── badge-ad.svg
│ │ ├── badge-ar-fill.svg
│ │ ├── badge-ar.svg
│ │ ├── badge-cc-fill.svg
│ │ ├── badge-cc.svg
│ │ ├── badge-hd-fill.svg
│ │ ├── badge-hd.svg
│ │ ├── badge-sd-fill.svg
│ │ ├── badge-sd.svg
│ │ ├── badge-tm-fill.svg
│ │ ├── badge-tm.svg
│ │ ├── badge-vo-fill.svg
│ │ ├── badge-vo.svg
│ │ ├── badge-vr-fill.svg
│ │ ├── badge-vr.svg
│ │ ├── badge-wc-fill.svg
│ │ ├── badge-wc.svg
│ │ ├── bag-check-fill.svg
│ │ ├── bag-check.svg
│ │ ├── bag-dash-fill.svg
│ │ ├── bag-dash.svg
│ │ ├── bag-fill.svg
│ │ ├── bag-heart-fill.svg
│ │ ├── bag-heart.svg
│ │ ├── bag-plus-fill.svg
│ │ ├── bag-plus.svg
│ │ ├── bag-x-fill.svg
│ │ ├── bag-x.svg
│ │ ├── bag.svg
│ │ ├── balloon-fill.svg
│ │ ├── balloon-heart-fill.svg
│ │ ├── balloon-heart.svg
│ │ ├── balloon.svg
│ │ ├── ban-fill.svg
│ │ ├── ban.svg
│ │ ├── bandaid-fill.svg
│ │ ├── bandaid.svg
│ │ ├── bank.svg
│ │ ├── bank2.svg
│ │ ├── bar-chart-fill.svg
│ │ ├── bar-chart-line-fill.svg
│ │ ├── bar-chart-line.svg
│ │ ├── bar-chart-steps.svg
│ │ ├── bar-chart.svg
│ │ ├── basket-fill.svg
│ │ ├── basket.svg
│ │ ├── basket2-fill.svg
│ │ ├── basket2.svg
│ │ ├── basket3-fill.svg
│ │ ├── basket3.svg
│ │ ├── battery-charging.svg
│ │ ├── battery-full.svg
│ │ ├── battery-half.svg
│ │ ├── battery.svg
│ │ ├── behance.svg
│ │ ├── bell-fill.svg
│ │ ├── bell-slash-fill.svg
│ │ ├── bell-slash.svg
│ │ ├── bell.svg
│ │ ├── bezier.svg
│ │ ├── bezier2.svg
│ │ ├── bicycle.svg
│ │ ├── bing.svg
│ │ ├── binoculars-fill.svg
│ │ ├── binoculars.svg
│ │ ├── blockquote-left.svg
│ │ ├── blockquote-right.svg
│ │ ├── bluetooth.svg
│ │ ├── body-text.svg
│ │ ├── book-fill.svg
│ │ ├── book-half.svg
│ │ ├── book.svg
│ │ ├── bookmark-check-fill.svg
│ │ ├── bookmark-check.svg
│ │ ├── bookmark-dash-fill.svg
│ │ ├── bookmark-dash.svg
│ │ ├── bookmark-fill.svg
│ │ ├── bookmark-heart-fill.svg
│ │ ├── bookmark-heart.svg
│ │ ├── bookmark-plus-fill.svg
│ │ ├── bookmark-plus.svg
│ │ ├── bookmark-star-fill.svg
│ │ ├── bookmark-star.svg
│ │ ├── bookmark-x-fill.svg
│ │ ├── bookmark-x.svg
│ │ ├── bookmark.svg
│ │ ├── bookmarks-fill.svg
│ │ ├── bookmarks.svg
│ │ ├── bookshelf.svg
│ │ ├── boombox-fill.svg
│ │ ├── boombox.svg
│ │ ├── bootstrap-fill.svg
│ │ ├── bootstrap-icons.svg
│ │ ├── bootstrap-reboot.svg
│ │ ├── bootstrap.svg
│ │ ├── border-all.svg
│ │ ├── border-bottom.svg
│ │ ├── border-center.svg
│ │ ├── border-inner.svg
│ │ ├── border-left.svg
│ │ ├── border-middle.svg
│ │ ├── border-outer.svg
│ │ ├── border-right.svg
│ │ ├── border-style.svg
│ │ ├── border-top.svg
│ │ ├── border-width.svg
│ │ ├── border.svg
│ │ ├── bounding-box-circles.svg
│ │ ├── bounding-box.svg
│ │ ├── box-arrow-down-left.svg
│ │ ├── box-arrow-down-right.svg
│ │ ├── box-arrow-down.svg
│ │ ├── box-arrow-in-down-left.svg
│ │ ├── box-arrow-in-down-right.svg
│ │ ├── box-arrow-in-down.svg
│ │ ├── box-arrow-in-left.svg
│ │ ├── box-arrow-in-right.svg
│ │ ├── box-arrow-in-up-left.svg
│ │ ├── box-arrow-in-up-right.svg
│ │ ├── box-arrow-in-up.svg
│ │ ├── box-arrow-left.svg
│ │ ├── box-arrow-right.svg
│ │ ├── box-arrow-up-left.svg
│ │ ├── box-arrow-up-right.svg
│ │ ├── box-arrow-up.svg
│ │ ├── box-fill.svg
│ │ ├── box-seam-fill.svg
│ │ ├── box-seam.svg
│ │ ├── box.svg
│ │ ├── box2-fill.svg
│ │ ├── box2-heart-fill.svg
│ │ ├── box2-heart.svg
│ │ ├── box2.svg
│ │ ├── boxes.svg
│ │ ├── braces-asterisk.svg
│ │ ├── braces.svg
│ │ ├── bricks.svg
│ │ ├── briefcase-fill.svg
│ │ ├── briefcase.svg
│ │ ├── brightness-alt-high-fill.svg
│ │ ├── brightness-alt-high.svg
│ │ ├── brightness-alt-low-fill.svg
│ │ ├── brightness-alt-low.svg
│ │ ├── brightness-high-fill.svg
│ │ ├── brightness-high.svg
│ │ ├── brightness-low-fill.svg
│ │ ├── brightness-low.svg
│ │ ├── brilliance.svg
│ │ ├── broadcast-pin.svg
│ │ ├── broadcast.svg
│ │ ├── browser-chrome.svg
│ │ ├── browser-edge.svg
│ │ ├── browser-firefox.svg
│ │ ├── browser-safari.svg
│ │ ├── brush-fill.svg
│ │ ├── brush.svg
│ │ ├── bucket-fill.svg
│ │ ├── bucket.svg
│ │ ├── bug-fill.svg
│ │ ├── bug.svg
│ │ ├── building-add.svg
│ │ ├── building-check.svg
│ │ ├── building-dash.svg
│ │ ├── building-down.svg
│ │ ├── building-exclamation.svg
│ │ ├── building-fill-add.svg
│ │ ├── building-fill-check.svg
│ │ ├── building-fill-dash.svg
│ │ ├── building-fill-down.svg
│ │ ├── building-fill-exclamation.svg
│ │ ├── building-fill-gear.svg
│ │ ├── building-fill-lock.svg
│ │ ├── building-fill-slash.svg
│ │ ├── building-fill-up.svg
│ │ ├── building-fill-x.svg
│ │ ├── building-fill.svg
│ │ ├── building-gear.svg
│ │ ├── building-lock.svg
│ │ ├── building-slash.svg
│ │ ├── building-up.svg
│ │ ├── building-x.svg
│ │ ├── building.svg
│ │ ├── buildings-fill.svg
│ │ ├── buildings.svg
│ │ ├── bullseye.svg
│ │ ├── bus-front-fill.svg
│ │ ├── bus-front.svg
│ │ ├── c-circle-fill.svg
│ │ ├── c-circle.svg
│ │ ├── c-square-fill.svg
│ │ ├── c-square.svg
│ │ ├── cake-fill.svg
│ │ ├── cake.svg
│ │ ├── cake2-fill.svg
│ │ ├── cake2.svg
│ │ ├── calculator-fill.svg
│ │ ├── calculator.svg
│ │ ├── calendar-check-fill.svg
│ │ ├── calendar-check.svg
│ │ ├── calendar-date-fill.svg
│ │ ├── calendar-date.svg
│ │ ├── calendar-day-fill.svg
│ │ ├── calendar-day.svg
│ │ ├── calendar-event-fill.svg
│ │ ├── calendar-event.svg
│ │ ├── calendar-fill.svg
│ │ ├── calendar-heart-fill.svg
│ │ ├── calendar-heart.svg
│ │ ├── calendar-minus-fill.svg
│ │ ├── calendar-minus.svg
│ │ ├── calendar-month-fill.svg
│ │ ├── calendar-month.svg
│ │ ├── calendar-plus-fill.svg
│ │ ├── calendar-plus.svg
│ │ ├── calendar-range-fill.svg
│ │ ├── calendar-range.svg
│ │ ├── calendar-week-fill.svg
│ │ ├── calendar-week.svg
│ │ ├── calendar-x-fill.svg
│ │ ├── calendar-x.svg
│ │ ├── calendar.svg
│ │ ├── calendar2-check-fill.svg
│ │ ├── calendar2-check.svg
│ │ ├── calendar2-date-fill.svg
│ │ ├── calendar2-date.svg
│ │ ├── calendar2-day-fill.svg
│ │ ├── calendar2-day.svg
│ │ ├── calendar2-event-fill.svg
│ │ ├── calendar2-event.svg
│ │ ├── calendar2-fill.svg
│ │ ├── calendar2-heart-fill.svg
│ │ ├── calendar2-heart.svg
│ │ ├── calendar2-minus-fill.svg
│ │ ├── calendar2-minus.svg
│ │ ├── calendar2-month-fill.svg
│ │ ├── calendar2-month.svg
│ │ ├── calendar2-plus-fill.svg
│ │ ├── calendar2-plus.svg
│ │ ├── calendar2-range-fill.svg
│ │ ├── calendar2-range.svg
│ │ ├── calendar2-week-fill.svg
│ │ ├── calendar2-week.svg
│ │ ├── calendar2-x-fill.svg
│ │ ├── calendar2-x.svg
│ │ ├── calendar2.svg
│ │ ├── calendar3-event-fill.svg
│ │ ├── calendar3-event.svg
│ │ ├── calendar3-fill.svg
│ │ ├── calendar3-range-fill.svg
│ │ ├── calendar3-range.svg
│ │ ├── calendar3-week-fill.svg
│ │ ├── calendar3-week.svg
│ │ ├── calendar3.svg
│ │ ├── calendar4-event.svg
│ │ ├── calendar4-range.svg
│ │ ├── calendar4-week.svg
│ │ ├── calendar4.svg
│ │ ├── camera-fill.svg
│ │ ├── camera-reels-fill.svg
│ │ ├── camera-reels.svg
│ │ ├── camera-video-fill.svg
│ │ ├── camera-video-off-fill.svg
│ │ ├── camera-video-off.svg
│ │ ├── camera-video.svg
│ │ ├── camera.svg
│ │ ├── camera2.svg
│ │ ├── capslock-fill.svg
│ │ ├── capslock.svg
│ │ ├── capsule-pill.svg
│ │ ├── capsule.svg
│ │ ├── car-front-fill.svg
│ │ ├── car-front.svg
│ │ ├── card-checklist.svg
│ │ ├── card-heading.svg
│ │ ├── card-image.svg
│ │ ├── card-list.svg
│ │ ├── card-text.svg
│ │ ├── caret-down-fill.svg
│ │ ├── caret-down-square-fill.svg
│ │ ├── caret-down-square.svg
│ │ ├── caret-down.svg
│ │ ├── caret-left-fill.svg
│ │ ├── caret-left-square-fill.svg
│ │ ├── caret-left-square.svg
│ │ ├── caret-left.svg
│ │ ├── caret-right-fill.svg
│ │ ├── caret-right-square-fill.svg
│ │ ├── caret-right-square.svg
│ │ ├── caret-right.svg
│ │ ├── caret-up-fill.svg
│ │ ├── caret-up-square-fill.svg
│ │ ├── caret-up-square.svg
│ │ ├── caret-up.svg
│ │ ├── cart-check-fill.svg
│ │ ├── cart-check.svg
│ │ ├── cart-dash-fill.svg
│ │ ├── cart-dash.svg
│ │ ├── cart-fill.svg
│ │ ├── cart-plus-fill.svg
│ │ ├── cart-plus.svg
│ │ ├── cart-x-fill.svg
│ │ ├── cart-x.svg
│ │ ├── cart.svg
│ │ ├── cart2.svg
│ │ ├── cart3.svg
│ │ ├── cart4.svg
│ │ ├── cash-coin.svg
│ │ ├── cash-stack.svg
│ │ ├── cash.svg
│ │ ├── cassette-fill.svg
│ │ ├── cassette.svg
│ │ ├── cast.svg
│ │ ├── cc-circle-fill.svg
│ │ ├── cc-circle.svg
│ │ ├── cc-square-fill.svg
│ │ ├── cc-square.svg
│ │ ├── chat-dots-fill.svg
│ │ ├── chat-dots.svg
│ │ ├── chat-fill.svg
│ │ ├── chat-heart-fill.svg
│ │ ├── chat-heart.svg
│ │ ├── chat-left-dots-fill.svg
│ │ ├── chat-left-dots.svg
│ │ ├── chat-left-fill.svg
│ │ ├── chat-left-heart-fill.svg
│ │ ├── chat-left-heart.svg
│ │ ├── chat-left-quote-fill.svg
│ │ ├── chat-left-quote.svg
│ │ ├── chat-left-text-fill.svg
│ │ ├── chat-left-text.svg
│ │ ├── chat-left.svg
│ │ ├── chat-quote-fill.svg
│ │ ├── chat-quote.svg
│ │ ├── chat-right-dots-fill.svg
│ │ ├── chat-right-dots.svg
│ │ ├── chat-right-fill.svg
│ │ ├── chat-right-heart-fill.svg
│ │ ├── chat-right-heart.svg
│ │ ├── chat-right-quote-fill.svg
│ │ ├── chat-right-quote.svg
│ │ ├── chat-right-text-fill.svg
│ │ ├── chat-right-text.svg
│ │ ├── chat-right.svg
│ │ ├── chat-square-dots-fill.svg
│ │ ├── chat-square-dots.svg
│ │ ├── chat-square-fill.svg
│ │ ├── chat-square-heart-fill.svg
│ │ ├── chat-square-heart.svg
│ │ ├── chat-square-quote-fill.svg
│ │ ├── chat-square-quote.svg
│ │ ├── chat-square-text-fill.svg
│ │ ├── chat-square-text.svg
│ │ ├── chat-square.svg
│ │ ├── chat-text-fill.svg
│ │ ├── chat-text.svg
│ │ ├── chat.svg
│ │ ├── check-all.svg
│ │ ├── check-circle-fill.svg
│ │ ├── check-circle.svg
│ │ ├── check-lg.svg
│ │ ├── check-square-fill.svg
│ │ ├── check-square.svg
│ │ ├── check.svg
│ │ ├── check2-all.svg
│ │ ├── check2-circle.svg
│ │ ├── check2-square.svg
│ │ ├── check2.svg
│ │ ├── chevron-bar-contract.svg
│ │ ├── chevron-bar-down.svg
│ │ ├── chevron-bar-expand.svg
│ │ ├── chevron-bar-left.svg
│ │ ├── chevron-bar-right.svg
│ │ ├── chevron-bar-up.svg
│ │ ├── chevron-compact-down.svg
│ │ ├── chevron-compact-left.svg
│ │ ├── chevron-compact-right.svg
│ │ ├── chevron-compact-up.svg
│ │ ├── chevron-contract.svg
│ │ ├── chevron-double-down.svg
│ │ ├── chevron-double-left.svg
│ │ ├── chevron-double-right.svg
│ │ ├── chevron-double-up.svg
│ │ ├── chevron-down.svg
│ │ ├── chevron-expand.svg
│ │ ├── chevron-left.svg
│ │ ├── chevron-right.svg
│ │ ├── chevron-up.svg
│ │ ├── circle-fill.svg
│ │ ├── circle-half.svg
│ │ ├── circle-square.svg
│ │ ├── circle.svg
│ │ ├── clipboard-check-fill.svg
│ │ ├── clipboard-check.svg
│ │ ├── clipboard-data-fill.svg
│ │ ├── clipboard-data.svg
│ │ ├── clipboard-fill.svg
│ │ ├── clipboard-heart-fill.svg
│ │ ├── clipboard-heart.svg
│ │ ├── clipboard-minus-fill.svg
│ │ ├── clipboard-minus.svg
│ │ ├── clipboard-plus-fill.svg
│ │ ├── clipboard-plus.svg
│ │ ├── clipboard-pulse.svg
│ │ ├── clipboard-x-fill.svg
│ │ ├── clipboard-x.svg
│ │ ├── clipboard.svg
│ │ ├── clipboard2-check-fill.svg
│ │ ├── clipboard2-check.svg
│ │ ├── clipboard2-data-fill.svg
│ │ ├── clipboard2-data.svg
│ │ ├── clipboard2-fill.svg
│ │ ├── clipboard2-heart-fill.svg
│ │ ├── clipboard2-heart.svg
│ │ ├── clipboard2-minus-fill.svg
│ │ ├── clipboard2-minus.svg
│ │ ├── clipboard2-plus-fill.svg
│ │ ├── clipboard2-plus.svg
│ │ ├── clipboard2-pulse-fill.svg
│ │ ├── clipboard2-pulse.svg
│ │ ├── clipboard2-x-fill.svg
│ │ ├── clipboard2-x.svg
│ │ ├── clipboard2.svg
│ │ ├── clock-fill.svg
│ │ ├── clock-history.svg
│ │ ├── clock.svg
│ │ ├── cloud-arrow-down-fill.svg
│ │ ├── cloud-arrow-down.svg
│ │ ├── cloud-arrow-up-fill.svg
│ │ ├── cloud-arrow-up.svg
│ │ ├── cloud-check-fill.svg
│ │ ├── cloud-check.svg
│ │ ├── cloud-download-fill.svg
│ │ ├── cloud-download.svg
│ │ ├── cloud-drizzle-fill.svg
│ │ ├── cloud-drizzle.svg
│ │ ├── cloud-fill.svg
│ │ ├── cloud-fog-fill.svg
│ │ ├── cloud-fog.svg
│ │ ├── cloud-fog2-fill.svg
│ │ ├── cloud-fog2.svg
│ │ ├── cloud-hail-fill.svg
│ │ ├── cloud-hail.svg
│ │ ├── cloud-haze-fill.svg
│ │ ├── cloud-haze.svg
│ │ ├── cloud-haze2-fill.svg
│ │ ├── cloud-haze2.svg
│ │ ├── cloud-lightning-fill.svg
│ │ ├── cloud-lightning-rain-fill.svg
│ │ ├── cloud-lightning-rain.svg
│ │ ├── cloud-lightning.svg
│ │ ├── cloud-minus-fill.svg
│ │ ├── cloud-minus.svg
│ │ ├── cloud-moon-fill.svg
│ │ ├── cloud-moon.svg
│ │ ├── cloud-plus-fill.svg
│ │ ├── cloud-plus.svg
│ │ ├── cloud-rain-fill.svg
│ │ ├── cloud-rain-heavy-fill.svg
│ │ ├── cloud-rain-heavy.svg
│ │ ├── cloud-rain.svg
│ │ ├── cloud-slash-fill.svg
│ │ ├── cloud-slash.svg
│ │ ├── cloud-sleet-fill.svg
│ │ ├── cloud-sleet.svg
│ │ ├── cloud-snow-fill.svg
│ │ ├── cloud-snow.svg
│ │ ├── cloud-sun-fill.svg
│ │ ├── cloud-sun.svg
│ │ ├── cloud-upload-fill.svg
│ │ ├── cloud-upload.svg
│ │ ├── cloud.svg
│ │ ├── clouds-fill.svg
│ │ ├── clouds.svg
│ │ ├── cloudy-fill.svg
│ │ ├── cloudy.svg
│ │ ├── code-slash.svg
│ │ ├── code-square.svg
│ │ ├── code.svg
│ │ ├── coin.svg
│ │ ├── collection-fill.svg
│ │ ├── collection-play-fill.svg
│ │ ├── collection-play.svg
│ │ ├── collection.svg
│ │ ├── columns-gap.svg
│ │ ├── columns.svg
│ │ ├── command.svg
│ │ ├── compass-fill.svg
│ │ ├── compass.svg
│ │ ├── cone-striped.svg
│ │ ├── cone.svg
│ │ ├── controller.svg
│ │ ├── cookie.svg
│ │ ├── copy.svg
│ │ ├── cpu-fill.svg
│ │ ├── cpu.svg
│ │ ├── credit-card-2-back-fill.svg
│ │ ├── credit-card-2-back.svg
│ │ ├── credit-card-2-front-fill.svg
│ │ ├── credit-card-2-front.svg
│ │ ├── credit-card-fill.svg
│ │ ├── credit-card.svg
│ │ ├── crop.svg
│ │ ├── crosshair.svg
│ │ ├── crosshair2.svg
│ │ ├── cup-fill.svg
│ │ ├── cup-hot-fill.svg
│ │ ├── cup-hot.svg
│ │ ├── cup-straw.svg
│ │ ├── cup.svg
│ │ ├── currency-bitcoin.svg
│ │ ├── currency-dollar.svg
│ │ ├── currency-euro.svg
│ │ ├── currency-exchange.svg
│ │ ├── currency-pound.svg
│ │ ├── currency-rupee.svg
│ │ ├── currency-yen.svg
│ │ ├── cursor-fill.svg
│ │ ├── cursor-text.svg
│ │ ├── cursor.svg
│ │ ├── dash-circle-dotted.svg
│ │ ├── dash-circle-fill.svg
│ │ ├── dash-circle.svg
│ │ ├── dash-lg.svg
│ │ ├── dash-square-dotted.svg
│ │ ├── dash-square-fill.svg
│ │ ├── dash-square.svg
│ │ ├── dash.svg
│ │ ├── database-add.svg
│ │ ├── database-check.svg
│ │ ├── database-dash.svg
│ │ ├── database-down.svg
│ │ ├── database-exclamation.svg
│ │ ├── database-fill-add.svg
│ │ ├── database-fill-check.svg
│ │ ├── database-fill-dash.svg
│ │ ├── database-fill-down.svg
│ │ ├── database-fill-exclamation.svg
│ │ ├── database-fill-gear.svg
│ │ ├── database-fill-lock.svg
│ │ ├── database-fill-slash.svg
│ │ ├── database-fill-up.svg
│ │ ├── database-fill-x.svg
│ │ ├── database-fill.svg
│ │ ├── database-gear.svg
│ │ ├── database-lock.svg
│ │ ├── database-slash.svg
│ │ ├── database-up.svg
│ │ ├── database-x.svg
│ │ ├── database.svg
│ │ ├── device-hdd-fill.svg
│ │ ├── device-hdd.svg
│ │ ├── device-ssd-fill.svg
│ │ ├── device-ssd.svg
│ │ ├── diagram-2-fill.svg
│ │ ├── diagram-2.svg
│ │ ├── diagram-3-fill.svg
│ │ ├── diagram-3.svg
│ │ ├── diamond-fill.svg
│ │ ├── diamond-half.svg
│ │ ├── diamond.svg
│ │ ├── dice-1-fill.svg
│ │ ├── dice-1.svg
│ │ ├── dice-2-fill.svg
│ │ ├── dice-2.svg
│ │ ├── dice-3-fill.svg
│ │ ├── dice-3.svg
│ │ ├── dice-4-fill.svg
│ │ ├── dice-4.svg
│ │ ├── dice-5-fill.svg
│ │ ├── dice-5.svg
│ │ ├── dice-6-fill.svg
│ │ ├── dice-6.svg
│ │ ├── disc-fill.svg
│ │ ├── disc.svg
│ │ ├── discord.svg
│ │ ├── display-fill.svg
│ │ ├── display.svg
│ │ ├── displayport-fill.svg
│ │ ├── displayport.svg
│ │ ├── distribute-horizontal.svg
│ │ ├── distribute-vertical.svg
│ │ ├── door-closed-fill.svg
│ │ ├── door-closed.svg
│ │ ├── door-open-fill.svg
│ │ ├── door-open.svg
│ │ ├── dot.svg
│ │ ├── download.svg
│ │ ├── dpad-fill.svg
│ │ ├── dpad.svg
│ │ ├── dribbble.svg
│ │ ├── dropbox.svg
│ │ ├── droplet-fill.svg
│ │ ├── droplet-half.svg
│ │ ├── droplet.svg
│ │ ├── duffle-fill.svg
│ │ ├── duffle.svg
│ │ ├── ear-fill.svg
│ │ ├── ear.svg
│ │ ├── earbuds.svg
│ │ ├── easel-fill.svg
│ │ ├── easel.svg
│ │ ├── easel2-fill.svg
│ │ ├── easel2.svg
│ │ ├── easel3-fill.svg
│ │ ├── easel3.svg
│ │ ├── egg-fill.svg
│ │ ├── egg-fried.svg
│ │ ├── egg.svg
│ │ ├── eject-fill.svg
│ │ ├── eject.svg
│ │ ├── emoji-angry-fill.svg
│ │ ├── emoji-angry.svg
│ │ ├── emoji-astonished-fill.svg
│ │ ├── emoji-astonished.svg
│ │ ├── emoji-dizzy-fill.svg
│ │ ├── emoji-dizzy.svg
│ │ ├── emoji-expressionless-fill.svg
│ │ ├── emoji-expressionless.svg
│ │ ├── emoji-frown-fill.svg
│ │ ├── emoji-frown.svg
│ │ ├── emoji-grimace-fill.svg
│ │ ├── emoji-grimace.svg
│ │ ├── emoji-grin-fill.svg
│ │ ├── emoji-grin.svg
│ │ ├── emoji-heart-eyes-fill.svg
│ │ ├── emoji-heart-eyes.svg
│ │ ├── emoji-kiss-fill.svg
│ │ ├── emoji-kiss.svg
│ │ ├── emoji-laughing-fill.svg
│ │ ├── emoji-laughing.svg
│ │ ├── emoji-neutral-fill.svg
│ │ ├── emoji-neutral.svg
│ │ ├── emoji-smile-fill.svg
│ │ ├── emoji-smile-upside-down-fill.svg
│ │ ├── emoji-smile-upside-down.svg
│ │ ├── emoji-smile.svg
│ │ ├── emoji-sunglasses-fill.svg
│ │ ├── emoji-sunglasses.svg
│ │ ├── emoji-surprise-fill.svg
│ │ ├── emoji-surprise.svg
│ │ ├── emoji-tear-fill.svg
│ │ ├── emoji-tear.svg
│ │ ├── emoji-wink-fill.svg
│ │ ├── emoji-wink.svg
│ │ ├── envelope-arrow-down-fill.svg
│ │ ├── envelope-arrow-down.svg
│ │ ├── envelope-arrow-up-fill.svg
│ │ ├── envelope-arrow-up.svg
│ │ ├── envelope-at-fill.svg
│ │ ├── envelope-at.svg
│ │ ├── envelope-check-fill.svg
│ │ ├── envelope-check.svg
│ │ ├── envelope-dash-fill.svg
│ │ ├── envelope-dash.svg
│ │ ├── envelope-exclamation-fill.svg
│ │ ├── envelope-exclamation.svg
│ │ ├── envelope-fill.svg
│ │ ├── envelope-heart-fill.svg
│ │ ├── envelope-heart.svg
│ │ ├── envelope-open-fill.svg
│ │ ├── envelope-open-heart-fill.svg
│ │ ├── envelope-open-heart.svg
│ │ ├── envelope-open.svg
│ │ ├── envelope-paper-fill.svg
│ │ ├── envelope-paper-heart-fill.svg
│ │ ├── envelope-paper-heart.svg
│ │ ├── envelope-paper.svg
│ │ ├── envelope-plus-fill.svg
│ │ ├── envelope-plus.svg
│ │ ├── envelope-slash-fill.svg
│ │ ├── envelope-slash.svg
│ │ ├── envelope-x-fill.svg
│ │ ├── envelope-x.svg
│ │ ├── envelope.svg
│ │ ├── eraser-fill.svg
│ │ ├── eraser.svg
│ │ ├── escape.svg
│ │ ├── ethernet.svg
│ │ ├── ev-front-fill.svg
│ │ ├── ev-front.svg
│ │ ├── ev-station-fill.svg
│ │ ├── ev-station.svg
│ │ ├── exclamation-circle-fill.svg
│ │ ├── exclamation-circle.svg
│ │ ├── exclamation-diamond-fill.svg
│ │ ├── exclamation-diamond.svg
│ │ ├── exclamation-lg.svg
│ │ ├── exclamation-octagon-fill.svg
│ │ ├── exclamation-octagon.svg
│ │ ├── exclamation-square-fill.svg
│ │ ├── exclamation-square.svg
│ │ ├── exclamation-triangle-fill.svg
│ │ ├── exclamation-triangle.svg
│ │ ├── exclamation.svg
│ │ ├── exclude.svg
│ │ ├── explicit-fill.svg
│ │ ├── explicit.svg
│ │ ├── exposure.svg
│ │ ├── eye-fill.svg
│ │ ├── eye-slash-fill.svg
│ │ ├── eye-slash.svg
│ │ ├── eye.svg
│ │ ├── eyedropper.svg
│ │ ├── eyeglasses.svg
│ │ ├── facebook.svg
│ │ ├── fan.svg
│ │ ├── fast-forward-btn-fill.svg
│ │ ├── fast-forward-btn.svg
│ │ ├── fast-forward-circle-fill.svg
│ │ ├── fast-forward-circle.svg
│ │ ├── fast-forward-fill.svg
│ │ ├── fast-forward.svg
│ │ ├── feather.svg
│ │ ├── feather2.svg
│ │ ├── file-arrow-down-fill.svg
│ │ ├── file-arrow-down.svg
│ │ ├── file-arrow-up-fill.svg
│ │ ├── file-arrow-up.svg
│ │ ├── file-bar-graph-fill.svg
│ │ ├── file-bar-graph.svg
│ │ ├── file-binary-fill.svg
│ │ ├── file-binary.svg
│ │ ├── file-break-fill.svg
│ │ ├── file-break.svg
│ │ ├── file-check-fill.svg
│ │ ├── file-check.svg
│ │ ├── file-code-fill.svg
│ │ ├── file-code.svg
│ │ ├── file-diff-fill.svg
│ │ ├── file-diff.svg
│ │ ├── file-earmark-arrow-down-fill.svg
│ │ ├── file-earmark-arrow-down.svg
│ │ ├── file-earmark-arrow-up-fill.svg
│ │ ├── file-earmark-arrow-up.svg
│ │ ├── file-earmark-bar-graph-fill.svg
│ │ ├── file-earmark-bar-graph.svg
│ │ ├── file-earmark-binary-fill.svg
│ │ ├── file-earmark-binary.svg
│ │ ├── file-earmark-break-fill.svg
│ │ ├── file-earmark-break.svg
│ │ ├── file-earmark-check-fill.svg
│ │ ├── file-earmark-check.svg
│ │ ├── file-earmark-code-fill.svg
│ │ ├── file-earmark-code.svg
│ │ ├── file-earmark-diff-fill.svg
│ │ ├── file-earmark-diff.svg
│ │ ├── file-earmark-easel-fill.svg
│ │ ├── file-earmark-easel.svg
│ │ ├── file-earmark-excel-fill.svg
│ │ ├── file-earmark-excel.svg
│ │ ├── file-earmark-fill.svg
│ │ ├── file-earmark-font-fill.svg
│ │ ├── file-earmark-font.svg
│ │ ├── file-earmark-image-fill.svg
│ │ ├── file-earmark-image.svg
│ │ ├── file-earmark-lock-fill.svg
│ │ ├── file-earmark-lock.svg
│ │ ├── file-earmark-lock2-fill.svg
│ │ ├── file-earmark-lock2.svg
│ │ ├── file-earmark-medical-fill.svg
│ │ ├── file-earmark-medical.svg
│ │ ├── file-earmark-minus-fill.svg
│ │ ├── file-earmark-minus.svg
│ │ ├── file-earmark-music-fill.svg
│ │ ├── file-earmark-music.svg
│ │ ├── file-earmark-pdf-fill.svg
│ │ ├── file-earmark-pdf.svg
│ │ ├── file-earmark-person-fill.svg
│ │ ├── file-earmark-person.svg
│ │ ├── file-earmark-play-fill.svg
│ │ ├── file-earmark-play.svg
│ │ ├── file-earmark-plus-fill.svg
│ │ ├── file-earmark-plus.svg
│ │ ├── file-earmark-post-fill.svg
│ │ ├── file-earmark-post.svg
│ │ ├── file-earmark-ppt-fill.svg
│ │ ├── file-earmark-ppt.svg
│ │ ├── file-earmark-richtext-fill.svg
│ │ ├── file-earmark-richtext.svg
│ │ ├── file-earmark-ruled-fill.svg
│ │ ├── file-earmark-ruled.svg
│ │ ├── file-earmark-slides-fill.svg
│ │ ├── file-earmark-slides.svg
│ │ ├── file-earmark-spreadsheet-fill.svg
│ │ ├── file-earmark-spreadsheet.svg
│ │ ├── file-earmark-text-fill.svg
│ │ ├── file-earmark-text.svg
│ │ ├── file-earmark-word-fill.svg
│ │ ├── file-earmark-word.svg
│ │ ├── file-earmark-x-fill.svg
│ │ ├── file-earmark-x.svg
│ │ ├── file-earmark-zip-fill.svg
│ │ ├── file-earmark-zip.svg
│ │ ├── file-earmark.svg
│ │ ├── file-easel-fill.svg
│ │ ├── file-easel.svg
│ │ ├── file-excel-fill.svg
│ │ ├── file-excel.svg
│ │ ├── file-fill.svg
│ │ ├── file-font-fill.svg
│ │ ├── file-font.svg
│ │ ├── file-image-fill.svg
│ │ ├── file-image.svg
│ │ ├── file-lock-fill.svg
│ │ ├── file-lock.svg
│ │ ├── file-lock2-fill.svg
│ │ ├── file-lock2.svg
│ │ ├── file-medical-fill.svg
│ │ ├── file-medical.svg
│ │ ├── file-minus-fill.svg
│ │ ├── file-minus.svg
│ │ ├── file-music-fill.svg
│ │ ├── file-music.svg
│ │ ├── file-pdf-fill.svg
│ │ ├── file-pdf.svg
│ │ ├── file-person-fill.svg
│ │ ├── file-person.svg
│ │ ├── file-play-fill.svg
│ │ ├── file-play.svg
│ │ ├── file-plus-fill.svg
│ │ ├── file-plus.svg
│ │ ├── file-post-fill.svg
│ │ ├── file-post.svg
│ │ ├── file-ppt-fill.svg
│ │ ├── file-ppt.svg
│ │ ├── file-richtext-fill.svg
│ │ ├── file-richtext.svg
│ │ ├── file-ruled-fill.svg
│ │ ├── file-ruled.svg
│ │ ├── file-slides-fill.svg
│ │ ├── file-slides.svg
│ │ ├── file-spreadsheet-fill.svg
│ │ ├── file-spreadsheet.svg
│ │ ├── file-text-fill.svg
│ │ ├── file-text.svg
│ │ ├── file-word-fill.svg
│ │ ├── file-word.svg
│ │ ├── file-x-fill.svg
│ │ ├── file-x.svg
│ │ ├── file-zip-fill.svg
│ │ ├── file-zip.svg
│ │ ├── file.svg
│ │ ├── files-alt.svg
│ │ ├── files.svg
│ │ ├── filetype-aac.svg
│ │ ├── filetype-ai.svg
│ │ ├── filetype-bmp.svg
│ │ ├── filetype-cs.svg
│ │ ├── filetype-css.svg
│ │ ├── filetype-csv.svg
│ │ ├── filetype-doc.svg
│ │ ├── filetype-docx.svg
│ │ ├── filetype-exe.svg
│ │ ├── filetype-gif.svg
│ │ ├── filetype-heic.svg
│ │ ├── filetype-html.svg
│ │ ├── filetype-java.svg
│ │ ├── filetype-jpg.svg
│ │ ├── filetype-js.svg
│ │ ├── filetype-json.svg
│ │ ├── filetype-jsx.svg
│ │ ├── filetype-key.svg
│ │ ├── filetype-m4p.svg
│ │ ├── filetype-md.svg
│ │ ├── filetype-mdx.svg
│ │ ├── filetype-mov.svg
│ │ ├── filetype-mp3.svg
│ │ ├── filetype-mp4.svg
│ │ ├── filetype-otf.svg
│ │ ├── filetype-pdf.svg
│ │ ├── filetype-php.svg
│ │ ├── filetype-png.svg
│ │ ├── filetype-ppt.svg
│ │ ├── filetype-pptx.svg
│ │ ├── filetype-psd.svg
│ │ ├── filetype-py.svg
│ │ ├── filetype-raw.svg
│ │ ├── filetype-rb.svg
│ │ ├── filetype-sass.svg
│ │ ├── filetype-scss.svg
│ │ ├── filetype-sh.svg
│ │ ├── filetype-sql.svg
│ │ ├── filetype-svg.svg
│ │ ├── filetype-tiff.svg
│ │ ├── filetype-tsx.svg
│ │ ├── filetype-ttf.svg
│ │ ├── filetype-txt.svg
│ │ ├── filetype-wav.svg
│ │ ├── filetype-woff.svg
│ │ ├── filetype-xls.svg
│ │ ├── filetype-xlsx.svg
│ │ ├── filetype-xml.svg
│ │ ├── filetype-yml.svg
│ │ ├── film.svg
│ │ ├── filter-circle-fill.svg
│ │ ├── filter-circle.svg
│ │ ├── filter-left.svg
│ │ ├── filter-right.svg
│ │ ├── filter-square-fill.svg
│ │ ├── filter-square.svg
│ │ ├── filter.svg
│ │ ├── fingerprint.svg
│ │ ├── fire.svg
│ │ ├── flag-fill.svg
│ │ ├── flag.svg
│ │ ├── floppy-fill.svg
│ │ ├── floppy.svg
│ │ ├── floppy2-fill.svg
│ │ ├── floppy2.svg
│ │ ├── flower1.svg
│ │ ├── flower2.svg
│ │ ├── flower3.svg
│ │ ├── folder-check.svg
│ │ ├── folder-fill.svg
│ │ ├── folder-minus.svg
│ │ ├── folder-plus.svg
│ │ ├── folder-symlink-fill.svg
│ │ ├── folder-symlink.svg
│ │ ├── folder-x.svg
│ │ ├── folder.svg
│ │ ├── folder2-open.svg
│ │ ├── folder2.svg
│ │ ├── font/
│ │ │ ├── bootstrap-icons.css
│ │ │ ├── bootstrap-icons.json
│ │ │ ├── bootstrap-icons.min.css
│ │ │ ├── bootstrap-icons.scss
│ │ │ └── fonts/
│ │ │     ├── bootstrap-icons.woff
│ │ │     └── bootstrap-icons.woff2
│ │ ├── fonts.svg
│ │ ├── forward-fill.svg
│ │ ├── forward.svg
│ │ ├── front.svg
│ │ ├── fuel-pump-diesel-fill.svg
│ │ ├── fuel-pump-diesel.svg
│ │ ├── fuel-pump-fill.svg
│ │ ├── fuel-pump.svg
│ │ ├── fullscreen-exit.svg
│ │ ├── fullscreen.svg
│ │ ├── funnel-fill.svg
│ │ ├── funnel.svg
│ │ ├── gear-fill.svg
│ │ ├── gear-wide-connected.svg
│ │ ├── gear-wide.svg
│ │ ├── gear.svg
│ │ ├── gem.svg
│ │ ├── gender-ambiguous.svg
│ │ ├── gender-female.svg
│ │ ├── gender-male.svg
│ │ ├── gender-neuter.svg
│ │ ├── gender-trans.svg
│ │ ├── geo-alt-fill.svg
│ │ ├── geo-alt.svg
│ │ ├── geo-fill.svg
│ │ ├── geo.svg
│ │ ├── gift-fill.svg
│ │ ├── gift.svg
│ │ ├── git.svg
│ │ ├── github.svg
│ │ ├── gitlab.svg
│ │ ├── globe-americas.svg
│ │ ├── globe-asia-australia.svg
│ │ ├── globe-central-south-asia.svg
│ │ ├── globe-europe-africa.svg
│ │ ├── globe.svg
│ │ ├── globe2.svg
│ │ ├── google-play.svg
│ │ ├── google.svg
│ │ ├── gpu-card.svg
│ │ ├── graph-down-arrow.svg
│ │ ├── graph-down.svg
│ │ ├── graph-up-arrow.svg
│ │ ├── graph-up.svg
│ │ ├── grid-1x2-fill.svg
│ │ ├── grid-1x2.svg
│ │ ├── grid-3x2-gap-fill.svg
│ │ ├── grid-3x2-gap.svg
│ │ ├── grid-3x2.svg
│ │ ├── grid-3x3-gap-fill.svg
│ │ ├── grid-3x3-gap.svg
│ │ ├── grid-3x3.svg
│ │ ├── grid-fill.svg
│ │ ├── grid.svg
│ │ ├── grip-horizontal.svg
│ │ ├── grip-vertical.svg
│ │ ├── h-circle-fill.svg
│ │ ├── h-circle.svg
│ │ ├── h-square-fill.svg
│ │ ├── h-square.svg
│ │ ├── hammer.svg
│ │ ├── hand-index-fill.svg
│ │ ├── hand-index-thumb-fill.svg
│ │ ├── hand-index-thumb.svg
│ │ ├── hand-index.svg
│ │ ├── hand-thumbs-down-fill.svg
│ │ ├── hand-thumbs-down.svg
│ │ ├── hand-thumbs-up-fill.svg
│ │ ├── hand-thumbs-up.svg
│ │ ├── handbag-fill.svg
│ │ ├── handbag.svg
│ │ ├── hash.svg
│ │ ├── hdd-fill.svg
│ │ ├── hdd-network-fill.svg
│ │ ├── hdd-network.svg
│ │ ├── hdd-rack-fill.svg
│ │ ├── hdd-rack.svg
│ │ ├── hdd-stack-fill.svg
│ │ ├── hdd-stack.svg
│ │ ├── hdd.svg
│ │ ├── hdmi-fill.svg
│ │ ├── hdmi.svg
│ │ ├── headphones.svg
│ │ ├── headset-vr.svg
│ │ ├── headset.svg
│ │ ├── heart-arrow.svg
│ │ ├── heart-fill.svg
│ │ ├── heart-half.svg
│ │ ├── heart-pulse-fill.svg
│ │ ├── heart-pulse.svg
│ │ ├── heart.svg
│ │ ├── heartbreak-fill.svg
│ │ ├── heartbreak.svg
│ │ ├── hearts.svg
│ │ ├── heptagon-fill.svg
│ │ ├── heptagon-half.svg
│ │ ├── heptagon.svg
│ │ ├── hexagon-fill.svg
│ │ ├── hexagon-half.svg
│ │ ├── hexagon.svg
│ │ ├── highlighter.svg
│ │ ├── highlights.svg
│ │ ├── hospital-fill.svg
│ │ ├── hospital.svg
│ │ ├── hourglass-bottom.svg
│ │ ├── hourglass-split.svg
│ │ ├── hourglass-top.svg
│ │ ├── hourglass.svg
│ │ ├── house-add-fill.svg
│ │ ├── house-add.svg
│ │ ├── house-check-fill.svg
│ │ ├── house-check.svg
│ │ ├── house-dash-fill.svg
│ │ ├── house-dash.svg
│ │ ├── house-door-fill.svg
│ │ ├── house-door.svg
│ │ ├── house-down-fill.svg
│ │ ├── house-down.svg
│ │ ├── house-exclamation-fill.svg
│ │ ├── house-exclamation.svg
│ │ ├── house-fill.svg
│ │ ├── house-gear-fill.svg
│ │ ├── house-gear.svg
│ │ ├── house-heart-fill.svg
│ │ ├── house-heart.svg
│ │ ├── house-lock-fill.svg
│ │ ├── house-lock.svg
│ │ ├── house-slash-fill.svg
│ │ ├── house-slash.svg
│ │ ├── house-up-fill.svg
│ │ ├── house-up.svg
│ │ ├── house-x-fill.svg
│ │ ├── house-x.svg
│ │ ├── house.svg
│ │ ├── houses-fill.svg
│ │ ├── houses.svg
│ │ ├── hr.svg
│ │ ├── hurricane.svg
│ │ ├── hypnotize.svg
│ │ ├── image-alt.svg
│ │ ├── image-fill.svg
│ │ ├── image.svg
│ │ ├── images.svg
│ │ ├── inbox-fill.svg
│ │ ├── inbox.svg
│ │ ├── inboxes-fill.svg
│ │ ├── inboxes.svg
│ │ ├── incognito.svg
│ │ ├── indent.svg
│ │ ├── infinity.svg
│ │ ├── info-circle-fill.svg
│ │ ├── info-circle.svg
│ │ ├── info-lg.svg
│ │ ├── info-square-fill.svg
│ │ ├── info-square.svg
│ │ ├── info.svg
│ │ ├── input-cursor-text.svg
│ │ ├── input-cursor.svg
│ │ ├── instagram.svg
│ │ ├── intersect.svg
│ │ ├── journal-album.svg
│ │ ├── journal-arrow-down.svg
│ │ ├── journal-arrow-up.svg
│ │ ├── journal-bookmark-fill.svg
│ │ ├── journal-bookmark.svg
│ │ ├── journal-check.svg
│ │ ├── journal-code.svg
│ │ ├── journal-medical.svg
│ │ ├── journal-minus.svg
│ │ ├── journal-plus.svg
│ │ ├── journal-richtext.svg
│ │ ├── journal-text.svg
│ │ ├── journal-x.svg
│ │ ├── journal.svg
│ │ ├── journals.svg
│ │ ├── joystick.svg
│ │ ├── justify-left.svg
│ │ ├── justify-right.svg
│ │ ├── justify.svg
│ │ ├── kanban-fill.svg
│ │ ├── kanban.svg
│ │ ├── key-fill.svg
│ │ ├── key.svg
│ │ ├── keyboard-fill.svg
│ │ ├── keyboard.svg
│ │ ├── ladder.svg
│ │ ├── lamp-fill.svg
│ │ ├── lamp.svg
│ │ ├── laptop-fill.svg
│ │ ├── laptop.svg
│ │ ├── layer-backward.svg
│ │ ├── layer-forward.svg
│ │ ├── layers-fill.svg
│ │ ├── layers-half.svg
│ │ ├── layers.svg
│ │ ├── layout-sidebar-inset-reverse.svg
│ │ ├── layout-sidebar-inset.svg
│ │ ├── layout-sidebar-reverse.svg
│ │ ├── layout-sidebar.svg
│ │ ├── layout-split.svg
│ │ ├── layout-text-sidebar-reverse.svg
│ │ ├── layout-text-sidebar.svg
│ │ ├── layout-text-window-reverse.svg
│ │ ├── layout-text-window.svg
│ │ ├── layout-three-columns.svg
│ │ ├── layout-wtf.svg
│ │ ├── life-preserver.svg
│ │ ├── lightbulb-fill.svg
│ │ ├── lightbulb-off-fill.svg
│ │ ├── lightbulb-off.svg
│ │ ├── lightbulb.svg
│ │ ├── lightning-charge-fill.svg
│ │ ├── lightning-charge.svg
│ │ ├── lightning-fill.svg
│ │ ├── lightning.svg
│ │ ├── line.svg
│ │ ├── link-45deg.svg
│ │ ├── link.svg
│ │ ├── linkedin.svg
│ │ ├── list-check.svg
│ │ ├── list-columns-reverse.svg
│ │ ├── list-columns.svg
│ │ ├── list-nested.svg
│ │ ├── list-ol.svg
│ │ ├── list-stars.svg
│ │ ├── list-task.svg
│ │ ├── list-ul.svg
│ │ ├── list.svg
│ │ ├── lock-fill.svg
│ │ ├── lock.svg
│ │ ├── luggage-fill.svg
│ │ ├── luggage.svg
│ │ ├── lungs-fill.svg
│ │ ├── lungs.svg
│ │ ├── magic.svg
│ │ ├── magnet-fill.svg
│ │ ├── magnet.svg
│ │ ├── mailbox-flag.svg
│ │ ├── mailbox.svg
│ │ ├── mailbox2-flag.svg
│ │ ├── mailbox2.svg
│ │ ├── map-fill.svg
│ │ ├── map.svg
│ │ ├── markdown-fill.svg
│ │ ├── markdown.svg
│ │ ├── marker-tip.svg
│ │ ├── mask.svg
│ │ ├── mastodon.svg
│ │ ├── medium.svg
│ │ ├── megaphone-fill.svg
│ │ ├── megaphone.svg
│ │ ├── memory.svg
│ │ ├── menu-app-fill.svg
│ │ ├── menu-app.svg
│ │ ├── menu-button-fill.svg
│ │ ├── menu-button-wide-fill.svg
│ │ ├── menu-button-wide.svg
│ │ ├── menu-button.svg
│ │ ├── menu-down.svg
│ │ ├── menu-up.svg
│ │ ├── messenger.svg
│ │ ├── meta.svg
│ │ ├── mic-fill.svg
│ │ ├── mic-mute-fill.svg
│ │ ├── mic-mute.svg
│ │ ├── mic.svg
│ │ ├── microsoft-teams.svg
│ │ ├── microsoft.svg
│ │ ├── minecart-loaded.svg
│ │ ├── minecart.svg
│ │ ├── modem-fill.svg
│ │ ├── modem.svg
│ │ ├── moisture.svg
│ │ ├── moon-fill.svg
│ │ ├── moon-stars-fill.svg
│ │ ├── moon-stars.svg
│ │ ├── moon.svg
│ │ ├── mortarboard-fill.svg
│ │ ├── mortarboard.svg
│ │ ├── motherboard-fill.svg
│ │ ├── motherboard.svg
│ │ ├── mouse-fill.svg
│ │ ├── mouse.svg
│ │ ├── mouse2-fill.svg
│ │ ├── mouse2.svg
│ │ ├── mouse3-fill.svg
│ │ ├── mouse3.svg
│ │ ├── music-note-beamed.svg
│ │ ├── music-note-list.svg
│ │ ├── music-note.svg
│ │ ├── music-player-fill.svg
│ │ ├── music-player.svg
│ │ ├── newspaper.svg
│ │ ├── nintendo-switch.svg
│ │ ├── node-minus-fill.svg
│ │ ├── node-minus.svg
│ │ ├── node-plus-fill.svg
│ │ ├── node-plus.svg
│ │ ├── noise-reduction.svg
│ │ ├── nut-fill.svg
│ │ ├── nut.svg
│ │ ├── nvidia.svg
│ │ ├── nvme-fill.svg
│ │ ├── nvme.svg
│ │ ├── octagon-fill.svg
│ │ ├── octagon-half.svg
│ │ ├── octagon.svg
│ │ ├── opencollective.svg
│ │ ├── optical-audio-fill.svg
│ │ ├── optical-audio.svg
│ │ ├── option.svg
│ │ ├── outlet.svg
│ │ ├── p-circle-fill.svg
│ │ ├── p-circle.svg
│ │ ├── p-square-fill.svg
│ │ ├── p-square.svg
│ │ ├── paint-bucket.svg
│ │ ├── palette-fill.svg
│ │ ├── palette.svg
│ │ ├── palette2.svg
│ │ ├── paperclip.svg
│ │ ├── paragraph.svg
│ │ ├── pass-fill.svg
│ │ ├── pass.svg
│ │ ├── passport-fill.svg
│ │ ├── passport.svg
│ │ ├── patch-check-fill.svg
│ │ ├── patch-check.svg
│ │ ├── patch-exclamation-fill.svg
│ │ ├── patch-exclamation.svg
│ │ ├── patch-minus-fill.svg
│ │ ├── patch-minus.svg
│ │ ├── patch-plus-fill.svg
│ │ ├── patch-plus.svg
│ │ ├── patch-question-fill.svg
│ │ ├── patch-question.svg
│ │ ├── pause-btn-fill.svg
│ │ ├── pause-btn.svg
│ │ ├── pause-circle-fill.svg
│ │ ├── pause-circle.svg
│ │ ├── pause-fill.svg
│ │ ├── pause.svg
│ │ ├── paypal.svg
│ │ ├── pc-display-horizontal.svg
│ │ ├── pc-display.svg
│ │ ├── pc-horizontal.svg
│ │ ├── pc.svg
│ │ ├── pci-card-network.svg
│ │ ├── pci-card-sound.svg
│ │ ├── pci-card.svg
│ │ ├── peace-fill.svg
│ │ ├── peace.svg
│ │ ├── pen-fill.svg
│ │ ├── pen.svg
│ │ ├── pencil-fill.svg
│ │ ├── pencil-square.svg
│ │ ├── pencil.svg
│ │ ├── pentagon-fill.svg
│ │ ├── pentagon-half.svg
│ │ ├── pentagon.svg
│ │ ├── people-fill.svg
│ │ ├── people.svg
│ │ ├── percent.svg
│ │ ├── person-add.svg
│ │ ├── person-arms-up.svg
│ │ ├── person-badge-fill.svg
│ │ ├── person-badge.svg
│ │ ├── person-bounding-box.svg
│ │ ├── person-check-fill.svg
│ │ ├── person-check.svg
│ │ ├── person-circle.svg
│ │ ├── person-dash-fill.svg
│ │ ├── person-dash.svg
│ │ ├── person-down.svg
│ │ ├── person-exclamation.svg
│ │ ├── person-fill-add.svg
│ │ ├── person-fill-check.svg
│ │ ├── person-fill-dash.svg
│ │ ├── person-fill-down.svg
│ │ ├── person-fill-exclamation.svg
│ │ ├── person-fill-gear.svg
│ │ ├── person-fill-lock.svg
│ │ ├── person-fill-slash.svg
│ │ ├── person-fill-up.svg
│ │ ├── person-fill-x.svg
│ │ ├── person-fill.svg
│ │ ├── person-gear.svg
│ │ ├── person-heart.svg
│ │ ├── person-hearts.svg
│ │ ├── person-lines-fill.svg
│ │ ├── person-lock.svg
│ │ ├── person-plus-fill.svg
│ │ ├── person-plus.svg
│ │ ├── person-raised-hand.svg
│ │ ├── person-rolodex.svg
│ │ ├── person-slash.svg
│ │ ├── person-square.svg
│ │ ├── person-standing-dress.svg
│ │ ├── person-standing.svg
│ │ ├── person-up.svg
│ │ ├── person-vcard-fill.svg
│ │ ├── person-vcard.svg
│ │ ├── person-video.svg
│ │ ├── person-video2.svg
│ │ ├── person-video3.svg
│ │ ├── person-walking.svg
│ │ ├── person-wheelchair.svg
│ │ ├── person-workspace.svg
│ │ ├── person-x-fill.svg
│ │ ├── person-x.svg
│ │ ├── person.svg
│ │ ├── phone-fill.svg
│ │ ├── phone-flip.svg
│ │ ├── phone-landscape-fill.svg
│ │ ├── phone-landscape.svg
│ │ ├── phone-vibrate-fill.svg
│ │ ├── phone-vibrate.svg
│ │ ├── phone.svg
│ │ ├── pie-chart-fill.svg
│ │ ├── pie-chart.svg
│ │ ├── piggy-bank-fill.svg
│ │ ├── piggy-bank.svg
│ │ ├── pin-angle-fill.svg
│ │ ├── pin-angle.svg
│ │ ├── pin-fill.svg
│ │ ├── pin-map-fill.svg
│ │ ├── pin-map.svg
│ │ ├── pin.svg
│ │ ├── pinterest.svg
│ │ ├── pip-fill.svg
│ │ ├── pip.svg
│ │ ├── play-btn-fill.svg
│ │ ├── play-btn.svg
│ │ ├── play-circle-fill.svg
│ │ ├── play-circle.svg
│ │ ├── play-fill.svg
│ │ ├── play.svg
│ │ ├── playstation.svg
│ │ ├── plug-fill.svg
│ │ ├── plug.svg
│ │ ├── plugin.svg
│ │ ├── plus-circle-dotted.svg
│ │ ├── plus-circle-fill.svg
│ │ ├── plus-circle.svg
│ │ ├── plus-lg.svg
│ │ ├── plus-slash-minus.svg
│ │ ├── plus-square-dotted.svg
│ │ ├── plus-square-fill.svg
│ │ ├── plus-square.svg
│ │ ├── plus.svg
│ │ ├── postage-fill.svg
│ │ ├── postage-heart-fill.svg
│ │ ├── postage-heart.svg
│ │ ├── postage.svg
│ │ ├── postcard-fill.svg
│ │ ├── postcard-heart-fill.svg
│ │ ├── postcard-heart.svg
│ │ ├── postcard.svg
│ │ ├── power.svg
│ │ ├── prescription.svg
│ │ ├── prescription2.svg
│ │ ├── printer-fill.svg
│ │ ├── printer.svg
│ │ ├── projector-fill.svg
│ │ ├── projector.svg
│ │ ├── puzzle-fill.svg
│ │ ├── puzzle.svg
│ │ ├── qr-code-scan.svg
│ │ ├── qr-code.svg
│ │ ├── question-circle-fill.svg
│ │ ├── question-circle.svg
│ │ ├── question-diamond-fill.svg
│ │ ├── question-diamond.svg
│ │ ├── question-lg.svg
│ │ ├── question-octagon-fill.svg
│ │ ├── question-octagon.svg
│ │ ├── question-square-fill.svg
│ │ ├── question-square.svg
│ │ ├── question.svg
│ │ ├── quora.svg
│ │ ├── quote.svg
│ │ ├── r-circle-fill.svg
│ │ ├── r-circle.svg
│ │ ├── r-square-fill.svg
│ │ ├── r-square.svg
│ │ ├── radar.svg
│ │ ├── radioactive.svg
│ │ ├── rainbow.svg
│ │ ├── receipt-cutoff.svg
│ │ ├── receipt.svg
│ │ ├── reception-0.svg
│ │ ├── reception-1.svg
│ │ ├── reception-2.svg
│ │ ├── reception-3.svg
│ │ ├── reception-4.svg
│ │ ├── record-btn-fill.svg
│ │ ├── record-btn.svg
│ │ ├── record-circle-fill.svg
│ │ ├── record-circle.svg
│ │ ├── record-fill.svg
│ │ ├── record.svg
│ │ ├── record2-fill.svg
│ │ ├── record2.svg
│ │ ├── recycle.svg
│ │ ├── reddit.svg
│ │ ├── regex.svg
│ │ ├── repeat-1.svg
│ │ ├── repeat.svg
│ │ ├── reply-all-fill.svg
│ │ ├── reply-all.svg
│ │ ├── reply-fill.svg
│ │ ├── reply.svg
│ │ ├── rewind-btn-fill.svg
│ │ ├── rewind-btn.svg
│ │ ├── rewind-circle-fill.svg
│ │ ├── rewind-circle.svg
│ │ ├── rewind-fill.svg
│ │ ├── rewind.svg
│ │ ├── robot.svg
│ │ ├── rocket-fill.svg
│ │ ├── rocket-takeoff-fill.svg
│ │ ├── rocket-takeoff.svg
│ │ ├── rocket.svg
│ │ ├── router-fill.svg
│ │ ├── router.svg
│ │ ├── rss-fill.svg
│ │ ├── rss.svg
│ │ ├── rulers.svg
│ │ ├── safe-fill.svg
│ │ ├── safe.svg
│ │ ├── safe2-fill.svg
│ │ ├── safe2.svg
│ │ ├── save-fill.svg
│ │ ├── save.svg
│ │ ├── save2-fill.svg
│ │ ├── save2.svg
│ │ ├── scissors.svg
│ │ ├── scooter.svg
│ │ ├── screwdriver.svg
│ │ ├── sd-card-fill.svg
│ │ ├── sd-card.svg
│ │ ├── search-heart-fill.svg
│ │ ├── search-heart.svg
│ │ ├── search.svg
│ │ ├── segmented-nav.svg
│ │ ├── send-arrow-down-fill.svg
│ │ ├── send-arrow-down.svg
│ │ ├── send-arrow-up-fill.svg
│ │ ├── send-arrow-up.svg
│ │ ├── send-check-fill.svg
│ │ ├── send-check.svg
│ │ ├── send-dash-fill.svg
│ │ ├── send-dash.svg
│ │ ├── send-exclamation-fill.svg
│ │ ├── send-exclamation.svg
│ │ ├── send-fill.svg
│ │ ├── send-plus-fill.svg
│ │ ├── send-plus.svg
│ │ ├── send-slash-fill.svg
│ │ ├── send-slash.svg
│ │ ├── send-x-fill.svg
│ │ ├── send-x.svg
│ │ ├── send.svg
│ │ ├── server.svg
│ │ ├── shadows.svg
│ │ ├── share-fill.svg
│ │ ├── share.svg
│ │ ├── shield-check.svg
│ │ ├── shield-exclamation.svg
│ │ ├── shield-fill-check.svg
│ │ ├── shield-fill-exclamation.svg
│ │ ├── shield-fill-minus.svg
│ │ ├── shield-fill-plus.svg
│ │ ├── shield-fill-x.svg
│ │ ├── shield-fill.svg
│ │ ├── shield-lock-fill.svg
│ │ ├── shield-lock.svg
│ │ ├── shield-minus.svg
│ │ ├── shield-plus.svg
│ │ ├── shield-shaded.svg
│ │ ├── shield-slash-fill.svg
│ │ ├── shield-slash.svg
│ │ ├── shield-x.svg
│ │ ├── shield.svg
│ │ ├── shift-fill.svg
│ │ ├── shift.svg
│ │ ├── shop-window.svg
│ │ ├── shop.svg
│ │ ├── shuffle.svg
│ │ ├── sign-dead-end-fill.svg
│ │ ├── sign-dead-end.svg
│ │ ├── sign-do-not-enter-fill.svg
│ │ ├── sign-do-not-enter.svg
│ │ ├── sign-intersection-fill.svg
│ │ ├── sign-intersection-side-fill.svg
│ │ ├── sign-intersection-side.svg
│ │ ├── sign-intersection-t-fill.svg
│ │ ├── sign-intersection-t.svg
│ │ ├── sign-intersection-y-fill.svg
│ │ ├── sign-intersection-y.svg
│ │ ├── sign-intersection.svg
│ │ ├── sign-merge-left-fill.svg
│ │ ├── sign-merge-left.svg
│ │ ├── sign-merge-right-fill.svg
│ │ ├── sign-merge-right.svg
│ │ ├── sign-no-left-turn-fill.svg
│ │ ├── sign-no-left-turn.svg
│ │ ├── sign-no-parking-fill.svg
│ │ ├── sign-no-parking.svg
│ │ ├── sign-no-right-turn-fill.svg
│ │ ├── sign-no-right-turn.svg
│ │ ├── sign-railroad-fill.svg
│ │ ├── sign-railroad.svg
│ │ ├── sign-stop-fill.svg
│ │ ├── sign-stop-lights-fill.svg
│ │ ├── sign-stop-lights.svg
│ │ ├── sign-stop.svg
│ │ ├── sign-turn-left-fill.svg
│ │ ├── sign-turn-left.svg
│ │ ├── sign-turn-right-fill.svg
│ │ ├── sign-turn-right.svg
│ │ ├── sign-turn-slight-left-fill.svg
│ │ ├── sign-turn-slight-left.svg
│ │ ├── sign-turn-slight-right-fill.svg
│ │ ├── sign-turn-slight-right.svg
│ │ ├── sign-yield-fill.svg
│ │ ├── sign-yield.svg
│ │ ├── signal.svg
│ │ ├── signpost-2-fill.svg
│ │ ├── signpost-2.svg
│ │ ├── signpost-fill.svg
│ │ ├── signpost-split-fill.svg
│ │ ├── signpost-split.svg
│ │ ├── signpost.svg
│ │ ├── sim-fill.svg
│ │ ├── sim-slash-fill.svg
│ │ ├── sim-slash.svg
│ │ ├── sim.svg
│ │ ├── sina-weibo.svg
│ │ ├── skip-backward-btn-fill.svg
│ │ ├── skip-backward-btn.svg
│ │ ├── skip-backward-circle-fill.svg
│ │ ├── skip-backward-circle.svg
│ │ ├── skip-backward-fill.svg
│ │ ├── skip-backward.svg
│ │ ├── skip-end-btn-fill.svg
│ │ ├── skip-end-btn.svg
│ │ ├── skip-end-circle-fill.svg
│ │ ├── skip-end-circle.svg
│ │ ├── skip-end-fill.svg
│ │ ├── skip-end.svg
│ │ ├── skip-forward-btn-fill.svg
│ │ ├── skip-forward-btn.svg
│ │ ├── skip-forward-circle-fill.svg
│ │ ├── skip-forward-circle.svg
│ │ ├── skip-forward-fill.svg
│ │ ├── skip-forward.svg
│ │ ├── skip-start-btn-fill.svg
│ │ ├── skip-start-btn.svg
│ │ ├── skip-start-circle-fill.svg
│ │ ├── skip-start-circle.svg
│ │ ├── skip-start-fill.svg
│ │ ├── skip-start.svg
│ │ ├── skype.svg
│ │ ├── slack.svg
│ │ ├── slash-circle-fill.svg
│ │ ├── slash-circle.svg
│ │ ├── slash-lg.svg
│ │ ├── slash-square-fill.svg
│ │ ├── slash-square.svg
│ │ ├── slash.svg
│ │ ├── sliders.svg
│ │ ├── sliders2-vertical.svg
│ │ ├── sliders2.svg
│ │ ├── smartwatch.svg
│ │ ├── snapchat.svg
│ │ ├── snow.svg
│ │ ├── snow2.svg
│ │ ├── snow3.svg
│ │ ├── sort-alpha-down-alt.svg
│ │ ├── sort-alpha-down.svg
│ │ ├── sort-alpha-up-alt.svg
│ │ ├── sort-alpha-up.svg
│ │ ├── sort-down-alt.svg
│ │ ├── sort-down.svg
│ │ ├── sort-numeric-down-alt.svg
│ │ ├── sort-numeric-down.svg
│ │ ├── sort-numeric-up-alt.svg
│ │ ├── sort-numeric-up.svg
│ │ ├── sort-up-alt.svg
│ │ ├── sort-up.svg
│ │ ├── soundwave.svg
│ │ ├── sourceforge.svg
│ │ ├── speaker-fill.svg
│ │ ├── speaker.svg
│ │ ├── speedometer.svg
│ │ ├── speedometer2.svg
│ │ ├── spellcheck.svg
│ │ ├── spotify.svg
│ │ ├── square-fill.svg
│ │ ├── square-half.svg
│ │ ├── square.svg
│ │ ├── stack-overflow.svg
│ │ ├── stack.svg
│ │ ├── star-fill.svg
│ │ ├── star-half.svg
│ │ ├── star.svg
│ │ ├── stars.svg
│ │ ├── steam.svg
│ │ ├── stickies-fill.svg
│ │ ├── stickies.svg
│ │ ├── sticky-fill.svg
│ │ ├── sticky.svg
│ │ ├── stop-btn-fill.svg
│ │ ├── stop-btn.svg
│ │ ├── stop-circle-fill.svg
│ │ ├── stop-circle.svg
│ │ ├── stop-fill.svg
│ │ ├── stop.svg
│ │ ├── stoplights-fill.svg
│ │ ├── stoplights.svg
│ │ ├── stopwatch-fill.svg
│ │ ├── stopwatch.svg
│ │ ├── strava.svg
│ │ ├── stripe.svg
│ │ ├── subscript.svg
│ │ ├── substack.svg
│ │ ├── subtract.svg
│ │ ├── suit-club-fill.svg
│ │ ├── suit-club.svg
│ │ ├── suit-diamond-fill.svg
│ │ ├── suit-diamond.svg
│ │ ├── suit-heart-fill.svg
│ │ ├── suit-heart.svg
│ │ ├── suit-spade-fill.svg
│ │ ├── suit-spade.svg
│ │ ├── suitcase-fill.svg
│ │ ├── suitcase-lg-fill.svg
│ │ ├── suitcase-lg.svg
│ │ ├── suitcase.svg
│ │ ├── suitcase2-fill.svg
│ │ ├── suitcase2.svg
│ │ ├── sun-fill.svg
│ │ ├── sun.svg
│ │ ├── sunglasses.svg
│ │ ├── sunrise-fill.svg
│ │ ├── sunrise.svg
│ │ ├── sunset-fill.svg
│ │ ├── sunset.svg
│ │ ├── superscript.svg
│ │ ├── symmetry-horizontal.svg
│ │ ├── symmetry-vertical.svg
│ │ ├── table.svg
│ │ ├── tablet-fill.svg
│ │ ├── tablet-landscape-fill.svg
│ │ ├── tablet-landscape.svg
│ │ ├── tablet.svg
│ │ ├── tag-fill.svg
│ │ ├── tag.svg
│ │ ├── tags-fill.svg
│ │ ├── tags.svg
│ │ ├── taxi-front-fill.svg
│ │ ├── taxi-front.svg
│ │ ├── telegram.svg
│ │ ├── telephone-fill.svg
│ │ ├── telephone-forward-fill.svg
│ │ ├── telephone-forward.svg
│ │ ├── telephone-inbound-fill.svg
│ │ ├── telephone-inbound.svg
│ │ ├── telephone-minus-fill.svg
│ │ ├── telephone-minus.svg
│ │ ├── telephone-outbound-fill.svg
│ │ ├── telephone-outbound.svg
│ │ ├── telephone-plus-fill.svg
│ │ ├── telephone-plus.svg
│ │ ├── telephone-x-fill.svg
│ │ ├── telephone-x.svg
│ │ ├── telephone.svg
│ │ ├── tencent-qq.svg
│ │ ├── terminal-dash.svg
│ │ ├── terminal-fill.svg
│ │ ├── terminal-plus.svg
│ │ ├── terminal-split.svg
│ │ ├── terminal-x.svg
│ │ ├── terminal.svg
│ │ ├── text-center.svg
│ │ ├── text-indent-left.svg
│ │ ├── text-indent-right.svg
│ │ ├── text-left.svg
│ │ ├── text-paragraph.svg
│ │ ├── text-right.svg
│ │ ├── text-wrap.svg
│ │ ├── textarea-resize.svg
│ │ ├── textarea-t.svg
│ │ ├── textarea.svg
│ │ ├── thermometer-half.svg
│ │ ├── thermometer-high.svg
│ │ ├── thermometer-low.svg
│ │ ├── thermometer-snow.svg
│ │ ├── thermometer-sun.svg
│ │ ├── thermometer.svg
│ │ ├── threads-fill.svg
│ │ ├── threads.svg
│ │ ├── three-dots-vertical.svg
│ │ ├── three-dots.svg
│ │ ├── thunderbolt-fill.svg
│ │ ├── thunderbolt.svg
│ │ ├── ticket-detailed-fill.svg
│ │ ├── ticket-detailed.svg
│ │ ├── ticket-fill.svg
│ │ ├── ticket-perforated-fill.svg
│ │ ├── ticket-perforated.svg
│ │ ├── ticket.svg
│ │ ├── tiktok.svg
│ │ ├── toggle-off.svg
│ │ ├── toggle-on.svg
│ │ ├── toggle2-off.svg
│ │ ├── toggle2-on.svg
│ │ ├── toggles.svg
│ │ ├── toggles2.svg
│ │ ├── tools.svg
│ │ ├── tornado.svg
│ │ ├── train-freight-front-fill.svg
│ │ ├── train-freight-front.svg
│ │ ├── train-front-fill.svg
│ │ ├── train-front.svg
│ │ ├── train-lightrail-front-fill.svg
│ │ ├── train-lightrail-front.svg
│ │ ├── translate.svg
│ │ ├── transparency.svg
│ │ ├── trash-fill.svg
│ │ ├── trash.svg
│ │ ├── trash2-fill.svg
│ │ ├── trash2.svg
│ │ ├── trash3-fill.svg
│ │ ├── trash3.svg
│ │ ├── tree-fill.svg
│ │ ├── tree.svg
│ │ ├── trello.svg
│ │ ├── triangle-fill.svg
│ │ ├── triangle-half.svg
│ │ ├── triangle.svg
│ │ ├── trophy-fill.svg
│ │ ├── trophy.svg
│ │ ├── tropical-storm.svg
│ │ ├── truck-flatbed.svg
│ │ ├── truck-front-fill.svg
│ │ ├── truck-front.svg
│ │ ├── truck.svg
│ │ ├── tsunami.svg
│ │ ├── tv-fill.svg
│ │ ├── tv.svg
│ │ ├── twitch.svg
│ │ ├── twitter-x.svg
│ │ ├── twitter.svg
│ │ ├── type-bold.svg
│ │ ├── type-h1.svg
│ │ ├── type-h2.svg
│ │ ├── type-h3.svg
│ │ ├── type-h4.svg
│ │ ├── type-h5.svg
│ │ ├── type-h6.svg
│ │ ├── type-italic.svg
│ │ ├── type-strikethrough.svg
│ │ ├── type-underline.svg
│ │ ├── type.svg
│ │ ├── ubuntu.svg
│ │ ├── ui-checks-grid.svg
│ │ ├── ui-checks.svg
│ │ ├── ui-radios-grid.svg
│ │ ├── ui-radios.svg
│ │ ├── umbrella-fill.svg
│ │ ├── umbrella.svg
│ │ ├── unindent.svg
│ │ ├── union.svg
│ │ ├── unity.svg
│ │ ├── universal-access-circle.svg
│ │ ├── universal-access.svg
│ │ ├── unlock-fill.svg
│ │ ├── unlock.svg
│ │ ├── upc-scan.svg
│ │ ├── upc.svg
│ │ ├── upload.svg
│ │ ├── usb-c-fill.svg
│ │ ├── usb-c.svg
│ │ ├── usb-drive-fill.svg
│ │ ├── usb-drive.svg
│ │ ├── usb-fill.svg
│ │ ├── usb-micro-fill.svg
│ │ ├── usb-micro.svg
│ │ ├── usb-mini-fill.svg
│ │ ├── usb-mini.svg
│ │ ├── usb-plug-fill.svg
│ │ ├── usb-plug.svg
│ │ ├── usb-symbol.svg
│ │ ├── usb.svg
│ │ ├── valentine.svg
│ │ ├── valentine2.svg
│ │ ├── vector-pen.svg
│ │ ├── view-list.svg
│ │ ├── view-stacked.svg
│ │ ├── vignette.svg
│ │ ├── vimeo.svg
│ │ ├── vinyl-fill.svg
│ │ ├── vinyl.svg
│ │ ├── virus.svg
│ │ ├── virus2.svg
│ │ ├── voicemail.svg
│ │ ├── volume-down-fill.svg
│ │ ├── volume-down.svg
│ │ ├── volume-mute-fill.svg
│ │ ├── volume-mute.svg
│ │ ├── volume-off-fill.svg
│ │ ├── volume-off.svg
│ │ ├── volume-up-fill.svg
│ │ ├── volume-up.svg
│ │ ├── vr.svg
│ │ ├── wallet-fill.svg
│ │ ├── wallet.svg
│ │ ├── wallet2.svg
│ │ ├── watch.svg
│ │ ├── water.svg
│ │ ├── webcam-fill.svg
│ │ ├── webcam.svg
│ │ ├── wechat.svg
│ │ ├── whatsapp.svg
│ │ ├── wifi-1.svg
│ │ ├── wifi-2.svg
│ │ ├── wifi-off.svg
│ │ ├── wifi.svg
│ │ ├── wikipedia.svg
│ │ ├── wind.svg
│ │ ├── window-dash.svg
│ │ ├── window-desktop.svg
│ │ ├── window-dock.svg
│ │ ├── window-fullscreen.svg
│ │ ├── window-plus.svg
│ │ ├── window-sidebar.svg
│ │ ├── window-split.svg
│ │ ├── window-stack.svg
│ │ ├── window-x.svg
│ │ ├── window.svg
│ │ ├── windows.svg
│ │ ├── wordpress.svg
│ │ ├── wrench-adjustable-circle-fill.svg
│ │ ├── wrench-adjustable-circle.svg
│ │ ├── wrench-adjustable.svg
│ │ ├── wrench.svg
│ │ ├── x-circle-fill.svg
│ │ ├── x-circle.svg
│ │ ├── x-diamond-fill.svg
│ │ ├── x-diamond.svg
│ │ ├── x-lg.svg
│ │ ├── x-octagon-fill.svg
│ │ ├── x-octagon.svg
│ │ ├── x-square-fill.svg
│ │ ├── x-square.svg
│ │ ├── x.svg
│ │ ├── xbox.svg
│ │ ├── yelp.svg
│ │ ├── yin-yang.svg
│ │ ├── youtube.svg
│ │ ├── zoom-in.svg
│ │ └── zoom-out.svg
│ ├── css/
│ │ ├── BeatifIntredPlayer.min.css
│ │ ├── DPlayer.min.css
│ │ ├── admin.css
│ │ └── artplayer.css
│ ├── favicon.ico
│ ├── favicon.png
│ ├── icons/
│ │ └── icon.png
│ ├── images/
│ │ ├── default_avatar.png
│ │ └── player/
│ │     ├── background.jpg*
│ │     ├── indicator.svg
│ │     ├── load.gif
│ │     ├── ploading.gif
│ │     └── state.svg
│ ├── js/
│ │ ├── BeatifIntredPlayer.min.js
│ │ ├── DPlayer.min.js
│ │ ├── artplayer.js
│ │ ├── flv.js
│ │ ├── hls.js
│ │ └── jquery.min.js
│ └── logo/
│     └── byusi.png
├── sw.js
└── templates/
    ├── admin.html
    ├── base.html
    ├── index.html
    ├── login.html
    ├── play.html
    ├── register.html
    ├── search_results.html
    ├── upload.html
    └── user_profile.html

25 directories, 4247 files
```