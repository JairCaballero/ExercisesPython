# se ejecuta siemre independientemente de lo que suceda


def error(x):

    try:
        eval(x)
    except ValueError as e:
        print(type(e))
    except (TypeError, NameError) as e:
        print(type(e))
    else:
        print("No se jecuto nunguna exepcion")
    finally:
        print("Siempre se ejecuta")


print("------------------------------")
# typeError
error("int+int")
print("------------------------------")

# NameError
error("a")
print("------------------------------")

# ValueError
error("int('a')")
print("------------------------------")

error("10+10")
print("------------------------------")
