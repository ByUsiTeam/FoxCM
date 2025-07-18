from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory, jsonify, Response, send_file
from werkzeug.utils import secure_filename
from datetime import datetime
import json
import os
import random
import string
import uuid
import sys
import requests
from requests.auth import HTTPBasicAuth
import threading
import time
import shutil
import mimetypes
import re
import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.traceback import install
import werkzeug.serving

# 安装Rich的异常处理
install()

# 基础路径设置
if getattr(sys, 'frozen', False):  # 如果是打包后的可执行文件
    base_path = os.path.dirname(sys.executable)
else:  # 如果是开发环境
    base_path = os.path.abspath(".")

template_folder = os.path.join(base_path, "templates")
static_folder = os.path.join(base_path, "static")
data_folder = os.path.join(base_path, "data")

# 创建Rich控制台
console = Console()

# 配置Rich日志处理器
rich_handler = RichHandler(
    rich_tracebacks=True,
    tracebacks_show_locals=True,
    markup=True,
    show_path=False
)

# 创建Flask应用
app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
app.secret_key = 'foxcm-key'
app.config['UPLOAD_FOLDER'] = os.path.join(static_folder, 'uploads/videos')
app.config['COVER_FOLDER'] = os.path.join(static_folder, 'uploads/covers')
app.config['AVATAR_FOLDER'] = os.path.join(static_folder, 'uploads/avatars')

# 配置应用日志
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[rich_handler]
)

# 禁用Flask默认的日志处理器
app.logger.handlers.clear()
app.logger.addHandler(rich_handler)

# 重写Werkzeug的日志处理器以使用Rich
class RichRequestHandler(werkzeug.serving.WSGIRequestHandler):
    def log(self, type, message, *args):
        try:
            # 尝试解析请求日志
            if type == 'info' and message == '"%s" %s %s':
                # 这是标准请求日志格式
                request_line = args[0] if len(args) > 0 else ''
                status_code = args[1] if len(args) > 1 else '000'
                response_size = args[2] if len(args) > 2 else '-'
                
                # 确保状态码是整数
                try:
                    status_code = int(status_code)
                except (ValueError, TypeError):
                    status_code = 000
                
                # 根据状态码设置颜色
                if status_code >= 500:
                    color = "bold red"
                elif status_code >= 400:
                    color = "bold yellow"
                elif status_code >= 300:
                    color = "bold blue"
                else:
                    color = "bold green"
                    
                # 创建富格式日志
                log_message = f"[bold]{self.address_string()}[/bold] - - [{self.log_date_time_string()}] "
                log_message += f"[{color}]{request_line} {status_code} {response_size}[/{color}]"
                
                # 发送到Rich处理器
                app.logger.info(log_message)
            else:
                # 其他类型的日志直接格式化
                formatted_message = message % args
                if type == 'error':
                    app.logger.error(formatted_message)
                elif type == 'warning':
                    app.logger.warning(formatted_message)
                else:
                    app.logger.info(formatted_message)
        except Exception as e:
            # 如果解析失败，记录原始消息
            app.logger.error(f"日志处理错误: {str(e)}")
            app.logger.info(f"原始消息: {message} | 参数: {args}")

# 设置自定义请求处理器
werkzeug.serving.WSGIRequestHandler = RichRequestHandler

USER_DATA_FILE = os.path.join(data_folder, 'user.json')
VIDEO_DATA_FILE = os.path.join(data_folder, 'foxcm-sp.json')
SYSTEM_DATA = os.path.join(data_folder, 'system.json')
COMMENT_DATA_FILE = os.path.join(data_folder, 'comments.json')
ADMIN = False

ALLOWED_VIDEO_EXTENSIONS = {'mp4', 'avi', 'mov', 'mp3', 'ogg'}
ALLOWED_COVER_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}
ALLOWED_AVATAR_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}

# 确保所有必要的目录都存在
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['COVER_FOLDER'], exist_ok=True)
os.makedirs(app.config['AVATAR_FOLDER'], exist_ok=True)
os.makedirs(data_folder, exist_ok=True)

