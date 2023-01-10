# def test_method(gender,**kwargs):
#     # print(kwargs.get('isdoingright'))
#     # if kwargs.get('isdoingright'):
#     #    print(kwargs.get('isdoingright'))
#     # else:
#     #     print("Khoong cos phan tu nafy dau")
#     print(kwargs)
#
#
# test_method(gender="man",dictionary="folder1", isdoingright="hello")



class TestClass:
    def __init__(self,raw):
        if raw:
            if "proxyType" in raw and raw["proxyType"]:
                print(raw["proxyType"])

test_class = TestClass({"proxyType":'https'})