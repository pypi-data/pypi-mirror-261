import os
import qianfan

# 使用安全认证AK/SK鉴权，通过环境变量方式初始化；替换下列示例中参数，安全认证Access Key替换your_iam_ak，Secret Key替换your_iam_sk
os.environ["QIANFAN_ACCESS_KEY"] = "305d10a117cc44e98098c8b111132bbc"
os.environ["QIANFAN_SECRET_KEY"] = "b8d8a03ed9044f11af72280970409db0"

def main():
    chat_comp = qianfan.ChatCompletion()
    msgs = qianfan.Messages()
    flag = 0
    while flag != True:
        txt = input(":")
        if txt != "exit":
            msgs.append(txt)         # 增加用户输入
            resp = chat_comp.do(model="ERNIE-Bot-4",messages=msgs)
            msgs.append(resp)            # 追加模型输出
            print(resp.body['result'])                  # 模型的输出
        else:
            flag = True
