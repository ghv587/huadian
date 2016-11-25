
基本环境
    python环境:python2.7.6
    操作系统:   ubuntu14.0.4
    数据库:     mysql 5.5.52-0
    开发工具:   pyCharm

依赖包
[
    MySQL-python==1.2.5
    crypto==1.4.1
    paramiko==2.0.2
    tornado==4.4.1
    torndb==0.3
    peewee==2.8.3
]

安装提示：
    需先安装数据库，建议开发平台linux


文件结构说明：

huadian/
├── app
│   ├── handler
│   │   ├── addhost.py
│   │   ├── exc_cmd.py
│   │   ├── hostcheck.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── main.py
│   ├── ping.py
│   ├── ping.txt
│   └── utils
│       ├── db
│       │   ├── db.py
│       │   └── __init__.py
│       ├── __init__.py
│       ├── paracls
│       │   ├── __init__.py
│       │   └── paramiko_class.py
│       ├── peeweecls
│       │   ├── __init__.py
│       │   ├── monitorhost_model.py
│       │   └── peewee.db
│       └── snmp
│           ├── hostsnmp.py
│           └── __init__.py
├── bin
│   └── install.sh
├── config
│   ├── config.ini
│   ├── define.py
│   ├── hostconfig.ini
│   └── __init__.py
├── logfile
│   └── main.log
├── README.md
├── README.md~
├── static
│   ├── css
│   │   ├── bootstrap.css
│   │   ├── bootstrap.css.map
│   │   ├── bootstrap.min.css
│   │   ├── bootstrap-theme.css
│   │   ├── bootstrap-theme.css.map
│   │   ├── bootstrap-theme.min.css
│   │   ├── dashboard.css
│   │   └── sigin.css
│   ├── fonts
│   │   ├── glyphicons-halflings-regular.eot
│   │   ├── glyphicons-halflings-regular.svg
│   │   ├── glyphicons-halflings-regular.ttf
│   │   ├── glyphicons-halflings-regular.woff
│   │   └── glyphicons-halflings-regular.woff2
│   └── js
│       ├── bootstrap.js
│       ├── bootstrap.min.js
│       ├── ie10-viewport-bug-workaround.js
│       ├── ie-emulation-modes-warning.js
│       ├── npm.js
│       └── vendor
│           └── holder.min.js
└── template
    ├── addhost.html
    ├── application_manager.html
    ├── bar.html
    ├── base.html
    ├── index.html
    ├── laiba.html
    ├── left.html
    ├── login.html
    ├── mid-one.html
    ├── mid-two.html
    ├── monitor_device.html
    ├── monitor_host.html
    ├── monitor_log.html
    ├── monitor_performance.html
    ├── oper_file.html
    └── ping.html










