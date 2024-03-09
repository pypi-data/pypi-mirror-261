import os
from rich.console import Console
import subprocess
from rich.progress import track
import time
import re
import sys
import traceback
from dingtalkchatbot.chatbot import DingtalkChatbot
import psutil
import copy
import argparse
from loguru import logger
from datetime import timedelta
import argparse
import json
import importlib
import inspect


console = Console()


def set_env_variables(env_variables: dict):
    for key, value in env_variables.items():
        os.environ[key] = value
        logger.info(f"设置环境变量 {key} = {value}")




def print_error_info(e: Exception):
    """打印错误信息

    Args:
        e (_type_): 异常事件
    """
    print("str(Exception):\t", str(Exception))
    print("str(e):\t\t", str(e))
    print("repr(e):\t", repr(e))
    # Get information about the exception that is currently being handled
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print("e.message:\t", exc_value)
    print(
        "Note, object e and exc of Class %s is %s the same."
        % (type(exc_value), ("not", "")[exc_value is e])
    )
    print("traceback.print_exc(): ", traceback.print_exc())
    print("traceback.format_exc():\n%s" % traceback.format_exc())



def load_module(module_path, class_name=None, method_name=None):
    """
    动态加载模块中的类或方法。

    :param module_path: 模块的完整路径，如 'mypackage.mymodule'。
    :param class_name: 可选，要加载的类的名称。
    :param method_name: 可选，要加载的方法的名称。
    :return: 返回类实例或方法，取决于class_name和method_name的设置。
    """
    try:
        # 导入模块
        module = importlib.import_module(module_path)
        
        if class_name:
            # 加载类并创建实例
            if inspect.isclass(getattr(module, class_name, None)):
                class_instance = getattr(module, class_name)()
                return class_instance
            else:
                raise AttributeError(f"{class_name} is not a class in {module_path}")
        elif method_name:
            # 加载方法
            if hasattr(module, method_name):
                method = getattr(module, method_name)
                return method
            else:
                raise AttributeError(f"{method_name} is not a method or does not exist in {module_path}")
        else:
            raise ValueError("Either class_name or method_name must be provided.")
    except ModuleNotFoundError:
        raise ImportError(f"Module {module_path} not found.")
    except Exception as e:
        raise e




def delete_between_delimiters(text, delimiter1, delimiter2):
    """删除text中位于delimiter1和delimiter2之间的字符

    Args:
        text (str): 文本
        delimiter1 (str): 前分隔符
        delimiter2 (str): 后分隔符

    Returns:
        result: 处理后的文本
    """
    pattern = re.escape(delimiter1) + ".*?" + re.escape(delimiter2)
    result = re.sub(pattern, '', text)
    return result


def echo(msg, color="green"):
    console.print(msg, style=color)
    
    
def run_cmd_inactivate(cmd_list):
    if isinstance(cmd_list, str):
        cmd = cmd_list
        print("\n" + cmd)
        while True:
            exitcode = os.system(cmd)
            if exitcode != 0:
                echo("执行 {} 失败！".format(cmd), "#FF6AB3")
                echo("可通过在下方修改命令继续执行，或者直接按下回车键结束操作：")
                cmd = input()
                if cmd == "":   
                    return exitcode
            else:
                return exitcode
            
    outputs = []
    for cmd in track(cmd_list, description="命令执行中", transient=True):
        print("\n" + cmd)
        while True:
            exitcode = os.system(cmd)
            if exitcode != 0:
                echo("执行 {} 失败！".format(cmd), "#FF6AB3")
                echo("可通过在下方修改命令继续执行，或者直接按下回车键结束操作：")
                cmd = input()
                if cmd == "":
                    break
            else:
                break

    return outputs   


def run_cmd(cmd_list, show_cmd=True):
    if isinstance(cmd_list, str):
        cmd = cmd_list
        if show_cmd:
            print("\n" + cmd)
        while True:
            exitcode, output = subprocess.getstatusoutput(cmd)
            if exitcode != 0:
                echo("执行 {} 失败！".format(cmd), "#FF6AB3")
                echo("错误信息：\n{}".format(output))
                echo("可通过在下方修改命令继续执行，或者直接按下回车键结束操作：")
                cmd = input()
                if cmd == "":
                    return output
            else:
                return output
            
    outputs = []
    for cmd in track(cmd_list, description="命令执行中", transient=True):
        if show_cmd:
            print("\n" + cmd)
        while True:
            exitcode, output = subprocess.getstatusoutput(cmd)
            if exitcode != 0:
                echo("执行 {} 失败！".format(cmd), "#FF6AB3")
                echo("错误信息：\n{}".format(output))
                echo("可通过在下方修改命令继续执行，或者直接按下回车键结束操作：")
                cmd = input()
                if cmd == "":
                    outputs.append(output)
                    break
            else:
                outputs.append(output)
                break

    return outputs 



