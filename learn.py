import pandas as pd #Pandas для работы с csv
from sklearn.feature_extraction.text import CountVectorizer #Шифрование в вектора
from sklearn.model_selection import train_test_split #Тренировка на двух выборказ
from sklearn.naive_bayes import BernoulliNB #Модель обучения
from sklearn.metrics import accuracy_score #Оценивание точности

df=pd.read_csv('train.csv', encoding='utf-8', delimiter=";") #Чтение большой базы данных для машинного обучение
test=pd.read_csv('test.csv', encoding='utf-8', delimiter=";") #Чтение произвольного файла для работы по модели обучения
result = pd.DataFrame(test.text) #Создаем фрейм, чтобы вставить результаты работы программы

vectorizer = CountVectorizer(binary=True) #Создаем бинарный вектор
x=vectorizer.fit_transform(df['text']) #Шифруем наш текст с большой базы данных и составляем словарь
y=pd.get_dummies(df['number'])['spam'] #Шифрование надпими spam
our=vectorizer.transform(test['text']) #Шифруем текст с произвольного файла, не составляем словарь

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.33, random_state=42) #Разделяем выборку на тестовую и тенировочную
clf=BernoulliNB() #Создаем модель обучения
clf.fit(x_train, y_train) #Заполняем нашу модель тренировочными данными
y_pred=clf.predict(x_train) #Тренируем
print ('Train accuracy: {:.2f}%'.format(100*accuracy_score(y_train,y_pred))) #Смотрим точность
y_pred=clf.predict(x_test) #Заполняем нашу модель тестовыми данными
print ('Test accuracy: {:.2f}%'.format(100*accuracy_score(y_test,y_pred))) #Смотрим точность

pred = clf.predict(our) #Запускаем нашу модель на нашем произвольном файле
result.insert (0, 'category', pred) #Вставляем результат в колонку категорий
result.to_csv('test.csv',encoding='utf-8', sep=';', index=False) #экспортируем в базу данных

res=pd.read_csv(r'test.csv', encoding='utf-8', delimiter=';') #читаем получишийся файл
for i in range (len(res.index)):
    if (res['category'][i]==0):
        res['category'][i] = 'hash' #меняем нули на hash
    else:
        res['category'][i] = 'spam' #меняем 1 на spam
res.to_csv('test.csv',encoding='utf-8', sep=';', index=False) #снова экспортируем в этот же файл

