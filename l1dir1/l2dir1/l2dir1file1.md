<span style="color:orange ;font-size:35px"><u>3-SYTB-2-MATE 002.03 Umgebungsvariablen und Commandsubstitution</u></span>

Name: Michael Obernhumer 
Klasse: 3 AHITS 
Fach: SYTB MATE 
Datum: 20.1.2022

<span style="font-size:25px">Inhaltsverzeichnis:</span>

[TOC]

# 1 Umgebungsvariablen
- `$SHELL` Zeigt den Aktuelle Shell Pfad an
- `PS1` gibt das Commandpromt vor und kann konfiguriert werden
- `$PWD` zeigt den Aktuellen Pfad an macht das selbe wie `pwd`
- `env` gibt alle environment variabln (Umgebungsvariablen) aus
- `$PATH` Verzeichnisse die standardmäßig Durchsucht werden wenn beispielsweise ein Programm gestartet werden (veränderbar)
- `/home/runner` ist das eigenlich home Verzeichnis in repl 

```sh
# $SHELL
~/3-SYTB-2-MATE-00203$ echo $SHELL 
/bin/bash

# Kommand Promt
~/3-SYTB-2-MATE-00203$ echo $PS1
\[\033[01;34m\]\w\[\033[00m\]\$ #Standard
~/3-SYTB-2-MATE-00203$ PS1='> ' #konfigurierbar
> 
> 
> PS1='$'
$
$
$PS1='\t $ ' 
09:01:40 $ 
09:01:41 $ 
09:01:42 $ 
09:01:43 $ 
09:01:45 $ PS1='\d $ '
Thu Jan 20 $ 
Thu Jan 20 $ 
Thu Jan 20 $ PS1='\w'
~/3-SYTB-2-MATE-00203
~/3-SYTB-2-MATE-00203PS1='\W'
3-SYTB-2-MATE-00203
3-SYTB-2-MATE-00203

# Absoluter Pfad
$ echo $PWD
/home/runner/3-SYTB-2-MATE-00203
$ pwd
/home/runner/3-SYTB-2-MATE-00203

#env
$ env 
# Gibt alle variablen aus 

# $PATH
$ echo $PATH
/nix/store/w07a7k61dw5gnsyxj3kgcq3shr76jax8-bash-interactive-4.4-
p23/bin:/nix/store/435paza0j48aa9vgvf6r2l12nrg4ld11-patchelf-
0.12/bin:/nix/store/4xs1xyj8728yvh9y5v6ji819kwgfy2fv-gcc-wrapper-
10.3.0/bin:/nix/store/dlni53myj53kx20pi4yhm7p68lw17b07-gcc-
10.3.0/bin:/nix/store/6z35qvn00xrjvaznv9kfy8xddbbdz4gl-glibc-2.33-47-
bin/bin:/nix/store/1570w56jrkvr90w9x158vyb5vahnk18v-coreutils-
8.32/bin:/nix/store/29bjq5hw1qglybp1a5f3ij9gxc2fyf94-binutils-wrapper-
2.35.1/bin:/nix/store/v8imx1nvyz0hgvx9cbcmh6gp4ngw3ffj-binutils-
2.35.1/bin:/nix/store/ihxk2vlm0vi7c4j3gpm084kbxvz6v585-findutils-
4.8.0/bin:/nix/store/kjx1mv85c5cgsrr4bwar22j7hbwj834m-diffutils-
3.7/bin:/nix/store/gm2w08wwsa3vd500d8vq879s2lv65ldh-gnused-
4.8/bin:/nix/store/v0slhpb2y3xa7gmv4q6gblkdk7n0f09j-gnugrep-
3.6/bin:/nix/store/2wn093wbc6ps4brcsppxjd14vxvaa8a2-gawk-
5.1.0/bin:/nix/store/5bxrjkyvqmzn1p897652y3lwa9fxagpw-gnutar-
1.34/bin:/nix/store/liva1jnjdskrn57s42kfawr2zz66szzm-gzip-
1.10/bin:/nix/store/ih2zkh2mbrx2c766ryk2i9hhlkly7snr-bzip2-1.0.6.0.2-
bin/bin:/nix/store/pvkiiw0mp1yx0b21b7k105yywccychgh-gnumake-
4.3/bin:/nix/store/dpjnjrqbgbm8a5wvi1hya01vd8wyvsq4-bash-4.4-
p23/bin:/nix/store/aicl3kwfnaizk45aygm8bviqv7lk0a16-patch-
2.7.6/bin:/nix/store/7jk6k46f56rszzc1bxi8mdrvcw53pym4-xz-5.2.5-
bin/bin:/nix/store/v71227svpfrp555hmzs20nkhx0rppird-prybar-elisp-0.0.0-
02c7adf/bin:/nix/store/3gl3vr0s5dr7ipq3lx559xypig2pzgqj-prybar-lua-
0.0.0-02c7adf/bin:/nix/store/drsgisc3rn4v2gri763spqm0jafqa1q4-prybar-
python3-0.0.0-02c7adf/bin:/nix/store/1g4yzg8qd3xcs4pyr75kbhxalcql1hkw-
prybar-sqlite-0.0.0-
02c7adf/bin:/nix/store/0vnrkrd04q4z3bjkqh52wwxmldngf4xr-prybar-tcl-
0.0.0-02c7adf/bin:/nix/store/r984vadc1xpr6gyd7qr6rfg55kirh122-pid1-
0.0.0-02a4b21/bin:/nix/store/1d14fcwp2z64wmmr5jpfa1m5zay0n9fq-silver-
searcher-2.2.0/bin:/nix/store/pcr60c6n4hcxqbaqvqv2ly6ihcnvn8f5-
bash/bin:/nix/store/0vkw1m51q34dr64z5i87dy99an4hfmyg-coreutils-
8.32/bin:/nix/store/ng35kcfzm03fdmp97nc2dxi63jv41sca-vscode-cpptools-
dap-1.3.1/bin:/nix/store/n578yqf36hxxs6nhcwq35gkqhv2b00cl-replit-python-
dap-wrapper-1.0.0/bin:/nix/store/knvdqxr2xkp73bb1xzl6a0i3rqnvycay-node-
dap/bin:/nix/store/yzr5fybypw977fxnqj3gsp3gznh1lbm2-
fluxbox/bin:/nix/store/vfnpx0k26ilwv3p2x8rdf0an5llpdmjw-prybar-nodejs-
0.0.0-02c7adf/bin:/nix/store/7bf2l1b07vj9m9p1fn4g64h5sba2i9ls-
pulseaudio-14.2/bin:/nix/store/8cpkwghsa1crf84x7155pnsx5xjqyzsz-
rfbproxy-0.0.0-b81eb2f/bin:/nix/store/fy1vhp96i11ng6mwbr0l5apj68c64lgr-
tigervnc-1.11.0/bin:/nix/store/mjbrcsjhn4smd1jdl4nkywpvzdyfcd14-upm-0.0.0-98447b2/bin:/nix/store/3hny06xvqvc4irdnknk732a2km9b93rq-xwininfo-1.1.4/bin:/nix/store/10c49axvzlavn6h3kwg6z1l5ha6f9cg0-
replbox/bin:/home/runner/.nix-
profile/bin:/home/runner/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/
sbin:/usr/bin:/sbin:/bin


$ mkdir subdir
$ cd subdir/
$ touch hello.sh
$ echo "echo Hallo Welt" > hello.sh 
$ cat hello.sh 
echo Hallo Welt
$ chmod u+x hello.sh 
$ ./hello.sh 
Hallo Welt

# Ausführen nicht möglich ohne den ganzen Pfad eingeben zu müssen weil dieser in der PATH Variable nicht vorhanden ist.
$ hello.sh
bash: hello.sh: command not found
$ cd ..
$ ls
bericht.md  main.sh  replit.nix  subdir
$ subdir/hello.sh 
Hallo Welt

# Ausführen möglich ohne den ganzen Pfad eingeben zu müssen weil dieser in die PATH Variable hinzugefügt worden ist.
$ pwd
/home/runner/3-SYTB-2-MATE-00203
$ PATH="$PATH:/home/runner/3-SYTB-2-MATE-00203/subdir"
$ hello.sh
Hallo Welt

# Homeverzeichniss in Repl
$ cd
$ pwd
/home/runner
$ ls -a # Zeigt die config Files an 
.   .bash_logout  .cache  .config  .nix-channels  .nix-profile  .profile
..  .bashrc   .cargo  .m2      .nix-defexpr   .npm      3-SYTB-2-MATE-00203
```