def hi():
    """Prints a banner.
    """
    # Banner
    print("")
    print("")
    print("")
    print("")
    print("")
    print("         __                         __  ___      __                ____")
    print("        / /   ____ _____  __  __   /  |/  /___ _/ /_____  _____   / __ )__  _________  __")
    print("       / /   / __ `/_  / / / / /  / /|_/ / __ `/ //_/ _ \\/ ___/  / __  / / / / ___/ / / /")
    print("      / /___/ /_/ / / /_/ /_/ /  / /  / / /_/ / ,< /  __(__  )  / /_/ / /_/ (__  ) /_/ /")
    print("     /_____/\\__,_/ /___/\\__, /  /_/  /_/\\__,_/_/|_|\\___/____/  /_____/\\__,_/____/\\__, /")
    print("                       /____/                                                   /____/")
    print("")
    print("")
    print("")
    print("")




def notice(msg: str = "", warning=False, access_token="", secret=""):
    """钉钉消息通知
    
    """
    access_token = os.environ.get('DINGDING_ACCESS_TOKEN', "") if access_token == "" else access_token
    secret = os.environ.get('DINGDING_SECRET', "") if secret == "" else secret
    if access_token == "" or secret == "":
        logger.warning("未设置钉钉Token，无法发送消息: " + msg)
        logger.warning("请在环境变量中设置 DINGDING_ACCESS_TOKEN 和 DINGDING_SECRET !")
        logger.warning("例如：export DINGDING_ACCESS_TOKEN=your_access_token")
        logger.warning("或者在调用函数时传入 access_token 和 secret 参数！")
        return
    
    pid = os.getpid()
    proctitle = psutil.Process(pid).name()
    if warning:
        msg = f"⚠️\n{msg}\n\n👾进程ID: {pid}\n👾进程名: {proctitle}"
    else:
        msg = f"🪼\n{msg}\n\n👾进程ID: {pid}\n👾进程名: {proctitle}"
    
    # WebHook地址
    webhook = f'https://oapi.dingtalk.com/robot/send?access_token={access_token}'
    xiaoding = DingtalkChatbot(webhook, secret=secret, pc_slide=True)
    # Text消息@所有人
    xiaoding.send_text(msg=msg)
    logger.info(f"已将下面通知发送到钉钉！")
    logger.info(msg)
    

class Result(dict):
    """返回结果基类

    Args:
        dict (_type_): 初始化字典
    """
    def __getattr__(self, name):
        try:
            # 尝试返回字典中对应的值
            return self[name]
        except KeyError:
            # 如果键不存在，抛出AttributeError
            raise AttributeError(f"No attribute '{name}'")

    def __init__(self, *args, **kwargs):
        super(Result, self).__init__()
        for arg in args:
            for key, value in arg.items():
                self[key] = value
        self.add(**kwargs)

    # 序列化时调用
    def __getstate__(self):
        return None

    def add(self, **kwargs):
        for k, v in kwargs.items():
            self[k] = v

    def delete(self, keys):
        for k in keys:
            self.pop(k)

    def merge(self, merge_dict):
        if not isinstance(merge_dict, Result) and not isinstance(merge_dict, dict):
            raise TypeError("不支持的合并类型")
        for k, v in merge_dict.items():
            if k in ["msg", "status"] or k in self:
                continue
            self[k] = v

    def merge_or_update(self, merge_dict):
        if not isinstance(merge_dict, Result) and not isinstance(merge_dict, dict):
            raise TypeError("不支持的合并类型")
        for k, v in merge_dict.items():
            if k in ["msg", "status"]:
                continue
            self[k] = v

    @staticmethod
    def create_error_msg_result(msg="Error Result", **kwargs):
        result = Result()
        result["msg"] = msg
        result["status"] = False
        result.add(**kwargs)
        return result

    def get(self, name, other=None):
        if name is None:
            return list(self.values())
        elif isinstance(name, str):
            return self[name] if name in self else other
        elif isinstance(name, list):
            values = [self[n] for n in name]
            return values
        else:
            return self.create_error_msg_result(msg=f"Key值类型{type(name)}不支持")

    def print(self, name=None):
        print("  =====" + self["msg"] + "=====")
        values = self.get(name)
        if name is None:
            name = list(self.keys())
        for i, k in enumerate(name):
            v = values[i]
            print(f"  {k}:    {v}")
        print("  =====" + self["msg"] + "=====")

    def flatten_to_print(self):
        value_str = ""
        keys = self.keys()
        for i, k in enumerate(keys):
            v = self[k]
            value_str = value_str + k + " : " + str(v) + "\n"
        return value_str

    def aprintend_values(self, next_dict):
        if not isinstance(next_dict, Result) and not isinstance(next_dict, dict):
            raise TypeError("不支持的合并类型")
        for key in next_dict.keys():
            if key not in self.keys():
                self[key] = []

            self[key].aprintend(next_dict[key]) if isinstance(self[key], list) else [
                self[key]
            ].aprintend(next_dict[key])

    def str(self, key_name, default_value=""):
        return self.get(key_name, default_value)

    def bool(self, key_name, default_value=False):
        return self.get(key_name, default_value)

    def int(self, key_name, default_value=0):
        return self.get(key_name, default_value)

    def float(self, key_name, default_value=0.0):
        return self.get(key_name, default_value)

    def list(self, key_name, default_value=[]):
        return self.get(key_name, default_value)

    def dict(self, key_name, default_value={}):
        return self.get(key_name, default_value)
    
    def get_dict(self):
        dict_item = {}
        for key, value in self.items():
            dict_item[key] = value
        return dict_item

    def set(self, key_name, value):
        self[key_name] = value

    def set_with_dict(self, dict_value):
        for key, value in dict_value.items():
            if "." in key:
                key_list = key.split(".")
                self[key_list[0]][key_list[1]] = value
            else:
                self[key] = value

    def __deepcopy__(self, memo=None, _nil=[]):
        if memo is None:
            memo = {}
        d = id(self)
        y = memo.get(d, _nil)
        if y is not _nil:
            return y

        dict = Result()
        memo[d] = id(dict)
        for key in self.keys():
            dict.__setattr__(
                copy.deepcopy(key, memo), copy.deepcopy(
                    self.__getattr__(key), memo)
            )
        return dict

    def copy(self):
        return super().copy()
    
    
    
