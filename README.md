# yandex-speechkit-recognizer
============================
yandex_speech_recognizer.py
===========================

Данный скрипт предназначен для тестирования технологии распознавания речи Yandex SpeechKit. Он использует облачный сервис Yandex SpeechKit Cloud.

## Требования
Для запуска скрипта необходим Python 2.7 и выше, а так же бибилиотека Requests.
Для ее установки необходимо ввести в конcоли следующую команду:
```shell
pip install requests

```
На вход скрипт принимает wav-файлы формата PCM. Файлы должны содержать надиктованный текст. Продолжительность звукового фрагмента не должна превышать 90 с., а размер файла должен быть не более 1 Мб (ограничения Yandex SpeechKit Cloud).

## Использование
```shell
python yandex_speech_recognizer.py [FILES]

```

## Пример
```shell
python yandex_speech_recognizer.py file1.wav file2.wav ...

```
