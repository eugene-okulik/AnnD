# Дан такой список:
#  person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
# С помощью распаковки создайте из этого списка
# переменные, содержащие соответствующие данные:
# name, last_name, city, phone, country

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person

print(f'name: {name}, last_name: {last_name}, city: {city}, '
      f'phone: {phone}, country: {country}')
