from datetime import date
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost, EditPost
from urllib.parse import urlparse
import frontmatter
import time
import os
from hashlib import md5, sha1
import json
import markdown2
import re

config_file_txt = ""

if((os.path.exists(os.path.join(os.getcwd(), "diy_config.txt")) == True)):
    config_file_txt = os.path.join(os.getcwd(), "diy_config.txt")
else:
    config_file_txt = os.path.join(os.getcwd(), "config.txt")

config_info = {}


with open (config_file_txt, 'rb') as f:
    config_info = json.loads(f.read())


username = config_info["USERNAME"]
password = config_info["PASSWORD"]
xmlrpc_php = config_info["XMLRPC_PHP"]

try:
    if(os.environ["USERNAME"]):
        username = os.environ["USERNAME"]

    if(os.environ["PASSWORD"]):
        password = os.environ["PASSWORD"]

    if(os.environ["XMLRPC_PHP"]):
        xmlrpc_php = os.environ["XMLRPC_PHP"]
except:
    print("无法获取 github 的 secrets 配置信息，开始使用本地变量")


url_info = urlparse(xmlrpc_php)

domain_name = url_info.netloc

wp = Client(xmlrpc_php, username, password)

# 获取已发布文章 id 列表
def get_posts():
    print(time.strftime('%Y-%m-%d-%H-%M-%S')+"开始从服务器获取文章列表...")
    posts = wp.call(GetPosts({'post_type': 'post', 'number': 1000000000}))
    post_link_id_list = []
    for post in posts:
        post_link_id_list.append({
            "id": post.id,
            "link": post.link
        })
    print(post_link_id_list)
    print(len(post_link_id_list))
    return post_link_id_list

# 创建 post 对象
def create_post_obj(title, content, link, post_status, terms_names_post_tag, terms_names_category):
    post_obj = WordPressPost()
    post_obj.title = title
    post_obj.content = content
    post_obj.link = link
    post_obj.post_status = post_status
    post_obj.comment_status = "open"
    print(post_obj.link)
    post_obj.terms_names = {
        #文章所属标签，没有则自动创建
        'post_tag': terms_names_post_tag,
         #文章所属分类，没有则自动创建
        'category': terms_names_category
    }

    return post_obj



# 新建文章
def new_post(title, content, link, post_status, terms_names_post_tag, terms_names_category):

    post_obj = create_post_obj(
        title = link, 
        content = content, 
        link = link, 
        post_status = post_status, 
        terms_names_post_tag = terms_names_post_tag, 
        terms_names_category = terms_names_category)
    # 先获取 id
    id = wp.call(NewPost(post_obj))
    # 再通过 EditPost 更新信息
    edit_post(id, title, 
        content, 
        link, 
        post_status, 
        terms_names_post_tag, 
        terms_names_category)


# 更新文章
def edit_post(id, title, content, link, post_status, terms_names_post_tag, terms_names_category):
    post_obj = create_post_obj(
        title, 
        content, 
        link, 
        post_status, 
        terms_names_post_tag, 
        terms_names_category)
    res = wp.call(EditPost(id, post_obj))
    print(res)

# 获取 markdown 文件中的内容
def read_md(file_path):
    content = ""
    metadata = {}
    with open(file_path) as f:
        post = frontmatter.load(f)
        content = post.content
        metadata = post.metadata
        print("==>>", post.content)
        print("===>>", post.metadata)
    return (content, metadata)

# 获取特定目录的 markdown 文件列表
def get_md_list(dir_path):
    md_list = []
    dirs = os.listdir(dir_path)
    for i in dirs:
        if os.path.splitext(i)[1] == ".md":   
            md_list.append(os.path.join(dir_path, i))
    print(md_list)
    return md_list

# 计算 sha1
def get_sha1(filename):
    sha1_obj = sha1()
    with open(filename, 'rb') as f:
        sha1_obj.update(f.read())
    result = sha1_obj.hexdigest()
    print(result)
    return result

# 将字典写入文件
def write_dic_info_to_file(dic_info, file):
    dic_info_str = json.dumps(dic_info)   
    file = open(file, 'w')  
    file.write(dic_info_str)  
    file.close()
    return True

# 将文件读取为字典格式
def read_dic_from_file(file):
    file_byte = open(file, 'r') 
    file_info = file_byte.read()
    dic = json.loads(file_info)   
    file_byte.close()
    return dic 

# 获取 md_sha1_dic

def get_md_sha1_dic(file):
    result = {}
    if(os.path.exists(file) == True):
        result = read_dic_from_file(file)
    else:
        write_dic_info_to_file({}, file)
    return result

# 重建 md_sha1_dic，将结果写入.md_sha1
def rebuild_md_sha1_dic(file, md_dir):
    md_sha1_dic = {}

    md_list = get_md_list(md_dir)

    for md in md_list:
        key = os.path.basename(md)
        value = get_sha1(md)
        md_sha1_dic[key] = value

    md_sha1_dic["update_time"] =  time.strftime('%Y-%m-%d-%H-%M-%S')
    write_dic_info_to_file(md_sha1_dic, file)

def post_link_id_list_2_link_id_dic(post_link_id_list):
    link_id_dic = {}
    for post in post_link_id_list:
        link_id_dic[post["link"]] = post["id"]
    return link_id_dic


