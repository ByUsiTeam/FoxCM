package main

import (
	"encoding/json"
	"fmt"
	"html/template"
	"io"
	"log"
	"net/http"
	"os"
	"path/filepath"
	"sort"
	"strconv"
	"strings"
	"time"

	"github.com/gin-contrib/sessions"
	"github.com/gin-contrib/sessions/cookie"
	"github.com/gin-gonic/gin"
	"github.com/google/uuid"
	"github.com/gorilla/websocket"
)

// 配置常量
const (
	BasePath       = "."
	TemplateFolder = "./templates"
	StaticFolder   = "./static"
	DataFolder     = "./data"
	UploadFolder   = "./static/uploads/videos"
	CoverFolder    = "./static/uploads/covers"
	AvatarFolder   = "./static/uploads/avatars"
	Port           = "6544"
	SecretKey      = "foxcm-key"
)

// 数据结构
type User struct {
	ID            int    `json:"id"`
	Username      string `json:"username"`
	Password      string `json:"password"`
	IsAdmin       bool   `json:"is_admin"`
	AvatarFile    string `json:"avatar_filename"`
	CreatedAt     string `json:"created_at"`
	LastLogin     string `json:"last_login"`
}

type Video struct {
	VideoFilename    string `json:"video_filename"`
	CoverFilename    string `json:"cover_filename"`
	Title            string `json:"title"`
	Description      string `json:"description"`
	Uploader         string `json:"uploader"`
	UploadTime       string `json:"upload_time"`
	UserID           int    `json:"user_id"`
	PlayCount        int    `json:"play_count"`
	LikeCount        int    `json:"like_count"`
	CommentCount     int    `json:"comment_count"`
	ViewsPerDay      int    `json:"views_per_day"`
	VideoStorageType string `json:"video_storage_type"`
	VideoURL         string `json:"video_url"`
	CoverStorageType string `json:"cover_storage_type"`
	CoverURL         string `json:"cover_url"`
	CreatedAt        string `json:"created_at"`
	UpdatedAt        string `json:"updated_at"`
	Category         string `json:"category"` // 新增：视频分类
}

type Comment struct {
	ID         int    `json:"id"`
	VideoID    string `json:"video_filename"`
	UserID     int    `json:"user_id"`
	Username   string `json:"username"`
	Text       string `json:"comment_text"`
	CreatedAt  string `json:"comment_time"`
	Likes      int    `json:"likes"`
	LikedBy    []int  `json:"liked_by"`
}

type SystemConfig struct {
	Title         string `json:"title"`
	WebDavVideo   struct {
		Enabled  bool   `json:"enabled"`
		URL      string `json:"url"`
		Username string `json:"username"`
		Password string `json:"password"`
	} `json:"webdav_video"`
	WebDavCover struct {
		Enabled  bool   `json:"enabled"`
		URL      string `json:"url"`
		Username string `json:"username"`
		Password string `json:"password"`
	} `json:"webdav_cover"`
}

// WebSocket 连接管理
var upgrader = websocket.Upgrader{
	CheckOrigin: func(r *http.Request) bool {
		return true
	},
}

type WSClient struct {
	conn *websocket.Conn
	userID int
}

var wsClients = make(map[*WSClient]bool)
var wsBroadcast = make(chan WSMessage)

type WSMessage struct {
	Type    string      `json:"type"` // "notification", "play_count", "like"
	Data    interface{} `json:"data"`
	UserID  int         `json:"user_id,omitempty"`
}

// 全局变量
var (
	users        []User
	videos       []Video
	comments     map[string][]Comment
	systemConfig SystemConfig
)

// 初始化函数
func init() {
	// 确保目录存在
	os.MkdirAll(DataFolder, 0755)
	os.MkdirAll(UploadFolder, 0755)
	os.MkdirAll(CoverFolder, 0755)
	os.MkdirAll(AvatarFolder, 0755)
	os.MkdirAll(TemplateFolder, 0755)
	
	// 加载数据
	loadData()
	
	// 启动WebSocket广播
	go handleWSBroadcast()
}

func loadData() {
	// 加载用户
	if data, err := os.ReadFile(filepath.Join(DataFolder, "users.json")); err == nil {
		json.Unmarshal(data, &users)
	}
	
	// 加载视频
	if data, err := os.ReadFile(filepath.Join(DataFolder, "videos.json")); err == nil {
		json.Unmarshal(data, &videos)
	}
	
	// 加载评论
	comments = make(map[string][]Comment)
	if data, err := os.ReadFile(filepath.Join(DataFolder, "comments.json")); err == nil {
		json.Unmarshal(data, &comments)
	}
	
	// 加载系统配置
	if data, err := os.ReadFile(filepath.Join(DataFolder, "system.json")); err == nil {
		json.Unmarshal(data, &systemConfig)
	} else {
		// 默认配置
		systemConfig.Title = "FoxCM"
		saveSystemConfig()
	}
}

func saveUsers() {
	data, _ := json.MarshalIndent(users, "", "  ")
	os.WriteFile(filepath.Join(DataFolder, "users.json"), data, 0644)
}

func saveVideos() {
	data, _ := json.MarshalIndent(videos, "", "  ")
	os.WriteFile(filepath.Join(DataFolder, "videos.json"), data, 0644)
}

func saveComments() {
	data, _ := json.MarshalIndent(comments, "", "  ")
	os.WriteFile(filepath.Join(DataFolder, "comments.json"), data, 0644)
}

func saveSystemConfig() {
	data, _ := json.MarshalIndent(systemConfig, "", "  ")
	os.WriteFile(filepath.Join(DataFolder, "system.json"), data, 0644)
}

