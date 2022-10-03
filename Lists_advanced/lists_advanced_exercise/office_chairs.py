count_of_rooms = int(input())

free_chairs = True
total_free_chairs = 0
current_room = 0

for room in range(count_of_rooms):
    chairs_visitors = input().split()
    current_room += 1
    if len(chairs_visitors[0]) >= int(chairs_visitors[1]):
        total_free_chairs += (len(chairs_visitors[0])
                              - int(chairs_visitors[1]))
    else:
        needed_chairs = abs(len(chairs_visitors[0]) - int(chairs_visitors[1]))
        print(
            f"{needed_chairs} more chairs needed in room {current_room}")
        free_chairs = False
if free_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")
