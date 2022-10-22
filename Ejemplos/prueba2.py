def pipeline(*funcs):
    def helper(arg):
        argCount = len(funcs)
        if argCount > 0:
            # Iterate over all the arguments and call each lamba's function
            res = []
            for elem in funcs:
                if(len(res) > 0):
                    helper = elem(res.pop())
                else:
                    helper = elem(arg)
                res.append(helper)
            helper = res.pop()
        else:   
            return helper
            
        print('before returning, helper value is: ', helper)
    return helper
    
fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
print('final result: ', fun(3)) #should print 5.0
