import pandas as pd

df = pd.read_csv("Pincode_30052019.csv", engine = 'python')
print(df)


states = set([(df['Circle Name'][i]) for i in range (0,len(df))])

#print(states)
head = [i for i in df]

while(True):
    state_name = (input("Select Circle/state Name: ")).title()
    if state_name in states:
        print("\nDistricts")
        district = []
        for i in range(0,len(df)):
            if df['Circle Name'][i] == state_name:
                dstrct = df['District'][i]
                district.append(dstrct)
        print(set(district))
        break
    else:
        print("Circle/state name not found")

while(True):
    district_name = input("\nSelect district: ")
    #district_name.upper() in district or district_name.lower() in district or district_name.title() in district
    if district_name in district:
        print("\nPincode")
        pincode = []
        for i in range(0,len(df)):
            if df['District'][i] == district_name:
                pc = df['Pincode'][i]
                pincode.append(pc)
        print(pincode)
        break
    else:
        print("district name not found")







#print(head)
#head_index = head.index('Region Name')
