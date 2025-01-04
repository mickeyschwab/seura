from seura import SeuraClient

client = SeuraClient(host="10.0.0.114")
# client.power_on()
# client.power_off()
# print(client.query_power())
# print(client.query_volume())
# print(client.query_channel())
# print(client.query_input())
# print(client.set_volume(10))
# print(client.remote_button("MENU"))
print(client.remote_button("MUTE"))
# print(client.remote_number(3))
