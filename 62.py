class ExampleClass:
    class_param = "Class Parameter"
    
    def __init__(self, instance_param):
        self.instance_param = instance_param

# Example usage
instance1 = ExampleClass("Instance Parameter 1")
instance2 = ExampleClass("Instance Parameter 2")

print(instance1.class_param)         # Output: Class Parameter
print(instance1.instance_param)      # Output: Instance Parameter 1

print(instance2.class_param)         # Output: Class Parameter
