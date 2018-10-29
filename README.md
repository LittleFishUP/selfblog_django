# selfblog_django
# 使用django搭建个人博客
## 项目区块
### 步骤1
models区块，目标：搭建所需的数据库模型<br>
如下所示<br>
        1.建立user表实体类<br>
        包含用户名称（username）varchar<br>
        邮箱（email）varchar<br>
        年级（age）int<br>
        个人主站地址（myurl）varchar（可以为空）<br>
        密码（password）varchar<br>
        是否是作者（tinyint）默认为False<br>
```
class User(models.Model):
    username = models.CharField(max_length=30,verbose_name='用户名称')
    email = models.EmailField(null=True,verbose_name='邮件')
    age = models.IntegerField(verbose_name='年龄')
    myurl = models.CharField(blank=True,null=True,max_length=200,verbose_name="个人主站地址")
    password = models.CharField(max_length=30,verbose_name='密码')
    isauther = models.BooleanField(verbose_name="是否是作者",default=False)


    def __str__(self):
        return self.username
    class Meta:
        db_table='user'
        verbose_name='用户'
        verbose_name_plural = verbose_name
        ordering = ['-age']

    def __repr__(self):
        return "<Author:%r>" % self.username


class Category(models.Model):
    """
    博客分类
    """
    name = models.CharField('名称', max_length=30)

    class Meta:
        verbose_name = "类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('名称', max_length=16)

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField('标题', max_length=32)
    author = models.CharField('作者', max_length=16)
    content = models.TextField('内容')
    pub = models.DateField('发布时间', auto_now_add=True)
    category = models.ForeignKey(
        Category, verbose_name='类别', on_delete='CASCADE')  # 多对一（博客--类别）
    tag = models.ManyToManyField(Tag, verbose_name='标签')  # (多对多）

    class Meta:
        verbose_name = "博客"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, verbose_name='博客',
                             on_delete='CASCADE')  # (博客--评论:一对多)
    name = models.CharField('称呼', max_length=16)
    email = models.EmailField('邮箱')
    content = models.CharField('内容', max_length=240)
    pub = models.DateField('发布时间', auto_now_add=True)

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = "评论"

    def __str__(self):
        return self.content
```
### 步骤2
利用jquery的ajax对注册界面进行了功能添加<br>
添加功能：验证唯一性数据是否重复<br>
下面展示核心函数jquery的ajax<br>
```
$(function(){
    // 记录用户名等是否已被注册过的状态值
    window.registerStatus = 1;


// 为username控件绑定blur事件
$("input[name='username']").blur(function(){
    if($(this).val().trim().length == 0)
        return;
    $.get(
        '/check_input/',
        {'username':$(this).val()},
        function(data){
            $('#username-tip').html(data.msg);
            window.registerStatus=data.status;
        },'json'
    );
    });
/**2.为#formReg表单元素绑定submit事件*/
$("#formReg").submit(function () {
    //判断registStatus的值，决定表单是否要被提交
    // console.log('registStatus:' + registStatus);
    if (window.registStatus == 1)
        return false;
    return true;
    });
});
```

