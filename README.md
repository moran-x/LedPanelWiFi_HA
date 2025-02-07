# LedPanelWiFi_HA
Управление [LedPanelWiFi 1.14+](https://github.com/vvip-68/LedPanelWiFi) в Home Assistant
![SCREN](https://github.com/moran-x/LedPanelWiFi_HA/blob/main/images/WiFiLedPAnel_HA.png)

> Данная интеграция делалась для **Home Assistant Operating System**

# Подготовка
## Дополнения для установки
- File editor или SAMBA

## Дополнения для работы интеграции
- [Pyscript: Python Scripting for Home Assistant](https://github.com/custom-components/pyscript?tab=readme-ov-file)
- [MQTT](https://www.home-assistant.io/integrations/mqtt/)
- [Компонент Yandex Smart Home для Home Assistant](https://docs.yaha-cloud.ru/v1.0.x/)

## Дополнения для удобства
- Studio Code Server (если хотите вносить много правок в код)

# Установка

- скачиваем архив с репозитория.
- любым доступным способом (**SAMBA**, **File editor**) размещаем папки **mqtt** и **pyscript** на сервере HA, желательно не изменяя структуру файлов и папок

# Настройка

- добавляем интеграцию **MQTT** и **Pyscript Python scripting** в HA
- создаем нового пользователя для взаимодействия с MQTT, либо можете использовать свой логин и пароль
- в файле скрипта **ledwindow.py** указываем ip адрес вашей ленты, здесь же можно указать список адресов, если у вас много лент
- если хотите можете поменять название ленты, но тогда придется править конфигурационные файлы, опять же если несколько лент добавляем свои названия.
- если меняли название ленты, то в файлах **led_light.yaml, led_sensors.yaml, led_switch.yaml** меняем все вхождения **LedWiFiWindow** на свое название,
- если несколько лент, то в файлах **led_light.yaml, led_sensors.yaml, led_switch.yaml** дублируем все содержимое файлов, так же заменив название.
- в основной конфигурационный файл HA добавляем строки из файла **conf.yaml**
- в файл **automations.yaml** добавляем строки из файла **auto.yaml**, заменив везде IP адрес на свой, и при необходимости изменяем название ленты на свое.
- если лент несколько, дублируем содержимое файла **auto.yaml**, кроме первой автоматизации, заменив IP, ID и название лент
- перезагружаем HA для применения всех изменений.