// 辅助函数
func findUserByID(id int) *User {
	for i := range users {
		if users[i].ID == id {
			return &users[i]
		}
	}
	return nil
}

func findUserByUsername(username string) *User {
	for i := range users {
		if users[i].Username == username {
			return &users[i]
		}
	}
	return nil
}

func findVideoByFilename(filename string) *Video {
	for i := range videos {
		if videos[i].VideoFilename == filename {
			return &videos[i]
		}
	}
	return nil
}

func getAllowedExtensions(filename string, allowed []string) bool {
	ext := strings.ToLower(filepath.Ext(filename))
	if ext == "" {
		return false
	}
	ext = ext[1:] // 移除点号
	for _, allowedExt := range allowed {
		if ext == allowedExt {
			return true
		}
	}
	return false
}

// 排序函数
func sortVideos(c *gin.Context, videos []Video) []Video {
	sortBy := c.DefaultQuery("sort", "hot") // 默认按热度排序
	
	switch sortBy {
	case "newest":
		// 按最新排序
		sort.Slice(videos, func(i, j int) bool {
			t1, _ := time.Parse("2006-01-02 15:04:05", videos[i].CreatedAt)
			t2, _ := time.Parse("2006-01-02 15:04:05", videos[j].CreatedAt)
			return t1.After(t2)
		})
	case "likes":
		// 按点赞数排序
		sort.Slice(videos, func(i, j int) bool {
			return videos[i].LikeCount > videos[j].LikeCount
		})
	case "views":
		// 按播放量排序
		sort.Slice(videos, func(i, j int) bool {
			return videos[i].PlayCount > videos[j].PlayCount
		})
	case "hot":
		fallthrough
	default:
		// 按热度排序（改进算法）
		sort.Slice(videos, func(i, j int) bool {
			// 计算视频年龄（小时）
			uploadTime, _ := time.Parse("2006-01-02 15:04:05", videos[i].CreatedAt)
			ageHours := time.Since(uploadTime).Hours()
			if ageHours < 1 {
				ageHours = 1
			}
			
			// 热度算法：播放数 + 点赞数*2 + 评论数*3 - 年龄衰减
			hotnessI := float64(videos[i].PlayCount) + 
				float64(videos[i].LikeCount)*2 + 
				float64(videos[i].CommentCount)*3
			
			// 时间衰减因子
			decay := 1.0 / (1.0 + ageHours/24.0) // 24小时衰减一半
			hotnessI = hotnessI * decay
			
			uploadTimeJ, _ := time.Parse("2006-01-02 15:04:05", videos[j].CreatedAt)
			ageHoursJ := time.Since(uploadTimeJ).Hours()
			if ageHoursJ < 1 {
				ageHoursJ = 1
			}
			
			hotnessJ := float64(videos[j].PlayCount) + 
				float64(videos[j].LikeCount)*2 + 
				float64(videos[j].CommentCount)*3
			decayJ := 1.0 / (1.0 + ageHoursJ/24.0)
			hotnessJ = hotnessJ * decayJ
			
			return hotnessI > hotnessJ
		})
	}
	
	return videos
}

// WebSocket处理
func handleWSBroadcast() {
	for {
		msg := <-wsBroadcast
		for client := range wsClients {
			// 如果消息指定了用户ID，只发送给该用户
			if msg.UserID > 0 && msg.UserID != client.userID {
				continue
			}
			
			err := client.conn.WriteJSON(msg)
			if err != nil {
				log.Printf("WebSocket发送错误: %v", err)
				client.conn.Close()
				delete(wsClients, client)
			}
		}
	}
}

func wsHandler(c *gin.Context) {
	session := sessions.Default(c)
	userID, ok := session.Get("user_id").(int)
	if !ok {
		c.JSON(http.StatusUnauthorized, gin.H{"error": "未登录"})
		return
	}
	
	conn, err := upgrader.Upgrade(c.Writer, c.Request, nil)
	if err != nil {
		log.Printf("WebSocket升级失败: %v", err)
		return
	}
	defer conn.Close()
	
	client := &WSClient{conn: conn, userID: userID}
	wsClients[client] = true
	
	// 保持连接
	for {
		var msg map[string]interface{}
		err := conn.ReadJSON(&msg)
		if err != nil {
			delete(wsClients, client)
			break
		}
		// 处理客户端消息（如果需要）
	}
}

// 中间件
func authRequired() gin.HandlerFunc {
	return func(c *gin.Context) {
		session := sessions.Default(c)
		if session.Get("logged_in") != true {
			if strings.Contains(c.Request.Header.Get("Accept"), "application/json") ||
				c.Request.Header.Get("X-Requested-With") == "XMLHttpRequest" {
				c.JSON(http.StatusUnauthorized, gin.H{
					"success": false,
					"message": "请先登录",
					"redirect": "/login",
				})
				c.Abort()
				return
			}
			c.Redirect(http.StatusFound, "/login")
			c.Abort()
			return
		}
		c.Next()
	}
}

func adminRequired() gin.HandlerFunc {
	return func(c *gin.Context) {
		session := sessions.Default(c)
		userID := session.Get("user_id")
		if userID == nil {
			c.Redirect(http.StatusFound, "/login")
			c.Abort()
			return
		}
		
		user := findUserByID(userID.(int))
		if user == nil || !user.IsAdmin {
			session.AddFlash("只有管理员可以访问该页面！", "error")
			session.Save()
			c.Redirect(http.StatusFound, "/")
			c.Abort()
			return
		}
		c.Next()
	}
}

