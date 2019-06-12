#Python3
import easygui,datetime,os
Title=input("Title:")
Original=input("Original link:")
Author=input("Author:")
tag=input("Tag:")
Num=input("Num:")
Context=""
print("Context(text/plane-1,file-2)")
if input() == "2":
    with open(input()) as f:
        Context=f.read()
else:
    while 1:
        thisCon=input(":")
        if thisCon==":quit":
            break
        else:
            Context+=thisCon+"<br/>"

with open("index.html","r") as f:
    index=f.read()

t="""                                <!-- Add New Articles Here -->
                                <h3 class="bh-card-main-title"><a href="articles/%s.html">%s</a></h3>
                                <div class="bh-card-tag">
                                    <div><i class="fa fa-clock-o"></i>%s</div>
                                    <div><i class="fa fa-eye"></i>%s</div>
                                </div>""" %(Num,Title,datetime.datetime.now().strftime('%Y-%m-%d'),Tag)
index=index.replace("<!-- Add New Articles Here -->",t)
with open("index.html","w") as f:
    f.write(index)




t2="""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>%s</title>
    <link href="../bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <link href="../css/bh-css.css" rel="stylesheet">
    <link href="../font-awesome/css/font-awesome.min.css" rel="stylesheet">
    <link rel="stylesheet" href="../highlight/styles/railscasts.css">
</head>
<body>
<div class="container-fluid" style="padding:0;">
    <div class="bh-content">
        <!-- <div class="bh-nav-sidebar"> -->
            <!-- <ul>
                <li><a class="active" href="bonhumeur-index.html">Index</a></li>
                <li><a href="bonhumeur-detail.html">Me!</a></li>
            </ul> -->
        <!-- </div> -->
        <div class="container">
            <nav class="bh-header">
                <!-- <a class="active" href="#">首页 .</a> -->
                <a class="active" href="blog.weathon.top">首页 .</a>
                <a href="https://www.weathon.top/">主站 .</a>
                <!-- <a href="#">技术教程 .</a>
                <a href="#">官方资讯 .</a>
                <a href="#">日常 .</a> -->
                <a href="https://space.bilibili.com/44744721/">哔哩哔哩主页 .</a>
                <a href="https://sighttp.qq.com/msgrd?v=1&uin=2907154449">商务合作 .</a>
            </nav>
            <div class="bh-artical-content">
                <h2 class="bh-artical-title">%s</h2>
                <div class="bh-card-tag">
                    <div class="">
                        <img src="face.jpg" class="img-fluid rounded-circle" alt="Responsive image">
                        <span class="text-success">%s</span>
                    </div>
                </div>
                <div class="bh-artical">
                    <img src="//i0.hdslb.com/bfs/article/a6a967bb5977e5460e20bfc4b9924424281f97e3.jpg@860w_482h.webp"/>
                        <div class="article-holder">
                        %s
                        /div>
                        <a href="%s"><font color="blue">阅读原文</font></a>
                    </div>

        <div class="bh-footer">
                <p class="bh-copyright"><a href="https://sighttp.qq.com/msgrd?v=1&uin=2907154449">联系我们</a> | 本模板设计由简.工作室荣誉出品</p>
                <p class="bh-copyright">本模板来自于开源社区的简.工作室（www.jeanstudio.cn），如有侵权，请联系我们删除</p>
                <p class="bh-copyright">本博客为Weathon软件开发组的博客，与主站没有直接联系</p>
                <script type="text/javascript" src="//js.users.51.la/19689467.js"></script>
            </div>

    </div>
</div>

<script src="../jquery/jquery.min.js"></script>
<script src="../bootstrap/js/bootstrap.min.js"></script>
<script src="../highlight/highlight.pack.js"></script>
<script>hljs.initHighlightingOnLoad();</script>
</body>
</html>
""" % (Title,Title,Author,Context,Original)
with open("articles/%s.html" % Num,"w") as f:
    c=f.write(t2)
if input("Push?(Y/n)") == "Y":
    os.system("git add .")
    os.system("git commit -m 'Add article'")
    os.system("git push")