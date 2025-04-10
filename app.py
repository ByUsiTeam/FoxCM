from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory, jsonify
from werkzeug.utils import secure_filename
from datetime import datetime
import json
import os
import random
import string
import uuid
import sys

if getattr(sys, 'frozen', False):  # 如果是打包后的可执行文件
    base_path = os.path.dirname(sys.executable)
else:  # 如果是开发环境
    base_path = os.path.abspath(".")

template_folder = os.path.join(base_path, "templates")
static_folder = os.path.join(base_path, "static")
data_folder = os.path.join(base_path, "data")

app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
app.secret_key = 'foxcm-key'
app.config['UPLOAD_FOLDER'] = os.path.join(static_folder, 'uploads/videos')
app.config['COVER_FOLDER'] = os.path.join(static_folder, 'uploads/covers')
app.config['AVATAR_FOLDER'] = os.path.join(static_folder, 'uploads/avatars')  # 新增头像上传目录
USER_DATA_FILE = os.path.join(data_folder, 'user.json')
VIDEO_DATA_FILE = os.path.join(data_folder, 'foxcm-sp.json')
SYSTEM_DATA = os.path.join(data_folder, 'system.json')
COMMENT_DATA_FILE = os.path.join(data_folder, 'comments.json')
ADMIN = False

ALLOWED_VIDEO_EXTENSIONS = {'mp4', 'avi', 'mov', '.mp3', '.ogg'}
ALLOWED_COVER_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}
ALLOWED_AVATAR_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}  # 新增头像允许格式