// 模板函数
func templateFunctions() template.FuncMap {
	return template.FuncMap{
		"formatTime": func(t string) string {
			parsed, err := time.Parse("2006-01-02 15:04:05", t)
			if err != nil {
				return t
			}
			now := time.Now()
			diff := now.Sub(parsed)
			
			if diff < time.Minute {
				return "刚刚"
			} else if diff < time.Hour {
				return fmt.Sprintf("%.0f分钟前", diff.Minutes())
			} else if diff < 24*time.Hour {
				return fmt.Sprintf("%.0f小时前", diff.Hours())
			} else if diff < 7*24*time.Hour {
				return fmt.Sprintf("%.0f天前", diff.Hours()/24)
			} else {
				return parsed.Format("2006-01-02")
			}
		},
		"formatNumber": func(n int) string {
			if n >= 10000 {
				return fmt.Sprintf("%.1f万", float64(n)/10000)
			} else if n >= 1000 {
				return fmt.Sprintf("%.1f千", float64(n)/1000)
			}
			return fmt.Sprintf("%d", n)
		},
		"truncate": func(s string, length int) string {
			if len(s) <= length {
				return s
			}
			return s[:length] + "..."
		},
	}
}

// Web路由
func setupWebRoutes(r *gin.Engine) {
	// 静态文件
	r.Static("/static", StaticFolder)
	r.StaticFile("/favicon.ico", filepath.Join(StaticFolder, "favicon.ico"))
	
	// 首页
	r.GET("/", func(c *gin.Context) {
		session := sessions.Default(c)
		if session.Get("logged_in") != true {
			c.Redirect(http.StatusFound, "/login")
			return
		}
		
		sortedVideos := sortVideos(c, videos)
		flashes := session.Flashes()
		session.Save()
		
		c.HTML(http.StatusOK, "index.html", gin.H{
			"title":   systemConfig.Title,
			"videos":  sortedVideos,
			"userID":  session.Get("user_id"),
			"flashes": flashes,
			"sort":    c.DefaultQuery("sort", "hot"),
		})
	})
	
	// 注册
	r.GET("/register", func(c *gin.Context) {
		session := sessions.Default(c)
		flashes := session.Flashes()
		session.Save()
		
		c.HTML(http.StatusOK, "register.html", gin.H{
			"title":   systemConfig.Title,
			"flashes": flashes,
		})
	})
	
	r.POST("/register", func(c *gin.Context) {
		username := c.PostForm("username")
		password := c.PostForm("password")
		
		session := sessions.Default(c)
		
		if len(username) < 3 || len(username) > 20 {
			session.AddFlash("用户名长度必须在3-20个字符之间", "error")
			session.Save()
			c.Redirect(http.StatusFound, "/register")
			return
		}
		
		if len(password) < 6 {
			session.AddFlash("密码长度必须至少6个字符", "error")
			session.Save()
			c.Redirect(http.StatusFound, "/register")
			return
		}
		
		if findUserByUsername(username) != nil {
			session.AddFlash("用户名已存在！", "error")
			session.Save()
			c.Redirect(http.StatusFound, "/register")
			return
		}
		
		newUser := User{
			ID:        len(users) + 1,
			Username:  username,
			Password:  password,
			IsAdmin:   false,
			AvatarFile: "",
			CreatedAt: time.Now().Format("2006-01-02 15:04:05"),
			LastLogin: time.Now().Format("2006-01-02 15:04:05"),
		}
		
		users = append(users, newUser)
		saveUsers()
		
		session.AddFlash("注册成功，请登录！", "success")
		session.Save()
		c.Redirect(http.StatusFound, "/login")
	})
	
	// 登录
	r.GET("/login", func(c *gin.Context) {
		session := sessions.Default(c)
		flashes := session.Flashes()
		session.Save()
		
		c.HTML(http.StatusOK, "login.html", gin.H{
			"title":   systemConfig.Title,
			"flashes": flashes,
		})
	})
	
	r.POST("/login", func(c *gin.Context) {
		username := c.PostForm("username")
		password := c.PostForm("password")
		
		session := sessions.Default(c)
		
		user := findUserByUsername(username)
		if user == nil || user.Password != password {
			session.AddFlash("用户名或密码错误！", "error")
			session.Save()
			c.Redirect(http.StatusFound, "/login")
			return
		}
		
		// 更新最后登录时间
		user.LastLogin = time.Now().Format("2006-01-02 15:04:05")
		saveUsers()
		
		session.Set("logged_in", true)
		session.Set("user_id", user.ID)
		session.Set("username", user.Username)
		session.AddFlash("登录成功！", "success")
		session.Save()
		
		// 发送WebSocket通知
		wsBroadcast <- WSMessage{
			Type: "notification",
			Data: gin.H{
				"message": fmt.Sprintf("用户 %s 已登录", user.Username),
				"time":    time.Now().Format("15:04:05"),
			},
		}
		
		c.Redirect(http.StatusFound, "/")
	})
	
	// 登出
	r.GET("/logout", func(c *gin.Context) {
		session := sessions.Default(c)
		username := session.Get("username")
		session.Clear()
		session.AddFlash("已注销登录！", "success")
		session.Save()
		
		log.Printf("用户注销: %v", username)
		c.Redirect(http.StatusFound, "/login")
	})
	
	// 上传视频
	r.GET("/upload", authRequired(), func(c *gin.Context) {
		session := sessions.Default(c)
		flashes := session.Flashes()
		session.Save()
		
		c.HTML(http.StatusOK, "upload.html", gin.H{
			"title":   systemConfig.Title,
			"flashes": flashes,
		})
	})
	
	r.POST("/upload", authRequired(), func(c *gin.Context) {
		session := sessions.Default(c)
		userID := session.Get("user_id").(int)
		user := findUserByID(userID)
		
		// 获取表单数据
		title := strings.TrimSpace(c.PostForm("title"))
		description := strings.TrimSpace(c.PostForm("description"))
		category := c.DefaultPostForm("category", "其他")
		
		// 验证
		if title == "" || len(title) > 100 {
			session.AddFlash("标题不能为空且不能超过100个字符", "error")
			session.Save()
			c.Redirect(http.StatusFound, "/upload")
			return
		}
		
		// 获取文件
		videoFile, err := c.FormFile("video")
		if err != nil {
			session.AddFlash("请选择视频文件", "error")
			session.Save()
			c.Redirect(http.StatusFound, "/upload")
			return
		}
		
		coverFile, err := c.FormFile("cover")
		if err != nil {
			session.AddFlash("请选择封面图片", "error")
			session.Save()
			c.Redirect(http.StatusFound, "/upload")
			return
		}
		
		// 检查文件大小
		if videoFile.Size > 500*1024*1024 { // 500MB限制
			session.AddFlash("视频文件不能超过500MB", "error")
			session.Save()
			c.Redirect(http.StatusFound, "/upload")
			return
		}
		
		if coverFile.Size > 10*1024*1024 { // 10MB限制
			session.AddFlash("封面图片不能超过10MB", "error")
			session.Save()
			c.Redirect(http.StatusFound, "/upload")
			return
		}
		
		// 检查文件类型
		videoExt := []string{"mp4", "avi", "mov", "mkv", "webm"}
		coverExt := []string{"jpg", "jpeg", "png", "gif", "webp"}
		
		if !getAllowedExtensions(videoFile.Filename, videoExt) {
			session.AddFlash("视频格式不支持（仅限 mp4/avi/mov/mkv/webm）", "error")
			session.Save()
			c.Redirect(http.StatusFound, "/upload")
			return
		}
		
		if !getAllowedExtensions(coverFile.Filename, coverExt) {
			session.AddFlash("封面格式不支持（仅限 jpg/png/gif/webp）", "error")
			session.Save()
			c.Redirect(http.StatusFound, "/upload")
			return
		}
		
		// 生成文件名
		videoExtStr := filepath.Ext(videoFile.Filename)
		coverExtStr := filepath.Ext(coverFile.Filename)
		
		videoFilename := fmt.Sprintf("video_%d_%s%s", time.Now().Unix(), uuid.New().String()[:8], videoExtStr)
		coverFilename := fmt.Sprintf("cover_%d_%s%s", time.Now().Unix(), uuid.New().String()[:8], coverExtStr)
		
		// 保存文件
		videoPath := filepath.Join(UploadFolder, videoFilename)
		coverPath := filepath.Join(CoverFolder, coverFilename)
		
		if err := c.SaveUploadedFile(videoFile, videoPath); err != nil {
			session.AddFlash("视频保存失败: " + err.Error(), "error")
			session.Save()
			c.Redirect(http.StatusFound, "/upload")
			return
		}
		
		if err := c.SaveUploadedFile(coverFile, coverPath); err != nil {
			// 删除已保存的视频
			os.Remove(videoPath)
			session.AddFlash("封面保存失败: " + err.Error(), "error")
			session.Save()
			c.Redirect(http.StatusFound, "/upload")
			return
		}
		
		// 创建视频记录
		now := time.Now().Format("2006-01-02 15:04:05")
		newVideo := Video{
			VideoFilename:    videoFilename,
			CoverFilename:    coverFilename,
			Title:            title,
			Description:      description,
			Category:         category,
			Uploader:         user.Username,
			UploadTime:       now,
			CreatedAt:        now,
			UpdatedAt:        now,
			UserID:           userID,
			PlayCount:        0,
			LikeCount:        0,
			CommentCount:     0,
			ViewsPerDay:      0,
			VideoStorageType: "local",
			CoverStorageType: "local",
		}
		
		videos = append(videos, newVideo)
		saveVideos()
		
		// 发送WebSocket通知
		wsBroadcast <- WSMessage{
			Type: "notification",
			Data: gin.H{
				"message": fmt.Sprintf("用户 %s 上传了新视频: %s", user.Username, title),
				"video":   videoFilename,
				"time":    now,
			},
		}
		
		session.AddFlash("视频上传成功！", "success")
		session.Save()
		c.Redirect(http.StatusFound, "/")
	})
	
	// 播放视频
	r.GET("/play/:filename", func(c *gin.Context) {
		filename := c.Param("filename")
		video := findVideoByFilename(filename)
		
		session := sessions.Default(c)
		
		if video == nil {
			session.AddFlash("视频不存在！", "error")
			session.Save()
			c.Redirect(http.StatusFound, "/")
			return
		}
		
		// 增加播放计数
		video.PlayCount++
		
		// 更新每日观看数
		uploadTime, _ := time.Parse("2006-01-02 15:04:05", video.CreatedAt)
		daysSinceUpload := time.Since(uploadTime).Hours() / 24
		if daysSinceUpload > 0 {
			video.ViewsPerDay = int(float64(video.PlayCount) / daysSinceUpload)
		}
		
		video.UpdatedAt = time.Now().Format("2006-01-02 15:04:05")
		saveVideos()
		
		// 获取评论
		videoComments := comments[filename]
		
		// 获取上传者信息
		uploader := findUserByID(video.UserID)
		
		// 获取相关视频（同分类）
		var relatedVideos []Video
		for _, v := range videos {
			if v.VideoFilename != filename && v.Category == video.Category {
				relatedVideos = append(relatedVideos, v)
				if len(relatedVideos) >= 4 {
					break
				}
			}
		}
		
		// 发送播放统计通知
		wsBroadcast <- WSMessage{
			Type: "play_count",
			Data: gin.H{
				"video": video.VideoFilename,
				"title": video.Title,
				"count": video.PlayCount,
			},
		}
		
		flashes := session.Flashes()
		session.Save()
		
		c.HTML(http.StatusOK, "play.html", gin.H{
			"title":         systemConfig.Title,
			"video":         video,
			"comments":      videoComments,
			"uploader":      uploader,
			"relatedVideos": relatedVideos,
			"flashes":       flashes,
		})
	})
	
	// 用户主页
	r.GET("/user/:username", authRequired(), func(c *gin.Context) {
		username := c.Param("username")
		user := findUserByUsername(username)
		
		session := sessions.Default(c)
		
		if user == nil {
			session.AddFlash("用户不存在", "error")
			session.Save()
			c.Redirect(http.StatusFound, "/")
			return
		}
		
		// 获取用户的视频
		var userVideos []Video
		for _, video := range videos {
			if video.UserID == user.ID {
				userVideos = append(userVideos, video)
			}
		}
		
		// 按上传时间排序
		sort.Slice(userVideos, func(i, j int) bool {
			t1, _ := time.Parse("2006-01-02 15:04:05", userVideos[i].CreatedAt)
			t2, _ := time.Parse("2006-01-02 15:04:05", userVideos[j].CreatedAt)
			return t1.After(t2)
		})
		
		flashes := session.Flashes()
		session.Save()
		
		c.HTML(http.StatusOK, "user_profile.html", gin.H{
			"title":   systemConfig.Title,
			"user":    user,
			"videos":  userVideos,
			"flashes": flashes,
		})
	})
	
	// 上传头像
	r.POST("/upload_avatar", authRequired(), func(c *gin.Context) {
		session := sessions.Default(c)
		userID := session.Get("user_id").(int)
		user := findUserByID(userID)
		
		if user == nil {
			session.AddFlash("用户不存在", "error")
			session.Save()
			c.Redirect(http.StatusFound, "/")
			return
		}
		
		avatarFile, err := c.FormFile("avatar")
		if err != nil {
			session.AddFlash("请选择头像文件", "error")
			session.Save()
			c.Redirect(http.StatusFound, "/user/"+user.Username)
			return
		}
		
		// 检查文件大小和类型
		if avatarFile.Size > 5*1024*1024 {
			session.AddFlash("头像文件不能超过5MB", "error")
			session.Save()
			c.Redirect(http.StatusFound, "/user/"+user.Username)
			return
		}
		
		avatarExt := []string{"jpg", "jpeg", "png", "gif", "webp"}
		if !getAllowedExtensions(avatarFile.Filename, avatarExt) {
			session.AddFlash("仅支持jpg、png、gif、webp格式", "error")
			session.Save()
			c.Redirect(http.StatusFound, "/user/"+user.Username)
			return
		}
		
		// 生成新文件名
		ext := filepath.Ext(avatarFile.Filename)
		newFilename := fmt.Sprintf("avatar_%d_%s%s", user.ID, uuid.New().String()[:8], ext)
		avatarPath := filepath.Join(AvatarFolder, newFilename)
		
		// 删除旧头像
		if user.AvatarFile != "" {
			oldPath := filepath.Join(AvatarFolder, user.AvatarFile)
			os.Remove(oldPath)
		}
		
		// 保存新头像
		if err := c.SaveUploadedFile(avatarFile, avatarPath); err != nil {
			session.AddFlash("头像上传失败: " + err.Error(), "error")
			session.Save()
			c.Redirect(http.StatusFound, "/user/"+user.Username)
			return
		}
		
		// 更新用户信息
		user.AvatarFile = newFilename
		saveUsers()
		
		session.AddFlash("头像上传成功", "success")
		session.Save()
		c.Redirect(http.StatusFound, "/user/"+user.Username)
	})
	
	// 管理员页面
	r.GET("/admin", authRequired(), adminRequired(), func(c *gin.Context) {
		session := sessions.Default(c)
		flashes := session.Flashes()
		session.Save()
		
		// 统计信息
		stats := gin.H{
			"total_users":    len(users),
			"total_videos":   len(videos),
			"total_comments": 0,
			"today_uploads":  0,
		}
		
		// 计算评论总数和今日上传
		for _, videoComments := range comments {
			stats["total_comments"] = stats["total_comments"].(int) + len(videoComments)
		}
		
		today := time.Now().Format("2006-01-02")
		for _, video := range videos {
			if strings.HasPrefix(video.CreatedAt, today) {
				stats["today_uploads"] = stats["today_uploads"].(int) + 1
			}
		}
		
		c.HTML(http.StatusOK, "admin.html", gin.H{
			"title":   systemConfig.Title,
			"users":   users,
			"videos":  videos,
			"stats":   stats,
			"flashes": flashes,
		})
	})
	
	r.POST("/admin/action", authRequired(), adminRequired(), func(c *gin.Context) {
		action := c.PostForm("action")
		
		session := sessions.Default(c)
		
		switch action {
		case "delete_user":
			userID, _ := strconv.Atoi(c.PostForm("user_id"))
			var newUsers []User
			for _, user := range users {
				if user.ID != userID {
					newUsers = append(newUsers, user)
				} else {
					// 删除用户的头像
					if user.AvatarFile != "" {
						avatarPath := filepath.Join(AvatarFolder, user.AvatarFile)
						os.Remove(avatarPath)
					}
				}
			}
			users = newUsers
			saveUsers()
			session.AddFlash("用户删除成功", "success")
			
		case "delete_video":
			videoFilename := c.PostForm("video_filename")
			var newVideos []Video
			for _, video := range videos {
				if video.VideoFilename != videoFilename {
					newVideos = append(newVideos, video)
				} else {
					// 删除文件
					videoPath := filepath.Join(UploadFolder, video.VideoFilename)
					coverPath := filepath.Join(CoverFolder, video.CoverFilename)
					os.Remove(videoPath)
					os.Remove(coverPath)
					
					// 删除评论
					delete(comments, videoFilename)
					saveComments()
				}
			}
			videos = newVideos
			saveVideos()
			session.AddFlash("视频删除成功", "success")
			
		case "update_system":
			title := c.PostForm("title")
			if title != "" {
				systemConfig.Title = title
				saveSystemConfig()
				session.AddFlash("系统配置已更新", "success")
			}
		}
		
		session.Save()
		c.Redirect(http.StatusFound, "/admin")
	})
	
	// 搜索
	r.GET("/search", func(c *gin.Context) {
		query := strings.TrimSpace(c.Query("q"))
		category := c.Query("category")
		
		session := sessions.Default(c)
		
		if query == "" && category == "" {
			session.AddFlash("请输入搜索内容或选择分类！", "info")
			session.Save()
			c.Redirect(http.StatusFound, "/")
			return
		}
		
		var searchResults []Video
		queryLower := strings.ToLower(query)
		
		for _, video := range videos {
			match := false
			
			if query != "" {
				if strings.Contains(strings.ToLower(video.Title), queryLower) ||
					strings.Contains(strings.ToLower(video.Description), queryLower) ||
					strings.Contains(strings.ToLower(video.Uploader), queryLower) {
					match = true
				}
			}
			
			if category != "" && video.Category == category {
				match = true
			}
			
			if query == "" || category != "" {
				match = true
			}
			
			if match {
				searchResults = append(searchResults, video)
			}
		}
		
		// 按相关度排序
		if query != "" {
			sort.Slice(searchResults, func(i, j int) bool {
				// 简单相关度算法
				scoreI := 0
				scoreJ := 0
				
				if strings.Contains(strings.ToLower(searchResults[i].Title), queryLower) {
					scoreI += 3
				}
				if strings.Contains(strings.ToLower(searchResults[i].Description), queryLower) {
					scoreI += 1
				}
				
				if strings.Contains(strings.ToLower(searchResults[j].Title), queryLower) {
					scoreJ += 3
				}
				if strings.Contains(strings.ToLower(searchResults[j].Description), queryLower) {
					scoreJ += 1
				}
				
				if scoreI == scoreJ {
					return searchResults[i].PlayCount > searchResults[j].PlayCount
				}
				return scoreI > scoreJ
			})
		}
		
		// 获取所有分类
		categories := make(map[string]int)
		for _, video := range videos {
			categories[video.Category]++
		}
		
		flashes := session.Flashes()
		session.Save()
		
		c.HTML(http.StatusOK, "search_results.html", gin.H{
			"title":      systemConfig.Title,
			"query":      query,
			"category":   category,
			"videos":     searchResults,
			"categories": categories,
			"flashes":    flashes,
		})
	})
	
	// 评论
	r.POST("/comment", authRequired(), func(c *gin.Context) {
		session := sessions.Default(c)
		userID := session.Get("user_id").(int)
		user := findUserByID(userID)
		
		videoFilename := c.PostForm("video_filename")
		commentText := strings.TrimSpace(c.PostForm("comment_text"))
		
		if user == nil {
			session.AddFlash("用户不存在，请重新登录！", "error")
			session.Save()
			c.Redirect(http.StatusFound, "/login")
			return
		}
		
		if commentText == "" || len(commentText) > 500 {
			session.AddFlash("评论内容不能为空且不能超过500个字符", "error")
			session.Save()
			c.Redirect(http.StatusFound, "/play/"+videoFilename)
			return
		}
		
		// 创建评论
		newComment := Comment{
			ID:        len(comments[videoFilename]) + 1,
			VideoID:   videoFilename,
			UserID:    userID,
			Username:  user.Username,
			Text:      commentText,
			CreatedAt: time.Now().Format("2006-01-02 15:04:05"),
			Likes:     0,
			LikedBy:   []int{},
		}
		
		// 添加到评论列表
		if comments[videoFilename] == nil {
			comments[videoFilename] = []Comment{}
		}
		comments[videoFilename] = append(comments[videoFilename], newComment)
		
		// 更新视频评论数
		video := findVideoByFilename(videoFilename)
		if video != nil {
			video.CommentCount = len(comments[videoFilename])
			video.UpdatedAt = time.Now().Format("2006-01-02 15:04:05")
			saveVideos()
		}
		
		saveComments()
		
		// 发送WebSocket通知
		if video != nil {
			wsBroadcast <- WSMessage{
				Type: "notification",
				Data: gin.H{
					"message": fmt.Sprintf("用户 %s 评论了视频: %s", user.Username, video.Title),
					"comment": commentText[:min(50, len(commentText))] + "...",
					"time":    time.Now().Format("15:04:05"),
				},
				UserID: video.UserID,
			}
		}
		
		session.AddFlash("评论成功！", "success")
		session.Save()
		c.Redirect(http.StatusFound, "/play/"+videoFilename)
	})
	
	// 点赞评论
	r.POST("/like_comment", authRequired(), func(c *gin.Context) {
		session := sessions.Default(c)
		userID := session.Get("user_id").(int)
		
		videoFilename := c.PostForm("video_filename")
		commentIndex, _ := strconv.Atoi(c.PostForm("comment_index"))
		
		videoComments := comments[videoFilename]
		if commentIndex >= 0 && commentIndex < len(videoComments) {
			comment := &videoComments[commentIndex]
			
			// 检查是否已经点赞
			alreadyLiked := false
			for _, likedUserID := range comment.LikedBy {
				if likedUserID == userID {
					alreadyLiked = true
					break
				}
			}
			
			if alreadyLiked {
				session.AddFlash("您已经点过赞了！", "info")
			} else {
				comment.Likes++
				comment.LikedBy = append(comment.LikedBy, userID)
				
				// 更新视频点赞数（所有评论的总点赞数）
				video := findVideoByFilename(videoFilename)
				if video != nil {
					totalLikes := 0
					for _, c := range videoComments {
						totalLikes += c.Likes
					}
					video.LikeCount = totalLikes
					saveVideos()
					
					// 发送点赞通知
					wsBroadcast <- WSMessage{
						Type: "like",
						Data: gin.H{
							"video":   videoFilename,
							"title":   video.Title,
							"comment": commentIndex + 1,
							"likes":   comment.Likes,
						},
					}
				}
				
				saveComments()
				session.AddFlash("点赞成功！", "success")
			}
		} else {
			session.AddFlash("评论不存在！", "error")
		}
		
		session.Save()
		c.Redirect(http.StatusFound, "/play/"+videoFilename)
	})
	
	// 点赞视频
	r.POST("/like_video", authRequired(), func(c *gin.Context) {
		session := sessions.Default(c)
		userID := session.Get("user_id").(int)
		
		videoFilename := c.PostForm("video_filename")
		video := findVideoByFilename(videoFilename)
		
		if video == nil {
			session.AddFlash("视频不存在！", "error")
			session.Save()
			c.Redirect(http.StatusFound, "/")
			return
		}
		
		// 简单点赞，实际应该记录用户是否已点赞
		video.LikeCount++
		video.UpdatedAt = time.Now().Format("2006-01-02 15:04:05")
		saveVideos()
		
		// 发送点赞通知
		wsBroadcast <- WSMessage{
			Type: "like",
			Data: gin.H{
				"video": videoFilename,
				"title": video.Title,
				"likes": video.LikeCount,
			},
		}
		
		session.AddFlash("点赞成功！", "success")
		session.Save()
		c.Redirect(http.StatusFound, "/play/"+videoFilename)
	})
	
	// WebSocket连接
	r.GET("/ws", func(c *gin.Context) {
		wsHandler(c)
	})
	
	// 静态文件服务
	r.GET("/static/uploads/covers/:filename", func(c *gin.Context) {
		filename := c.Param("filename")
		filePath := filepath.Join(CoverFolder, filename)
		
		if _, err := os.Stat(filePath); os.IsNotExist(err) {
			c.String(http.StatusNotFound, "封面未找到")
			return
		}
		
		c.File(filePath)
	})
	
	r.GET("/static/uploads/videos/:filename", func(c *gin.Context) {
		filename := c.Param("filename")
		filePath := filepath.Join(UploadFolder, filename)
		
		if _, err := os.Stat(filePath); os.IsNotExist(err) {
			c.String(http.StatusNotFound, "视频未找到")
			return
		}
		
		// 支持Range请求
		http.ServeFile(c.Writer, c.Request, filePath)
	})
	
	r.GET("/static/uploads/avatars/:filename", func(c *gin.Context) {
		filename := c.Param("filename")
		filePath := filepath.Join(AvatarFolder, filename)
		
		if _, err := os.Stat(filePath); os.IsNotExist(err) {
			c.String(http.StatusNotFound, "头像未找到")
			return
		}
		
		c.File(filePath)
	})
	
	// 获取视频流（支持断点续传）
	r.GET("/stream/:filename", func(c *gin.Context) {
		filename := c.Param("filename")
		filePath := filepath.Join(UploadFolder, filename)
		
		video := findVideoByFilename(filename)
		if video == nil {
			c.String(http.StatusNotFound, "视频未找到")
			return
		}
		
		// 增加播放计数
		video.PlayCount++
		saveVideos()
		
		// 使用http.ServeFile支持Range请求
		http.ServeFile(c.Writer, c.Request, filePath)
	})
}

