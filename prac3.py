k = int(input())

hotelroom = map(int, input().split())
hotelroom = sorted(hotelroom)

for i in range(len(hotelroom)):
    if(i != len(hotelroom)-1):
        if(hotelroom[i]!=hotelroom[i-1] and hotelroom[i]!=hotelroom[i+1]):
            print(hotelroom[i])
            break;
    else:
        print(hotelroom[i])
