# selfblog_django
# 使用django搭建个人博客
## 项目区块
### 区块1
models区块，目标：搭建所需的数据库模型<br>
如下所示<br>
        1.建立user表实体类
        包含用户名称（username）varchar
        邮箱（email）varchar
        年级（age）int
        个人主站地址（myurl）varchar（可以为空）
        密码（password）varchar
        是否是作者（tinyint）默认为False
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
### 区块2
搭建blog_main博客主界面，将其定义为baseview，后续跳转页面以baseview为基础，利用block函数进行编写。
