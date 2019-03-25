import configparser
from kindle_maker.ebook_maker import make_ebook
import pdfkit
from process_data import ProcessData, create_dir

# 获取配置文件
cf = configparser.ConfigParser()
cf.read('conf.ini')
account_id = cf.get("juejin", "id")
client_id = cf.get("juejin", "client_id")
uid = cf.get("juejin", "uid")
src = cf.get("juejin", "src")
token = cf.get("juejin", "token")
get_url = cf.get("juejin", "getUrl")
section_url = cf.get("juejin", "getSectionUrl")
book_name = cf.get("juejin", "bookName")

create_dir()
process = ProcessData(account_id=account_id, uid=uid, client_id=client_id, token=token,
                      book_name=book_name, get_url=get_url, section_url=section_url, src=src,
                      dir_path="source")

section_ids = process.get_section_id()

process.get_content_from_section(section_ids)
# 制作mobi使用
# create_dir("dist")

# 本来打算用这个库制作mobi https://github.com/jachinlin/kindle_maker,但是目前这个库报错
# make_ebook("source", "dist")

# 使用pdfkit制作电子书
pdfkit.from_file(book_name.strip('"')+'.html', book_name.strip('"')+'.pdf')