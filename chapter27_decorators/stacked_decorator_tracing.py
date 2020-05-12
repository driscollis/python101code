def bold(func):
    print(f'You are wrapping {func.__name__} in bold')
    def bold_wrapper():
        return "<b>" + func() + "</b>"
    return bold_wrapper

def italic(func):
    print(f'You are wrapping {func.__name__} in italic')
    def italic_wrapper():
        return "<i>" + func() + "</i>"
    return italic_wrapper

@bold
@italic
def formatted_text():
    return 'Python rocks!'

print(formatted_text())