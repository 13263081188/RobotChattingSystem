<h1> 本文件为RobotChattingSystem前后端交互所需API</h1>

## 1.邮箱验证：
**api**:	url+emailCheck<br>
**param**:email<br>
**return**:     
	{<br>
	***'isOk':true***,     (若为false，则无'number')<br>
	***'errmsg':"未知错误"***     (默认为未知错误，考虑到该邮箱已注册)<br>
	***'number':''***    (四位数的str类型验证码)<br>
	}<br>

注：需要前端进行判断验证码是否正确.(后端向邮箱也发送了相同的验证码）<br>

## 2.注册：
**api**:	url+signUp<br>
**param**:	email,username,password<br>
**return**:<br>	
	{<br>
	***'isOk':true*** (注册成功则为true)<br>
	***'errmsg':"未知错误"***<br>
	}<br>
注：该api只判断用户名是否唯一，邮箱在emailCheck时已判断<br>

## 3.登录：
**api**:	url+signIn<br>
**param**:	name, psw<br>
**return**:<br>
	{<br>
	**'isOk'**:true<br>
	**'errmsg'**:'未知错误'/'密码错误'/'邮箱错误'/'用户名错误'  
	}
