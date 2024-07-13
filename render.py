import json
import os
from jinja2 import Environment, FileSystemLoader


class Jinja2Demo:
    # 读取json文件，并返回一个字典
    # 可以接收1个参数（文件路径）或者两个参数（路径，文件名）
    @staticmethod
    def read_json(*args, **kwargs):
        file_name = args[0] if len(args) == 1 else os.path.join(args[0], args[1])
        with open(file_name, "r", encoding="utf-8") as file:
            file_content = file.read()
            if file_content == "":
                return None

        # 解析JSON数据
        parsed_data = json.loads(file_content)
        return parsed_data  # 返回解析后的数据

    """render_template ：渲染模板
    @prop:
        *fill_data:填充数据[Dict]
        *template_path:模板html文件路径
        output_path:输出文件路径
    @return:boolen 成功/失败

    注意：默认path是完整的路径
    """

    @staticmethod
    def render_template(fill_data, output_path, template_path="", *args, **kwargs):
        # 处理参数：
        output_path = (
            output_path
            if output_path
            else os.path.join(
                os.path.dirname(template_path), os.path.basename(template_path)
            )
        )
        # 加载模板文件
        env = Environment()
        try:
            # 渲染模板
            # rendered_file = env.from_string(str).render(fill_data)
            # 1. 创建一个加载器，指定模板文件所在目录
            loader = FileSystemLoader(os.path.dirname(template_path))
            # 2. 使用加载器创建一个环境
            env = Environment(loader=loader)
            # 3. 从文件加载模板
            template = env.get_template(os.path.basename(template_path))
            # 4. 渲染模板，使用数据字典填充模板变量
            rendered_file = template.render(fill_data)
            # 输出渲染后的Markdown
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(rendered_file)
            return True
        except Exception as e:
            print(e)
            # logging.error(e)
            return False


# 测试
def main():
    # 获取当前目录
    current_file_path = os.path.abspath(__file__)
    current_dir = os.path.dirname(current_file_path)
    # 读取config
    template_list = Jinja2Demo.read_json(os.path.join(current_dir, "config.json"))["template"]
    for index in template_list:
        print("正在处理",index)
        fill_data_path = os.path.join(current_dir, "json", index+'.json')
        output_path = os.path.join(current_dir, index+'.html')
        template_path = os.path.join(current_dir, "template",index+".html")
        
        # print(fill_data_path, "\n", output_path, "\n", template_path)
        
        data = Jinja2Demo.read_json(fill_data_path)
        Jinja2Demo.render_template(data, output_path, template_path)
    
    print("处理结束")


if __name__ == "__main__":
    main()
