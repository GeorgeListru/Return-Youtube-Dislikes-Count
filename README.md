# Return Youtube Dislikes Count
Proiectul preia numărul de dislike-uri de la fiecare videoclip și îl inserează în descrierea acestuia folosind Youtube Data API V3

### Codul Sursă
```bash
https://github.com/GeorgeListru/Return-Youtube-Dislikes-Count.git
```

### Cerințe
Aveți nevoie de un fișier numit ``` client_secret.json ```. Acesta poate fi obținut prin următorii pași:
1. Accesați ``` https://console.cloud.google.com/ ``` și căutați pentru Youtube DATA API V3 și apăsați pe  ``` ENABLE ```
2. Intrați la ``` Credentials ```, apoi la ``` CREATE CREDENTIALS ``` și selectați ``` OAuth client ID ```
3. Dați click pe ``` CONFIGURE CONSENT SCREEN ```
4. Dați o denumire aplicației și introduceți email-ul dumneavoastră
5. Apăsați pe ``` Next ``` până ajungeți la final
6. Odată ajunși la final, apăsați pe ``` PUBLISH APP ```
7. Intrați la ``` Credentials ```, apoi la ``` CREATE CREDENTIALS ``` selectați ``` OAuth client ID ```
8. Alegeți tipul aplicației ``` Desktop app ``` și dați-i o denumire, după care apăsați ``` Create ```
9. Pe ecran va apărea o fereastră cu informațiile despre client. Apăsați pe ``` DOWNLOAD JSON ``` pentru a descărca fișierul.
10. Redenumiți fișierul în ``` client_secret.json ``` și mutațil în mapa proiectului.
