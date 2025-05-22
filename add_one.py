
""" TODO LIST, feel free to add/check/remove items from here
[V]  nested classes
[ ]  more nested classes
[ ]  use decorators
[ ]  split into multiple files and packages
[ ]  add logging and checks
[ ]  try/except(/finally) blocks
[ ]  comments maybe??
"""

class IncrementNumberFunctionGenerator:
    class FunctionWrapper:
        class InnerWrapper:
            class Function:
                def __init__(self, *args, **kwargs):
                    self.args = args
                    self.kwargs = kwargs
                    self.value = 1
                
                def GenerateValue(self, what):
                    increment_by = self.value
                    result = what + increment_by
                    return result
            
            def __init__(self, *kwargs, **args):
                self.kwa = kwargs
                self.kva = args
            
            def _Execute(self, _inner_argument):
                result = sum(self.kwa[i] for i in self.kva)
                return self.Function.GenerateValue(_inner_argument)
        
        def __init__(self, *args, **kwargs):
            self.kwargs = args
            self.args = kwargs
            return
        
        def Run(self, argument):
            return_ = self.InnerWrapper._Execute(argument)
            return return_
    
    FunctionWrapper = FunctionWrapper()
    FunctionWrapper.InnerWrapper = FunctionWrapper.InnerWrapper()
    FunctionWrapper.InnerWrapper.Function = FunctionWrapper.InnerWrapper.Function()
    
    def __init__(self, *args, **kwargs):
        self.FunctionWrapperProperty = self.FunctionWrapper
    
    def Increment(self, this):
        result = self.FunctionWrapperProperty.Run(this)
        return result


# Usage
a = 1
func = IncrementNumberFunctionGenerator()
a = func.Increment(a)
print(a)
