class c:
    def __call__(self):
        return ''

functions_must_be_functions = {
    'type': str,
    'function': lambda: '',
    'object': c(),
}
