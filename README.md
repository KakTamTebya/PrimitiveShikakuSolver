# Shikaku
Алгоритм способен быстро решать небольшие головоломки - [shikaku](https://en.wikipedia.org/wiki/Shikaku),  
причем значения в квадратах можно не только указывать явно, но и ограничивать сверху или снизу.  
Можно решать как свои shikaku, записанные в виде текстовых файлов (пример таких файлов в src/grid_examples),  
так и сгенерированные автоматически (в этом случае следует запускать main без аргументов).


### КОМПОНЕНТЫ
- puzzle_generator.py - генератор shikaku
- file_parser.py - парсинг файлов с shikaku
- main.py - исполняемый файл
- visualizer.py - визуализация решения
- solver.py - модуль для решения shikaku


### ФУНКЦИОНАЛ ИСПОЛНЯЕМОГО ФАЙЛА
- Справка: main.py [-h|--help]
- Использование: python main.py [-f FILE] [-n N]
 
### ФЛАГИ
- [-n|--number] - Указать количество решений, которое требуется показать
- [-f|--file] - Имя файла с shikaku, которое требуется решить. Пустые квадраты должны
быть отмечены символом '-', между квадратами требуется разделитель - пробел.
