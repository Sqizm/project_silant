# Final Project

Финальный проект: Реальный опыт | Дипломный проект: реальный кейс от компании "Силант"

## Как запустить проект

1. Для запуска приложения, первым запускается сервер DRF:\
В первом терминале IDE, переходим в директорию `cd project_silant/backend_silant`, устанавливаем зависимости проекта командой `pip install -r requirements.txt`, после запускаем сервер командой `python manage.py runserver`
2. Вторым действием запускаем фронт на React:\
Во втором терминале IDE, переходим в директорию `cd project_silant/frontend_silant`, устанавливаем необходимые библиотеки командой `npm install`, после запускаем клиент командой `npm start`
3. URL адреса fullstack-project:\
Главная страница: <a href='http://localhost:3000/'>Главная</a>\
Главная страница: <a href='http://localhost:3000/auth'>Авторизация</a>
4. Функционал сервиса:\
Сортировка данных в Таблицах по умолчанию проводиться по полям:\
«дата отгрузки с завода» для таблицы «машина»;\
«дата проведения ТО» для таблицы «ТО»;\
«дата отказа« для таблицы «рекламации».\
Можно убедится в этом, открыв файл `models.py`, такие модели как `Car; Maintenance; Complaints` в `class Meta` имеют поле `ordering`
5. В таблицах предусмотрена функция фильтрации по следующим полям:\
модель техники;\
модель двигателя;\
модель трансмиссии;\
модель управляемого моста;\
модель ведущего моста для таблицы «Машина»;\
вид ТО;\
зав.номер машины;\
сервисная компания для таблицы «ТО»;\
узел отказа;\
способ восстановления;\
сервисная компания для таблицы «Рекламация».\
Фильтрация имеет тип `text`, то есть нужно вводить, то что хочешь отфильтровать!
6. Строки в таблицах кликабельны и ведут на страницу с отображением полных данных.
7. Авторизация проводиться по логину/паролю, которые назначаются администратором системы. Пользователь не может самостоятельно поменять логин и/или пароль.
8. На сайте запрещена регистрация! Администратор может создавать пользователя в админ панели.
9. Пользователь без авторизации может получить ограниченную информацию о комплектации машины, введя её заводской номер.Данному типу пользователя доступно поле для ввода заводского номера машины и кнопка поиск.
10. Результат поиска: таблица с данными по определённой машине со следующими полями: таблица «Машина» (поля 1–10). Если данные по заводскому номеру не найдены, то выдается сообщение, что данных о машине с таким заводским номером нет в системе.
11. Авторизованные пользователи имеют разный доступ к данным, получают таблицы с данными обо всех доступных им машинах.
## Зарегистрированные пользователи:
### Администратор/Менеджер:
Логин: admin\
Пароль: admin
### Сервисные компании:
`ООО Промышленная техника:`\
Логин: user8\
Пароль: pas12345678\
`ООО Силант:`\
Логин: user9\
Пароль: pas12345678\
`ООО ФНС:`\
Логин: user10\
Пароль: pas12345678
### Клиента/Покупатели:
`ИП Трудников С.В`\
Логин: user1\
Пароль: pas12345678\
`ООО "ФПК21"`\
Логин: user2\
Пароль: pas12345678\
`ООО "МНС77"`\
Логин: user3\
Пароль: pas12345678\
`ООО "Раинский ЛПХ"`\
Логин: user4\
Пароль: pas12345678\
`ООО "Комплект-Поставка"`\
Логин: user5\
Пароль: pas12345678\
`ООО "РМК"`\
Логин: user6\
Пароль: pas12345678\
`АО "Зандер"`\
Логин: user7\
Пароль: pas12345678\
