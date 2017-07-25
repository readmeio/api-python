import api
api = api.config('abdul_f9cfcade4264cba870585a')

val, res = api('temp-deprecated').run('sayHello', {
    'name': 'hi'
})

if res.error:
    print 'oh no'
else:
    print val
