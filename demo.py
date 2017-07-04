import api
api = api.config('...')

val, res = api('temp-deprecated').run('sayHello', {
    'name': 'hi'
})

if res.error:
    print 'oh no'
else:
    print val
