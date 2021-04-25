def revStr(str2Rev):
    revfStr = ""
    for i in reversed(range(len(str2Rev))):
        revfStr = revfStr + str2Rev[i]

    return revfStr



print(revStr("Mohanish Mahajan"))