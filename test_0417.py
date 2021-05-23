# import requests
# class Response():
#     pass
#
# def process(raw_response):
#     response = Response()
#     response.raw = raw_response
#     response.status_code = raw_response.status_code
#     try:
#         response.content = raw_response.json()
#     except:
#         response.content = raw_response.content
#     return response
#
# if __name__ == '__main__':
#     # headers = {""}
#     raw = requests.get("https://api.github.com/repos/jianyingfeng/789/git/refs/heads/main")
#     r = process(raw)
#     print(r.content)
#     print(r.content['object']['sha'])


def fun(a):
    if a == 1:
        # return "sss"
        pass
    print(123)

print(fun(1))