# 2 Command substituion

= den output eines Programmes als Variablen weiter verwenden. 
generelle Syntax $(...)

```sh
echo "Heute ist der $(date -I)"
# Ausgabe:
Heute ist der 2022-01-20
```

Beispiel: einen Text generieren
Es sind 123 Files im Verzeichnis /etc

```sh
FILECOUNT = $(ls /etc | wc -l)
echo "Es sind $FILECOUNT Files im Verzeichnis /etc"
echo "Es sind $(ls /etc | wc -l) Files im Verzeichnis /etc"
# Ausgabe:
Es sind 86 Files im Verzeichnis /etc
Es sind 86 Files im Verzeichnis /etc
```

# 2.1 Übung (Zufälliges Wort)

Erstelle ein Skript das einen Satz aus 5 zufälligen Wörtern bildet, z.B.:
`richtig ganzen Kilometer auf Mittel.`
Wähle die Wörter aus der Wortliste (1000 häufigste deutsche Wörter).

Hinweis: Das Komando `sed -n 5p` gibt vom Input bspw. nur die 5te Zeile aus. 
Hinweis: Berechnungen `(+, -, *, /, %)` können mit der Syntax `$(( EXPR ))` durchgeführt werden.

Erweiterung: Das Skript soll auch die Anzahl der in der Wortliste enthaltenen Wörter ermitteln. D.h. die Konstante 1000 soll im Skript nicht vorkommen.

**Lösung wird im nächsten Bericht Vorhanden sein.**