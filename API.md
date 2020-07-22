<h1> 本文件为RobotChattingSystem前后端交互所需API</h1>
<h3>默认为post方法</h3>
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
	**'errmsg'**:'未知错误'/'密码错误'/'邮箱错误'/'用户名错误'  <br>
	**'user_id'**:''<br>
	}

## 4.发帖：
**api**:  url+toPost<br>
**param**: content(评论的内容),label(吐槽的标签）,isAnonymity<br>
**return**:<br>
{<br>
**'isOk'**:true<br>
**'errmsg'**:'未知错误'<br>
}

## 5.贴吧广场：（查看所有帖子）
**method**： GET
**api**: url+Posts<br>
**return**:<br>
{<br>
**'isOk'**:true<br>
**'errmsg'**:'未知错误'<br>
**'Posts'**: {'name':'','category':'','date':'','like':'','dislike':'','content':'','user_id':'','pk':''}<br>
}<br>

**注：**：posts为所有帖子的集合，每一个帖子包含以下信息：name为发帖人昵称，匿名则返回‘匿名’，category为帖子标签，like为点赞数，dislike为不喜欢数，content为内容,user_id为发帖人在数据库中的id，pk为该帖子在数据库中的id。

## 6.帖子信息：（查看单个帖子信息）
**api**：url+PostInfo<br>
**param**:pk<br>
**return**:<br>
{<br>
**'isOk'**:true<br>
**'errmsg'**:'未知错误'<br>
**'name'**:''<br>
**'category'**:''<br>
**'date'**:''<br>
**'like'**:''<br>
**'dislike'**:''<br>
**'content'**:''<br>
**'comments'**:{'name':,'content':''}<br>
}

## 7.发表评论
**api**：url+comment<br>
**param**:pk,comment,isAnonymity<br>
**return**:<br>
{<br>
**'isOk'**:true<br>
**'errmsg'**:'未知错误'<br>
}









