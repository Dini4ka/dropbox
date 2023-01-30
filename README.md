# dropbox
Выше представлен скрипт, который позволяет загружать в/скачивать из Dropbox произвольный двоичный файл (произвольного формата и размера).<br>
Инструкции указаны только для <em><b>Windows!!</b></em> Для использования необходимо иметь браузер google Chrome последней версии https://www.google.com/intl/ru_ru/chrome/ <br>
Для его сборки необходимо:<br>
1)установить Python версии 3.10.1 - https://www.python.org/downloads/release/python-3101/ <br>
2)установить все пакеты из файла requirements.txt: <br>
<em><b>pip install undetected_chromedriver==3.2.1</b></em> <br>
<em><b>pip install selenium==4.8.0</b></em> <br>
<em><b>pip install requests==2.28.2</b></em> <br>
<em><b>pip install click==8.1.3</b></em> <br>
3)перезагрузить ваш компьютер для того, чтобы Python добавился в PATH и изменения вступили в силу<br>
4)Установить утилиту auto-py-to-exe <br><b>pip install auto-py-to-exe</b><br> Скачать и распаковать архив dropbox в удобном для вас месте <br>![zip](https://user-images.githubusercontent.com/77235598/215338434-a30c4a30-e9e8-436d-8c0b-a794222836ee.PNG)<br>
5)Запустить утилиту командой в консоли <em><b>auto-py-to-exe</b></em>(выбрать так, как показано на картинке) и указать исполнящий фаил <em><b>main.py</em></b><br>![auto-py-to-exe](https://user-images.githubusercontent.com/77235598/215334841-af7b6b5f-07b9-4f4d-82e2-4a7fbb152590.PNG)<br>
6)Дождаться конца конвертации<br>
7)Открыть консоль <em><b>cmd</b></em> и запустить получившуюся программу по следующему шаблону<br>
<em><b>testtool login password put/get src_path dst_path</b></em>
<br>![console](https://user-images.githubusercontent.com/77235598/215337538-29312f7e-b086-40a2-a3bb-6d25777f1090.PNG)
