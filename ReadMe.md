# "Catch the Hacker"

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

## Übersicht

- [Die Idee](#die-idee-)
- [Spielziel](#ziel-)
- [Technische Umsetzung](#technische-umsetzung-)
  -  [Das Spielfeld](#das-spielfeld)
  - [Bewegung](#bewegung-)
- [Weitere Analyse](#weitere-analyse-)
- [Arbeitsteilung](#arbeitsteilung)
  - [Fragmente](#fragmenteaufgaben-)
  - [Aufteilung](#aufteilung)
- [Mockup GUI](#mockup-gui)

## Die Idee:
Ich mag das Spiel Scotland Yard. Es kommt auf Taktik, Kombinatorik und ein bisschen Glück an.
Nun muss das Spiel nicht auf einer Karte von London spielen.
Letztendlich benötigt man eine Karte mit 4 verschiedenen Fortbewegungsmitteln 
und einzelnen "Stationen"
(Analog Taxi, Bus, Metro, Fähre)

Nun wäre die Idee, dass das Spielfeld randomisiert in unterschiedlichen Größen, je nach Spielerzahl erstellt wird.
Hinzu würde ich von einer Stadt und öffentlichem Transportwesen weg gehen und bzw. im futuristischen
Layout ein IT-Netzwerk als Karte nehmen. Mister X ist ein "Hacker" und die SpielerInnen z.B. ForensikerInnen.


## Technische Umsetzung:

### Das Spielfeld
Für diese 4 Fortbewegungsmittel müssen 4 Graphen gebaut werden, die sich überlappen.
- Gelb = "Taxi" : Am häufigsten, kurze Strecken, eng vermascht.
- Grün = "Bus" : Seltener als Taxi, längere Strecken, in verbundenen Ringen.
- Rot = "Metro" : Deutlich seltener als Taxi und Bus, weitere Stecken, in Ringen
- Schwarz = "Fähre" : Am seltensten, **kein** Ring

Gelb: ca 200
Grün: ca 60
Rot: ca 15
Schwarz: ca 5

Jeder Punkt ist eine gelbe Station. 
Jede grüne Station ist auch eine gelbe Station
Jede rote Station ist auch eine grüne und gelbe Station.

Die schwarze Station folgt diesen Regeln nicht.

Das Verhältnis zwischen den Punkten

| Gelb | Grün | Rot | Schwarz          |
|------|------|-----|------------------|
| 200  | 60   | 15  | 5 |


### Bewegung:
Für Bewegung im Spiel nutzt man klassischerweise Tickets. 

#### "Mister X" erhält:

| Gelb | Grün | Rot | Schwarz               |
|------|------|-----|-----------------------|
| 4    | 3    | 3   | <Anzahl SpielerInnen> |

- +2 Doppelzugkarten, mit denen 2 Züge ausgeführt werden dürfen.
- Muss seinen aktuellen Punkt im 3, 8, 13, 18 Zug aufdecken.
- Spieler sehen das Verkehrsmittel, welches "Mister X" nutzt, außer er nutzt ein Black Ticket.
- Nur mit Black Tickets kann die Schwarze Linie genutzt werden.

#### SpielerIn erhält:

| Gelb | Grün | Rot | Schwarz |
|------|------|-----|---------|
| 10   | 8    | 4   | keine   |

## Ziel: 
Die ErmittlerInnen müssen den/die HackerIn "erwischen". D.h. auf dasselbe Feld ziehen.
Wird X bis Zug 22 nicht entdeckt 
oder können die Detektive nicht mehr ziehen, hat X gewonnen.

## Weitere Analyse:
### Verhältnis Stationen:

 Gelb | Grün | Rot | Schwarz          |
|------|------|-----|------------------|
| 40  | 12   | 3  | 1 |

### Verhältnis Tickets:

| Info         | Gelb | Grün | Rot | Schwarz |
|--------------|------|------|-----|---------|
| Stationen    | 200  | 60   | 15  | 5       |
| X            | 4    | 3    | 3   | *       |
| ErmittelerIn | 10   | 8    | 4   | 0       |

#### X:
- 1 gelbes Ticket pro 50 Stationen
- 1 grünes Ticket pro 20 Stationen
- 1 rotes Ticket pro 5 Stationen
- 1 schwarzes Ticket pro ErmittlerIn

#### ErmittlerIn:
- 1 gelbes Ticket pro 20 Stationen
- 1 grünes Ticket pro 7,5 Stationen
- 1 rotes Ticket pro 3,75 Stationen
- Keine schwarzen Tickets

# Arbeitsteilung

## Fragmente/Aufgaben:
- Anforderungen definieren
- Menü, Menüführung, GUI
- Spielfeldgenerierung
- Spielablauf & Logik
- Datenhaltung
- Single Player "KI"
- ggf. Multiplayer ggf. LAN
- ggf. Skalierung (mehrere X's? Skalierende Spielfelder? Mehr Züge?)
- Grafik

## Aufteilung

| HF           | CS (w) | CS (m) | 
|--------------|--------|--------|
| A            | B      | C      |
| A1           | B1     | C1     |


# Mockup GUI

![Diagram](Mocup.drawio.svg)