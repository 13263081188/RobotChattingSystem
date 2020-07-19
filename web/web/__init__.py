import pymysql
pymysql.version_info = (1, 3, 13, "final", 0) #conda只能安装0.9.3版本，但django3.0需要1.3.13
pymysql.install_as_MySQLdb()
