def create_class(name):
    if name=="user":
        class User:
            def __str__(self):
                return "user"
        return User
    elif name=="company":
        class Company:
            def __str__(self):
                return "company"
        return Company

#type 动态创建类

class BaseClass:
    def answer(self):
        return "I'm base class"

def say(self):
    return "I'm user"

if __name__ == "__main__":
    # 第一种方法
    MyClass = create_class("user")
    my_obj = MyClass()
    print(type(my_obj))

    # 第二种方法
    User = type("User", (BaseClass, ), {"name":"user", "say": say})
    my_obj = User()
    print(my_obj.name)
    print(my_obj.say())
    print(my_obj.answer())