# 使用Rich打印启动信息
console.print("=" * 60, style="bold blue")
console.print(f"{'FoxCM 媒体分享平台':^60}", style="bold green")
console.print(f"{'版本: 1.2.0':^60}", style="bold yellow")
console.print(f"{'作者: FoxHome':^60}", style="bold magenta")
console.print("=" * 60, style="bold blue")
console.print(f"基础路径: {base_path}", style="cyan")
console.print(f"模板目录: {template_folder}", style="cyan")
console.print(f"静态目录: {static_folder}", style="cyan")
console.print(f"数据目录: {data_folder}", style="cyan")

def generate_random_filename(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

# 评论实现
def load_comments():
    try:
        with open(COMMENT_DATA_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        app.logger.error(f"加载评论数据失败: {str(e)}")
        return {}

def save_comments(comments):
    try:
        with open(COMMENT_DATA_FILE, 'w') as file:
            json.dump(comments, file, indent=4)
    except Exception as e:
        app.logger.error(f"保存评论数据失败: {str(e)}")

def load_users():
    try:
        with open(USER_DATA_FILE, 'r') as file:
            users = json.load(file)
            # 为旧用户添加avatar_filename字段
            for user in users:
                if 'avatar_filename' not in user:
                    user['avatar_filename'] = ''
            return users
    except (FileNotFoundError, json.JSONDecodeError) as e:
        app.logger.error(f"加载用户数据失败: {str(e)}")
        return []

def save_users(users):
    try:
        with open(USER_DATA_FILE, 'w') as file:
            json.dump(users, file, indent=4)
    except Exception as e:
        app.logger.error(f"保存用户数据失败: {str(e)}")

def load_system_data():
    try:
        with open(SYSTEM_DATA, 'r') as file:
            system_data = json.load(file)
            # 确保有WebDav配置项
            system_data.setdefault('webdav_video', {'enabled': False})
            system_data.setdefault('webdav_cover', {'enabled': False})
            return system_data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        app.logger.error(f"加载系统配置失败: {str(e)}，使用默认配置")
        return {
            'title': 'FoxCM',
            'webdav_video': {'enabled': False},
            'webdav_cover': {'enabled': False}
        }

def get_system_title():
    system_data = load_system_data()
    return system_data.get('title', 'FoxCM')

def load_videos():
    try:
        with open(VIDEO_DATA_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        app.logger.error(f"加载视频数据失败: {str(e)}")
        return []

def save_videos(videos):
    try:
        with open(VIDEO_DATA_FILE, 'w') as file:
            json.dump(videos, file, indent=4)
    except Exception as e:
        app.logger.error(f"保存视频数据失败: {str(e)}")

def find_user_by_id(user_id):
    users = load_users()
    return next((user for user in users if user['id'] == user_id), None)

def find_user_by_username(username):
    users = load_users()
    return next((user for user in users if user['username'] == username), None)

# WebDav上传函数
def upload_to_webdav(file_obj, filename, config):
    """上传文件到WebDav服务器"""
    try:
        # 构建完整URL
        if not config['url'].endswith('/'):
            config['url'] += '/'
        remote_url = config['url'] + filename
        
        # 重置文件指针
        file_obj.seek(0)
        
        # 使用HTTP Basic Auth
        auth = HTTPBasicAuth(config['username'], config['password'])
        
        # 发送PUT请求上传文件
        app.logger.info(f"开始上传文件到WebDav: {filename}")
        start_time = time.time()
        response = requests.put(
            remote_url,
            data=file_obj,
            auth=auth,
            headers={'Content-Type': 'application/octet-stream'},
            timeout=30  # 30秒超时
        )
        elapsed = time.time() - start_time
        
        # 检查响应状态
        if response.status_code in [200, 201, 204]:
            app.logger.info(f"文件上传成功: {filename} [耗时: {elapsed:.2f}秒]")
            return True, remote_url
        else:
            app.logger.error(f"WebDav上传失败: {response.status_code} - {response.text}")
            return False, f"WebDav错误: {response.status_code}"
    
    except Exception as e:
        app.logger.error(f"WebDav上传异常: {str(e)}")
        return False, str(e)

# 文件代理函数 - 支持Range请求
def proxy_file(file_url, config, range_header=None):
    """代理文件请求到WebDav服务器，支持断点续传"""
    try:
        # 使用基本认证
        auth = None
        if config and 'username' in config and 'password' in config:
            auth = HTTPBasicAuth(config['username'], config['password'])
        
        # 构建请求头
        headers = {}
        if range_header:
            headers['Range'] = range_header
            app.logger.debug(f"处理Range请求: {range_header}")
        
        # 流式请求文件
        response = requests.get(file_url, stream=True, auth=auth, headers=headers, timeout=30)
        
        # 获取内容类型
        content_type = response.headers.get('Content-Type')
        if not content_type:
            # 根据文件扩展名猜测内容类型
            ext = os.path.splitext(file_url)[1].lower()
            if ext in ['.jpg', '.jpeg', '.jpe']:
                content_type = 'image/jpeg'
            elif ext == '.png':
                content_type = 'image/png'
            elif ext == '.gif':
                content_type = 'image/gif'
            elif ext == '.mp4':
                content_type = 'video/mp4'
            elif ext == '.avi':
                content_type = 'video/x-msvideo'
            elif ext == '.mov':
                content_type = 'video/quicktime'
            else:
                content_type = 'application/octet-stream'
        
        # 创建响应
        response_headers = dict(response.headers)
        # 移除不必要的头
        for key in ['Connection', 'Transfer-Encoding']:
            if key in response_headers:
                del response_headers[key]
        
        # 如果原始响应是206，则传递这个状态码
        status_code = response.status_code
        
        # 创建生成器函数
        def generate():
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    yield chunk
        
        # 返回响应
        return Response(
            generate(),
            status=status_code,
            headers=response_headers,
            content_type=content_type,
            direct_passthrough=True
        )
    
    except Exception as e:
        app.logger.error(f"文件代理失败: {file_url}, 错误: {str(e)}")
        return str(e), 500

@app.route('/')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    videos = load_videos()
    random.shuffle(videos)
    title = get_system_title()
    app.logger.info(f"用户 {session.get('user_id')} 访问首页")
    return render_template('index.html', videos=videos, title=title)

@app.route('/register', methods=['GET', 'POST'])
def register():
    title = get_system_title()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = load_users()
        if find_user_by_username(username):
            flash('用户名已存在！')
            app.logger.warning(f"用户名已存在: {username}")
            return redirect(url_for('register'))
        new_user = {
            "id": len(users) + 1,
            "username": username,
            "password": password,
            "is_admin": ADMIN,
            "avatar_filename": ''  # 初始化头像字段
        }
        users.append(new_user)
        save_users(users)
        flash('注册成功，请登录！')
        app.logger.info(f"新用户注册: {username}")
        return redirect(url_for('login'))
    return render_template('register.html', title=title)

@app.route('/login', methods=['GET', 'POST'])
def login():
    title = get_system_title()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = find_user_by_username(username)
        if user and user['password'] == password:
            session['logged_in'] = True
            session['user_id'] = user['id']
            flash('登录成功！')
            app.logger.info(f"用户登录: {username}")
            return redirect(url_for('index'))
        flash('用户名或密码错误！')
        app.logger.warning(f"登录失败: {username}")
    return render_template('login.html', title=title)

@app.route('/logout')
def logout():
    user_id = session.get('user_id')
    session.clear()
    flash('已注销登录！')
    app.logger.info(f"用户注销: {user_id}")
    return redirect(url_for('login'))

def handle_response(message, status_code=200, redirect_url=None):
    """统一处理响应格式"""
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify({
            'success': status_code == 200,
            'message': message,
            'redirect': redirect_url
        }), status_code
    else:
        if status_code != 200:
            flash(message, 'danger')
            app.logger.warning(f"操作失败: {message}")
        else:
            flash(message, 'success')
            app.logger.info(f"操作成功: {message}")
        return redirect(redirect_url if redirect_url else url_for('upload'))

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    # 身份验证检查
    if not session.get('logged_in'):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({'success': False, 'message': '请先登录', 'redirect': url_for('login')}), 401
        return redirect(url_for('login'))
    
    # 加载系统配置
    system_config = load_system_data()
    title = system_config.get('title', 'FoxCM')
    
    # GET请求处理（显示上传页面）
    if request.method == 'GET':
        app.logger.info(f"用户 {session.get('user_id')} 访问上传页面")
        return render_template('upload.html', title=title)
    
    # POST请求处理（文件上传）
    try:
        # 字段验证
        required_fields = {
            'video': request.files.get('video'),
            'cover': request.files.get('cover'),
            'title': request.form.get('title', '').strip()
        }
        
        # 检查必填字段
        if not all(required_fields.values()):
            error_msg = "视频文件、封面和标题是必填项"
            app.logger.warning(f"上传失败: {error_msg}")
            return handle_response(error_msg, 400)
        
        # 文件类型验证
        video_file = required_fields['video']
        cover_file = required_fields['cover']
        if not allowed_file(video_file.filename, ALLOWED_VIDEO_EXTENSIONS):
            error_msg = "视频格式不支持（仅限 mp4/avi/mov）"
            app.logger.warning(f"上传失败: {error_msg}")
            return handle_response(error_msg, 400)
        
        if not allowed_file(cover_file.filename, ALLOWED_COVER_EXTENSIONS):
            error_msg = "封面格式不支持（仅限 jpg/png）"
            app.logger.warning(f"上传失败: {error_msg}")
            return handle_response(error_msg, 400)
        
        # 生成唯一文件名
        def generate_filename(file, prefix):
            ext = file.filename.rsplit('.', 1)[1].lower()
            return f"{prefix}-{uuid.uuid4()}.{ext}"
        
        video_filename = generate_filename(video_file, "video")
        cover_filename = generate_filename(cover_file, "cover")
        
        app.logger.info(f"开始上传视频: {video_filename}")
        app.logger.info(f"开始上传封面: {cover_filename}")
        
        # 视频存储逻辑
        video_storage_type = "local"
        video_url = ""
        webdav_video_config = system_config.get('webdav_video', {})
        
        if webdav_video_config.get('enabled', False):
            # WebDav存储视频
            success, result = upload_to_webdav(video_file, video_filename, webdav_video_config)
            if success:
                video_storage_type = "webdav"
                video_url = result
            else:
                return handle_response(f"视频上传到WebDav失败: {result}", 500)
        else:
            # 本地存储视频
            video_path = os.path.join(app.config['UPLOAD_FOLDER'], video_filename)
            video_file.save(video_path)
            app.logger.info(f"视频保存到本地: {video_path}")
        
        # 封面存储逻辑
        cover_storage_type = "local"
        cover_url = ""
        webdav_cover_config = system_config.get('webdav_cover', {})
        
        if webdav_cover_config.get('enabled', False):
            # WebDav存储封面
            success, result = upload_to_webdav(cover_file, cover_filename, webdav_cover_config)
            if success:
                cover_storage_type = "webdav"
                cover_url = result
            else:
                # 如果封面上传失败，删除已上传的视频
                if video_storage_type == "webdav":
                    # 注意：实际应用中可能需要实现WebDav删除操作
                    app.logger.warning("封面上传失败，需要删除WebDav视频")
                elif video_storage_type == "local":
                    local_video = os.path.join(app.config['UPLOAD_FOLDER'], video_filename)
                    if os.path.exists(local_video):
                        os.remove(local_video)
                        app.logger.info(f"删除本地视频: {local_video}")
                return handle_response(f"封面上传到WebDav失败: {result}", 500)
        else:
            # 本地存储封面
            cover_path = os.path.join(app.config['COVER_FOLDER'], cover_filename)
            cover_file.save(cover_path)
            app.logger.info(f"封面保存到本地: {cover_path}")
        
        # 记录元数据
        user = find_user_by_id(session['user_id'])
        video_data = {
            "video_filename": video_filename,
            "cover_filename": cover_filename,
            "title": required_fields['title'],
            "description": request.form.get('description', ''),
            "uploader": user['username'] if user else "未知用户",
            "upload_time": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "user_id": session['user_id'],
            "play_count": 0,
            # 新增存储类型和URL字段
            "video_storage_type": video_storage_type,
            "video_url": video_url,
            "cover_storage_type": cover_storage_type,
            "cover_url": cover_url
        }
        
        # 更新数据库
        videos = load_videos()
        videos.append(video_data)
        save_videos(videos)
        
        app.logger.info(f"视频上传完成: {video_filename}")
        
        # 响应处理
        return handle_response("视频上传成功", 200, url_for('index'))
    
    except Exception as e:
        app.logger.error(f"上传错误: {str(e)}", exc_info=True)
        return handle_response(f"服务器错误: {str(e)}", 500)

@app.route('/play/<video_filename>')
def play(video_filename):
    videos = load_videos()
    video = next((v for v in videos if v['video_filename'] == video_filename), None)
    if video:
        video['play_count'] += 1
        save_videos(videos)
        comments = load_comments().get(video['video_filename'], [])
        title = get_system_title()
        uploader_user = find_user_by_id(video['user_id'])
        
        app.logger.info(f"播放视频: {video_filename} (播放次数: {video['play_count']})")
        
        # 确定视频和封面的实际URL
        video_url = ""
        if video.get('video_storage_type') == 'webdav' and video.get('video_url'):
            # 使用代理路径
            video_url = url_for('static', filename=f'uploads/videos/{video_filename}')
        else:
            video_url = url_for('static', filename=f'uploads/videos/{video_filename}')
        
        cover_url = ""
        if video.get('cover_storage_type') == 'webdav' and video.get('cover_url'):
            # 使用代理路径
            cover_url = url_for('static', filename=f'uploads/covers/{video["cover_filename"]}')
        else:
            cover_url = url_for('static', filename=f'uploads/covers/{video["cover_filename"]}')
        
        return render_template(
            'play.html', 
            video=video, 
            title=title, 
            comments=comments, 
            uploader=uploader_user,
            video_url=video_url,
            cover_url=cover_url
        )
    flash('视频不存在！')
    app.logger.warning(f"视频不存在: {video_filename}")
    return redirect(url_for('index'))

@app.route('/user/<username>')
def user_profile(username):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    user = find_user_by_username(username)
    if not user:
        flash('用户不存在')
        app.logger.warning(f"用户不存在: {username}")
        return redirect(url_for('index'))
    videos = load_videos()
    user_videos = [v for v in videos if v['user_id'] == user['id']]
    title = get_system_title()
    app.logger.info(f"访问用户主页: {username}")
    return render_template('user_profile.html', user=user, videos=user_videos, title=title)

@app.route('/upload_avatar', methods=['POST'])
def upload_avatar():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    user = find_user_by_id(session['user_id'])
    if not user:
        flash('用户不存在')
        return redirect(url_for('index'))
    if 'avatar' not in request.files:
        flash('未选择文件')
        return redirect(url_for('user_profile', username=user['username']))
    avatar_file = request.files['avatar']
    if avatar_file.filename == '':
        flash('未选择文件')
        return redirect(url_for('user_profile', username=user['username']))
    if allowed_file(avatar_file.filename, ALLOWED_AVATAR_EXTENSIONS):
        ext = avatar_file.filename.rsplit('.', 1)[1].lower()
        new_filename = f"{uuid.uuid4()}.{ext}"  # 重命名头像文件
        avatar_path = os.path.join(app.config['AVATAR_FOLDER'], new_filename)
        avatar_file.save(avatar_path)
        if user.get('avatar_filename'):
            old_path = os.path.join(app.config['AVATAR_FOLDER'], user['avatar_filename'])
            if os.path.exists(old_path):
                os.remove(old_path)
                app.logger.info(f"删除旧头像: {old_path}")
        users = load_users()
        for u in users:
            if u['id'] == user['id']:
                u['avatar_filename'] = new_filename
                break
        save_users(users)
        flash('头像上传成功')
        app.logger.info(f"用户 {user['username']} 上传新头像: {new_filename}")
    else:
        flash('仅支持jpg、png格式')
        app.logger.warning(f"无效的头像格式: {avatar_file.filename}")
    return redirect(url_for('user_profile', username=user['username']))

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    user = find_user_by_id(session['user_id'])
    if not user or not user.get('is_admin'):
        flash('只有管理员可以访问该页面！')
        app.logger.warning(f"非管理员访问尝试: {user['username'] if user else '未知用户'}")
        return redirect(url_for('index'))
    users = load_users()
    videos = load_videos()
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'delete_user':
            user_id_to_delete = int(request.form.get('user_id'))
            user_to_delete = next((u for u in users if u['id'] == user_id_to_delete), None)
            if user_to_delete:
                users = [u for u in users if u['id'] != user_id_to_delete]
                save_users(users)
                flash('用户删除成功！')
                app.logger.warning(f"删除用户: {user_to_delete['username']}")
            return redirect(url_for('admin'))
        elif action == 'delete_video':
            video_filename_to_delete = request.form.get('video_filename')
            video_to_delete = next((v for v in videos if v['video_filename'] == video_filename_to_delete), None)
            if video_to_delete:
                videos = [v for v in videos if v['video_filename'] != video_filename_to_delete]
                save_videos(videos)
                video_path = os.path.join(app.config['UPLOAD_FOLDER'], video_filename_to_delete)
                cover_path = os.path.join(app.config['COVER_FOLDER'], video_to_delete.get('cover_filename', ''))
                if os.path.exists(video_path):
                    os.remove(video_path)
                    app.logger.info(f"删除视频文件: {video_path}")
                if cover_path and os.path.exists(cover_path):
                    os.remove(cover_path)
                    app.logger.info(f"删除封面文件: {cover_path}")
                flash('视频删除成功！')
                app.logger.warning(f"删除视频: {video_filename_to_delete}")
            return redirect(url_for('admin'))
    title = get_system_title()
    app.logger.info(f"管理员 {user['username']} 访问管理页面")
    return render_template('admin.html', users=users, videos=videos, title=title)

@app.route('/search')
def search():
    query = request.args.get('q', '').strip()
    if not query:
        flash("请输入搜索内容！", "info")
        return redirect(url_for('index'))
    videos = load_videos()
    search_results = [
        video for video in videos 
        if query.lower() in video['title'].lower() or query.lower() in video['description'].lower()
    ]
    title = get_system_title()
    app.logger.info(f"搜索查询: '{query}' 找到 {len(search_results)} 个结果")
    return render_template('search_results.html', query=query, videos=search_results, title=title)

# 评论发送
@app.route('/comment', methods=['POST'])
def comment():
    if not session.get('logged_in'):
        flash('请先登录后再发表评论！')
        next_url = request.form.get('next', url_for('index'))
        return redirect(url_for('login', next=next_url))
    
    video_filename = request.form['video_filename']
    user_id = session['user_id']
    user = find_user_by_id(user_id)
    
    if user is None:
        flash('用户不存在，请重新登录！')
        return redirect(url_for('login'))
    
    comment_text = request.form['comment_text']
    comment_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    comments = load_comments()
    if video_filename not in comments:
        comments[video_filename] = []
    
    comment_data = {
        "user_id": user_id,
        "username": user['username'],
        "comment_text": comment_text,
        "comment_time": comment_time,
        "likes": 0,
        "liked_by": []  # 初始化 liked_by 字段
    }
    comments[video_filename].append(comment_data)
    save_comments(comments)
    
    flash('评论成功！')
    app.logger.info(f"用户 {user['username']} 评论视频: {video_filename}")
    return redirect(url_for('play', video_filename=video_filename))

# 评论点赞
@app.route('/like_comment', methods=['POST'])
def like_comment():
    if not session.get('logged_in'):
        flash('请先登录后再点赞！')
        next_url = request.form.get('next', url_for('index'))
        return redirect(url_for('login', next=next_url))
    
    video_filename = request.form['video_filename']
    comment_index = int(request.form['comment_index'])
    user_id = session['user_id']
    
    comments = load_comments()
    if video_filename in comments and 0 <= comment_index < len(comments[video_filename]):
        comment = comments[video_filename][comment_index]
        if user_id in comment['liked_by']:
            flash('您已经点过赞了！')
        else:
            comment['likes'] += 1
            comment['liked_by'].append(user_id)
            save_comments(comments)
            flash('点赞成功！')
            app.logger.info(f"用户 {user_id} 点赞评论: 视频 {video_filename} 评论 #{comment_index}")
    else:
        flash('评论不存在！')
    
    return redirect(url_for('play', video_filename=video_filename))

# 文件代理路由 - 封面
@app.route('/static/uploads/covers/<path:filename>')
def serve_cover(filename):
    """处理封面文件请求"""
    # 首先检查本地文件是否存在
    cover_path = os.path.join(app.config['COVER_FOLDER'], filename)
    if os.path.exists(cover_path):
        # 如果本地文件存在，直接发送
        return send_file(cover_path)
    
    # 如果本地文件不存在，查找视频数据
    videos = load_videos()
    video = next((v for v in videos if v.get('cover_filename') == filename), None)
    
    if not video or not video.get('cover_url'):
        app.logger.warning(f"封面未找到: {filename}")
        return "封面未找到", 404
    
    # 获取系统配置
    system_config = load_system_data()
    webdav_cover_config = system_config.get('webdav_cover', {})
    
    # 如果WebDav未启用或配置无效
    if not webdav_cover_config.get('enabled', False) or not webdav_cover_config.get('url'):
        app.logger.warning("WebDav封面未配置或未启用")
        return "WebDav未配置或未启用", 500
    
    # 检查请求的文件URL是否匹配配置的WebDav URL
    cover_url = video.get('cover_url', '')
    if not cover_url.startswith(webdav_cover_config.get('url', '')):
        app.logger.warning(f"封面URL不匹配WebDav配置: {cover_url}")
        return "封面URL不匹配WebDav配置", 403
    
    # 代理文件请求
    app.logger.info(f"从WebDav代理封面: {filename}")
    return proxy_file(cover_url, webdav_cover_config)

# 文件代理路由 - 视频（支持断点续传）
@app.route('/static/uploads/videos/<path:filename>')
def serve_video(filename):
    """处理视频文件请求，支持断点续传"""
    # 首先检查本地文件是否存在
    video_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(video_path):
        # 如果本地文件存在，使用send_file发送（支持Range请求）
        app.logger.info(f"从本地提供视频: {filename}")
        return send_file(video_path)
    
    # 如果本地文件不存在，查找视频数据
    videos = load_videos()
    video = next((v for v in videos if v.get('video_filename') == filename), None)
    
    if not video or not video.get('video_url'):
        app.logger.warning(f"视频未找到: {filename}")
        return "视频未找到", 404
    
    # 获取系统配置
    system_config = load_system_data()
    webdav_video_config = system_config.get('webdav_video', {})
    
    # 如果WebDav未启用或配置无效
    if not webdav_video_config.get('enabled', False) or not webdav_video_config.get('url'):
        app.logger.warning("WebDav视频未配置或未启用")
        return "WebDav未配置或未启用", 500
    
    # 检查请求的文件URL是否匹配配置的WebDav URL
    video_url = video.get('video_url', '')
    if not video_url.startswith(webdav_video_config.get('url', '')):
        app.logger.warning(f"视频URL不匹配WebDav配置: {video_url}")
        return "视频URL不匹配WebDav配置", 403
    
    # 获取Range请求头
    range_header = request.headers.get('Range', None)
    
    # 代理文件请求，支持Range
    app.logger.info(f"从WebDav代理视频: {filename} {'(带Range请求)' if range_header else ''}")
    return proxy_file(video_url, webdav_video_config, range_header)

# PWA
# @app.route('/manifest.json')
# def manifest():
#     return send_from_directory(base_path, 'manifest.json')

# @app.route('/sw.js')
# def service_worker():
#     return send_from_directory(base_path, 'sw.js')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(static_folder, 'favicon.ico', mimetype='image/vnd.microsoft.icon')

# 初始化数据文件
if not os.path.exists(USER_DATA_FILE):
    with open(USER_DATA_FILE, 'w') as file:
        json.dump([], file)
    app.logger.info("创建用户数据文件")
if not os.path.exists(VIDEO_DATA_FILE):
    with open(VIDEO_DATA_FILE, 'w') as file:
        json.dump([], file)
    app.logger.info("创建视频数据文件")
if not os.path.exists(COMMENT_DATA_FILE):
    with open(COMMENT_DATA_FILE, 'w') as file:
        json.dump({}, file)
    app.logger.info("创建评论数据文件")
if not os.path.exists(SYSTEM_DATA):
    with open(SYSTEM_DATA, 'w') as file:
        json.dump({
            'title': 'FoxCM',
            'webdav_video': {'enabled': False},
            'webdav_cover': {'enabled': False}
        }, file)
    app.logger.info("创建系统配置文件")

if __name__ == '__main__':
    app.logger.info("=" * 60)
    app.logger.info("FoxCM 服务启动")
    app.logger.info(f"运行地址: http://0.0.0.0:6544")
    app.logger.info("=" * 60)
    app.run(host='0.0.0.0', port=6544, debug=True)