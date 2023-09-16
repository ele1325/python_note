global_var = 10
print(global_var)
print(id(global_var))
def modify_global():
    global global_var    
    global_var = 20
    print(global_var)
    print(id(global_var))

if __name__ == "__main__":
    modify_global()
    print(global_var)
    print(id(global_var))


 