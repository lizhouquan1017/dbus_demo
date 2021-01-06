# 测试说明
1. 安装pip3：sudo apt-get install python3-pip

2. cd 到工程目录resource下，安装python所需的三方包：pip3 install -r requestment.txt

3. 安装 allure离线安装包，解压后执行 mv allure-2.13.5 /usr/bin/allure,将/usr/bin/allure/bin添加到环境变量

4. sudo apt install openjdk-8-jdk  安装java

5. 脚本选择：从resource/caselist 里面copy 想要执行的dbus脚本到excute.txt即可

   如：\script\dbus\systemBus\soundThemePlayer\001_enableSoundDesktopLogin.py

6. 脚本执行：工程目录下打开终端，直接运行 python3 pytest_runner.py

7. 日志查看：jenkins执行直接看allure报告。本地执行，需要将pytest_runner.py os.system(f"allure generate --clean {allure_results_path} -o {allure_report_path}")代码放开注释，cd 到allure-report目录里面，终端执行 allure open . 查看。

# dbus测试环境自动化部署说明
1. cd 到工程目录resource/tools/auto_envion_deploy下，使用命令sh auto_envion_deploy.sh 执行脚本，完成环境安装