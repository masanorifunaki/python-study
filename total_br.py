all_guests = {'アリス': {'りんご': 5, 'プレッツェル': 12},
              'ボブ': {'ハムサンド': 3, 'りんご': 2},
              'キャロル': {'コップ': 3, 'アップルパイ': 1}}

def total_brought(guests, item):
    num_brought = 0
    for k, v in guests.items(): #1
        num_brought = num_brought + v.get(item, 0) #2
    return num_brought

print(' - リンゴ ' + str(total_brought(all_guests, 'りんご')))
print(' - コップ ' + str(total_brought(all_guests, 'コップ')))
print(' - ハムサンド ' + str(total_brought(all_guests, 'ハムサンド')))
print(' - アップルパイ ' + str(total_brought(all_guests, 'アップルパイ')))



