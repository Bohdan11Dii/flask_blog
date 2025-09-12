# Blog Flask


## 📂 Project Structure

```bash
.
├── 📄 app.py
├── 📂 blog
│   ├── 📂 forms
│   │   ├── 📄 form_account.py
│   │   ├── 📄 form_post.py
│   │   └── 📄 __init__.py
│   ├── 📂 models
│   │   ├── 📄 post.py
│   │   ├── 📄 user.py
│   │   └── 📄 __init__.py
│   ├── 📂 routes
│   │   ├── 📄 main_routes.py
│   │   ├── 📄 posts_routes.py
│   │   ├── 📄 users_routs.py
│   │   └── 📄 __init__.py
│   ├── 📂 static
│   │   ├── 🎨 css
│   │   │   ├── 🎨 account.css
│   │   │   ├── 🎨 alert.css
│   │   │   ├── 🎨 forms.css
│   │   │   ├── 🎨 posts.css
│   │   │   ├── 🎨 registration.css
│   │   │   └── 🎨 styles.css
│   │   ├── 📜 js
│   │   │   ├── 📜 alert.js
│   │   │   └── 📜 scripts.js
│   │   ├── 🖼️ assets
│   │   │   ├── 🖼️ favicon.ico
│   │   │   └── 📂 img
│   │   │       ├── 🖼️ about-bg.jpg
│   │   │       ├── 🖼️ autumn.jpg
│   │   │       ├── 🖼️ contact-bg.jpg
│   │   │       ├── 🖼️ forest.jpg
│   │   │       ├── 🖼️ home-bg.jpg
│   │   │       ├── 🖼️ images.jpeg
│   │   │       ├── 🖼️ images.jpg
│   │   │       ├── 🖼️ post-bg.jpg
│   │   │       └── 🖼️ post-sample-image.jpg
│   │   └── 📂 profile_pics
│   │       ├── 🖼️ default.jpg
│   │       ├── 🖼️ *.jpg
│   └── 📂 templates
│       ├── 📝 layout.html
│       ├── 📝 contact.html
│       ├── 📂 about
│       │   └── 📝 about.html
│       ├── 📂 account
│       │   └── 📝 account.html
│       ├── 📂 home
│       │   └── 📝 index.html
│       ├── 📂 post
│       │   ├── 📝 create_post.html
│       │   ├── 📝 post.html
│       │   └── 📝 user_posts.html
│       ├── 📂 includes
│       │   ├── 📝 alert_box.html
│       │   ├── 📝 footer.html
│       │   ├── 📝 header.html
│       │   └── 📝 sidebar.html
│       └── 📂 registration
│           ├── 📝 base.html
│           ├── 📝 login.html
│           ├── 📝 register.html
│           ├── 📝 reset_request.html
│           └── 📝 reset_token.html
├── 📂 configurations
│   ├── 📄 config.py
│   ├── 📄 utils.py
│   └── 📄 __init__.py
├── 📂 instance
│   └── 📄 site.db
└── 📄 README.md
