class c:
    def __call__(self):
        return 2

functions_must_be_functions = {
    'python_type': int,
    'function': lambda: 1,
    'other_callable': c(),
}
