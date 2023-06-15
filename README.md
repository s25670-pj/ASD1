Podsumowanie na podstawie wyników czasowych dla różnych algorytmów sortowania (Quicksort, Heapsort, Shellsort) na danych wejściowych w różnych konfiguracjach:

![image](https://github.com/s25670-pj/ASD1/assets/92204700/ddd7d94b-79b6-482c-9f36-f1877d7a186f)


Dla danych losowych:
Najlepszy czas sortowania: Quicksort (1.1102912s)
Średni czas sortowania: Shellsort (2.250248s)
Najgorszy czas sortowania: Heapsort (2.473177s)

Dla danych posortowanych w kolejności rosnącej:
Najlepszy czas sortowania: Quicksort (9e-07s)
Średni czas sortowania: Shellsort (0.6898446s)
Najgorszy czas sortowania: Heapsort (2.2232682s)

Dla danych posortowanych w kolejności malejącej:
Najlepszy czas sortowania: Shellsort (0.7114681s)
Średni czas sortowania: Heapsort (2.1737259s)
Najgorszy czas sortowania: Quicksort (3.1418522s)

Wnioski:
Quicksort jest najwydajniejszym algorytmem sortowania w przypadku danych losowych i posortowanych rosnąco. Ma najkrótszy czas sortowania.
Shellsort osiąga bardzo dobry czas sortowania dla danych posortowanych rosnąco, ale gorszy czas dla danych losowych i posortowanych malejąco.
Heapsort osiąga gorsze wyniki w porównaniu do Quicksort i Shellsort w każdej konfiguracji danych.

Warto zauważyć, że wybór optymalnego algorytmu sortowania zależy od specyfiki danych wejściowych i kontekstu aplikacji. W przypadku danych losowych i posortowanych rosnąco, Quicksort jest zdecydowanie preferowanym algorytmem ze względu na swoją wydajność. Jednak dla danych posortowanych malejąco, Shellsort wykazuje lepsze rezultaty niż inne algorytmy.
