bicycles = ['trek', 'cannondale', 'redline', 'specialized'];
print(bicycles);
print(bicycles[1]);

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append("jialin");
print(motorcycles);

del motorcycles[0];
print(motorcycles);

popped_moto = motorcycles.pop(-1);
print(motorcycles);
print(popped_moto);

removed_moto = motorcycles.remove('yamaha');
print(motorcycles);
print(removed_moto);
