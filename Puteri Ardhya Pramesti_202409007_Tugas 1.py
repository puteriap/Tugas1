Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> var1=[1,2,3,4]
>>> print(type(var1))
<class 'list'>
>>> print(len(var1))
4
>>> first=[11.25,18.0,20.0]
>>> second=[10.75,9.50]
>>> full=first+second
>>> print(full)
[11.25, 18.0, 20.0, 10.75, 9.5]
>>> full_sorted=sorted(full,reverse=True)
>>> print(full_sorted)
[20.0, 18.0, 11.25, 10.75, 9.5]
>>> area=[11.25,18.0,20.0,10.75,9.50]
>>> print(area.index(20.0))
2
>>> print(area.count(14.5))
0
>>> area.append(24.5)
>>> area.append(15.45)
>>> print(area)
[11.25, 18.0, 20.0, 10.75, 9.5, 24.5, 15.45]
>>> area=sorted(area,reverse=True)
>>> print(area)
[24.5, 20.0, 18.0, 15.45, 11.25, 10.75, 9.5]
>>> import math
>>> print(math.pi)
3.141592653589793
>>> r=0.43
>>> keliling=2*math.pi*r
>>> luas=math.pi*r*r
>>> print(keliling)
2.701769682087222
>>> print(luas)
0.5808804816487527
>>> area_3=["hallway",11.25,"kitchen",18.0,"chill zone",20.0,"bedroom",10.75,"bathroom",10.50,"poolhouse",24.5,"garage",15.45]
>>> del area_3[11:14]
>>> print(area_3)
['hallway', 11.25, 'kitchen', 18.0, 'chill zone', 20.0, 'bedroom', 10.75, 'bathroom', 10.5, 'poolhouse']
>>> del area_3[10:13]
>>> print(area_3)
['hallway', 11.25, 'kitchen', 18.0, 'chill zone', 20.0, 'bedroom', 10.75, 'bathroom', 10.5]
>>> area_4=["hallway",11.25,"kitchen",18.0,"living room",20.0,"bedroom",10.75,"bathroom",9.50]
>>> print(area_4.index("bathroom"))
8
>>> area_4[8]=10.8
>>> print(area_4)
['hallway', 11.25, 'kitchen', 18.0, 'living room', 20.0, 'bedroom', 10.75, 10.8, 9.5]
>>> print(area_4.index("living room"))
4
>>> area_4[4]="ruang tamu"
>>> print(area_4)
['hallway', 11.25, 'kitchen', 18.0, 'ruang tamu', 20.0, 'bedroom', 10.75, 10.8, 9.5]
>>> 
