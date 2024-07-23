"""
Жадные алгоритмы
"""

from typing import Mapping, Iterable

states_needed: Iterable[str] = set(
    ["mt", "wa", "or", "id", "nv", "ut", "ca", "az"]
)

stations: Mapping[str, Iterable[str]] = {
    "kone": set(["id", "nv", "ut"]),
    "ktwo": set(["wa", "id", "mt"]),
    "kthree": set(["or", "nv", "ca"]),
    "kfour": set(["nv", "ut"]),
    "kfive": set(["ca", "az"]),
}

final_stations: Iterable[str] = set()

while states_needed:
    best_station: str | None = None
    states_covered: Iterable[str] = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    if best_station:
        final_stations.add(best_station)

print(final_stations)
