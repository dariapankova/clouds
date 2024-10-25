# Лабораторная работа 2
## Задание

1. Написать “плохой” CI/CD файл, который работает, но в нем есть не менее пяти “bad practices” по написанию CI/CD
2. Написать “хороший” CI/CD, в котором эти плохие практики исправлены
3. В Readme описать каждую из плохих практик в плохом файле, почему она плохая и как в хорошем она была исправлена, как исправление повлияло на результат

## Ход работы

Сначала были написаны 2 ```.yml``` файла [CI/CD с bad partices](https://github.com/dariapankova/clouds/blob/main/.github/workflows/bad_file.yml) и [CI/CD с good partices](https://github.com/dariapankova/clouds/blob/main/.github/workflows/good_file.yml).

Проведем сравнение этих файлов, описывая плохие практики и их исправление во втором файле.

**1. Запуск пайплайна при пуше в любой ветке**
```
on: push
```
Как можно увидеть в плохом файле любой пуш может развернуть изменение. В хорошем файле данная проблема была исправлена путем прописывания запуска только при пуше в ```.main```
```
on:
  push:
    branches:
      - main
```
**2. Отсутствие изоляции версии python**

В плохой версии файла используется системный python, что может привести к несовместимости версий.
```
- name: Install dependencies
        run: sudo apt-get update && sudo apt-get install -y python3-pip
```
В хорошей же версии была настроена изолированная среда python и задана версия 3.9, что помогло избежать несовместимости.
```
- name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
```
**3. Использование ```sudo``` для установки python**

В плохой версии файла используется системный python, что может привести к несовместимости версий.
```
- name: Install dependencies
        run: sudo apt-get update && sudo apt-get install -y python3-pip
```
В хорошей же версии была настроена изолированная среда python и задана версия 3.9, что помогло избежать несовместимости.
```
- name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
```
![](images/photo2.jpg)

