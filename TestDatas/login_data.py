# -*- coding: utf-8 -*-


class LoginData:
    # 正常登录
    login_success_data = {'username':'zhwwm','pwd':'Qqqq1111'}
    # 用户名或密码为空
    error_msg_from_login_box_data = [{'username':'zhwwm','pwd':'','excepted':'必填字段'},
                                     {'username':'','pwd':'Qqqq111','excepted':'必填字段'}]
    # 密码错误
    error_msg_from_wrong_pwd_data = {'username':'zhwwm', 'pwd':'Qqqq11', 'excepted': 'DSIE0011:账号或密码错误'}
    # 用户名错误
    error_msg_from_wrong_username_data = {'username':'zhww','pwd':'Qqqq1111','excepted':'DSIE0104:操作员不存在'}