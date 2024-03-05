import heapq

cables = [3, 17, 9, 27, 6]
heap = []
for cable in cables:
    heapq.heappush(heap, cable)

total_cost = 0

print("Початкові кабелі:", cables)
print("Починаємо процес об'єднання...")

while len(heap) > 1:
    cable1 = heapq.heappop(heap)
    cable2 = heapq.heappop(heap)

    combined_cable = cable1 + cable2
    heapq.heappush(heap, combined_cable)
    total_cost += combined_cable

    print(f"Об'єднуємо кабелі з довжиною {cable1} та {cable2}, утворюємо новий кабель довжиною {combined_cable}. Загальна вартість = {total_cost}.")

print("\nЗагальна вартість мінімального об'єднання всіх кабелів:", total_cost)
