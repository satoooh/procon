# create function
def num2words(num):
    nums_20_90 = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    nums_0_19 = ['zero','one','two','three','four','five','six','seven','eight',"nine",
'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    nums_dict = {100:'hundred', 1000:'thousand'}
    if num < 20:
        return nums_0_19[num]
    if num < 100:
        return nums_20_90[num//10-2] + ('' if num%10 == 0 else ' ' + nums_0_19[num%10])
    # find the largest key smaller than num
    maxkey = max([key for key in nums_dict.keys() if key <= num])
    return num2words(num//maxkey) + ' ' + nums_dict[maxkey] + ('' if num%maxkey == 0 else ' and ' +
    num2words(num%maxkey))

print(num2words(342), len(num2words(342).replace(" ", "")))

ans = 0
for i in range(1, 1001):
    ans += len(num2words(i).replace(" ", ""))

print(ans)
