import requests
import os
import time


def create_dir(path="source"):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)


header = {'user-agent':
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}


class ProcessData:
    def __init__(self, account_id, client_id, uid, token, src, get_url, section_url,book_name,dir_path):
        self.account_id = account_id
        self.client_id = client_id
        self.uid = uid
        self.token = token
        self.src = src
        self.get_url = get_url
        self.section_url = section_url
        self.dir_path = dir_path
        self.book_name = book_name

    def get_section_id(self):
        pay_load = {"id": self.account_id, "uid": self.uid, "token": self.token, "client_id": self.client_id,
                    "src": self.src}
        time.sleep(1)
        req = requests.get(self.get_url, params=pay_load)

        return req.json()["d"]["section"]

    def get_content_from_section(self, section_list):
        # with open("./source/" + "toc.md", 'w') as f:
        #     f.write("# "+self.book_name.strip('"')+'\n')
        with open(self.book_name.strip('"') + ".html", 'a', encoding="utf-8") as html:
            html.writelines('<meta charset="UTF-8">')
        for section in section_list:
            time.sleep(1)
            pay_load = {"id": self.account_id, "uid": self.uid, "token": self.token, "client_id": self.client_id,
                        "src": self.src, "sectionId": section}
            req = requests.get(self.section_url, params=pay_load)
            # import pdb;pdb.set_trace()
            # with open("./source/"+"toc.md", 'a') as f:
            #     f.write("## "+req.json()["d"]["title"]+'\n')
            with open(self.book_name.strip('"')+".html", 'a', encoding="utf-8") as htmlf:

                htmlf.writelines(req.json()["d"]["html"])