def generate_random_filename(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

# 评论实现
def load_comments():
    try:
        with open(COMMENT_DATA_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_comments(comments):
    with open(COMMENT_DATA_FILE, 'w') as file:
        json.dump(comments, file, indent=4)

def load_users():
    try:
        with open(USER_DATA_FILE, 'r') as file:
            users = json.load(file)
            # 为旧用户添加avatar_filename字段
            for user in users:
                if 'avatar_filename' not in user:
                    user['avatar_filename'] = ''
            return users
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_users(users):
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(users, file, indent=4)

def load_system_data():
    try:
        with open(SYSTEM_DATA, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def get_system_title():
    system_data = load_system_data()
    return system_data.get('title', 'FoxCM')

def load_videos():
    try:
        with open(VIDEO_DATA_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_videos(videos):
    with open(VIDEO_DATA_FILE, 'w') as file:
        json.dump(videos, file, indent=4)

def find_user_by_id(user_id):
    users = load_users()
    return next((user for user in users if user['id'] == user_id), None)

def find_user_by_username(username):
    users = load_users()
    return next((user for user in users if user['username'] == username), None)

@app.route('/')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    videos = load_videos()
    random.shuffle(videos)
    title = get_system_title()
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
            return redirect(url_for('index'))
        flash('用户名或密码错误！')
    return render_template('login.html', title=title)

@app.route('/logout')
def logout():
    session.clear()
    flash('已注销登录！')
    return redirect(url_for('login'))

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    # 身份验证检查
    if not session.get('logged_in'):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({'success': False, 'message': '请先登录', 'redirect': url_for('login')}), 401
        return redirect(url_for('login'))
    
    # 系统标题加载
    title = get_system_title()
    
    # GET 请求处理（显示上传页面）
    if request.method == 'GET':
        return render_template('upload.html', title=title)
    
    # POST 请求处理（文件上传）
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
            return handle_response(error_msg, 400)
        
        # 文件类型验证
        video_file = required_fields['video']
        cover_file = required_fields['cover']
        if not allowed_file(video_file.filename, ALLOWED_VIDEO_EXTENSIONS):
            return handle_response("视频格式不支持（仅限 mp4/avi/mov）", 400)
        
        if not allowed_file(cover_file.filename, ALLOWED_COVER_EXTENSIONS):
            return handle_response("封面格式不支持（仅限 jpg/png）", 400)
        
        # 生成唯一文件名
        def generate_filename(file, prefix):
            ext = file.filename.rsplit('.', 1)[1].lower()
            return f"{prefix}-{uuid.uuid4()}.{ext}"
        
        video_filename = generate_filename(video_file, "video")
        cover_filename = generate_filename(cover_file, "cover")
        
        # 保存文件
        def save_upload(file_obj, filename, folder):
            save_path = os.path.join(app.config[folder.upper() + '_FOLDER'], filename)
            file_obj.save(save_path)
            return save_path
        
        video_path = save_upload(video_file, video_filename, 'UPLOAD')
        cover_path = save_upload(cover_file, cover_filename, 'COVER')
        
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
            "play_count": 0
        }
        
        # 更新数据库
        videos = load_videos()
        videos.append(video_data)
        save_videos(videos)
        
        # 响应处理
        return handle_response("视频上传成功", 200, url_for('index'))
    
    except Exception as e:
        app.logger.error(f"上传错误: {str(e)}")
        return handle_response(f"服务器错误: {str(e)}", 500)

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
        else:
            flash(message, 'success')
        return redirect(redirect_url if redirect_url else url_for('upload'))

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
        return render_template('play.html', video=video, title=title, comments=comments, uploader=uploader_user)
    flash('视频不存在！')
    return redirect(url_for('index'))

@app.route('/user/<username>')
def user_profile(username):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    user = find_user_by_username(username)
    if not user:
        flash('用户不存在')
        return redirect(url_for('index'))
    videos = load_videos()
    user_videos = [v for v in videos if v['user_id'] == user['id']]
    title = get_system_title()
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
        users = load_users()
        for u in users:
            if u['id'] == user['id']:
                u['avatar_filename'] = new_filename
                break
        save_users(users)
        flash('头像上传成功')
    else:
        flash('仅支持jpg、png格式')
    return redirect(url_for('user_profile', username=user['username']))

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    user = find_user_by_id(session['user_id'])
    if not user or not user.get('is_admin'):
        flash('只有管理员可以访问该页面！')
        return redirect(url_for('index'))
    users = load_users()
    videos = load_videos()
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'delete_user':
            user_id_to_delete = int(request.form.get('user_id'))
            users = [u for u in users if u['id'] != user_id_to_delete]
            save_users(users)
            flash('用户删除成功！')
            return redirect(url_for('admin'))
        elif action == 'delete_video':
            video_filename_to_delete = request.form.get('video_filename')
            videos = [v for v in videos if v['video_filename'] != video_filename_to_delete]
            save_videos(videos)
            video_path = os.path.join(app.config['UPLOAD_FOLDER'], video_filename_to_delete)
            cover_path = os.path.join(app.config['COVER_FOLDER'], next((v['cover_filename'] for v in videos if v['video_filename'] == video_filename_to_delete), ''))
            if os.path.exists(video_path):
                os.remove(video_path)
            if os.path.exists(cover_path):
                os.remove(cover_path)
            flash('视频删除成功！')
            return redirect(url_for('admin'))
    title = get_system_title()
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
    return render_template('search_results.html', query=query, videos=search_results, title=title)

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
    else:
        flash('评论不存在！')
    
    return redirect(url_for('play', video_filename=video_filename))

# 初始化目录和文件
if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['COVER_FOLDER'], exist_ok=True)
    os.makedirs(app.config['AVATAR_FOLDER'], exist_ok=True)  # 新增头像目录
    os.makedirs('data', exist_ok=True)
    if not os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'w') as file:
            json.dump([], file)
    if not os.path.exists(VIDEO_DATA_FILE):
        with open(VIDEO_DATA_FILE, 'w') as file:
            json.dump([], file)
    # 评论数据生成
    if not os.path.exists(COMMENT_DATA_FILE):
        with open(COMMENT_DATA_FILE, 'w') as file:
            json.dump({}, file)
    app.run(host='0.0.0.0', port=6544, debug=True)