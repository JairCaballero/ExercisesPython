def func():
    print("func")

    def fun_internal():
        print("func_interna")

    fun_internal()


func()
