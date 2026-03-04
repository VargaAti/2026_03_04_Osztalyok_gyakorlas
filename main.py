import random as rn
import statistics as st
from auto import Auto

auto1 = Auto("Toyota", "Corolla", 2015,)
auto2 = Auto("Ford", "Focus", 2018)
auto3 = Auto("Volkswagen", "Bora", 2004)
auto4 = Auto("Suzuki", "Ignis", 2016)

autok = [auto1, auto2, auto3, auto4]

for i in autok:
    print(i)

for i in autok:
    i.gyorsit(rn.randint(10,50))

for i in autok:
    print(i)

autok_kora = []
for i in autok:
    autok_kora.append(2026 - i.gyartasi_ev)

print(f"az autók átlagéletkora: {st.mean(autok_kora)} év")

legiosebb_auto = autok_kora.index(max(autok_kora))
print(f"A legöregebb autó: {autok[legiosebb_auto].marka} {autok[legiosebb_auto].tipus}, {autok_kora[legiosebb_auto]} éves")

#A version


#C version
# gyartasi_evek = [auto.gyartasi_ev for auto in autok]
# for auto in autok:
#     if auto.gyartasi_ev == min(gyartasi_evek):
#         print(f"A legidősebb autó: {auto.marka} {auto.tipus}")