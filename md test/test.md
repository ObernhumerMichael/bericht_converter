---
pdf_options:
  format: a4
  margin: 30mm 20mm
  printBackground: true
  headerTemplate: |-
    <style>
      section {
        margin: 0 auto;
        font-family: system-ui;
        font-size: 11px;
      }
    </style>
    <section>
      <span class="title"></span>
      <span class="date"></span>
    </section>
  footerTemplate: |-
    <section>
      <div>
        Page <span class="pageNumber"></span>
        of <span class="totalPages"></span>
      </div>
    </section>
---


<span style="color:orange ;font-size:35px"><u>3-SYTB-2-MATE 002.04 Übungen</u></span>

Name: Michael Obernhumer 
Klasse: 3 AHITS 
Fach: SYTB MATE 
Datum: 3.2.2022

<span style="font-size:25px">Inhaltsverzeichnis:</span>

[TOC]

# 1 Übung (Zufälliges Wort)
Erstelle ein Skript das einen Satz aus 5 zufälligen Wörtern bildet, z.B.:

richtig ganzen Kilometer auf Mittel.
Wähle die Wörter aus der Wortliste (1000 häufigste deutsche Wörter).

Hinweis: Das Komando sed -n 5p gibt vom Input bspw. nur die 5te Zeile aus.

Hinweis: Berechnungen (+, -, *, /, %) können mit der Syntax $(( EXPR )) durchgeführt werden.

Erweiterung: Das Skript soll auch die Anzahl der in der Wortliste enthaltenen Wörter ermitteln. D.h. die Konstante 1000 soll im Skript nicht vorkommen.


## 1.1 Lösung
**Code**
```sh
for ((i=1;i<=5;i++)); 
do 
sed -n $(( $RANDOM % $(cat wortliste1000.txt | wc -w)))p wortliste1000.txt;
done
echo $TEXT
```

**Ausgabe**
```sh
diesen
bislang
keinen
sprechen
einfach
```



# 2 Übung (dated copy V1)
Create a script which will take a filename as its first argument and create a dated copy of the file. eg. If our file was named file1.txt it would create a copy such as 2021-10-29_file1.txt. (To achieve this you will probably want to play with command substitution and the command date)

## 2.1 Lösung
**Code**
```sh
NAME=$1
DATEDNAME=$(date +%Y)"-"$(date +%m)"-"$(date +%d)"_"$NAME
touch $DATEDNAME
cp $NAME $DATEDNAME
```
**Eingabe**
```sh
./datedCopyV1.sh Text
```

**Ausgabe (Filename)**
- `2022-02-03_Text`

# 3 Übung (dated copy V2)
Challenge: To make it a bit harder, see if you can get it so that the date is after the name of the file (eg. file1_2021-10-29.txt (Hint: Use cut to seperate filename from extension)

## 3.1 Lösung
**Code**
```sh
NAME=$1
FILENAME=$(echo $NAME | cut -d'.' -f'1')
FILEENDING=$(echo $NAME | cut -d'.' -f'2')
DATEDNAME=$FILENAME"_"$(date +%Y)"-"$(date +%m)"-"$(date +%d)"."$FILEENDING
touch $DATEDNAME
cp $NAME $DATEDNAME
```

**Eingabe**
```sh
~/3-SYTB-2-MATE-00203$ ./datedCopyV2.sh Text.txt
```

**Ausgabe (Filename)**
- `Text_2022-02-03.txt`

# 4 Übung (dated copy V3)
Challenge: Now see if you can expand the previous question to accept a list of files on the command line and it will create a named copy of all of them. (Hint: The command xargs may be useful here.)

## 4.1 Lösung 
**Code**
```sh
for args in "$@"
do
NAME=$args
FILENAME=$(echo $NAME | cut -d'.' -f'1')
FILEENDING=$(echo $NAME | cut -d'.' -f'2')
DATEDNAME=$FILENAME"_"$(date +%Y)"-"$(date +%m)"-"$(date +%d)"."$FILEENDING
touch $DATEDNAME
cp $NAME $DATEDNAME
done
```

**Eingabe**
```sh
~/3-SYTB-2-MATE-00203$ ./datedCopyV3.sh Text.txt wortliste1000.txt 
```

**Ausgaben (Filename)**
- `wortliste1000_2022-02-03.txt`
- `Text_2022-02-03.txt`
