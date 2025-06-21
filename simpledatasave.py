
def datasave(file_name, file_value, file_directory = None):
    if file_directory == None:
        f = open(f"./{file_name}", "w", encoding="utf-8")
        f.write(str(file_value))
    else:
        f = open(f"{file_directory}/{file_name}.txt", "w", encoding="utf-8")
        f.write(str(file_value))
        
def dataview(file_name):
    f = open(f"{file_name}", "r", encodeing="utf-8")
    content = f.read()
    return content

def intdataview(file_name):
    f = open(f"{file_name}", "r", encodeing="utf-8")
    content = f.read()
    return int(content)