import os,sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+"/base"))
import login_index
#用户管理测试
driver = login_index.getLoginIndex()