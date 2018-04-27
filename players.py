players = ['LBJ', 'Wade', 'Kobe', 'Michel', 'Kara', 'James'];
print(players[0:3]);
print(players[:4]);
print(players[2:]);

my_favirate_player = players[:];
print(players);
print(my_favirate_player);

players.append("Yao");
print(players);
print(my_favirate_player);

my_favirate_player.append("Derant");

print(players);
print(my_favirate_player);


my_favirate_player = players;
print(players);
print(my_favirate_player);

players.append("Doctor");
print(players);
print(my_favirate_player);

my_favirate_player.append("Maidi");
print(players);
print(my_favirate_player);

print("The first three items in the list are:");
print(players[:3]);
