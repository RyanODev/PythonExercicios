a = int(input('digite um número: '))
km = (a / 10) / 10 / 10
hm = (a / 10) / 10
dam = a / 10
dm = a * 10
cm = a * 10 * 10
mm = a * 10 * 10 * 10

print('{} metros vale:'.format(a))
print('{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm'.format(km, hm, dam, dm, cm, mm))
