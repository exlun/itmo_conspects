# itmo_conspects

**Конспекты по разным предметам первого потока ИСy27 университета ИТМО**

Друзья, второй семестр закончился🥳🥳🥳, спасибо, что пользовались моими конспектами и находили в них ошибки🥰🥰🥰, увидимся в третьем семестре с новыми конспектами😼😼😼 (пока за лето я буду фиксить старые)


### Математический анализ II

[**Весь курс с программой экзамена**](https://pelmesh619.github.io/itmo_conspects/conspects/calculus/calculus_superconspect.pdf)


### Специальные разделы высшей математики

[**Весь курс с неполной программой экзамена**](https://pelmesh619.github.io/itmo_conspects/conspects/specsec/specsec_superconspect.pdf)

### Дискретная математика II

[**Почти весь курс с неполной программой экзамена**](https://pelmesh619.github.io/itmo_conspects/conspects/dismath/dismath_superconspect.pdf)

[**Шпаргалка по Комбинаторике**](https://pelmesh619.github.io/itmo_conspects/conspects/dismath/dismath_cheatsheet_combinatorics.pdf)

[**Шпаргалка по Рекуррентностям и Производящим функциям**](https://pelmesh619.github.io/itmo_conspects/conspects/dismath/dismath_cheatsheet_recurrences.pdf)

### Алгоритмы и Структуры Данных I-II

Почти все алгоритмы из курса и некоторые пояснения к ним есть в моем другом репозитории: [pelmesh619/algorithm_archives](https://github.com/pelmesh619/algorithm_archives)



## TODO

Буду рад, если вы поможете мне:

* Сделать картинки примеров (желательно какие-нибудь приличные и красивые, из графкалькуляторов)

* Проверить на очепятки и неточности

* Сделать конспекты первых лекций второго семестра

## PS

linter.py автоматически добавляет форматирование (добавляет \displaystyle, где надо и т.д.), создает новый файл в ./linted/ и рендерит .pdf в директорию ./conspects/ при помощи pdflatex:

```bash
python linter.py ./directory/tex_file.tex
```

В основном, я делаю пдфки так (мне было проще написать скрипт на питоне, чем загуглить, как сделать везде \displaystyle)

superconspect.py автоматически "соединяет" все .tex файлы конспектов лекций из данной директории в один файл, добавляет содержание и делает то, что делает linter.py

```bash
python superconspect.py ./directory
```

compile_all.py рендерит все .tex в данной директории (в том числе создает суперконспект) (полезно, если что-то поменял глобально и нужно все перерендерить)

```bash
python compile_all.py ./directory
```

for contact write me: [t.me/pelmeshke](https://t.me/pelmeshke)

## Extra

### Немецкий язык

[Фонетика](https://github.com/pelmesh619/itmo_conspects/blob/deutsch/conspects/deutsch/phonetics.pdf)

[**(почти) Полный конспект**](https://github.com/pelmesh619/itmo_conspects/blob/deutsch/conspects/deutsch/deutsch_superconspect.pdf)
