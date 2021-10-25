from django import template
 
register = template.Library() # если мы не зарегестрируем наши фильтры, то django никогда не узнает где именно их искать и фильтры потеряются :(

@register.filter(name='multiply')  
def multiply(value, arg):
    if isinstance(value, str) and isinstance(arg, int): # проверяем, что value — это точно строка, а arg — точно число, чтобы не возникло курьёзов
        return str(value) * arg
    else:
        raise ValueError(f'Нельзя умножить {type(value)} на {type(arg)}') # в случае, если кто-то неправильно воспользовался нашим тегом, выводим ошибку

@register.filter(name='censor') # регистрируем наш фильтр под именем, чтоб django понимал, что это именно фильтр, а не простая функция
def censor(value, arg): # первый аргумент здесь — это то значение, к которому надо применить фильтр, второй аргумент — это аргумент фильтра, т.е. примерно следующее будет в шаблоне value|multiply:arg
    s = value.lower().replace(arg, 'XXX')
    return s

@register.filter(name='update_page')
def update_page(full_path:str, page:int):
    try:
        params_list = full_path.split('?')[1].split('&')
        params = dict([tuple(str(param).split('=')) for param  in params_list])
        params.update({'page' : page})
        link = ''
        for key, value in params.items():
            link += (f"{key}={value}&")
        return link[:-1]
    except:
        return f"page={page}"       