def get_file_paths_in_directory(directory="./", ignored_files=[], only_files=[]):
    file_paths = []
    # 遍历指定目录
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 获取文件的扩展名
            _, file_extension = os.path.splitext(file)
            if len(only_files) > 0 and file_extension.lower() in only_files:
                file_path = os.path.join(root, file)
                file_paths.append(file_path)
                continue
            # 如果文件的扩展名不在排除列表中，则添加到列表中
            if len(only_files) == 0 and file_extension.lower() not in ignored_files:
                file_path = os.path.join(root, file)
                file_paths.append(file_path)

    return file_paths


def get_args_value(argument_key):
    # 创建ArgumentParser对象
    parser = argparse.ArgumentParser(description="Get a specific argument value from command line.")
    
    # 添加参数，这里假设我们想要获取的键是'--flag'
    parser.add_argument(f'-{argument_key}', help=f'The value for the {argument_key} argument.')
    
    # 解析命令行参数
    args = parser.parse_args()
    
    # 获取指定的参数值
    value = getattr(args, argument_key, None)
    
    return value





class Timer:
    def __init__(self):
        self.start_time = None

    def start(self):
        # 开始计时，记录开始时间
        self.start_time = time.time()

    def end(self):
        # 结束计时，记录结束时间
        if self.start_time is None:
            raise ValueError("计时器尚未开始，请先调用start方法。")
        self.end_time = time.time()
        # 计算时间间隔
        elapsed_seconds = self.end_time - self.start_time
        # 将秒数转换为天数、小时、分钟和秒数
        timedelta_obj = timedelta(seconds=elapsed_seconds)
        days = timedelta_obj.days
        # 初始化remainder为0，以避免在divmod返回值为0时出现问题
        remainder = timedelta_obj.seconds
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        # 返回格式化的时间间隔
        return days, hours, minutes, seconds




def parse_args(arg_file_path):
    # 创建ArgumentParser对象
    parser = argparse.ArgumentParser(description='Update command line arguments with configurations from a file.')
    
    # 解析命令行参数
    args = vars(parser.parse_args())
    
    # 读取配置文件
    try:
        with open(arg_file_path, 'r') as config_file:
            config = json.load(config_file)
    except FileNotFoundError:
        logger.warning(f"The args config file {arg_file_path} was not found.")
        return args
    except json.JSONDecodeError as e:
        logger.warning(f"Error decoding JSON: {e}")
        return args
    
    # 更新命令行参数
    for key, value in config.items():
        if hasattr(args, key):
            setattr(args, key, value)
        else:
            args[key] = value
    
    logger.info(f"Updated command line arguments with values from {arg_file_path}.")
    
    return args