def href_info(link):
    return "<br/><br/><br/>\n\n\n\n本文永久更新地址：\n[" + link + "](" + link + ")"

# 在 README.md 中插入信息文章索引信息，更容易获取 google 的收录
def insert_index_info_in_readme():
    # 获取_posts 下所有 markdown 文件
    md_list = get_md_list(os.path.join(os.getcwd(), "_posts"))
    # 生成插入列表
    insert_info = ""
    md_list.sort(reverse=True)
    # 读取 md_list 中的文件标题
    for md in md_list:
        (content, metadata) = read_md(md)
        title = metadata.get("title", "")
        insert_info = insert_info + "[" + title +"](" + "https://"+domain_name + "/p/" + os.path.basename(md).split(".")[0] +"/" + ")\n\n"
    # 替换 ---start--- 到 ---end--- 之间的内容，调整目录标题格式

    insert_info = "---start---\n\n_" + time.strftime('%Y.%m.%d') + " 更新_" +"\n\n" + "## 📜 文章目录\n\n" + insert_info + "---end---"

    # 获取 README.md 内容
    with open (os.path.join(os.getcwd(), "README.md"), 'r', encoding='utf-8') as f:
        readme_md_content = f.read()

    print(insert_info)

    new_readme_md_content = re.sub(r'---start---(.|\n)*---end---', insert_info, readme_md_content)

    with open (os.path.join(os.getcwd(), "README.md"), 'w', encoding='utf-8') as f:
        f.write(new_readme_md_content)

    print("==new_readme_md_content==>>", new_readme_md_content)

    return True

def main():
    # 1. 获取网站数据库中已有的文章列表
    post_link_id_list = get_posts()
    print(post_link_id_list)
    link_id_dic = post_link_id_list_2_link_id_dic(post_link_id_list)
    print(link_id_dic)
    # 2. 获取 md_sha1_dic
    # 查看目录下是否存在 md_sha1.txt，如果存在则读取内容；
    # 如果不存在则创建 md_sha1.txt，内容初始化为{}，并读取其中的内容；
    # 将读取的字典内容变量名，设置为 md_sha1_dic
    md_sha1_dic = get_md_sha1_dic(os.path.join(os.getcwd(), ".md_sha1"))

    # 3. 开始同步
    # 读取_posts 目录中的 md 文件列表
    md_list = get_md_list(os.path.join(os.getcwd(), "_posts"))

    for md in md_list:
        # 计算 md 文件的 sha1 值，并与 md_sha1_dic 做对比
        sha1_key =  os.path.basename(md)
        sha1_value = get_sha1(md)
        # 如果 sha1 与 md_sha1_dic 中记录的相同，则打印：XX 文件无需同步;
        if((sha1_key in md_sha1_dic.keys()) and (sha1_value == md_sha1_dic[sha1_key])):
            print(md+"无需同步")
        # 如果 sha1 与 md_sha1_dic 中记录的不同，则开始同步
        else:
            # 读取 md 文件信息
            (content, metadata) = read_md(md)
            # 获取 title
            title = metadata.get("title", "")
            terms_names_post_tag = metadata.get("tags",  domain_name)
            terms_names_category = metadata.get("categories", domain_name)
            post_status = "publish"
            link = sha1_key.split(".")[0]
            # 修改 3: 文章头部添加编辑时间
            # 从 markdown 改为 markdown2，并去除 markdown 的 extensions
            content = "<pre>更新于 "+ time.strftime('%Y-%m-%d %H:%M:%S')+" UTC</pre>\n"+ markdown2.markdown(content) + href_info("https://"+domain_name+"/p/"+link+"/")
            #content = markdown.markdown("<pre>更新于 "+ time.strftime('%Y-%m-%d %H:%M:%S')+" UTC</pre>\n"+ content + href_info("https://"+domain_name+"/p/"+link+"/"), extensions=['tables', 'fenced_code'])
            # 如果文章无 id，则直接新建
            # 修改 1:去掉链接尾部的/符号，原本为 if(("https://"+domain_name+"/p/"+link+"/" in link_id_dic.keys()) == False):
            if(("https://"+domain_name+"/p/"+link in link_id_dic.keys()) == False):
                new_post(title, content, link, post_status, terms_names_post_tag, terms_names_category)
                # print("新建文章：https://"+domain_name+"/p/"+link+"/")
            # 如果文章有 id, 则更新文章
            else:
                # 获取 id
                # 修改 2:去掉链接尾部的/符号，原本为 id = link_id_dic["https://"+domain_name+"/p/"+link+"/"]
                id = link_id_dic["https://"+domain_name+"/p/"+link]
                edit_post(id, title, content, link, post_status, terms_names_post_tag, terms_names_category)
                # print("更新文章：https://"+domain_name+"/p/"+link+"/")
            # print(link_id_dic.keys())
    # 4. 重建 md_sha1_dic
    rebuild_md_sha1_dic(os.path.join(os.getcwd(), ".md_sha1"), os.path.join(os.getcwd(), "_posts"))
    # 5. 将链接信息写入 insert_index_info_in_readme
    insert_index_info_in_readme()

main()