// API路由
func setupAPIRoutes(r *gin.Engine) {
	api := r.Group("/api/v1")
	
	// 公共API
	api.GET("/videos", func(c *gin.Context) {
		sortedVideos := sortVideos(c, videos)
		
		// 分页
		page, _ := strconv.Atoi(c.DefaultQuery("page", "1"))
		pageSize, _ := strconv.Atoi(c.DefaultQuery("page_size", "20"))
		if pageSize > 100 {
			pageSize = 100
		}
		
		start := (page - 1) * pageSize
		end := start + pageSize
		if start >= len(sortedVideos) {
			start = len(sortedVideos)
		}
		if end > len(sortedVideos) {
			end = len(sortedVideos)
		}
		
		pagedVideos := sortedVideos[start:end]
		
		c.JSON(http.StatusOK, gin.H{
			"success": true,
			"data": gin.H{
				"videos": pagedVideos,
				"pagination": gin.H{
					"page":       page,
					"page_size":  pageSize,
					"total":      len(sortedVideos),
					"total_page": (len(sortedVideos) + pageSize - 1) / pageSize,
				},
			},
		})
	})
	
	api.GET("/video/:filename", func(c *gin.Context) {
		filename := c.Param("filename")
		video := findVideoByFilename(filename)
		
		if video == nil {
			c.JSON(http.StatusNotFound, gin.H{
				"success": false,
				"message": "视频未找到",
			})
			return
		}
		
		c.JSON(http.StatusOK, gin.H{
			"success": true,
			"data":    video,
		})
	})
	
	api.GET("/categories", func(c *gin.Context) {
		categories := make(map[string]int)
		for _, video := range videos {
			categories[video.Category]++
		}
		
		c.JSON(http.StatusOK, gin.H{
			"success": true,
			"data":    categories,
		})
	})
	
	api.GET("/stats", func(c *gin.Context) {
		totalComments := 0
		for _, videoComments := range comments {
			totalComments += len(videoComments)
		}
		
		today := time.Now().Format("2006-01-02")
		todayUploads := 0
		for _, video := range videos {
			if strings.HasPrefix(video.CreatedAt, today) {
				todayUploads++
			}
		}
		
		c.JSON(http.StatusOK, gin.H{
			"success": true,
			"data": gin.H{
				"total_users":    len(users),
				"total_videos":   len(videos),
				"total_comments": totalComments,
				"today_uploads":  todayUploads,
			},
		})
	})
	
	// 需要认证的API
	authAPI := api.Group("/")
	authAPI.Use(authRequired())
	
	authAPI.POST("/video/:filename/like", func(c *gin.Context) {
		filename := c.Param("filename")
		video := findVideoByFilename(filename)
		
		if video == nil {
			c.JSON(http.StatusNotFound, gin.H{
				"success": false,
				"message": "视频未找到",
			})
			return
		}
		
		video.LikeCount++
		saveVideos()
		
		c.JSON(http.StatusOK, gin.H{
			"success": true,
			"data": gin.H{
				"likes": video.LikeCount,
			},
		})
	})
	
	authAPI.POST("/video/:filename/comment", func(c *gin.Context) {
		session := sessions.Default(c)
		userID := session.Get("user_id").(int)
		user := findUserByID(userID)
		
		filename := c.Param("filename")
		var req struct {
			Text string `json:"text"`
		}
		
		if err := c.ShouldBindJSON(&req); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{
				"success": false,
				"message": "请求格式错误",
			})
			return
		}
		
		if user == nil {
			c.JSON(http.StatusUnauthorized, gin.H{
				"success": false,
				"message": "用户不存在",
			})
			return
		}
		
		if req.Text == "" || len(req.Text) > 500 {
			c.JSON(http.StatusBadRequest, gin.H{
				"success": false,
				"message": "评论内容不能为空且不能超过500个字符",
			})
			return
		}
		
		newComment := Comment{
			ID:        len(comments[filename]) + 1,
			VideoID:   filename,
			UserID:    userID,
			Username:  user.Username,
			Text:      req.Text,
			CreatedAt: time.Now().Format("2006-01-02 15:04:05"),
			Likes:     0,
			LikedBy:   []int{},
		}
		
		if comments[filename] == nil {
			comments[filename] = []Comment{}
		}
		comments[filename] = append(comments[filename], newComment)
		
		// 更新视频评论数
		video := findVideoByFilename(filename)
		if video != nil {
			video.CommentCount = len(comments[filename])
			saveVideos()
		}
		
		saveComments()
		
		c.JSON(http.StatusOK, gin.H{
			"success": true,
			"data":    newComment,
		})
	})
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	// 设置Gin模式
	gin.SetMode(gin.ReleaseMode)
	
	// 初始化Gin
	r := gin.Default()
	
	// 设置session
	store := cookie.NewStore([]byte(SecretKey))
	r.Use(sessions.Sessions("foxcm_session", store))
	
	// 自定义模板函数
	r.SetFuncMap(templateFunctions())
	
	// 加载模板
	r.LoadHTMLGlob(filepath.Join(TemplateFolder, "*.html"))
	
	// 设置路由
	setupWebRoutes(r)
	setupAPIRoutes(r)
	
	// 启动信息
	fmt.Println("=" + strings.Repeat("=", 60))
	fmt.Println("FoxCM 媒体分享平台 - Go重构版")
	fmt.Println("版本: 2.0.0")
	fmt.Println("作者: FoxHome")
	fmt.Println("=" + strings.Repeat("=", 60))
	fmt.Printf("运行地址: http://0.0.0.0:%s\n", Port)
	fmt.Printf("API地址: http://0.0.0.0:%s/api/v1/\n", Port)
	fmt.Printf("WebSocket: ws://0.0.0.0:%s/ws\n", Port)
	fmt.Printf("数据目录: %s\n", DataFolder)
	fmt.Printf("上传目录: %s\n", UploadFolder)
	fmt.Println("=" + strings.Repeat("=", 60))
	fmt.Println("排序功能已启用:")
	fmt.Println("  /?sort=hot     - 热门排序（默认）")
	fmt.Println("  /?sort=newest  - 最新上传")
	fmt.Println("  /?sort=likes   - 最多点赞")
	fmt.Println("  /?sort=views   - 最多播放")
	fmt.Println("=" + strings.Repeat("=", 60))
	
	// 启动服务器
	log.Printf("服务器启动在端口 %s", Port)
	if err := r.Run(":" + Port); err != nil {
		log.Fatal("服务器启动失败:", err)
	}
}