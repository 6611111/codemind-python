hf,sf,sdf=map(int,input().split())
if hf>50 and sf>60 and sdf>100:
    print("10")
elif hf>50 and sf>60:
    print("9")
elif sf>60 and sdf>100:
    print("8")
elif hf>50 and sdf>100:
    print("7")
elif hf>50 or sf>60 or sdf>100:
    print("6")
else:
    print("5")