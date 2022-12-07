data = open('input_day6.txt', 'r')
data = data.read().strip()


packet = [data[i] for i in range(4)]
for x, i in enumerate(data):

    if len(set([packet[i] for i in range(4)])) == 4:
        answer_1 = x
        break

    else:
        packet.pop(0)
        packet.append(i)


packet_2 = [data[i] for i in range(14)]
for x, i in enumerate(data):

    if len(set([packet_2[i] for i in range(14)])) == 14:
        answer_2 = x
        break

    else:
        packet_2.pop(0)
        packet_2.append(i)


print('the answer for part 1 is:', answer_1)
print('the answer for part 2 is:', answer_2)