en = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
ru = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
num = (dict(zip(en, ru)))
print(num)

def num_translated(key, num):
    for k, v in num.items():
        if k == key:
            return v

print(num_translated('ell', num))
print(num_translated('two', num))
print(num_translated('three', num))
print(num_translated('ten', num))
