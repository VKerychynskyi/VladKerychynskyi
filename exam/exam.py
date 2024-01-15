class MyClass:
    global_variable = None  
    def __init__(self, global_arg):
        
        self.global_variable = global_arg

    def print_global_variable(self):
        
        print(f"Global Variable: {self.global_variable}")



global_arg_value = "Hello, global variable!"


my_instance = MyClass(global_arg_value)


my_instance.print_global_variable()